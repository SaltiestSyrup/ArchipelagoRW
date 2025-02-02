__all__ = ["can_access_creature_factory_factory", "can_access_multiple_creatures_factory_factory",
           "can_access_dragonslayer_factory",
           "dragonslayer_vanilla", "dragonslayer_msc", "lizards_any", "data"]

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


def can_access_creature_factory_factory(name: str) -> Callable[[int], Callable[[CollectionState], bool]]:
    def can_access_creature_factory(player: int) -> Callable[[CollectionState], bool]:
        def can_access_creature(state: CollectionState) -> bool:
            return state.has(name, player)
            # try:
            #     regions = data["MSC" if state.has("MSC", player) else "Vanilla"]["Red"][name]["normal"]
            #     return state.has_any((f"Access-{region}" for region in regions), player)
            # except KeyError:
            #     return False
        return can_access_creature
    return can_access_creature_factory


def can_access_multiple_creatures_factory_factory(names: list[str], count: int) -> Callable[[int], Callable[[CollectionState], bool]]:
    def can_access_multiple_creatures_factory(player: int) -> Callable[[CollectionState], bool]:
        def can_access_multiple_creatures(state: CollectionState) -> bool:
            return state.has_from_list_unique(names, player, count)
            # hits = 0
            # for name in names:
            #     try:
            #         regions = data["MSC" if state.has("MSC", player) else "Vanilla"]["Red"][name]["normal"]
            #         if state.has_any((f"Access-{region}" for region in regions), player):
            #             hits += 1
            #             if hits >= count:
            #                 return True
            #     except KeyError:
            #         continue
            # return False
        return can_access_multiple_creatures
    return can_access_multiple_creatures_factory


def can_access_dragonslayer_factory(player: int) -> Callable[[CollectionState], bool]:
    def can_access_multiple_creatures(state: CollectionState) -> bool:
        return state.has_from_list_unique(
            dragonslayer_msc if state.has("MSC", player) else dragonslayer_vanilla,
            player, 6
        )

        # hits = 0
        # msc = state.has("MSC", player)
        # for name in dragonslayer_msc if msc else dragonslayer_vanilla:
        #     regions = data["MSC" if msc else "Vanilla"]["Red"][name]["normal"]
        #     if state.has_any((f"Access-{region}" for region in regions), player):
        #         hits += 1
        #         if hits >= 6:
        #             return True
        # return False

    return can_access_multiple_creatures

