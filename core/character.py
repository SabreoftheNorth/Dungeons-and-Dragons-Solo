#this is for the full dungeons and dragons (5e edition) data model
#as well as the page 1 of the official character sheet.
#
#All derived values like modifiers, saving throws, skills, passive perception,
#proficiency bonus are auto-calculated from base stats.
#
#presets for text fields, which are: personality traits, ideals, bonds, flaws,
#features, etc. are intentionally left as commented placeholders
#YOU HAVE PRESETS THOUGH, so you can use those or fill in yourselves

from dataclasses import dataclass, field
from typing import Optional

#constants used throughout this code
ABILITIES = ["strength", "dexterity", "constitution",
             "intelligence", "wisdom", "charisma"]

SKILL_ABILITY_MAP = {
    "acrobatics":   "dexterity",
    "animal_handling":  "wisdom",
    "arcana":   "intelligence",
    "athletics":    "strength",
    "deception":    "charisma",
    "history":  "intelligence",
    "insight":  "wisdom",
    "intimidation": "charisma",
    "investigation":    "intelligence",
    "medicine": "wisdom",
    "nature":   "intelligence",
    "perception":   "wisdom",
    "performance":  "charisma",
    "persuasion":   "charisma",
    "religion": "intelligence",
    "sleight_of_hand":  "dexterity",
    "stealth":  "dexterity",
    "survival": "wisdom"
}

SAVING_THROW_ABILITIES = {
    "strength": "strength",
    "dexterity":    "dexterity",
    "constitution": "constitution",
    "intelligence": "intelligence",
    "wisdom":   "wisdom",
    "charisma": "charisma",
}

PLAYABLE_RACES = [
    "Human",
    "High Elf",
    "Wood Elf",
    "Hill Dwarf",
    "Mountain Dwarf",
    "Lightfoot Halfling",
    "Stout Halfling",
    "Forest Gnome",
    "Rock Gnome",
    "Half-Elf",
    "Half-Orc",
    "Tiefling",
    "Dragonborn",
]

#TODO MAKE CLASSES SELECTABLE TOO

#oooh bonuses...
#each race has a bonus
RACE_BONUSES: dict[str, dict[str, int] | None] = {
    "Human":                {"strength": 1, "dexterity": 1, "constitution": 1,
                            "intelligence": 1, "wisdom": 1, "charisma": 1},
    "High Elf":             {"dexterity": 2, "intelligence": 1},
    "Wood Elf":             {"dexterity": 2, "wisdom": 1},
    "Hill Dwarf":           {"constitution": 2, "wisdom": 1},
    "Mountain Dwarf":       {"constitution": 2, "strength": 2},
    "Lightfoot Halfling":   {"dexterity": 2, "charisma": 1},
    "Stout Halfling":       {"dexterity": 2, "constitution": 1},
    "Forest Gnome":         {"intelligence": 2, "dexterity": 1},
    "Rock Gnome":           {"intelligence": 2, "constitution": 1},
    "Half-Elf":             None,   # because the player will pick any two abilities
                                    #to recieve +1. However I'll prolly forget abt
                                    #this so
                                    #UPDATE: I didnt... nice
    "Half-Orc":             {"strength": 2, "constitution": 1},
    "Tiefling":             {"charisma": 2, "intelligence": 1},
    "Dragonborn":           {"strength": 2, "charisma": 1},
}
#presets for personality, ideal, etc.
PERSONALITY_TRAIT_PRESENTS = [
    #presets coming soon
]

IDEAL_PRESETS = [
    #presets coming soon
]

BOND_PRESETS = [
    #presets coming soon
]

FLAW_PRESETS = [
    #presets coming soon
]

FEATURE_PRESETS = [
    #presets coming soon
]

PROFICIENCY_LANGUAGE_PRESETS = [
    #presets coming soon
]

