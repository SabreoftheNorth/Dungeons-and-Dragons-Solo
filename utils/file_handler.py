#this will be the file handler
#what does it do?
#it will handle all the JSON save/load functions for this app
#as well as storing those saves in data/saves/ as individual .json files
#each save file will represent one complete character.

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

from core.character import Character

#paths. root of this very own project, it'll resolves correctly
#regardless of where the script will be called from
PROJECT_ROOT    = Path(__file__).resolve().parent.parent
SAVES_DIR       = PROJECT_ROOT / "data" / "saves"
BACKUPS_DIR     = PROJECT_ROOT / "data" / "saves" / "backups"

def _ensure_dirs() -> None:
    #this will create save and backup directories if they havent
    #existed
    SAVES_DIR.mkdir(parents=True, exist_ok=True)
    BACKUPS_DIR.mkdir(parents=True, exist_ok=True)

#da save function
def save_character(character: Character, filename: str = "") -> Path:
    #it'll save a character to the json file i talked abt earlier
    # if theres no filename, then the character's name will be used
    
    #spaces will be replaced with and underscore ("_"), format... all undercase
    #a timestamp backup will also be written to its own place

    _ensure_dirs() #returns the path for the saved file

    if not filename:
        save_name = character.character_name.strip().lower().replace(" ", "_")
        if not save_name:
            save_name = "unnamed_character"
        filename = f"{save_name}.json"
    
    if not filename.endswith(".json"):
        filename += ".json" #ensure that the .json extension will always be used

    save_path = SAVES_DIR / filename

    #building the save payload, which is the character data and its metadata
    payload = {
        "_metadata": {
            "app_version":  "0.1.0",
            "last_saved":   datetime.now().isoformat(),
            "save_version": 1,
        },
        "character":    character.to_dict()
    }

    _write_json(save_path, payload) #writes the main save file

    #writes timestamped backup
    timestamp =     datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name =   f"{save_path.stem}_{timestamp}.json"
    backup_path =   BACKUPS_DIR / backup_name
    _write_json(backup_path, payload)

    return save_path

#da load function
def load_character(filepath: str | Path) -> Character:
    #it'll loads the character from its .json save file
    #it'll also do:
    #   - returns a fully reconstructed Character instance.
    #   - it'll raises "FileNotFoundError" if file doesnt exist
    #   - it'll also raises "ValueError" if the file has problems

    path = _resolve_path(filepath)

    raw = _read_json(path)

    if "character" not in raw:
        raise ValueError(
            f"Save file '{path.name}' is missing character data"
            "It may be corrupted"
        )

    return Character.from_dict(raw["character"])

#listings & deletes
def list_saves() -> list[dict]:
    #this will return a list of all save files with each entry
    #being a dict with useful display info
    # files that failed to parse will be skipped with a warning

    _ensure_dirs()

    saves = []
    for path in sorted(SAVES_DIR.glob("*.json")):
        try:
            raw =   _read_json(path)
            char =  raw.get("character", {})
            meta =  raw.get("_metadata", {})
            saves.append({
                "filename":         path.name,
                "filepath":         path,
                "character_name":   char.get("character_name", "Unknown"),
                "class_name":       char.get("class_name", "Unknown"),
                "level":            char.get("level", 1),
                "race":             char.get("race", "Unknown"),
                "last_saved":       meta.get("last_saved", "Unknown"),
            })
        except Exception as e:
            print(f"[file_handler] Warning: could not read '{path.name}': {e}")

    return saves

def delete_character(filepath: str | Path) -> None:
    #self explanatory, although yes, it is a bit different
    #instead of just deleting it straight up, it'll move it to backups/ with a suffix
    #like : '_deleted'. So yeah, you can always recover it.

    _ensure_dirs()
    path = _resolve_path(filepath)
    
    timestamp =         datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name =       f"{path.stem}_deleted_{timestamp}.json"
    backup_path =       BACKUPS_DIR / backup_name

    shutil.move(str(path), str(backup_path))

#da internal helpers............ :3
def _resolve_path(filepath: str | Path) -> Path:
    #if the filepath is just a filename, then look inside SAVES_DIR
    #if its a full path, then use it
    #it raises FileNotFoundError in case of... well an error

    path = Path(filepath)
    if not path.is_absolute():
        path = SAVES_DIR / path

    if not path.exists():
        raise FileNotFoundError(f"Save file not found: '{path}'")
    
    return path

#dealing with the earlier functions

def _write_json(path: Path, data: dict) -> None:
    #it'll write a dict to a .json file with readable indentation
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def _read_json(path: Path) -> dict:
    #this will read a json file and returns a dict from it
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)