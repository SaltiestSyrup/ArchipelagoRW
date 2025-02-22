from . import physical, classes, abstract, gates
from ..options import RainWorldOptions


def generate(options: RainWorldOptions) -> list[classes.RegionData | classes.ConnectionData]:
    return [
        *abstract.generate(options),
        *physical.generate(options),
        *gates.generate(options),
    ]
