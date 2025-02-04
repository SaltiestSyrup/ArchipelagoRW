#################################################################
# REGION DATA
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
    "CL": "Silent Construct",
    "RM": "The Rot",
    "UG": "Undergrowth",
    "LM": "Waterfront Facility",
    "HR": "Rubicon",
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

regions_vanilla = ["SU", "HI", "DS", "GW", "SL", "SH", "UW", "SS", "CC", "SI", "LF", "SB"]

#################################################################
# SCUG DATA
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

scugs_msc = ['Yellow', 'White', 'Red', 'Gourmand', 'Artificer', 'Rivulet', 'Spear', 'Saint', 'Inv']
scugs_vanilla = ['Yellow', 'White', 'Red']

#################################################################
# PASSAGE DATA
passages = ["Chieftain", "DragonSlayer", "Friend", "Hunter", "Martyr", "Monk", "Mother",
            "Nomad", "Outlaw", "Pilgrim", "Saint", "Scholar", "Survivor", "Wanderer"]
# Passages that can't be automatically set as priority until early logic detection improves.
prioritizable_passages = set(passages) - {"Chieftain", "Wanderer", "Mother"}

food_quest_items = [
    "SlimeMold", "DangleFruit", "Fly", "Mushroom", "BlackLizard", "WaterNut",
    "JellyFish", "JetFish", "GlowWeed", "Salamander", "Snail", "Hazer",
    "EggBug", "LillyPuck", "YellowLizard", "TubeWorm", "SSOracleSwarmer", "Centiwing",
    "DandelionPeach", "CyanLizard", "GooieDuck", "RedCentipede"
]

dragonslayer_vanilla = ["GreenLizard", "PinkLizard", "BlueLizard", "WhiteLizard", "YellowLizard", "BlackLizard"]
dragonslayer_msc = dragonslayer_vanilla + ["CyanLizard", "RedLizard", "SpitLizard", "ZoopLizard"]
lizards_any = dragonslayer_msc + ["Salamander", "EelLizard", "TrainLizard"]
