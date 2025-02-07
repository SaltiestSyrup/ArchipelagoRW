from . import passages, misc, physical, echoes, foodquest
from .classes import LocationData

all_locations: list[LocationData] = [
    *physical.locations,
    *echoes.locations,
    *passages.locations,
    *foodquest.locations,
    *misc.locations,
]

# ID OFFSET BLOCKS:
# Physical             0 - 1420
# Passages          5000 - 5046
# Echoes            5070 - 5079
# Food Quest        5250 - 5271
