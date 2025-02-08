from typing import Iterable

from BaseClasses import ItemClassification, MultiWorld, Item, Location, CollectionState
from worlds.generic.Rules import add_rule
from ..game_data.general import region_code_to_name
from ..conditions.classes import Condition


class EventData:
    def __init__(self, item_name: str, location_name: str, region: str,
                 classification: ItemClassification = ItemClassification.progression,
                 condition: Condition = None):
        self.item_name = item_name
        self.location_item = location_name
        self.region = region
        self.classification = classification
        self.condition = condition

    def make(self, player: int, multiworld: MultiWorld):
        region = multiworld.get_region(self.region, player)
        if region.populate:
            item = Item(self.item_name, self.classification, None, player)
            location = Location(player, self.location_item, None, region)
            region.locations.append(location)
            location.place_locked_item(item)
            if self.condition is not None:
                add_rule(location, self.condition.check(player))


class VictoryEvent(EventData):
    def __init__(self, location_name: str, region: str, condition: Condition = None):
        # Note: events have to be progression even if they're not used in the condition for another conn/loc
        super().__init__("Victory", location_name, region, condition=condition)


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
