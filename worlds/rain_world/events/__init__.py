from . import world, misc
from .. import RainWorldOptions


def get_events(options: RainWorldOptions):
    return [
        *world.generate_events_for_one_gamestate("placed_objects", options),
        *world.generate_events_for_one_gamestate("creatures", options),
        *misc.generate_events(),
    ]
