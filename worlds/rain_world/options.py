from dataclasses import dataclass

from Options import PerGameCommonOptions, Toggle, Range, OptionGroup, Choice, Visibility, ProgressionBalancing
from .game_data.general import scug_names


class PassageProgressWithoutSurvivor(Toggle):
    """Whether the Remix setting `Passage progress without Survivor` is enabled.
    This MUST match the setting you use in-game."""
    display_name = "Passage progress without Survivor"
    default = True


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


class WtTrapStun(WtGeneric):
    """The relative weight of stun traps in the trap filler item pool."""
    display_name = "Stun"
    item_name = "Trap-Stun"
    default = 100


class WtTrapZoomies(WtGeneric):
    """The relative weight of zoomies traps in the trap filler item pool."""
    display_name = "Zoomies"
    item_name = "Trap-Zoomies"
    default = 70


class WtTrapTimer(WtGeneric):
    """The relative weight of timer traps in the trap filler item pool."""
    display_name = "Timer"
    item_name = "Trap-Timer"
    default = 100


class WtTrapRedLizard(WtGeneric):
    """The relative weight of red lizard traps in the trap filler item pool."""
    display_name = "RedLizard"
    item_name = "Trap-RedLizard"
    default = 40


class WtTrapRedCentipede(WtGeneric):
    """The relative weight of red centipede traps in the trap filler item pool."""
    display_name = "RedCentipede"
    item_name = "Trap-RedCentipede"
    default = 25


class WtTrapSpitterSpider(WtGeneric):
    """The relative weight of spitter spider traps in the trap filler item pool."""
    display_name = "RedCentipede"
    item_name = "Trap-RedCentipede"
    default = 30


class WtTrapBrotherLongLegs(WtGeneric):
    """The relative weight of brother long legs traps in the trap filler item pool."""
    display_name = "BrotherLongLegs"
    item_name = "Trap-BrotherLongLegs"
    default = 15


class WtTrapDaddyLongLegs(WtGeneric):
    """The relative weight of daddy long legs traps in the trap filler item pool."""
    display_name = "DaddyLongLegs"
    item_name = "Trap-DaddyLongLegs"
    default = 5


class WtTrapFlood(WtGeneric):
    """The relative weight of flood traps in the trap filler item pool."""
    display_name = "Flood"
    item_name = "Trap-Flood"
    default = 15


class WtTrapRain(WtGeneric):
    """The relative weight of rain traps in the trap filler item pool."""
    display_name = "Rain"
    item_name = "Trap-Rain"
    default = 15


class WtTrapGravity(WtGeneric):
    """The relative *weight* of gravity traps in the trap filler item pool."""
    display_name = "Gravity"
    item_name = "Trap-Gravity"
    default = 15


class WtTrapFog(WtGeneric):
    """The relative weight of fog traps in the trap filler item pool."""
    display_name = "Fog"
    item_name = "Trap-Fog"
    default = 20


class WtTrapKillSquad(WtGeneric):
    """The relative weight of kill squad traps in the trap filler item pool."""
    display_name = "KillSquad"
    item_name = "Trap-KillSquad"
    default = 10


class WtTrapAlarm(WtGeneric):
    """The relative weight of alarm traps in the trap filler item pool."""
    display_name = "Alarm"
    item_name = "Trap-Alarm"
    default = 15


@dataclass
class RainWorldOptions(PerGameCommonOptions):
    passage_progress_without_survivor: PassageProgressWithoutSurvivor
    which_gamestate: WhichGamestate

    @property
    def msc_enabled(self) -> bool: return self.which_gamestate.value > 9
    @property
    def starting_scug(self) -> str: return scug_names[self.which_gamestate.value]

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
    wt_killsquads: WtTrapKillSquad
    wt_alarms: WtTrapAlarm
    wt_fogs: WtTrapFog
    wt_floods: WtTrapFlood
    wt_rains: WtTrapRain
    wt_gravity: WtTrapGravity

    wt_redlizard: WtTrapRedLizard
    wt_redcentipede: WtTrapRedCentipede
    wt_spitterspider: WtTrapSpitterSpider
    wt_brotherlonglegs: WtTrapBrotherLongLegs
    wt_daddylonglegs: WtTrapDaddyLongLegs

    def get_trap_weight_dict(self) -> dict[str, float]:
        return {a.item_name: a.value for a in [
            self.wt_stuns, self.wt_zoomies, self.wt_timers, self.wt_alarms, self.wt_killsquads,
            self.wt_gravity, self.wt_rains, self.wt_floods, self.wt_fogs,

            self.wt_redcentipede, self.wt_redlizard, self.wt_spitterspider,
            self.wt_brotherlonglegs, self.wt_daddylonglegs
        ]}


filler_weight_classes: list[type] = [
    WtRock, WtSpear, WtExplosiveSpear, WtGrenade, WtFlashbang, WtSporePuff, WtCherrybomb,
    WtLillyPuck, WtFruit, WtBubbleFruit, WtEggbugEgg, WtJellyfish, WtMushroom, WtSlimeMold,
    WtFireEgg, WtGlowWeed
]

trap_weight_classes: list[type] = [
    WtTrapStun, WtTrapZoomies, WtTrapTimer, WtTrapAlarm, WtTrapKillSquad,
    WtTrapGravity, WtTrapRain, WtTrapFlood, WtTrapFog,

    WtTrapRedLizard, WtTrapRedCentipede, WtTrapSpitterSpider,
    WtTrapBrotherLongLegs, WtTrapDaddyLongLegs
]

option_groups = [
    OptionGroup(
        "Important",
        [ProgressionBalancing, PassageProgressWithoutSurvivor, WhichGamestate]
    ),
    OptionGroup("Start settings", [RandomStartingRegion], True),
    OptionGroup("Progression item settings", [ExtraKarmaCapIncreases], True),
    OptionGroup("Location settings", [PassagePriority], True),
    OptionGroup("Filler item relative weights", [PctTraps] + filler_weight_classes, True),
    OptionGroup("Trap relative weights", trap_weight_classes, True),
]
