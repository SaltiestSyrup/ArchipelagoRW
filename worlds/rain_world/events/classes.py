from BaseClasses import ItemClassification, MultiWorld, Item, Location, CollectionState
from worlds.generic.Rules import add_rule


class EventData:
    item_name: str
    location_item: str
    region: str
    classification: ItemClassification

    def __init__(self, item_name: str, location_name: str, region: str, classification: ItemClassification = ItemClassification.progression):
        self.item_name = item_name
        self.location_item = location_name
        self.region = region
        self.classification = classification

    def make(self, player: int, multiworld: MultiWorld):
        item = Item(self.item_name, self.classification, None, player)
        region = multiworld.get_region(self.region, player)
        location = Location(player, self.location_item, None, region)
        region.locations.append(location)
        location.place_locked_item(item)


class ObjectEventData:
    def __init__(self, item_name: str, location_name: str, region: str, conditions: list[tuple]):
        self.item_name = item_name
        self.location_item = location_name
        self.region = region
        self.classification = ItemClassification.progression
        self.conditions = conditions

    def access_rule(self):
        def factory(player: int):
            def inner(state: CollectionState) -> bool:
                for gamestate, scug, spawntype in self.conditions:
                    if state.has("MSC", player) == (gamestate == "MSC"):
                        if state.has(f"Scug-{scug}", player):
                            return True
                return False
            return inner
        return factory

    def make(self, player: int, multiworld: MultiWorld):
        item = Item(self.item_name, self.classification, None, player)
        region = multiworld.get_region(self.region, player)
        location = Location(player, self.location_item, None, region)
        region.locations.append(location)
        location.place_locked_item(item)
        add_rule(location, self.access_rule()(player))


