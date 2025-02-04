"""
Conditions for passage locations.
"""

from BaseClasses import MultiWorld
from .. import game_data
from worlds.generic.Rules import add_rule
from .classes import Condition, Simple, AnyOf, AllOf


class LocationAccessRule:
    def __init__(self, name: str, condition: Condition):
        self.name: str = name
        self.condition: Condition = condition

    def make(self, player: int, multiworld: MultiWorld):
        add_rule(multiworld.get_location(self.name, player), self.condition.check(player))


#################################################################
# LIZARDS
cond_dragonslayer_vanilla = Simple(game_data.general.dragonslayer_vanilla)
cond_dragonslayer_msc = AllOf(Simple(game_data.general.dragonslayer_msc, 6), Simple("MSC"))
cond_dragonslayer = AnyOf(cond_dragonslayer_vanilla, cond_dragonslayer_msc)
cond_friend = Simple(game_data.general.lizards_any, 1)

#################################################################
# CHIEFTAIN
cond_chieftain = AllOf(
    Simple("MSC"),
    Simple(["Scavenger", "EliteScavenger"], 1),
    Simple([f"Scug-{s}" for s in set(game_data.general.scug_names.values()) - {"Artificer"}], 1)
)

#################################################################
# HUNTER
cond_hunter = AnyOf(
    Simple(["Scug-Hunter", "Scug-Artificer", "Scug-Spearmaster", "Scug-Gourmand", "Scug-Inv"], 1),
    AllOf(
        Simple(["Scug-Monk", "Scug-Survivor", "Scug-Rivulet"], 1),
        Simple(["Fly", "SmallNeedleWorm", "SmallCentipede", "Centipede", "EggBug", "JellyFish", "Hazer", "VultureGrub"],
               1)
    )
)

#################################################################
# MONK
cond_monk = AnyOf(
    Simple(game_data.general.monk_foods_vanilla, 1),
    AllOf(Simple('MSC'), Simple(game_data.general.monk_foods_msc))
)

#################################################################
# MOTHER
cond_mother = AllOf(
    Simple("MSC"),
    Simple([f"Scug-{scug}" for scug in ("White", "Red", "Gourmand")], 1),
    Simple(game_data.general.slugpup_normal_regions, 1)
)

#################################################################
# NOMAD
cond_nomad = AllOf(
    Simple("MSC"),
    Simple([f"Access-{region}" for region in game_data.general.regions_all], 5)
)

#################################################################
# PILGRIM
cond_pilgrim = AllOf(
    Simple("MSC"),
    Simple([f"Echo-{e}" for e in ('CC', 'SI', 'LF', 'SB')], locations=True),
    Simple(["Echo-SH", "Scug-Saint"], 1),
    Simple(["Echo-UW", "Scug-Saint"], 1),
    AnyOf(
        Simple([f"Scug-{scug}" for scug in set(game_data.general.scugs_msc) - {"Artificer", "Saint"}]),
        AllOf(Simple("Scug-Artificer"), Simple("Echo-LC", locations=True)),
        AllOf(Simple("Scug-Saint"), Simple(["Echo-UG", "Echo-SL", "Echo-CL"], locations=True)),
    )
)

#################################################################
# SCHOLAR
cond_scholar = AnyOf(
    AllOf(
        Simple("MSC", negative=True),
        Simple(["Scug-Monk", "Access-SL", "Mark"])
    ),
    AllOf(
        Simple(["Scug-White", "Scug-Gourmand"], 1),
        Simple(["Access-SL", "Mark"])
    ),
    Simple(["Scug-Red", "Scug-Rivulet"], 1),
    AllOf(
        Simple(["Scug-Artificer", "Scug-Spearmaster"], 1),
        Simple("Mark")
    ),
)

