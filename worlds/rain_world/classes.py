"""
A collection of custom classes used by the Rain World world, some of which inherit BaseClasses.
"""

from typing import List, Dict, Callable, Optional

from BaseClasses import Location, Region, MultiWorld, CollectionState
from .constants import FIRST_ID
from ..generic.Rules import add_rule

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


class Condition:
    def __call__(self):
        return self.check

    def check(self, player: int) -> Callable[[CollectionState], bool]:
        return lambda state: True


ConditionBlank = Condition()


class Simple(Condition):
    """Represents a simple check against a CollectionState."""
    def __init__(self, items: list[str] | str, count: Optional[int] = None,
                 unique: Optional[bool] = None, negative: bool = False,
                 locations: bool = False):
        """
        :param items:  The item or list of items to check against.
        :param count:  The number of items that must be found in the CollectionState.
        If unspecified, all items must be found (`count == len(items)` if `items` is a list, or 1 otherwise).
        :param unique:  Whether duplicate items should be ignored.
        If unspecified, `unqiue` is `False` if `items` is a string and `True` if it's a list.
        :param negative:  Whether the condition should be negated.
        """
        self.unique: bool = unique or (type(items) == list)
        self.items: list[str] = [items] if type(items) == str else items
        self.count: int = count or len(self.items)
        self.negative: bool = negative
        self.locations: bool = locations

    def check(self, player: int) -> Callable[[CollectionState], bool]:
        def inner(state: CollectionState) -> bool:
            if len(self.items) == 0:
                return True
            if self.locations:
                ret = sum(state.can_reach_location(item) for item in self.items) >= self.count
            elif self.unique:
                ret = state.has_from_list_unique(self.items, player, self.count)
            else:
                ret = state.has_from_list(self.items, player, self.count)

            return (not ret) if self.negative else ret
        return inner


class Compound(Condition):
    """Represents multiple checks against a CollectionState, some specified number of which must be satsified."""
    def __init__(self, count: int, *conditions: Condition):
        self.conditions = conditions
        self.count = count

    def check(self, player: int) -> Callable[[CollectionState], bool]:
        def inner(state: CollectionState) -> bool:
            if self.count > len(self.conditions):
                return False
            elif self.count == len(self.conditions):
                return all(c.check(player)(state) for c in self.conditions)
            elif self.count == 1:
                return any(c.check(player)(state) for c in self.conditions)
            else:
                return sum(c.check(player)(state) for c in self.conditions) >= self.count
        return inner


class AnyOf(Compound):
    def __init__(self, *conditions: Condition):
        super().__init__(1, *conditions)


class AllOf(Compound):
    def __init__(self, *conditions: Condition):
        super().__init__(len(conditions), *conditions)
