from . import physical, classes, abstract, gates, portals, warping
from ..options import RainWorldOptions


def generate(options: RainWorldOptions) -> list[classes.RegionData | classes.ConnectionData]:
    return [
        *abstract.generate(options),
        *physical.generate(options),
        *gates.generate(options),
        *portals.generate(options),
        *warping.generate(options),
    ]

def generate_regions(options: RainWorldOptions) -> list[classes.RegionData]:
    return [
        *abstract.generate(options),
        *physical.generate(options),
    ]

def generate_connections(options: RainWorldOptions) -> list[classes.ConnectionData]:
    return [
        *gates.generate(options),
        *portals.generate(options),
        *warping.generate(options),
    ]
