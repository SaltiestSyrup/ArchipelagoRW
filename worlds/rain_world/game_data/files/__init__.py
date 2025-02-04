__all__ = ['placed_objects', 'creatures']

import json
import os

# Dictionary of PlacedObjects.  data[objtype][dlcstate][scug] -> list of rooms.
placed_objects: dict[str, dict[str, [dict[str, list[str]]]]] = json.load(
    open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "placed_objects.json"))
)

# Dictionary of creature spawners.  data[dentype][crittype][dlcstate][scug] -> list of rooms.
creatures: dict[str, dict[str, dict[str, [dict[str, list[str]]]]]] = json.load(
    open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "creatures.json"))
)
