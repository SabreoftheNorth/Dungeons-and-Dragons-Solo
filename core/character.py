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
    race:               str = "" #i am obsessed with elves
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
    
#TODO CONTINUE