#this is for the sub-models
@dataclass
class AbilityScores:
    #for the six core ability scores. std values
    strength:       int = 10
    dexterity:      int = 10
    constitution:   int = 10
    intelligence:   int = 10
    wisdom:         int = 10
    charisma:       int = 10

    def modifier(self, ability: str) -> int:
        #remember the standard formula for modifiers in
        #5e, (score - 10) // 2
        score = getattr(self, ability)
        return (score - 10) // 2
    
    def all_modifiers(self) -> dict[str, int]:
        return {ability: self.modifier(ability) for ability in ABILITIES}
    
@dataclass
class SavingThrows:
    #proficiency flags as per for each saving throw
    #the actual throw value in itself will be calculated in Character
    #where it needs both the ability modifier as well as the proficiency bonus
    #hell yeah

    strength:       bool = False
    dexterity:      bool = False
    constitution:   bool = False
    intelligence:   bool = False
    wisdom:         bool = False
    charisma:       bool = False

@dataclass
class Skills:
    #proficiency flags for all eighteen skills.
    #for the experise, which is double proficiency
    #will be tracked seperately by the skills (per skill)

    acrobatics:         bool = False
    animal_handling:    bool = False
    arcana:             bool = False
    athletics:          bool = False
    deception:          bool = False
    history:            bool = False
    insight:            bool = False
    intimidation:       bool = False
    investigation:      bool = False
    medicine:           bool = False
    nature:             bool = False
    perception:         bool = False
    performance:        bool = False
    persuasion:         bool = False
    religion:           bool = False
    sleight_of_hand:    bool = False
    stealth:            bool = False
    survival:           bool = False

    #EXPERTISE: if True for any skill, then proficiency
    # bonus will be doubled...

    expertise: dict = field(default_factory=lambda: {
        skill: False for skill in SKILL_ABILITY_MAP
    })

@dataclass
class HitPoints:
    #HP, self explanatory if you played ANY game.
    maximum:    int = 0
    current:    int = 0
    temporary:  int = 0

@dataclass
class HitDice:
    #for example: total 3d8 for a level 3 monk
    # for the remainder, tracks how many have been spent.
    total:      str = "" #for example, "3d8"
    remaining:  int = 0

@dataclass
class DeathSaves:
    successes:  int = 0
    failures:   int = 0
    #range is 0-3 for both of them

@dataclass
class Attack:
    #one row in the attacks and spellcasting table
    name:       str = ""
    atk_bonus:  str = "" #example, "+5" or "spell"
    dmg_type:   str = "" #example, "1d8+3 slashing... ik complicated ik"

