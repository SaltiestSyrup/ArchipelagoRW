import random
from typing import Mapping, Any

from .constants import REGION_CODE_DICT
from .events import all_events
from .general_helpers import flounder2, normalize
from .items import RainWorldItem, all_items, RainWorldItemData
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, ItemClassification, Tutorial, LocationProgressType
from . import constants, state_helpers
from .options import RainWorldOptions
from .classes import location_name_to_id, RainWorldRegion, RegionData
from .regions_new import all_regions, all_connections
from .locations_new import all_locations, location_map
from .rules import all_rules
from Utils import visualize_regions


class RainWorldWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Rain World for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["alphappy"]
    )]
    option_groups = options.option_groups


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
    starting_region = 'SU'

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

        for n in range(self.options.maximum_required_food_quest_pips + 1, 23):
            self.multiworld.get_location(f'FQ|{n}', self.player).progress_type = (
                LocationProgressType.EXCLUDED)

        if self.options.passage_progress_without_survivor:
            self.multiworld.get_region('Menu', self.player).connect(
                self.multiworld.get_region('PPwS Passages', self.player)
            )

        if self.options.random_starting_shelter:
            self.starting_region = random.choice(['SU', 'HI', 'DS', 'LF'])

        start = self.multiworld.get_region(REGION_CODE_DICT[self.starting_region], self.player)
        self.multiworld.get_region('Starting region', self.player).connect(start)

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
        # all_items["Karma cap increase"].precollect += self.options.starting_karma - 1

        for item_data in items.all_items.values():
            for i in range(item_data.count):
                if i >= item_data.precollect:
                    self.multiworld.itempool.append(item_data.generate_item(self.player))
                    added_items += 1
                else:
                    self.multiworld.push_precollected(item_data.generate_item(self.player))
                    item_data.precollect -= 1

        remaining_slots = self.location_count - added_items
        trap_fraction = self.options.pct_traps / 100

        nontrap_weights = normalize({
            "Rock": self.options.wt_rocks / 100,
            "Spear": self.options.wt_spears / 100,
            "Grenade": self.options.wt_grenades / 100,
            "Fuit": self.options.wt_fruit / 100,
        })

        trap_weights = normalize({
            "Stun Trap": self.options.wt_stuns / 100,
            "Zoomies Trap": self.options.wt_zoomies / 100,
            "Timer Trap": self.options.wt_timers / 100,
            "Red Lizard Trap": self.options.wt_redlizard / 100,
            "Red Centipede Trap": self.options.wt_redcentipede / 100,
            "Spitter Spider Trap": self.options.wt_spitterspider / 100
        })

        d: dict[str, float] = {}
        d.update({k: v * (1 - trap_fraction) for k, v in nontrap_weights.items()})
        d.update({k: v * trap_fraction for k, v in trap_weights.items()})

        self.multiworld.itempool += [self.create_item(e) for e in flounder2(d, remaining_slots)]
        #
        # filler_weight_total = sum(items.filler_weights.values())
        # for item_name, weight in items.filler_weights.items():
        #     amt = int(fillers_to_add * weight / filler_weight_total)
        #     for _ in range(amt):
        #         self.multiworld.itempool.append(self.create_item(item_name))
        #     added_items += amt
        #
        # trap_weight_total = sum(items.trap_weights.values())
        # for item_name, weight in items.trap_weights.items():
        #     amt = int(traps_to_add * weight / trap_weight_total)
        #     for _ in range(amt):
        #         self.multiworld.itempool.append(self.create_item(item_name))
        #     added_items += amt

        # for _ in range(self.location_count - added_items):
        #     self.multiworld.itempool.append(self.create_item("Rock"))

    def set_rules(self) -> None:
        ascension_item = Item("Ascension", ItemClassification.progression, None, self.player)
        self.multiworld.get_location("Ascension", self.player).place_locked_item(ascension_item)
        self.multiworld.completion_condition[self.player] = state_helpers.ascension(self.player)

        for data in all_rules:
            data.make(self.player, self.multiworld)

        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml", show_locations=False)

    def fill_slot_data(self) -> Mapping[str, Any]:
        d = self.options.as_dict("which_worldstate", "food_quest_mode")
        d['STARTING_SHELTER'] = self.starting_region
        return d
