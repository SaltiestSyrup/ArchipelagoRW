from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, Range, OptionGroup, Choice


class PassageProgressWithoutSurvivor(Toggle):
    """Whether the Remix setting `Passage progress without Survivor` is enabled.
    This MUST match the setting you use in-game."""
    display_name = "Passage progress without Survivor"
    default = True


class MoreSlugcatsExpansionEnabled(Toggle):
    """Whether the More Slugcats Expansion is enabled.
    This MUST match the setting you use in-game."""
    display_name = "(UNIMPLEMENTED) More Slugcats"
    default = True


class WhichWorldstate(Choice):
    """Which campaign / worldstate you will start in.  Downpour must be enabled to pick a Downpour slugcat."""
    display_name = "(UNIMPLEMENTED) Starting scug"
    option_monk = 0
    option_survivor = 1
    option_hunter = 2
    option_gourmand = 3
    option_artificer = 4
    option_rivulet = 5
    option_spearmaster = 6
    option_saint = 7
    option_sofanthiel = 8
    default = 1


class FoodQuestMode(Choice):
    """How food quest checks are awarded.

    In **per-count** mode, checks are associated with total numbers of food quest items
    (e.g. `FQ|02` is always the second food quest check, regardless of which foods are consumed).

    In **per-food** mode, each food has its own check (e.g., blue fruit is always `FQ|02`)."""
    rich_text_doc = True
    display_name = "(UNIMPLEMENTED) Food quest mode"
    option_per_count = 0
    option_per_food = 1


class RegionKeys(Range):
    """Number of random region keys to start with."""
    display_name = "Starting region keys"
    range_start = 0
    range_end = 14
    default = 5


class RandomStartingShelter(Toggle):
    """Whether to start in a random shelter anywhere in the world.
    If `False`, you will start at the default starting point for the selected starting scug."""
    display_name = "(UNIMPLEMENTED) Random starting shelter"
    default = True


class PassagePriority(Range):
    """Number of Passage completion checks that are marked as priority checks,
    guaranteeing that they will contain a progression item."""
    display_name = "Priority Passages"
    range_start = 0
    range_end = 14
    default = 5


class MaximumRequiredFoodQuestPips(Range):
    """Maximum number of food quest items that could be required.
    All pips beyond this number will never have progression items."""
    display_name = "Maximum required food quest pips"
    range_start = 0
    range_end = 22
    default = 15


class ExtraKarmaCapIncreases(Range):
    """Number of extra karma cap increases in the pool beyond the minimum for ascension."""
    display_name = "Extra karma cap increases"
    range_start = 0
    range_end = 30
    default = 1


class PctTraps(Range):
    """The percentage of filler items that will be traps.  Set to 0 to remove traps entirely."""
    display_name = "Trap percentage"
    range_start = 0
    range_end = 100
    default = 30


class WtRock(Range):
    """The relative weight of rocks in the non-trap filler item pool."""
    display_name = "Rock"
    range_start = 0
    range_end = 100
    default = 100


class WtSpear(Range):
    """The relative weight of spears in the non-trap filler item pool."""
    display_name = "Spear"
    range_start = 0
    range_end = 100
    default = 50


class WtGrenade(Range):
    """The relative weight of grenades in the non-trap filler item pool."""
    display_name = "Grenade"
    range_start = 0
    range_end = 100
    default = 15


class WtFruit(Range):
    """The relative weight of blue fruits in the non-trap filler item pool."""
    display_name = "Fruit"
    range_start = 0
    range_end = 100
    default = 30


class WtTrapStun(Range):
    """The relative weight of stun traps in the trap filler item pool."""
    display_name = "Stun trap"
    range_start = 0
    range_end = 100
    default = 100


class WtTrapZoomies(Range):
    """The relative weight of zoomies traps in the trap filler item pool."""
    display_name = "Zoomies trap"
    range_start = 0
    range_end = 100
    default = 70


class WtTrapTimer(Range):
    """The relative weight of timer traps in the trap filler item pool."""
    display_name = "Timer trap"
    range_start = 0
    range_end = 100
    default = 100


class WtTrapRedLizard(Range):
    """The relative weight of red lizard traps in the trap filler item pool."""
    display_name = "Red lizard trap"
    range_start = 0
    range_end = 100
    default = 40


class WtTrapRedCentipede(Range):
    """The relative weight of red centipede traps in the trap filler item pool."""
    display_name = "Red centipede trap"
    range_start = 0
    range_end = 100
    default = 25


class WtTrapSpitterSpider(Range):
    """The relative weight of spitter spider traps in the trap filler item pool."""
    display_name = "Spitter spider trap"
    range_start = 0
    range_end = 100
    default = 30


@dataclass
class RainWorldOptions(PerGameCommonOptions):
    passage_progress_without_survivor: PassageProgressWithoutSurvivor
    more_slugcats_expansion_enabled: MoreSlugcatsExpansionEnabled
    which_worldstate: WhichWorldstate
    food_quest_mode: FoodQuestMode

    region_keys: RegionKeys
    random_starting_shelter: RandomStartingShelter

    passage_priority: PassagePriority
    maximum_required_food_quest_pips: MaximumRequiredFoodQuestPips
    extra_karma_cap_increases: ExtraKarmaCapIncreases

    pct_traps: PctTraps

    wt_rocks: WtRock
    wt_spears: WtSpear
    wt_grenades: WtGrenade
    wt_fruit: WtFruit

    wt_stuns: WtTrapStun
    wt_zoomies: WtTrapZoomies
    wt_timers: WtTrapTimer
    wt_redlizard: WtTrapRedLizard
    wt_redcentipede: WtTrapRedCentipede
    wt_spitterspider: WtTrapSpitterSpider


option_groups = [
    OptionGroup(
        "Important",
        [PassageProgressWithoutSurvivor, MoreSlugcatsExpansionEnabled, WhichWorldstate, FoodQuestMode]
    ),
    OptionGroup("Start settings", [RegionKeys, RandomStartingShelter], True),
    OptionGroup("Progression item settings", [ExtraKarmaCapIncreases], True),
    OptionGroup("Location settings", [MaximumRequiredFoodQuestPips, PassagePriority], True),
    OptionGroup("Filler item relative weights", [PctTraps, WtRock, WtSpear, WtGrenade, WtFruit], True),
    OptionGroup(
        "Trap relative weights",
        [WtTrapStun, WtTrapZoomies, WtTrapTimer, WtTrapRedLizard, WtTrapRedCentipede, WtTrapSpitterSpider],
        True
    ),
]
