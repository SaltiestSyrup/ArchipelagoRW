OBJECTS = {
    "SlimeMold": ["SH", "UW"],
    "DangleFruit": ["SL", "SB", "UW", "SU", "HI", "SH", "CC", "DS", "GW", "SI", "LF"],
    "Fly": ["SU", "HI", "DS", "GW", "SL", "SH", "UW", "CC", "SI", "LF", "SB", "VS", "MS"],
    "Mushroom": ["SB", "DS", "SU", "LF", "SH", "CC", "UW", "GW", "HI", "SI", "VS", "OE"],
    "WaterNut": ["GW", "DS", "SL", "SB", "SH", "HI", "LF"],
    "JellyFish": ["MS", "SL"],
    "JetFish": ["SL", "SB", "MS", "VS"],
    "GlowWeed": ["SL", "SB", "MS"],
    "Snail": ["DS", "SL", "CC", "MS", "GW", "VS"],
    "Hazer": ["HI", "GW", "SL", "DS", "LF", "SU"],
    "EggBug": ["SU", "SH", "SI", "LF", "HI", "GW", "CC", "SB", "VS"],
    "LillyPuck": ["DS", "VS"],
    "TubeWorm": ["UW", "CC"],
    "Centiwing": ["SI"],
    "DandelionPeach": ["SI"],
    "GooieDuck": ["LF", "SB", "OE"],
    "RedCentipede": ["SL", "MS", "GW", "SB", "VS"],  # TODO
    "BlueLizard": ["SU", "HI", "UW", "CC", "SI", "LF", "SB", "MS"],
    "BlackLizard": ["SH", "SB", "VS"],
    "Salamander": ["DS", "SL", "SB", "VS", "CC", "MS"],  # TODO
    "YellowLizard": ["UW", "SI", "MS"],
    "CyanLizard": ["HI", "DS", "GW", "UW", "CC", "SI", "SB", "VS"],
    "GreenLizard": ["SU", "GW", "LF", "DS"],
    "PinkLizard": ["SU", "HI", "SL", "CC", "SI", "LF"],
    "RedLizard": ["SU", "HI"],
    "SSOracleSwarmer": ["SL", "SS"],
}


lizzies = {
    'SU': ['BlueLizard', 'GreenLizard', 'PinkLizard', 'RedLizard', 'WhiteLizard'],
    'HI': ['BlueLizard', 'CyanLizard', 'PinkLizard', 'RedLizard', 'WhiteLizard'],
    'GW': ['SpitLizard', 'CyanLizard', 'GreenLizard', 'PinkLizard'],
    'SL': ['CyanLizard', 'WhiteLizard', 'Salamander'],
    'SH': ['BlackLizard'],
    'UW': ['BlueLizard', 'CyanLizard', 'WhiteLizard', 'YellowLizard'],
    'CC': ['BlueLizard', 'SpitLizard', 'CyanLizard', 'EelLizard', 'PinkLizard', 'WhiteLizard'],
    'SI': ['BlueLizard', 'CyanLizard', 'PinkLizard', 'WhiteLizard', 'YellowLizard'],
    'LF': ['BlueLizard', 'SpitLizard', 'GreenLizard', 'PinkLizard'],
    'SB': ['BlackLizard', 'BlueLizard', 'SpitLizard', 'CyanLizard', 'Salamander'],
    'DS': ['CyanLizard', 'GreenLizard', 'Salamander'],
    'VS': ['BlackLizard', 'CyanLizard', 'Salamander'],
    'MS': ['Blue', 'Eel', 'White', 'Yellow'],
    'OE': [],
}

food_quest_items = [
    "SlimeMold", "DangleFruit", "Fly", "Mushroom", "BlackLizard", "WaterNut",
    "JellyFish", "JetFish", "GlowWeed", "Salamander", "Snail", "Hazer",
    "EggBug", "LillyPuck", "YellowLizard", "TubeWorm", "SSOracleSwarmer", "Centiwing",
    "DandelionPeach", "CyanLizard", "GooieDuck", "RedCentipede"
]


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
    # "OE": "Outer Expanse",
    # "LC": "Metropolis",
    # "DM": "Looks to the Moon",
}
