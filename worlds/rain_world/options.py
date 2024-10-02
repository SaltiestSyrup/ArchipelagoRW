from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, Range


class PassageProgressWithoutSurvivor(Toggle):
    """Whether the Remix setting `Passage progress without Survivor` is enabled.
    Note that this MUST match the setting you use in-game."""
    display_name = "Passage progress without Survivor"
    default = True


class RegionKeys(Range):
    """Number of region keys to start with (chosen at random)."""
    range_start = 0
    range_end = 14
    default = 5


class PassagePriority(Range):
    """Number of Passage completion checks that are marked as priority checks."""
    range_start = 0
    range_end = 14
    default = 5


class MaximumRequiredFoodQuestPips(Range):
    """Maximum number of food quest items that could be required."""
    range_start = 0
    range_end = 22
    default = 15


class ExtraKarmaCapIncreases(Range):
    """Number of extra karma cap increases in the pool beyond the minimum for ascension."""
    range_start = 0
    range_end = 30
    default = 1


class StartingKarma(Range):
    """Starting karma."""
    range_start = 1
    range_end = 10
    default = 1


@dataclass
class RainWorldOptions(PerGameCommonOptions):
    passage_progress_without_survivor: PassageProgressWithoutSurvivor
    region_keys: RegionKeys
    passage_priority: PassagePriority
    maximum_required_food_quest_pips: MaximumRequiredFoodQuestPips
    extra_karma_cap_increases: ExtraKarmaCapIncreases
    starting_karma: StartingKarma
