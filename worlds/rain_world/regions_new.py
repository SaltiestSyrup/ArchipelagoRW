from typing import NamedTuple, Callable

from BaseClasses import Region, CollectionState, MultiWorld
from . import state_helpers
from .state_helpers import karma_and_key, max_karma_factory_factory


class ConnectionData:
    """
    Represents a connection between Archi regions.
    """
    def __init__(self, source: str, dest: str, rule: Callable[[int], Callable[[CollectionState], bool]] = None):
        self.source = source
        self.dest = dest
        self.rule = rule

    def make(self, player: int, multiworld: MultiWorld):
        source = multiworld.get_region(self.source, player)
        dest = multiworld.get_region(self.dest, player)
        source.connect(dest, rule=self.rule(player) if self.rule is not None else None)


class Gate(ConnectionData):
    """
    Represents a karma gate connection between actual regions.
    """
    def __init__(self, source: str, dest: str, cost: int):
        super().__init__(source, dest)
        self.cost = cost

    def make(self, player: int, multiworld: MultiWorld):
        source = multiworld.get_region(self.source, player)
        dest = multiworld.get_region(self.dest, player)
        source.connect(dest, rule=karma_and_key(player, self.cost, self.dest))


class RegionData(NamedTuple):
    full_name: str
    short_name: str

    def make(self, player: int, multiworld: MultiWorld):
        multiworld.regions.append(Region(self.full_name, player, multiworld))


all_regions = [
    RegionData("Menu", "Menu"),
    RegionData("Early Passages", "(P1)"),
    RegionData("PPwS Passages", "(P2)"),
    RegionData("Late Passages", "(P3)"),
    RegionData("Food Quest", "(FQ)"),
    RegionData("Outskirts", "SU"),
    RegionData("Outskirts filtration", "SU^"),
    RegionData("Industrial Complex", "HI"),
    RegionData("Drainage System", "DS"),
    RegionData("Garbage Wastes", "GW"),
    RegionData("Shoreline", "SL"),
    RegionData("Shoreline above Moon", "SL^"),
    RegionData("Pipeyard", "VS"),
    RegionData("Shaded Citadel", "SH"),
    RegionData("The Exterior", "UW"),
    RegionData("Five Pebbles", "SS"),
    RegionData("Five Pebbles above puppet", "SS^"),
    RegionData("Chimney Canopy", "CC"),
    RegionData("Sky Islands", "SI"),
    RegionData("Farm Arrays", "LF"),
    RegionData("Subterranean", "SB"),
    RegionData("Subterranean ravine", "SB^"),
    RegionData("Submerged Superstructure", "MS"),
    RegionData("Bitter Aerie", "MS^"),
    RegionData("Outer Expanse", "OE"),
    RegionData("Outer Expanse filtration", "OE^"),
    RegionData("Metropolis", "LC"),
    RegionData("Looks to the Moon", "DM"),
    RegionData("Void Sea", "(Vo)")
]


all_connections = [
    ConnectionData("Menu", "Early Passages"),
    ConnectionData("Menu", "PPwS Passages"),
    ConnectionData("Menu", "Food Quest"),
    ConnectionData("Early Passages", "Late Passages", state_helpers.haves_survivor_factory),
    ConnectionData("Menu", "Outskirts"),

    ConnectionData("Outskirts filtration", "Outskirts"),
    Gate("Outskirts", "Industrial Complex", 3),
    Gate("Outskirts", "Drainage System", 4),
    Gate("Outskirts", "Farm Arrays", 5),

    Gate("Industrial Complex", "Outskirts", 2),
    Gate("Industrial Complex", "Garbage Wastes", 2),
    Gate("Industrial Complex", "Chimney Canopy", 3),
    Gate("Industrial Complex", "Shaded Citadel", 5),
    Gate("Industrial Complex", "Pipeyard", 4),

    Gate("Garbage Wastes", "Drainage System", 3),
    Gate("Garbage Wastes", "Industrial Complex", 2),
    Gate("Garbage Wastes", "Shoreline", 3),
    Gate("Garbage Wastes", "Shaded Citadel", 4),

    Gate("Drainage System", "Outskirts", 2),
    Gate("Drainage System", "Garbage Wastes", 1),
    Gate("Drainage System", "Subterranean", 4),
    Gate("Drainage System", "Chimney Canopy", 5),

    ConnectionData("Subterranean ravine", "Subterranean"),
    Gate("Subterranean", "Drainage System", 1),
    Gate("Subterranean", "Shoreline", 2),
    Gate("Subterranean", "Pipeyard", 3),
    Gate("Subterranean", "Outer Expanse", 1),

    Gate("Farm Arrays", "Outskirts", 2),
    Gate("Farm Arrays", "Sky Islands", 3),
    Gate("Farm Arrays", "Subterranean ravine", 4),

    Gate("Sky Islands", "Chimney Canopy", 3),
    Gate("Sky Islands", "Farm Arrays", 3),
    Gate("Sky Islands", "Pipeyard", 3),

    Gate("Chimney Canopy", "Industrial Complex", 3),
    Gate("Chimney Canopy", "Sky Islands", 2),
    Gate("Chimney Canopy", "The Exterior", 4),
    Gate("Chimney Canopy", "Drainage System", 3),

    Gate("The Exterior", "Chimney Canopy", 1),
    Gate("The Exterior", "Shaded Citadel", 1),
    Gate("The Exterior", "Five Pebbles above puppet", 1),
    Gate("The Exterior", "Five Pebbles", 5),

    Gate("Shaded Citadel", "Industrial Complex", 1),
    Gate("Shaded Citadel", "Shoreline", 3),
    Gate("Shaded Citadel", "The Exterior", 1),
    Gate("Shaded Citadel", "Garbage Wastes", 2),

    Gate("Shoreline", "Garbage Wastes", 2),
    Gate("Shoreline", "Shaded Citadel", 2),
    Gate("Shoreline", "Subterranean", 5),
    Gate("Shoreline", "Pipeyard", 3),
    Gate("Shoreline", "Submerged Superstructure", 5),
    Gate("Shoreline", "Bitter Aerie", 6),
    ConnectionData("Shoreline above Moon", "Shoreline"),

    Gate("Pipeyard", "Industrial Complex", 2),
    Gate("Pipeyard", "Shoreline", 3),
    Gate("Pipeyard", "Subterranean", 5),
    Gate("Pipeyard", "Sky Islands", 4),

    Gate("Five Pebbles", "The Exterior", 1),
    Gate("Five Pebbles above puppet", "The Exterior", 1),
    ConnectionData("Five Pebbles", "Five Pebbles above puppet"),

    Gate("Outer Expanse", "Subterranean", 5),
    ConnectionData("Outer Expanse", "Outer Expanse filtration"),
    Gate("Outer Expanse filtration", "Outskirts filtration", 1),

    Gate("Bitter Aerie", "Shoreline above Moon", 5),
    Gate("Shoreline above Moon", "Bitter Aerie", 6),
    Gate("Submerged Superstructure", "Shoreline", 1),

    ConnectionData("Subterranean", "Void Sea", max_karma_factory_factory(10))
]
