from typing import NamedTuple

from BaseClasses import MultiWorld, Item, ItemClassification, Location
from worlds.rain_world.constants import REGION_CODE_DICT
from worlds.rain_world.utils import flatten
from . import game_data


class EventData(NamedTuple):
    item_name: str
    location_item: str
    region: str
    classification: ItemClassification = ItemClassification.progression

    def make(self, player: int, multiworld: MultiWorld):
        item = Item(self.item_name, self.classification, None, player)
        region = multiworld.get_region(self.region, player)
        location = Location(player, self.location_item, None, region)
        region.locations.append(location)
        location.place_locked_item(item)


all_events: list[EventData] = [
    EventData(f"Access-{short}", f"Access-{short}", full)
    for short, full in game_data.REGION_CODE_DICT.items()
]

########################################################################
# Events tracking what Lizards are accessible for things like Dragon Slayer


