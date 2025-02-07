from . import passages, misc, physical, echoes, foodquest
from .classes import LocationData

all_locations: list[LocationData] = [
    *physical.locations,
    *echoes.locations,
    *passages.locations,
    *foodquest.locations,
    *misc.locations,
]
