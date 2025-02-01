"""
Definitions for location rules (though the logic is mostly in `state_helpers`).
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
    LocationAccessRule("Passage-DragonSlayer", state_helpers.lizard_factory_factory(6)),
    LocationAccessRule("Passage-Friend", state_helpers.lizard_factory_factory(1)),
    LocationAccessRule("Passage-Survivor", state_helpers.max_karma_factory_factory(5)),
    LocationAccessRule("Passage-Pilgrim", state_helpers.pilgrim_factory),
]

# all_rules += [
#     LocationAccessRule(f"Wa|{p:0>2}", state_helpers.wanderer_factory_factory(p))
#     for p in range(1, 14)
# ]

all_rules += [
    LocationAccessRule(f"FoodQuest-{p}", state_helpers.food_quest_factory_factory_2(p))
    for p in game_data.food_quest_items
]
