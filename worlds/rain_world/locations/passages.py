from typing import Callable

from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, Has, HasAny, HasAll, HasFromList, CanReachLocation, And
from .classes import Passage, LocationData, AbstractLocation
from .. import game_data
from ..conditions import rule_helper
from ..game_data.general import watcher_pearls
from ..options import RainWorldOptions, DifficultyChieftain, DifficultyHunter, \
    DifficultyMonk, DifficultyNomad, DifficultyOutlaw


#################################################################
# SURVIVOR
cond_survivor = Has("Karma", 4) | rule_helper.watcher


#################################################################
# CHIEFTAIN
def generate_cond_chieftain(options: RainWorldOptions) -> Rule:
    return (Has("Toll", options=[OptionFilter(DifficultyChieftain, DifficultyChieftain.option_true)],
                filtered_resolution=True)
            & HasAny("Scavenger", "ScavengerElite"))


#################################################################
# DRAGON SLAYER
def generate_cond_dragonslayer(options: RainWorldOptions) -> Rule:
    if not options.msc_enabled:
        return HasFromList(*game_data.general.dragonslayer_vanilla, count=6)
    if options.difficulty_extreme_threats:
        return HasFromList(*game_data.general.dragonslayer_msc, count=6)
    else:
        return HasFromList(*game_data.general.dragonslayer_msc.difference({"RedLizard"}), count=6)


#################################################################
# FRIEND
cond_friend = HasAny(*game_data.general.lizards_any)


#################################################################
# HUNTER
def generate_cond_hunter(options: RainWorldOptions) -> Rule:
    # Carnivorous slugcats use simple region check
    if options.starting_scug in ["Red", "Artificer", "Spear", "Gourmand", "Inv"]:
        return HasAny(*[f"Access-{region}" for region in set(game_data.general.regions_all).difference({"SS", "MS"})])
    return HasFromList(
        *["Fly", "SmallNeedleWorm", "SmallCentipede", "Centipede",
          "EggBug", "JellyFish", "Hazer", "VultureGrub", "Frog", "Tardigrade",
          "SandGrubNetwork", "PlacedRats", "Barnacle"],
        count=FromOption(DifficultyHunter)
    )


#################################################################
# MONK
def generate_cond_monk(options: RainWorldOptions) -> Rule:
    if options.starting_scug in ["Spear", "Artificer", "Red"]:
        return HasAny("Access-SI", "Access-LF", "Access-SS", "Access-DM")
    foods = [
        *game_data.general.monk_foods_vanilla,
        *(game_data.general.monk_foods_msc if options.msc_enabled else []),
        *(game_data.general.monk_foods_watcher if options.is_watcher_enabled else []),
     ]
    return HasFromList(*foods, count=FromOption(DifficultyMonk))


#################################################################
# MOTHER
cond_mother = HasAny(*[f"Access-{region}" for region in game_data.general.slugpup_normal_regions])


#################################################################
# NOMAD
def generate_cond_nomad(options: RainWorldOptions) -> Rule:
    return HasFromList(*[f"Access-{region}" for region in game_data.general.regions_all],
                       count=FromOption(DifficultyNomad))


#################################################################
# OUTLAW
def generate_cond_outlaw(options: RainWorldOptions) -> Rule:
    return HasFromList(
        *list(game_data.general.outlaw_whitelist if options.difficulty_extreme_threats else
             game_data.general.outlaw_whitelist.difference(game_data.general.extreme_threat_creatures)),
        count=FromOption(DifficultyOutlaw)
    )


#################################################################
# PILGRIM
def generate_cond_pilgrim(options: RainWorldOptions) -> Rule:
    if options.starting_scug == "Saint":
        echoes = ["CC", "SI", "LF", "SB", "UG", "SL", "CL"]
    elif options.starting_scug == "Artificer":
        echoes = ["CC", "SI", "LF", "SB", "UW", "SH", "LC"]
    else:
        echoes = ["CC", "SI", "LF", "SB", "UW", "SH"]

    return And(*[CanReachLocation(f"{game_data.general.region_code_to_name[e]} - Echo") for e in echoes])


#################################################################
# SCHOLAR
def generate_cond_scholar(options: RainWorldOptions) -> Rule:
    if options.starting_scug in ["Yellow", "White", "Gourmand"]:
        return HasAll("Access-SL", "The Mark")
    if options.starting_scug == "Watcher":
        return Has("The Mark") & HasFromList(*[f"Access-{r}" for r in watcher_pearls], count=3)
    return Has("The Mark") & wanderer_pip_factory_factory(3)(options)


