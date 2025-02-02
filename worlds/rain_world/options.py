from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, Range, OptionGroup, Choice, Visibility, ProgressionBalancing
from .game_data.general import scug_names


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
    display_name = "Starting scug"
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


class WhichGamestate(Choice):
    """Which campaign / worldstate you will start in."""
    display_name = "Game state"
    option_monk_vanilla = 0
    option_survivor_vanilla = 1
    option_hunter_vanilla = 2

    option_monk_msc = 10
    option_survivor_msc = 11
    option_hunter_msc = 12
    option_gourmand = 13
    option_artificer = 14
    option_rivulet = 15
    option_spearmaster = 16
    option_saint = 17
    option_sofanthiel = 18

    default = 1

    @classmethod
    def get_option_name(cls, value: int) -> str:
        if value < 19:
            return f"{scug_names[value]}{' (Vanilla)' if value < 10 else (' (MSC)' if value < 13 else '')}"
        return f"{value}"


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


class RandomStartingRegion(Choice):
    """Where Slugcat will initially spawn."""
    display_name = "Random starting shelter"
    option_default_starting_point = 0

    option_outskirts = 1
    option_industrial_complex = 2
    option_drainage_system = 3
    option_garbage_wastes = 4
    option_shoreline = 5
    option_shaded_citadel = 6
    option_the_exterior = 7
    option_five_pebbles = 8
    option_chimney_cannopy = 9
    option_sky_islands = 10
    option_farm_arrays = 11
    option_subterranean = 12

    option_pipeyard = 20

    default = 0


class PassagePriority(Range):
    """Number of Passage completion checks that are marked as priority checks,
    increasing the chance that they will contain progression items."""
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


class WtGeneric(Range):
    range_start = 0
    range_end = 100


class WtRock(WtGeneric):
    """The relative weight of rocks in the non-trap filler item pool."""
    display_name = "Rock"
    item_name = "Object-Rock"
    default = 100


class WtSpear(WtGeneric):
    """The relative weight of spears in the non-trap filler item pool."""
    display_name = "Spear"
    item_name = "Object-Spear"
    default = 40


class WtExplosiveSpear(WtGeneric):
    """The relative weight of explosive spears in the non-trap filler item pool."""
    display_name = "ExplosiveSpear"
    item_name = "Object-ExplosiveSpear"
    default = 10


class WtGrenade(WtGeneric):
    """The relative weight of grenades in the non-trap filler item pool."""
    display_name = "Grenade"
    item_name = "Object-ScavengerBomb"
    default = 10


class WtFlashbang(WtGeneric):
    """The relative weight of flashbangs in the non-trap filler item pool."""
    display_name = "Flashbang"
    item_name = "Object-FlareBomb"
    default = 20


class WtSporePuff(WtGeneric):
    """The relative weight of spore puffs in the non-trap filler item pool."""
    display_name = "Spore puff"
    item_name = "Object-PuffBall"
    default = 20


class WtCherrybomb(WtGeneric):
    """The relative weight of cherrybombs in the non-trap filler item pool."""
    display_name = "Cherrybomb"
    item_name = "Object-FirecrackerPlant"
    default = 30


class WtLillyPuck(WtGeneric):
    """The relative weight of lilypucks in the non-trap filler item pool."""
    display_name = "Lilypuck (MSC)"
    item_name = "Object-LillyPuck"
    default = 20


class WtFruit(WtGeneric):
    """The relative weight of blue fruit in the non-trap filler item pool."""
    display_name = "Blue fruit"
    item_name = "Object-DangleFruit"
    default = 60


class WtBubbleFruit(WtGeneric):
    """The relative weight of bubble fruit in the non-trap filler item pool."""
    display_name = "Bubble fruit"
    item_name = "Object-WaterNut"
    default = 40


class WtEggbugEgg(WtGeneric):
    """The relative weight of eggbug eggs in the non-trap filler item pool."""
    display_name = "Eggbug egg"
    item_name = "Object-EggBugEgg"
    default = 30


class WtJellyfish(WtGeneric):
    """The relative weight of jellyfish in the non-trap filler item pool."""
    display_name = "Jellyfish"
    item_name = "Object-JellyFish"
    default = 15


