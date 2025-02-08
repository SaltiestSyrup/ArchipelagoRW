from . import passages, physical, echoes, foodquest, broadcasts, unique
from .classes import LocationData
from ..options import RainWorldOptions

# ID OFFSET BLOCKS:
# Physical             0 - 2020
# Unique            4900 - 4999
# Passages          5000 - 5046
# Echoes            5070 - 5079
# Food Quest        5250 - 5271
# Broadcasts        5350 - 5375


def generate(options: RainWorldOptions) -> list[LocationData]:
    return [
        *physical.locations,
        *unique.generate(options),
        *passages.generate(options),
        *echoes.locations,
        *foodquest.locations,
        *broadcasts.locations,
    ]