#################################################################
# WANDERER
# These sets are *story regions*.
regions = game_data.general.story_regions_vanilla
regions_msc = game_data.general.story_regions_msc
regions_gourmand = game_data.general.story_regions_gourmand
regions_artificer = game_data.general.story_regions_artificer
regions_rivulet = game_data.general.story_regions_rivulet
regions_spearmaster = game_data.general.story_regions_spearmaster
regions_saint = game_data.general.story_regions_saint


def generate_cond_wanderer(options: RainWorldOptions) -> Rule:
    return HasAll(*[f"Access-{r}" for r in wanderer_regions(options.starting_scug, options.msc_enabled)])


def wanderer_regions(scug: str, msc: bool) -> set[str]:
    if not msc:
        return regions
    elif scug in ["Yellow", "White", "Red", "Inv"]:
        return regions_msc
    else:
        return {
            "Gourmand": regions_gourmand, "Artificer": regions_artificer, "Rivulet": regions_rivulet,
            "Spear": regions_spearmaster, "Saint": regions_saint, "Watcher": set()
        }[scug]


def wanderer_pip_factory_factory(count: int) -> Callable[[RainWorldOptions], Rule]:
    def wanderer_pip_factory(options: RainWorldOptions) -> Rule:
        return HasFromList(
            *[f"Access-{r}" for r in wanderer_regions(options.starting_scug, options.msc_enabled)],
            count=count
        )
    return wanderer_pip_factory


#################################################################
# LOCATIONS
locations: dict[str, LocationData] = {
    "Martyr": Passage("Martyr", "Early Passages", 5000),
    "Mother": Passage("Mother", "Early Passages", 5001, cond_mother),
    "Pilgrim": Passage("Pilgrim", "Early Passages", 5002, access_condition_generator=generate_cond_pilgrim),
    "Survivor": Passage("Survivor", "Early Passages", 5003, cond_survivor),

    "DragonSlayer": Passage("DragonSlayer", "PPwS Passages", 5020,
                            access_condition_generator=generate_cond_dragonslayer),
    "Friend": Passage("Friend", "PPwS Passages", 5021, cond_friend),
    "Traveller": Passage("Traveller", "PPwS Passages", 5022, access_condition_generator=generate_cond_wanderer),

    "Chieftain": Passage("Chieftain", "Late Passages", 5040, access_condition_generator=generate_cond_chieftain),
    "Hunter": Passage("Hunter", "Late Passages", 5041, access_condition_generator=generate_cond_hunter),
    "Monk": Passage("Monk", "Late Passages", 5042, access_condition_generator=generate_cond_monk),
    "Outlaw": Passage("Outlaw", "Late Passages", 5043, access_condition_generator=generate_cond_outlaw),
    "Saint": Passage("Saint", "Late Passages", 5044, access_condition_generator=generate_cond_monk),
    "Scholar": Passage("Scholar", "Late Passages", 5045, access_condition_generator=generate_cond_scholar),
    "Nomad": Passage("Nomad", "Late Passages", 5046, access_condition_generator=generate_cond_nomad),
    **{
        f"Wanderer-{i}": AbstractLocation(
            f"The Wanderer - {i} pip{'s' if i > 1 else ''}",
            f"Wanderer-{i}", [], 5049 + i, "PPwS Passages", access_condition_generator=wanderer_pip_factory_factory(i)
        ) for i in range(1, 15)
    }
}


def generate(options: RainWorldOptions) -> list[LocationData]:
    if not options.checks_passages:
        return []

    keys = ["Survivor", "Friend", "Monk", "Saint"]

    if options.starting_scug != "Artificer":
        keys.append("Chieftain")

    if options.starting_scug != "Saint":
        keys += ["Hunter", "Outlaw", "DragonSlayer"]
        if (options.starting_scug != "Yellow" or options.msc_enabled) and options.starting_scug != "Inv":
            keys.append("Scholar")

    if options.msc_enabled:
        keys.append("Martyr")
        if options.starting_scug != "Watcher":
            keys += ["Pilgrim", "Nomad"]
        if options.starting_scug in ["White", "Red", "Gourmand", "Inv"]:
            keys.append("Mother")

    if options.starting_scug != "Watcher":
        # Riv can't get last pip if Submerged inaccessible
        if options.starting_scug != "Rivulet" or options.submerged_should_populate:
            keys += [f"Wanderer-{i + 1}" for i in range(len(wanderer_regions(options.starting_scug, options.msc_enabled)))]
            keys.append("Traveller")
        else:
            keys += [f"Wanderer-{i + 1}" for i in range(len(wanderer_regions(options.starting_scug, options.msc_enabled)) - 1)]

    return [locations[key] for key in keys]
