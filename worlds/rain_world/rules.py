"""
Definitions for location rules (though the logic is mostly in `state_helpers`).
Region access rules are not declared here.
"""

from typing import NamedTuple, Callable

from BaseClasses import CollectionState, MultiWorld
from . import state_helpers, game_data
from ..generic.Rules import add_rule


class LocationAccessRule(NamedTuple):
    name: str
    factory: Callable[[int], Callable[[CollectionState], bool]]

    def make(self, player: int, multiworld: MultiWorld):
        add_rule(multiworld.get_location(self.name, player), self.factory(player))


all_rules: list[LocationAccessRule] = [
    LocationAccessRule("Passage-DragonSlayer", game_data.creatures.can_access_dragonslayer_factory),
    LocationAccessRule("Passage-Friend", game_data.creatures.can_access_multiple_creatures_factory_factory(game_data.creatures.lizards_any, 1)),
    LocationAccessRule("Passage-Survivor", state_helpers.max_karma_factory_factory(5)),
    LocationAccessRule("Passage-Pilgrim", state_helpers.pilgrim_factory),
    LocationAccessRule("Passage-Wanderer", state_helpers.wanderer_factory_factory(12)),  # TODO
    LocationAccessRule("Passage-Chieftain", state_helpers.has("Scavenger")),
    LocationAccessRule("Passage-Chieftain", state_helpers.has_some(
        [f"Scug-{scug}" for scug in set(game_data.general.scug_names.values()) - {"Artificer"}], 1
    )),
    LocationAccessRule("Passage-Mother", state_helpers.has_some(
        [f"Scug-{scug}" for scug in ("White", "Red", "Gourmand")], 1
    )),
    LocationAccessRule("Passage-Nomad", state_helpers.wanderer_factory_factory(3)),
]

all_rules += [
    LocationAccessRule(f"Wanderer-{p}", state_helpers.wanderer_factory_factory(p))
    for p in range(1, 14)
]

all_rules += [
    LocationAccessRule(f"FoodQuest-{p}", state_helpers.has(p))
    for p in game_data.general.food_quest_items
]
