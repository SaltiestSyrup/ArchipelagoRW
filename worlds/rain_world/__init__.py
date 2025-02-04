import random
from typing import Mapping, Any

from .conditions.classes import Simple
from .game_data.general import REGION_CODE_DICT
from .events import all_events
from .utils import normalize, flounder2
from .items import RainWorldItem, all_items, RainWorldItemData
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, ItemClassification, Tutorial, LocationProgressType
from . import constants
from .options import RainWorldOptions
from .classes import location_name_to_id, RainWorldRegion, RegionData
from .regions import all_regions, all_connections
from .locations import all_locations, location_map
from .conditions import all_rules
from Utils import visualize_regions
from .game_data.general import scug_names, default_starting_regions, prioritizable_passages, regions


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

        #################################################################
        # PRIORITY PASSAGES
        passage_locations = [
            loc for loc in
            [self.multiworld.get_location(f'Passage-{passage}', self.player) for passage in prioritizable_passages]
            if loc.progress_type == LocationProgressType.DEFAULT
        ]

        num = max(0, min(self.options.passage_priority.value, len(passage_locations)))

        for passage in random.sample(passage_locations, num):
            passage.progress_type = LocationProgressType.PRIORITY

        #################################################################
        # PPWS: add a new free connection if PPWS is enabled.
        if self.options.passage_progress_without_survivor:
            self.multiworld.get_region('Menu', self.player).connect(
                self.multiworld.get_region('PPwS Passages', self.player)
            )

        #################################################################
        # STARTING REGION
        if self.options.random_starting_region.value == 0:
            self.starting_region = default_starting_regions[scug_names[self.options.which_gamestate.value]]
        else:
            self.starting_region = regions[self.options.random_starting_region.value]

        start = self.multiworld.get_region(self.starting_region, self.player)
        self.multiworld.get_region('Starting region', self.player).connect(start)

    def create_item(self, name: str) -> RainWorldItem:
        return items.all_items[name].generate_item(self.player)

    def create_items(self) -> None:
        added_items = 0

        #################################################################
        # TESTING
        # all_items["Karma"].count -= 1
        # self.multiworld.get_location("Passage-DragonSlayer", self.player).place_locked_item(self.create_item("Karma"))

        #################################################################
        # STARTING ITEM SETTINGS
        all_items["Karma"].count += self.options.extra_karma_cap_increases
        # all_items["Karma cap increase"].precollect += self.options.starting_karma - 1

        #################################################################
        # FAUX ITEM SETTINGS
        self.multiworld.push_precollected(self.create_item(f"Scug-{scug_names[self.options.which_gamestate.value]}"))
        if self.options.which_gamestate.value > 9:
            self.multiworld.push_precollected(self.create_item("MSC"))

        #################################################################
        # PREDETERMINED POPULATION
        for item_data in items.all_items.values():
            for i in range(item_data.count):
                if i >= item_data.precollect:
                    self.multiworld.itempool.append(item_data.generate_item(self.player))
                    added_items += 1
                else:
                    self.multiworld.push_precollected(item_data.generate_item(self.player))
                    item_data.precollect -= 1

        #################################################################
        # FILLER POPULATION
        remaining_slots = self.location_count - added_items
        trap_fraction = self.options.pct_traps / 100

        nontrap_weights = normalize(self.options.get_nontrap_weight_dict())

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

    def set_rules(self) -> None:
        ascension_item = Item("Ascension", ItemClassification.progression, None, self.player)
        self.multiworld.get_location("Ascension", self.player).place_locked_item(ascension_item)
        self.multiworld.completion_condition[self.player] = Simple("Ascension").check(self.player)

        for data in all_rules:
            data.make(self.player, self.multiworld)

        visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml", show_locations=False)

    def fill_slot_data(self) -> Mapping[str, Any]:
        d = self.options.as_dict("which_gamestate", "random_starting_region", "passage_progress_without_survivor")
        return d
