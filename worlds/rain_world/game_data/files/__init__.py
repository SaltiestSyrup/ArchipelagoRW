__all__ = ['placed_objects', 'creatures', 'white_tokens']

import json
from os.path import dirname, realpath, join
from ..general import regions_vanilla

realpath = dirname(realpath(__file__))

# Dictionary of PlacedObjects.  data[objtype][dlcstate][scug] -> list of rooms.
placed_objects: dict[str, dict[str, [dict[str, list[str]]]]] = json.load(open(join(realpath, "placed_objects.json")))

# Dictionary of creature spawners.  data[dentype][crittype][dlcstate][scug] -> list of rooms.
creatures: dict[str, dict[str, dict[str, [dict[str, list[str]]]]]] = json.load(open(join(realpath, "creatures.json")))

creatures["normal"]["Fly"] = {
    "Vanilla": {"Yellow": [], "White": [], "Red": [],
                "*ALL": [f"{r}_dummy" for r in set(regions_vanilla).difference({"SS"})]},
    "MSC": {
        "Yellow": [f"{r}_dummy" for r in {"DS", "SL", "SH", "UW", "MS", "OE"}],
        "White": [f"{r}_dummy" for r in {"DS", "SL", "SH", "UW", "MS", "OE"}],
        "Red": [f"{r}_dummy" for r in {"DS", "SL", "SH", "UW", "MS"}],
        "Gourmand": [f"{r}_dummy" for r in {"DS", "SL", "SH", "UW", "MS", "OE"}],
        "Artificer": [f"{r}_dummy" for r in {"DS", "LM", "SH", "UW", "LC"}],
        "Rivulet": [f"{r}_dummy" for r in {"DS", "SL", "SH", "UW", "MS"}],
        "Spear": [f"{r}_dummy" for r in {"DS", "SH", "UW", "LM", "DM"}],
        "Saint": [f"{r}_dummy" for r in {"SL", "MS", "UG", "CL"}],
        "*ALL": [f"{r}_dummy" for r in {"SU", "HI", "GW", "CC", "SI", "LF", "SB", "VS"}]
    }
}

creatures["normal"]["SSOracleSwarmer"] = {
    "Vanilla": {"Yellow": [], "White": [], "Red": [], "*ALL": [f"{r}_dummy" for r in {"SL", "SS"}]},
    "MSC": {
        **{scug: [f"{r}_dummy" for r in {"SL", "SS"}]
           for scug in ["Yellow", "White", "Red", "Gourmand"]},
        "Artificer": [f"{r}_dummy" for r in {"LC", "SS"}],
        "Rivulet": [f"{r}_dummy" for r in {"RM", "SL"}],
        "Spear": [f"{r}_dummy" for r in {"DM", "SS"}],
        "Saint": ["SL_dummy"],
        "*ALL": []
    }
}

# Dictionary of white (broadcast) tokens.  data[id] -> {"room": room, "blacklist": list of scugs}.
white_tokens: dict[str, dict[str, str | list[str]]] = json.load(open(join(realpath, "white_tokens.json")))
