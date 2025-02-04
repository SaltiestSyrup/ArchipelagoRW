import json
import os.path
from typing import Callable

from BaseClasses import CollectionState

from .general import REGION_CODE_DICT, food_quest_items, scugs_msc, scugs_vanilla
from ..classes import Simple, ConditionBlank, AnyOf, AllOf
from .files import placed_objects


def generate_events(constructor: Callable):
    ret = []
    for otype, by_otype in placed_objects.items():
        condition = \
            AnyOf(
                *[AllOf(
                    Simple("MSC", negative=neg),
                    AnyOf(
                        *[AllOf(
                            Simple(f"Scug-{scug}"),
                            Simple(
                                [
                                    f"Access-{region}" for region in
                                    set(room.split("_")[0] for room in
                                        by_otype[dlcstate][scug] + by_otype[dlcstate]["*ALL"])
                                ],
                                1
                            )
                        ) for scug in scugs]
                    )
                ) for neg, dlcstate, scugs in zip((True, False), ("Vanilla", "MSC"), (scugs_vanilla, scugs_msc))]
            )

        ret.append(constructor(otype, otype, "Events", condition))
    return ret
