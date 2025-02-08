__all__ = ["RainWorldWorld", "RainWorldWebWorld"]

from typing import Mapping, Any

from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, ItemClassification, Tutorial
from .options import RainWorldOptions
from .conditions.classes import Simple
from .game_data.general import region_code_to_name
from .events import get_events
from .utils import normalize, flounder2
from .items import RainWorldItem, all_items, RainWorldItemData
from . import locations
from .regions import all_regions, all_connections
from .game_data.general import (
    setting_to_scug_id, scug_id_to_starting_region, prioritizable_passages, regions, passages_all, passages_vanilla)


class RainWorldWebWorld(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Rain World for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["alphappy"]
    )]
    option_groups = options.option_groups
    rich_text_options_doc = True
    theme = "ocean"
    bug_report_page = "https://github.com/alphappy/ArchipelagoRW/issues"


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
    location_name_to_id = locations.classes.location_map

    location_count = 0
    starting_region = 'SU'

    def create_regions(self):
        for data in all_regions:
            data.make(self.player, self.multiworld, self.options)

        for data in all_connections:
            data.make(self.player, self.multiworld)

        # return for each datum is a bool for whether that location was actually generated
        locs = [data.make(self.player, self.multiworld, self.options) for data in locations.generate(self.options)]
        self.location_count = sum(locs)

        for data in get_events(self.options):
            data.make(self.player, self.multiworld)

        #################################################################
        # PRIORITY PASSAGES: pick a number of passages matching the relevant option
        # that are not already prioritized and are prioritizable
        # passage_locations = [
        #     loc for loc in
        #     [self.multiworld.get_location(f'Passage-{passage}', self.player) for passage in prioritizable_passages]
        #     if loc.progress_type == LocationProgressType.DEFAULT
        # ]
        #
        # num = max(0, min(self.options.passage_priority.value, len(passage_locations)))
        #
        # for passage in random.sample(passage_locations, num):
        #     passage.progress_type = LocationProgressType.PRIORITY

        #################################################################
        # PPWS: add a new free connection if PPWS is enabled.
        if self.options.passage_progress_without_survivor:
            self.multiworld.get_region('Menu', self.player).connect(
                self.multiworld.get_region('PPwS Passages', self.player)
            )

        #################################################################
        # STARTING REGION
        if self.options.random_starting_region.value == 0:
            self.starting_region = scug_id_to_starting_region[setting_to_scug_id[self.options.which_gamestate.value]]
        else:
            self.starting_region = regions[self.options.random_starting_region.value]

        start = self.multiworld.get_region(self.starting_region, self.player)
        self.multiworld.get_region('Starting region', self.player).connect(start)

    def create_item(self, name: str) -> RainWorldItem:
        return items.all_items[name].generate_item(self.player)

    def create_items(self) -> None:
        added_items = 0

        pool = {
            "Karma": 8 + self.options.extra_karma_cap_increases.value,
            **{k: 1 for k in items.all_items.keys() if k.startswith("GATE")},
            **{f"Passage-{p}": 1 for p in (passages_all if self.options.msc_enabled else passages_vanilla)},
            "The Mark": 1,
            "The Glow": 1,
            "Object-NSHSwarmer": 1 if self.options.starting_scug == "Red" else 0,
            "IdDrone": 1 if self.options.starting_scug == "Artificer" else 0,
            "Disconnect_FP": 1 if self.options.starting_scug == "Rivulet" else 0,
            "Object-EnergyCell": 1 if self.options.starting_scug == "Rivulet" else 0,
            "Rewrite_Spear_Pearl": 1 if self.options.starting_scug == "Spear" else 0,
            "Spear_Pearl": 1 if self.options.starting_scug == "Spear" else 0,
        }
        precollect = {
            "MSC": 1 if self.options.msc_enabled else 0,
            f"Scug-{setting_to_scug_id[self.options.which_gamestate.value]}": 1,
        }

        for name, count in pool.items():
            for i in range(count):
                self.multiworld.itempool.append(self.create_item(name))
            added_items += count

        for name, count in precollect.items():
            for i in range(count):
                self.multiworld.push_precollected(self.create_item(name))

        #################################################################
        # FILLER POPULATION
        remaining_slots = self.location_count - added_items
        trap_fraction = self.options.pct_traps / 100

        nontrap_weights = normalize(self.options.get_nontrap_weight_dict())
        trap_weights = normalize(self.options.get_trap_weight_dict())

        d: dict[str, float] = {}
        d.update({k: v * (1 - trap_fraction) for k, v in nontrap_weights.items()})
        d.update({k: v * trap_fraction for k, v in trap_weights.items()})

        self.multiworld.itempool += [self.create_item(e) for e in flounder2(d, remaining_slots)]

    def set_rules(self) -> None:
        # ascension_item = Item("Ascension", ItemClassification.progression, None, self.player)
        # self.multiworld.get_location("Ascension", self.player).place_locked_item(ascension_item)
        self.multiworld.completion_condition[self.player] = Simple("Victory").check(self.player)

    def fill_slot_data(self) -> Mapping[str, Any]:
        d = self.options.as_dict("which_gamestate", "random_starting_region", "passage_progress_without_survivor")
        return d
