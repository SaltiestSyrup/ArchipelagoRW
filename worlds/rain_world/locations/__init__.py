from . import passages, misc, physical, echoes
from .classes import LocationData

all_locations: list[LocationData] = [
    *physical.locations,
    *echoes.locations,
    *passages.locations,
    *misc.locations,
]