#################################################################
# WANDERER
# These sets are *story regions*.
regions = set(game_data.general.regions_vanilla)
regions_msc = regions.union({"VS"})
regions_gourmand = regions_msc.union({"OE"})
regions_artificer = regions_msc.union({"LC", "LM"}).difference({"SL"})
regions_rivulet = regions_msc.union({"RM", "MS"}).difference({"SS"})
regions_spearmaster = regions_msc.union({"DM", "LM"}).difference({"SL"})
regions_saint = regions_msc.union({"UG", "CL", "HR"}).difference({"DS", "SH", "UW", "SS"})

cond_wanderer_vanilla = AllOf(Simple([f"Access-{r}" for r in regions]), Simple("MSC", negative=True))
cond_wanderer_msc_base = AllOf(
    Simple([f"Access-{r}" for r in regions_msc] + ["MSC"]),
    Simple(["Scug-Yellow", "Scug-White", "Scug-Red"], 1)
)
cond_wanderer_gourmand = Simple([f"Access-{r}" for r in regions_gourmand] + ["MSC", "Scug-Gourmand"])
cond_wanderer_artificer = Simple([f"Access-{r}" for r in regions_artificer] + ["MSC", "Scug-Artificer"])
cond_wanderer_rivulet = Simple([f"Access-{r}" for r in regions_rivulet] + ["MSC", "Scug-Rivulet"])
cond_wanderer_spearmaster = Simple([f"Access-{r}" for r in regions_spearmaster] + ["MSC", "Scug-Spear"])
cond_wanderer_saint = Simple([f"Access-{r}" for r in regions_saint] + ["MSC", "Scug-Saint"])

cond_wanderer = AnyOf(cond_wanderer_vanilla, cond_wanderer_msc_base, cond_wanderer_gourmand,
                      cond_wanderer_artificer, cond_wanderer_rivulet, cond_wanderer_spearmaster, cond_wanderer_saint)


def wanderer_pip_factory(count: int) -> Condition:
    return AnyOf(
        AllOf(Simple("MSC", negative=True), Simple([f"Access-{r}" for r in regions], count)),
        AllOf(
            Simple("MSC"),
            Simple(["Scug-Yellow", "Scug-White", "Scug-Red"]),
            Simple([f"Access-{r}" for r in regions_msc], count)
        ),
        AllOf(Simple("Scug-Gourmand"), Simple([f"Access-{r}" for r in regions_gourmand], count)),
        AllOf(Simple("Scug-Artificer"), Simple([f"Access-{r}" for r in regions_artificer], count)),
        AllOf(Simple("Scug-Rivulet"), Simple([f"Access-{r}" for r in regions_rivulet], count)),
        AllOf(Simple("Scug-Spear"), Simple([f"Access-{r}" for r in regions_spearmaster], count)),
        AllOf(Simple("Scug-Saint"), Simple([f"Access-{r}" for r in regions_saint], count)),
    )


#################################################################
# LISTING
# Passages without any implemented rules yet: Saint, Outlaw, Martyr
all_rules: list[LocationAccessRule] = [
    LocationAccessRule("Passage-DragonSlayer", cond_dragonslayer),
    LocationAccessRule("Passage-Chieftain", cond_chieftain),
    LocationAccessRule("Passage-Friend", cond_friend),
    LocationAccessRule("Passage-Hunter", cond_hunter),
    LocationAccessRule("Passage-Monk", cond_monk),
    LocationAccessRule("Passage-Mother", cond_mother),
    LocationAccessRule("Passage-Nomad", cond_nomad),
    LocationAccessRule("Passage-Pilgrim", cond_pilgrim),
    LocationAccessRule("Passage-Scholar", cond_scholar),
    LocationAccessRule("Passage-Survivor", Simple("Karma", 5)),
    LocationAccessRule("Passage-Wanderer", cond_wanderer),
]

all_rules += [LocationAccessRule(f"Wanderer-{p}", wanderer_pip_factory(p)) for p in range(1, 14)]
all_rules += [LocationAccessRule(f"FoodQuest-{p}", Simple(p)) for p in game_data.general.food_quest_items]
