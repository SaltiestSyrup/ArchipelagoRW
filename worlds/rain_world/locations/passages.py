from .classes import Passage
from .. import game_data
from ..conditions.classes import Condition, Simple, AnyOf, AllOf
from ..conditions import generate

#################################################################
# LIZARDS
cond_dragonslayer_vanilla = Simple(game_data.general.dragonslayer_vanilla)
cond_dragonslayer_msc = AllOf(Simple(game_data.general.dragonslayer_msc, 6), Simple("MSC"))
cond_dragonslayer = AnyOf(cond_dragonslayer_vanilla, cond_dragonslayer_msc)
cond_friend = Simple(game_data.general.lizards_any, 1)

#################################################################
# CHIEFTAIN
cond_chieftain = AllOf(
    Simple(["Scavenger", "ScavengerElite"], 1),
    Simple([f"Scug-{s}" for s in set(game_data.general.scug_names.values()) - {"Artificer"}], 1)
)

#################################################################
# HUNTER
cond_hunter = AnyOf(
    Simple(["Scug-Red", "Scug-Artificer", "Scug-Spear", "Scug-Gourmand", "Scug-Inv"], 1),
    AllOf(
        Simple(["Scug-Yellow", "Scug-White", "Scug-Rivulet"], 1),
        Simple(["Fly", "SmallNeedleWorm", "SmallCentipede", "Centipede", "EggBug", "JellyFish", "Hazer", "VultureGrub"],
               1)
    )
)

#################################################################
# MONK
cond_monk = AnyOf(
    Simple(game_data.general.monk_foods_vanilla, 1),
    AllOf(Simple('MSC'), Simple(game_data.general.monk_foods_msc, 1))
)

#################################################################
# MOTHER
cond_mother = AllOf(
    Simple("MSC"),
    Simple([f"Scug-{scug}" for scug in ("White", "Red", "Gourmand")], 1),
    Simple([f"Access-{region}" for region in game_data.general.slugpup_normal_regions], 1)
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
    AnyOf(Simple("Scug-Saint"), Simple(["Echo-SH", "Echo-UW"], locations=True)),
    AnyOf(
        Simple([f"Scug-{scug}" for scug in set(game_data.general.scugs_msc) - {"Artificer", "Saint"}], 1),
        AllOf(Simple("Scug-Artificer"), Simple("Echo-LC", locations=True)),
        AllOf(Simple("Scug-Saint"), Simple(["Echo-UG", "Echo-SL", "Echo-CL"], locations=True)),
    )
)

#################################################################
# SCHOLAR
cond_scholar = AnyOf(
    Simple(["MSC", "Scug-Yellow", "Access-SL", "The Mark"]),  # Monk requires MSC to see colored pearls
    AllOf(
        Simple(["Scug-White", "Scug-Gourmand"], 1),
        Simple(["Access-SL", "The Mark"])
    ),
    Simple(["Scug-Red", "Scug-Rivulet"], 1),
    AllOf(
        Simple(["Scug-Artificer", "Scug-Spear"], 1),
        Simple("The Mark")
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
            Simple(["Scug-Yellow", "Scug-White", "Scug-Red"], 1),
            Simple([f"Access-{r}" for r in regions_msc], count)
        ),
        AllOf(Simple("Scug-Gourmand"), Simple([f"Access-{r}" for r in regions_gourmand], count)),
        AllOf(Simple("Scug-Artificer"), Simple([f"Access-{r}" for r in regions_artificer], count)),
        AllOf(Simple("Scug-Rivulet"), Simple([f"Access-{r}" for r in regions_rivulet], count)),
        AllOf(Simple("Scug-Spear"), Simple([f"Access-{r}" for r in regions_spearmaster], count)),
        AllOf(Simple("Scug-Saint"), Simple([f"Access-{r}" for r in regions_saint], count)),
    )


#################################################################
# LOCATIONS
# Passages without any implemented rules yet: Saint, Outlaw
locations = [
    Passage("Martyr", "Early Passages", 5000, Simple("MSC"), generate.msc(True)),
    Passage("Mother", "Early Passages", 5001, cond_mother,
            generate.whitelist_scugs(["White", "Red", "Gourmand"], True)),
    Passage("Pilgrim", "Early Passages", 5002, cond_pilgrim, generate.msc(True)),
    Passage("Survivor", "Early Passages", 5003, Simple("Karma", 4)),

    # Passages which require Survivor only if PPwS is disabled.
    Passage("DragonSlayer", "PPwS Passages", 5020, cond_dragonslayer),
    Passage("Friend", "PPwS Passages", 5021, cond_friend),
    Passage("Traveller", "PPwS Passages", 5022, cond_wanderer),

    # Passages which always require Survivor.
    Passage("Chieftain", "Late Passages", 5040, cond_chieftain, generate.blacklist_scugs(["Artificer"])),
    Passage("Hunter", "Late Passages", 5041, cond_hunter, generate.blacklist_scugs(["Saint"])),
    Passage("Monk", "Late Passages", 5042, cond_monk),
    Passage("Outlaw", "Late Passages", 5043),
    Passage("Saint", "Late Passages", 5044),
    Passage("Scholar", "Late Passages", 5045, cond_scholar, generate.scholar()),

    # Passages where the dependence on Survivor is royally screwed up.
    Passage("Nomad", "Late Passages", 5046, cond_nomad, generate.msc(True)),
]
