"""
A collection of custom classes used by the Rain World world, some of which inherit BaseClasses.
"""

from typing import List, Dict

from BaseClasses import Location, Region, MultiWorld
from .constants import FIRST_ID


location_name_to_id: Dict[str, int] = {}


class LocationData:
    """
    Represents information common to all Rain World location types.
    """
    def __init__(self, name: str, room: str, offset: int):
        self.name = name
        self.room = room
        self.offset = offset
        self.region = room.split("_")[0]
        location_name_to_id[name] = FIRST_ID + offset

    def generate_location(self, player: int, region: Region) -> Location:
        """
        Generate a `Location` from this data.
        """
        return Location(player, self.name, FIRST_ID + self.offset, region)


class TokenData(LocationData):
    """
    Represents an unlockable token.
    """
    def __init__(self, name: str, room: str, offset: int, color: str):
        super().__init__(f"CT|{color}|{name}", room, offset)
        self.color = color


class EchoData(LocationData):
    def generate_location(self, player: int, region: Region) -> Location:
        pass


class RainWorldRegion(Region):
    def __init__(self, name: str, player: int, multiworld: MultiWorld, region_code: str):
        super().__init__(name, player, multiworld)
        self.region_code = region_code


class RegionData:
    """
    Represents a Rain World region.
    """
    def __init__(self, full_name: str, region_code: str, locations: List[LocationData]):
        self.full_name: str = full_name
        self.region_code: str = region_code
        self.locations: List[LocationData] = locations

    def generate_region(self, player: int, multiworld: MultiWorld) -> RainWorldRegion:
        """
        Generate a `RainWorldRegion` from this data.  Locations are automatically generated and appended.
        """
        region = RainWorldRegion(self.region_code, player, multiworld, self.region_code)

        for data in self.locations:
            region.locations.append(data.generate_location(player, region))

        return region
