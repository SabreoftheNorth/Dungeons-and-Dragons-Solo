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
    #TODO: CONTINUE