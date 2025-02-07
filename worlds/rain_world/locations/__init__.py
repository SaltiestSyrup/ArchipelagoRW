from . import passages, misc, physical, echoes, foodquest, broadcasts
from .classes import LocationData

all_locations: list[LocationData] = [
    *physical.locations,
    *passages.locations,
    *echoes.locations,
    *foodquest.locations,
    *broadcasts.locations,
    *misc.locations,
]

# ID OFFSET BLOCKS:
# Physical             0 - 2020
# Passages          5000 - 5046
# Echoes            5070 - 5079
# Food Quest        5250 - 5271
# Broadcasts        5350 - 5375
