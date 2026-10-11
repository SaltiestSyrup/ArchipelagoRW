from BaseClasses import Region, MultiWorld
from rule_builder.rules import Rule, True_
from ..options import RainWorldOptions
from ..conditions.classes import Condition
from ...AutoWorld import World


class RainWorldRegion(Region):
    game = "Rain World"

    def __init__(self, name: str, player: int, multiworld: MultiWorld, populate: bool,
                 rooms: set[str] | None = None, code: str = ""):
        super().__init__(name, player, multiworld)
        self.populate, self.rooms, self.code = populate, rooms, code


class RegionData:
    def __init__(self, name: str, populate: bool = True):
        self.name, self.populate = name, populate

    def make(self, world: World, _: RainWorldOptions) -> Region:
        return RainWorldRegion(self.name, world.player, world.multiworld, self.populate)


class ConnectionData:
    """
    Represents a connection between Archi regions.
    """
    def __init__(self, source: str, dest: str, name: str, condition: Condition | Rule = True_()):
        self.source, self.dest, self.name = source, dest, name
        self.condition = condition if isinstance(condition, Rule) else condition.get_rule()

    def make(self, world: World, options: RainWorldOptions, regions: dict[str, Region]):
        if self.source in regions and self.dest in regions:
            source = regions[self.source]
            dest = regions[self.dest]
            world.create_entrance(source, dest, self.condition, self.name)


room_to_region: dict[str, str] = dict()


class PhysicalRegion(RegionData):
    def __init__(self, name: str, prefix: str, rooms: set[str]):
        super().__init__(name, True)
        self.prefix, self.rooms = prefix, rooms

    def make(self, world: World, options: RainWorldOptions) -> Region | None:
        room_to_region.update({room: self.name for room in self.rooms})
        return RainWorldRegion(self.name, world.player, world.multiworld, self.populate, self.rooms, self.prefix)