class WtMushroom(WtGeneric):
    """The relative weight of mushrooms in the non-trap filler item pool."""
    display_name = "Mushroom"
    item_name = "Object-Mushroom"
    default = 15


class WtSlimeMold(WtGeneric):
    """The relative weight of slime mold in the non-trap filler item pool."""
    display_name = "Slime mold"
    item_name = "Object-SlimeMold"
    default = 35


class WtFireEgg(WtGeneric):
    """The relative weight of firebug eggs in the non-trap filler item pool."""
    display_name = "Firebug egg (MSC)"
    item_name = "Object-FireEgg"
    default = 5


class WtGlowWeed(WtGeneric):
    """The relative weight of glow weed in the non-trap filler item pool."""
    display_name = "Glow weed (MSC)"
    item_name = "Object-GlowWeed"
    default = 15


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


class Accessibility(Choice):
    """
    Unused
    """
    display_name = "Accessibility"
    rich_text_doc = True
    visibility = Visibility.none
    option_minimal = 2
    alias_none = 2
    default = 2


@dataclass
class RainWorldOptions(PerGameCommonOptions):
    accessibility: Accessibility

    passage_progress_without_survivor: PassageProgressWithoutSurvivor
    which_gamestate: WhichGamestate

    random_starting_region: RandomStartingRegion

    passage_priority: PassagePriority
    extra_karma_cap_increases: ExtraKarmaCapIncreases

    pct_traps: PctTraps

    wt_rocks: WtRock
    wt_spears: WtSpear
    wt_explosive_spears: WtExplosiveSpear
    wt_grenades: WtGrenade
    wt_flashbangs: WtFlashbang
    wt_sporepuffs: WtSporePuff
    wt_cherrybombs: WtCherrybomb
    wt_lilypucks: WtLillyPuck

    wt_fruit: WtFruit
    wt_bubblefruit: WtBubbleFruit
    wt_eggbugeggs: WtEggbugEgg
    wt_jellyfish: WtJellyfish
    wt_mushrooms: WtMushroom
    wt_slimemold: WtSlimeMold
    wt_fireeggs: WtFireEgg
    wt_glowweed: WtGlowWeed

    def get_nontrap_weight_dict(self) -> dict[str, float]:
        return {a.item_name: a.value for a in [
            self.wt_rocks, self.wt_spears, self.wt_explosive_spears, self.wt_grenades,
            self.wt_flashbangs, self.wt_sporepuffs, self.wt_cherrybombs, self.wt_lilypucks,
            self.wt_fruit, self.wt_bubblefruit, self.wt_eggbugeggs, self.wt_jellyfish,
            self.wt_mushrooms, self.wt_slimemold, self.wt_fireeggs, self.wt_glowweed
        ]}

    wt_stuns: WtTrapStun
    wt_zoomies: WtTrapZoomies
    wt_timers: WtTrapTimer
    wt_redlizard: WtTrapRedLizard
    wt_redcentipede: WtTrapRedCentipede
    wt_spitterspider: WtTrapSpitterSpider


filler_weight_classes: list[type] = [
    WtRock, WtSpear, WtExplosiveSpear, WtGrenade, WtFlashbang, WtSporePuff, WtCherrybomb,
    WtLillyPuck, WtFruit, WtBubbleFruit, WtEggbugEgg, WtJellyfish, WtMushroom, WtSlimeMold,
    WtFireEgg, WtGlowWeed
]

option_groups = [
    OptionGroup(
        "Important",
        [ProgressionBalancing, PassageProgressWithoutSurvivor, WhichGamestate]
    ),
    OptionGroup("Start settings", [RandomStartingRegion], True),
    OptionGroup("Progression item settings", [ExtraKarmaCapIncreases], True),
    OptionGroup("Location settings", [PassagePriority], True),
    OptionGroup(
        "Filler item relative weights",
        [PctTraps] + filler_weight_classes,
        True),
    OptionGroup(
        "Trap relative weights",
        [WtTrapStun, WtTrapZoomies, WtTrapTimer, WtTrapRedLizard, WtTrapRedCentipede, WtTrapSpitterSpider],
        True
    ),
]
