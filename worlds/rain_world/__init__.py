import random

from .events import all_events
from .items import RainWorldItem, all_items, RainWorldItemData  # data used below to add items to the World
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, ItemClassification, Tutorial, LocationProgressType
from . import constants, state_helpers
from .options import RainWorldOptions
from .classes import location_name_to_id, RainWorldRegion, RegionData
from .regions_new import all_regions, all_connections
from .locations_new import all_locations, location_map
from .rules import all_rules


class RainWorldWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Rain World for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["alphappy"]
    )]


class RainWorldWorld(World):
    """You are a nomadic slugcat, both predator and prey in a broken ecosystem. Grab your spear and brave the
    industrial wastes, hunting enough food to survive, but be wary— other, bigger creatures have the same plan...
    and slugcats look delicious."""
    game = "Rain World"  # name of the game/world
    options_dataclass = RainWorldOptions  # options the player can set
    options: RainWorldOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler
    web = RainWorldWebWorld()

    item_name_to_id = items.item_name_to_id
    location_name_to_id = location_map

    # Items can be grouped using their names to allow easy checking if any item
    # from that group has been collected. Group names can also be used for !hint
    # item_name_groups = {
    #     "lizard_kills": {"sword", "lance"},
    # }

    location_count = 0

    def create_regions(self):
        for data in all_regions:
            data.make(self.player, self.multiworld)

        for data in all_connections:
            data.make(self.player, self.multiworld)

        for data in all_locations:
            data.make(self.player, self.multiworld)

        for data in all_events:
            data.make(self.player, self.multiworld)

        self.location_count = len(all_locations)

        priority_locs = ["FQ|12"]
        for name in priority_locs:
            self.multiworld.get_location(name, self.player).progress_type = LocationProgressType.PRIORITY

        for n in range(self.options.maximum_required_food_quest_pips + 1, 23):
            self.multiworld.get_location(f'FQ|{n}', self.player).progress_type = (
                LocationProgressType.EXCLUDED)

        # menu_region = Region("Menu", self.player, self.multiworld)
        #
        # true_regions: list[RainWorldRegion] = [
        #     data.generate_region(self.player, self.multiworld) for data in actual_regions.values()
        # ]
        #
        # voidsea_region = Region("Void Sea", self.player, self.multiworld)
        # voidsea_region.locations.append(Location(self.player, "Ascension", None, voidsea_region))
        #
        # self.multiworld.regions += [menu_region] + true_regions
        #
        # self.multiworld.get_region('SB', self.player).connect(voidsea_region, rule=state_helpers.max_karma_at_least(10, self.player))
        #
        # for connection in vanilla_connections:
        #     left = self.multiworld.get_region(connection.left_region, self.player)
        #     right = self.multiworld.get_region(connection.right_region, self.player)
        #     left.connect(right, rule=state_helpers.karma_and_key(self.player, connection.left_cost, right.name))
        #     right.connect(left, rule=state_helpers.karma_and_key(self.player, connection.right_cost, left.name))
        #     # left.connect(right, rule=state_helpers.max_karma_at_least(connection.left_cost, self.player))
        #     # right.connect(left, rule=state_helpers.max_karma_at_least(connection.right_cost, self.player))
        #
        # menu_region.add_exits(['SU'])
        # self.location_count = sum(len(r.locations) for r in true_regions)

    def create_item(self, name: str) -> RainWorldItem:
        return items.all_items[name].generate_item(self.player)

    def create_items(self) -> None:
        added_items = 0

        if self.options.region_keys > 0:
            item: RainWorldItemData
            for item in random.sample([v for k, v in all_items.items() if k.startswith("Key to")],
                                      k=self.options.region_keys.value):
                item.precollect += 1

        all_items["Karma cap increase"].count += self.options.extra_karma_cap_increases
        all_items["Karma cap increase"].precollect += self.options.starting_karma - 1

        for item_data in items.all_items.values():
            for i in range(item_data.count):
                if i >= item_data.precollect:
                    self.multiworld.itempool.append(item_data.generate_item(self.player))
                    added_items += 1
                else:
                    self.multiworld.push_precollected(item_data.generate_item(self.player))
                    item_data.precollect -= 1

        for _ in range(self.location_count - added_items):
            self.multiworld.itempool.append(self.create_item("Rock"))

    def set_rules(self) -> None:
        ascension_item = Item("Ascension", ItemClassification.progression, None, self.player)
        self.multiworld.get_location("Ascension", self.player).place_locked_item(ascension_item)
        self.multiworld.completion_condition[self.player] = state_helpers.ascension(self.player)

        for data in all_rules:
            data.make(self.player, self.multiworld)

        from Utils import visualize_regions
        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml", show_locations=False)
