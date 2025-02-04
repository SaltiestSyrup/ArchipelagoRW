from . import world, misc

all_events = [
    *world.generate_events("placed_objects"),
    *world.generate_events("creatures"),
    *misc.generate_events(),
]
