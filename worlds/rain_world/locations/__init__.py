from . import passages, misc, physical, echoes, foodquest, broadcasts
from .classes import LocationData
from ..options import RainWorldOptions

# ID OFFSET BLOCKS:
# Physical             0 - 2020
# Passages          5000 - 5046
# Echoes            5070 - 5079
# Food Quest        5250 - 5271
# Broadcasts        5350 - 5375


def generate(options: RainWorldOptions) -> list[LocationData]:
    return [
        *physical.locations,
        *passages.generate(options),
        *echoes.locations,
        *foodquest.locations,
        *broadcasts.locations,
        *misc.locations,
    ]
