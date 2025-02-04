__all__ = ["dragonslayer_vanilla", "dragonslayer_msc", "lizards_any", "data"]

import json
import os.path
from typing import Callable

from BaseClasses import CollectionState

from .general import REGION_CODE_DICT, food_quest_items

fp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "creatures.json")
data = json.load(open(fp))  # data[gamestate][scug][crit][spawntype] -> list of regions
dragonslayer_vanilla = ["GreenLizard", "PinkLizard", "BlueLizard", "WhiteLizard", "YellowLizard", "BlackLizard"]
dragonslayer_msc = dragonslayer_vanilla + ["CyanLizard", "RedLizard", "SpitLizard", "ZoopLizard"]
lizards_any = dragonslayer_msc + ["Salamander", "EelLizard", "TrainLizard"]


def generate_events(constructor: Callable):
    ret = []
    for region_short, region_full in REGION_CODE_DICT.items():
        for crit in list(set(lizards_any + food_quest_items)):
            conditions = []
            for gamestate, by_gamestate in data.items():
                for scug, by_scug in by_gamestate.items():
                    if crit in by_scug.keys():
                        if region_short in by_scug[crit]["normal"]:
                            conditions.append((gamestate, scug, "normal"))
            if conditions:
                ret.append(constructor(crit, f"{region_short} {crit}", region_full, conditions))

    return ret




