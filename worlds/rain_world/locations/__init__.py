from . import passages, echoes, foodquest, unique, tokens_pearls
from .classes import LocationData
from ..options import RainWorldOptions

# ID OFFSET BLOCKS:
# Tokens/Pearls        0 -  999
# Unique            4900 - 4999
# Passages          5000 - 5046
# Echoes            5070 - 5079
# Food Quest        5250 - 5271


def generate(options: RainWorldOptions) -> list[LocationData]:
    return [
        *tokens_pearls.generate(options),
        *unique.generate(options),
        *passages.generate(options),
        *echoes.locations,
        *foodquest.generate(options),
    ]