#main character model here
@dataclass
class Character:
    #the full dnd 5e character, based off the page 1 in the official
    #  dnd character sheet
    # all derived stats are computed using properties and NEVER stored directly
    # figure smth out abt that

    #header
    character_name:     str = ""
    class_name:         str = ""
    level:              int = 1
    background:         str = ""
    player_name:        str = ""
    race:               str = PLAYABLE_RACES[0]
    #AHHH I DIDNT FORGET ABT IT NICE
    half_elf_bonus_choices: list[str] = field(default_factory=list)
    alignment:          str = ""
    experience_points:  int = 0

    #core stats for the character
    ability_scores: AbilityScores   = field(default_factory=AbilityScores)
    saving_throws:  SavingThrows    = field(default_factory=SavingThrows)
    skills:         Skills          = field(default_factory=Skills)

    inspiration:    bool = False #it will be a toggle on the sheet

    #combat stats, located in the middle column
    armor_class:    int = 10
    speed:          int = 30
    
    hit_points:     HitPoints       = field(default_factory=HitPoints)
    hit_dice:       HitDice         = field(default_factory=HitDice)
    death_saves:    DeathSaves      = field(default_factory=DeathSaves)

    attacks: list[Attack] = field(default_factory=list)

    #spellcasting notes, it will be located below attacks
    spellcasting_notes: str = ""

    #right column for the personality and roleplay
    personality_traits: str = ""
    ideals:             str = ""
    bonds:              str = ""
    flaws:              str = ""
    #the input can be presets or custom, you diy

    #the bottom section of it
    other_proficiencies_languages:  str = ""
    equipment:                      str = ""
    features_and_traits:            str = ""

    #THIS. this will be the properties that are auto-calculated based on the
    # stats

    @property
    def proficiency_bonus(self) -> int:
        #based on the official book, proficiency bonus is measured by total 
        #char level:
        #Levels 1-4 -> +2
        #Levels 5-8 -> +3
        #Levels 9-12 -> +4
        #Levels 13-16 -> +5
        #Levels 17-20 -> +6
        return (self.level - 1) // 4 + 2
    
    @property
    def initiative(self) -> int:
        #initiative is measured by dexterity modifier
        return self.ability_scores.modifier("dexterity")
    
    @property
    def passive_perception(self) -> int:
        #passive wisdom (based off perception) = 10 + perception skill total.
        #accounts for proficiency and expertise automatically
        return 10 + self.skill_total("perception")
    
    def ability_modifier(self, ability: str) -> int:
        return self.ability_scores.modifier(ability)
    
    def saving_throw_total(self, ability: str) -> int:
        #saving throw is ability modifier + proficiency bonus (IF YOU ARE PROFICIENT)
        base = self.ability_scores.modifier(ability)
        proficient = getattr(self.saving_throws, ability)
        return base + (self.proficiency_bonus if proficient else 0)
    
    def skill_total(self, skill: str) -> int:
        #skill tota is ab. mod. + prof. (IF prof.)
        #it'll doubles your proficiency if expertise is set for that skill.
        ability     = SKILL_ABILITY_MAP[skill]
        base        = self.ability_scores.modifier(ability)
        proficient  = getattr(self.skills, skill)
        expert      = self.skills.expertise.get(skill, False)

        if expert:
            return base + self.proficiency_bonus * 2
        elif proficient:
            return base + self.proficiency_bonus
        else:
            return base
        
    def all_saving_throw_totals(self) -> dict[str, int]:
        return {ability: self.saving_throw_total(ability)
            for ability in ABILITIES}
        
    def all_skill_totals(self) -> dict[str, int]:
        return {skill: self.skill_total(skill)
            for skill in SKILL_ABILITY_MAP}
    
    def apply_race_bonuses(self) -> None:
        #this will apply racial ASI bonuses to the ability scores
        #it should be called once during character creation when the race is
        #set. For half-elves, half_elf_bonus_choices must be populated first
        #with exactly 2 ability names before calling.
        if self.race == "Half-Elf":
            #exactly two choices to validate
            if len(self.half_elf_bonus_choices) != 2:
                raise ValueError(
                    "Half-Elves need exactly two ability choices as bonuses"
                )
            for ability in self.half_elf_bonus_choices:
                current = getattr(self.ability_scores, ability)
                setattr(self.ability_scores, ability, current + 1)

        elif race_asi is not None:
            for ability, bonus in race_asi.items():
                current = getattr(self.ability_scores, ability)
                setattr(self.ability_scores, ability, current + bonus)
                #why yellow, hmm we'll fix it.
                #TODO WHY
    
    #the rest is for the serialisation helpers, to be used by file_handler.py
    def to_dict(self) -> dict:
        #this is so that the character would be flattened into a JSON-like dict.
        return {
            "character_name":           self.character_name,
            "class_name":               self.class_name,
            "level":                    self.level,
            "background":               self.background,
            "player_name":              self.player_name,
            "race":                     self.race,
            "half_elf_bonus_choices":   self.half_elf_bonus_choices,
            "alignment":                self.alignment,
            "experience_points":        self.experience_points,
            
            "ability_scores": {
                ability: getattr(self.ability_scores, ability)
                for ability in ABILITIES
            },

            "saving_throws": {
                ability: getattr(self.saving_throws, ability)
                for ability in ABILITIES
            },

            "skills": {
                skill: getattr(self.skills, skill)
                for skill in SKILL_ABILITY_MAP
            },

            "expertise": self.skills.expertise,

            #combat scenario
            "inspiration":      self.inspiration,
            "armor_class":      self.armor_class,
            "speed":            self.speed,
            "hit_points": {
                "maximum":      self.hit_points.maximum,
                "current":      self.hit_points.current,
                "minimum":      self.hit_points.temporary,
            },
            "hit_dice": {
                "total":        self.hit_dice.total,
                "remaining":    self.hit_dice.remaining,
            },
            "death_saves": {
                "successes":    self.death_saves.successes,
                "failures":     self.death_saves.failures,
            },
            "attacks": [{
                    "name":        atk.name,
                    "atk_bonus":   atk.atk_bonus,
                    "damage_type": atk.damage_type,
                }
                for atk in self.attacks
            ],
            "spellcasting_notes": self.spellcasting_notes,

            "personality_traits":   self.personality_traits,
            "ideals":               self.ideals,
            "bonds":                self.bonds,
            "flaws":                self.flaws,

            #bottom section
            "other_proficiencies_languages": self.other_proficiencies_languages,
            "equipment":                     self.equipment,
            "features_and_traits":           self.features_and_traits,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Character":
        #this will reconstruct  a character from the saved JSON dict...
        c = cls()
        
        #whattheactualfuck, wait so how, fuck it.
        #OH OKAY got it nvm

        # just like before...
        c.character_name =          data.get("character_name", "")
        c.class_name =              data.get("class_name", "")
        c.level =                   data.get("level", 1)
        c.background =              data.get("background", "")
        c.player_name =             data.get("player_name", "")
        c.race =                    data.get("race", "")
        c.half_elf_bonus_choices =  data.get("half_elf_bonus_choices", [])
        c.alignment =               data.get("alignment", "")
        c.experience_points =       data.get("experience_points", 0)

        for ability in ABILITIES:
            setattr(c.ability_scores, ability, 
                    data.get("ability_scores", {}).get(ability, 10))
            
        for ability in ABILITIES:
            setattr(c.saving_throws, ability,
                    data.get("saving_throws", {}).get(ability, False))
            
        for skill in SKILL_ABILITY_MAP:
            setattr(c.skills, skill,
                    data.get("skills", {}).get(skill, False))
            
        c.skills.expertise =        data.get("expertise",
                                             {s: False for s in SKILL_ABILITY_MAP})

        c.inspiration =             data.get("inspiration", False)
        c.armor_class =             data.get("armor_class", 10)
        c.speed =                   data.get("speed", 30)

        hp =                        data.get("hit_points", {})
        c.hit_points.maximum =      hp.get("maximum", 0)
        c.hit_points.current =      hp.get("current", 0)
        c.hit_points.temporary =    hp.get("temporary", 0)

        hd =                        data.get("hit_dice", {})
        c.hit_dice.total =          hd.get("total", "")
        c.hit_dice.remaining =      hd.get("remaining", 0)

        ds =                        data.get("death_saves", {})
        c.death_saves.successes =   ds.get("successes", 0)
        c.death_saves.failures =    ds.get("failures", 0)

        # i really don't understand what did i do wrong here but whatever
        c.attacks = [
            Attack(
                name=               a.get("name", ""),
                atk_bonus=          a.get("atk_bonus", ""),
                damage_type=        a.get("damage_type", "")
            )
            for a in data.get("attacks", [])
        ]
        c.spellcasting_notes =       data.get("spellcasting_notes", "")

        c.personality_traits =       data.get("personality_traits", "")

        c.ideals =                   data.get("ideals", "")
        c.bonds =                    data.get("bonds", "")
        c.flaws =                    data.get("flaws", "")

        c.other_proficiencies_languages = data.get("other_proficiencies_languages", "")
        c.equipment =                     data.get("equipment", "")
        c.features_and_traits =           data.get("features_and_traits", "")

        return c