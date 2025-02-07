from BaseClasses import MultiWorld, Item, ItemClassification, Location
from .. import game_data


class EventData:
    item_name: str
    location_item: str
    region: str
    classification: ItemClassification

    def __init__(self, item_name: str, location_name: str, region: str,
                 classification: ItemClassification = ItemClassification.progression):
        self.item_name = item_name
        self.location_item = location_name
        self.region = region
        self.classification = classification

    def make(self, player: int, multiworld: MultiWorld):
        region = multiworld.get_region(self.region, player)
        if region.populate:
            item = Item(self.item_name, self.classification, None, player)
            location = Location(player, self.location_item, None, region)
            region.locations.append(location)
            location.place_locked_item(item)


def generate_events():
    return [
        EventData(f"Access-{short}", f"Access-{short}", full)
        for short, full in game_data.general.REGION_CODE_DICT.items()
    ]
