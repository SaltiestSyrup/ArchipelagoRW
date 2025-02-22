from . import world, misc, victory
from .. import RainWorldOptions
from ..regions.classes import RainWorldRegion


def get_events(options: RainWorldOptions, regions: list[RainWorldRegion]):
    return [
        *world.generate_events_for_one_gamestate(options, regions),
        *victory.generate(options),
        *misc.generate_events(),
    ]
