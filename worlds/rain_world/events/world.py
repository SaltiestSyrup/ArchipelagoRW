from typing import Iterable

from BaseClasses import ItemClassification, MultiWorld, Item, Location
from ..options import RainWorldOptions

from ..game_data.general import scugs_all, scugs_vanilla, region_code_to_name
from ..conditions.classes import Simple, AnyOf, AllOf, Condition
from ..game_data.files import placed_objects, creatures
from ...generic.Rules import add_rule


class ObjectEventData2:
    def __init__(self, item_name: str, location_name: str, region: str, condition: Condition, regions: Iterable[str]):
        self.item_name = item_name
        self.location_item = location_name
        self.region = region
        self.classification = ItemClassification.progression
        self.condition = condition
        self.regions = regions

    def make(self, player: int, multiworld: MultiWorld):
        regions = {r for r in self.regions if multiworld.get_region(region_code_to_name[r], player).populate}

        if len(regions) > 0:
            item = Item(self.item_name, self.classification, None, player)
            region = multiworld.get_region(self.region, player)
            location = Location(player, self.location_item, None, region)
            region.locations.append(location)
            location.place_locked_item(item)
            add_rule(location, self.condition.check(player))


def generate_events(which: str) -> list[ObjectEventData2]:
    ret = []
    data = placed_objects if which == "placed_objects" else creatures["normal"]

    for otype, by_otype in data.items():
        condition = \
            AnyOf(
                *[AllOf(
                    Simple("MSC", neg),
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
                ) for neg, dlcstate, scugs in zip((True, False), ("Vanilla", "MSC"), (scugs_vanilla, scugs_all))]
            )

        ret.append(ObjectEventData2(otype, otype, "Events", condition))
    return ret


def generate_events_for_one_gamestate(which: str, options: RainWorldOptions) -> list[ObjectEventData2]:
    dlcstate = "MSC" if options.msc_enabled else "Vanilla"
    scug = options.starting_scug

    ret = []
    data = placed_objects if which == "placed_objects" else creatures["normal"]

    for otype, by_otype in data.items():
        regions = set(room.split("_")[0] for room in by_otype[dlcstate][scug] + by_otype[dlcstate]["*ALL"])

        if len(regions) != 0:
            condition = \
                AllOf(
                    Simple("MSC", negative=not options.msc_enabled),
                    Simple(f"Scug-{scug}"),
                    Simple([f"Access-{region}" for region in regions], 1)
                )
            ret.append(ObjectEventData2(otype, otype, "Events", condition, regions))

    return ret
