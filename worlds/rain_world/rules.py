"""
Definitions for location rules (though the logic is mostly in `state_helpers`).
Region access rules are not declared here.
"""

from typing import NamedTuple, Callable

from BaseClasses import CollectionState, MultiWorld
from . import state_helpers, game_data
from ..generic.Rules import add_rule
from .classes import Simple, Compound


class LocationAccessRule(NamedTuple):
    name: str
    factory: Callable[[int], Callable[[CollectionState], bool]]

    def make(self, player: int, multiworld: MultiWorld):
        add_rule(multiworld.get_location(self.name, player), self.factory(player))


#################################################################
# LIZARDS
cond_dragonslayer_vanilla = Simple(game_data.creatures.dragonslayer_vanilla)
cond_dragonslayer_msc = Compound(2, Simple(game_data.creatures.dragonslayer_msc, 6), Simple("MSC"))
cond_dragonslayer = Compound(1, cond_dragonslayer_vanilla, cond_dragonslayer_msc)
cond_friend = Simple(game_data.creatures.lizards_any, 1)

#################################################################
# WANDERER
regions = set(game_data.general.regions_vanilla)
regions_msc = regions.union({"VS"})
regions_gourmand = regions_msc.union({"OE"})
regions_artificer = regions_msc.union({"LC", "LM"}).difference({"SL"})
regions_rivulet = regions_msc.union({"RM", "MS"}).difference({"SS"})
regions_spearmaster = regions_msc.union({"DM", "LM"}).difference({"SL"})
regions_saint = regions_msc.union({"UG", "CL", "HR"}).difference({"DS", "SH", "UW", "SS"})

cond_wanderer_vanilla = Compound(2, Simple([f"Access-{r}" for r in regions]), Simple("MSC", negative=True))
cond_wanderer_msc_base = Compound(
    2,
    Simple([f"Access-{r}" for r in regions_msc] + ["MSC"]),
    Simple(["Scug-Yellow", "Scug-White", "Scug-Red"], 1)
)
cond_wanderer_gourmand = Simple([f"Access-{r}" for r in regions_gourmand] + ["MSC", "Scug-Gourmand"])
cond_wanderer_artificer = Simple([f"Access-{r}" for r in regions_artificer] + ["MSC", "Scug-Artificer"])
cond_wanderer_rivulet = Simple([f"Access-{r}" for r in regions_rivulet] + ["MSC", "Scug-Rivulet"])
cond_wanderer_spearmaster = Simple([f"Access-{r}" for r in regions_spearmaster] + ["MSC", "Scug-Spear"])
cond_wanderer_saint = Simple([f"Access-{r}" for r in regions_saint] + ["MSC", "Scug-Saint"])

cond_wanderer = Compound(1, cond_wanderer_vanilla, cond_wanderer_msc_base, cond_wanderer_gourmand,
                         cond_wanderer_artificer, cond_wanderer_rivulet, cond_wanderer_spearmaster, cond_wanderer_saint)

#################################################################
# CHIEFTAIN
cond_chieftain = Compound(
    2,
    Simple("Scavenger"),
    Simple([f"Scug-{s}" for s in set(game_data.general.scug_names.values()) - {"Artificer"}], 1)
)

all_rules: list[LocationAccessRule] = [
    LocationAccessRule("Passage-DragonSlayer", cond_dragonslayer.check),
    LocationAccessRule("Passage-Friend", cond_friend.check),
    LocationAccessRule("Passage-Survivor", Simple("Karma", 5).check),
    LocationAccessRule("Passage-Pilgrim", state_helpers.pilgrim_factory),
    LocationAccessRule("Passage-Wanderer", cond_wanderer.check),
    LocationAccessRule("Passage-Chieftain", cond_chieftain.check),
    LocationAccessRule("Passage-Mother", Simple([f"Scug-{scug}" for scug in ("White", "Red", "Gourmand")], 1).check),
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
