REGION_CODE_DICT = {
    "SU": "Outskirts",
    "HI": "Industrial Complex",
    "DS": "Drainage System",
    "GW": "Garbage Wastes",
    "SL": "Shoreline",
    "VS": "Pipeyard",
    "SH": "Shaded Citadel",
    "UW": "The Exterior",
    "SS": "Five Pebbles",
    "CC": "Chimney Canopy",
    "SI": "Sky Islands",
    "LF": "Farm Arrays",
    "SB": "Subterranean",
    "MS": "Submerged Superstructure",
    "OE": "Outer Expanse",
    "LC": "Metropolis",
    "DM": "Looks to the Moon",
}

food_quest_items = [
    "SlimeMold", "DangleFruit", "Fly", "Mushroom", "BlackLizard", "WaterNut",
    "JellyFish", "JetFish", "GlowWeed", "Salamander", "Snail", "Hazer",
    "EggBug", "LillyPuck", "YellowLizard", "TubeWorm", "SSOracleSwarmer", "Centiwing",
    "DandelionPeach", "CyanLizard", "GooieDuck", "RedCentipede"
]

scug_names = {
    "monk": "Yellow",
    "survivor": "White",
    "hunter": "Red",
    "gourmand": "Gourmand",
    "artificer": "Artificer",
    "rivulet": "Rivulet",
    "spearmaster": "Spear",
    "saint": "Saint",
    "sofanthiel": "Sofanthiel",
    0: "Yellow",
    1: "White",
    2: "Red",
    10: "Yellow",
    11: "White",
    12: "Red",
    13: "Gourmand",
    14: "Artificer",
    15: "Rivulet",
    16: "Spear",
    17: "Saint",
    18: "Sofanthiel"
}

default_starting_regions = {
    "Yellow": "Outskirts",
    "White": "Outskirts",
    "Red": "Farm Arrays",
    "Gourmand": "Shaded Citadel",
    "Artificer": "Garbage Wastes",
    "Rivulet": "Drainage System",
    "Spear": "Outskirts filtration",
    "Saint": "Sky Islands",
    "Sofanthiel": "Shaded Citadel"
}

passages = ["Chieftain", "DragonSlayer", "Friend", "Hunter", "Martyr", "Monk", "Mother",
            "Nomad", "Outlaw", "Pilgrim", "Saint", "Scholar", "Survivor", "Wanderer"]

prioritizable_passages = set(passages) - {"Chieftain", "Wanderer", "Mother"}

regions = {
    1: "Outskirts",
    2: "Industrial Complex",
    3: "Drainage System",
    4: "Garbage Wastes",
    5: "Shoreline",
    6: "Shaded Citadel",
    7: "The Exterior",
    8: "Five Pebbles",
    9: "Chimney Canopy",
    10: "Sky Islands",
    11: "Farm Arrays",
    12: "Subterranean",

    20: "Pipeyard"
}

regions_vanilla = ["SU", "HI", "DS", "GW", "SL", "VS", "SH", "UW", "SS", "CC", "SI", "LF", "SB"]
