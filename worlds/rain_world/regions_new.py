from typing import NamedTuple, Callable

from BaseClasses import Region, CollectionState, MultiWorld
from . import state_helpers
from .state_helpers import max_karma_factory_factory, karma_and_gate


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
    def __init__(self, source: str, dest: str, cost: int, gate_name: str):
        super().__init__(source, dest)
        self.cost = cost
        self.gate_name = gate_name

    def make(self, player: int, multiworld: MultiWorld):
        source = multiworld.get_region(self.source, player)
        dest = multiworld.get_region(self.dest, player)
        source.connect(dest, rule=karma_and_gate(player, self.cost, self.gate_name))


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
    RegionData("Starting region", "START"),

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
    ConnectionData("Late Passages", "PPwS Passages"),  # default connect PPwS to late to require survivor
    ConnectionData("Menu", "Food Quest"),
    ConnectionData("Early Passages", "Late Passages", state_helpers.haves_survivor_factory),
    ConnectionData("Menu", "Starting region"),

    ConnectionData("Outskirts filtration", "Outskirts"),
    Gate("Outskirts", "Industrial Complex", 3, "SU_HI"),
    Gate("Outskirts", "Drainage System", 4, "SU_DS"),
    Gate("Outskirts", "Farm Arrays", 5, "LF_SU"),

    Gate("Industrial Complex", "Outskirts", 2, "SU_HI"),
    Gate("Industrial Complex", "Garbage Wastes", 2, "HI_GW"),
    Gate("Industrial Complex", "Chimney Canopy", 3, "HI_CC"),
    Gate("Industrial Complex", "Shaded Citadel", 5, "HI_SH"),
    Gate("Industrial Complex", "Pipeyard", 4, "HI_VS"),

    Gate("Garbage Wastes", "Drainage System", 3, "DS_GW"),
    Gate("Garbage Wastes", "Industrial Complex", 2, "HI_GW"),
    Gate("Garbage Wastes", "Shoreline", 3, "GW_SL"),
    Gate("Garbage Wastes", "Shaded Citadel", 4, "GW_SH"),

    Gate("Drainage System", "Outskirts", 2, "SU_DS"),
    Gate("Drainage System", "Garbage Wastes", 1, "DS_GW"),
    Gate("Drainage System", "Subterranean", 4, "DS_SB"),
    Gate("Drainage System", "Chimney Canopy", 5, "DS_CC"),

    ConnectionData("Subterranean ravine", "Subterranean"),
    Gate("Subterranean", "Drainage System", 1, "DS_SB"),
    Gate("Subterranean", "Shoreline", 2, "SB_SL"),
    Gate("Subterranean", "Pipeyard", 3, "SB_VS"),
    Gate("Subterranean", "Outer Expanse", 1, "OE_SB"),

    Gate("Farm Arrays", "Outskirts", 2, "LF_SU"),
    Gate("Farm Arrays", "Sky Islands", 3, "SI_LF"),
    Gate("Farm Arrays", "Subterranean ravine", 4, "LF_SB"),

    Gate("Sky Islands", "Chimney Canopy", 3, "SI_CC"),
    Gate("Sky Islands", "Farm Arrays", 3, "SI_LF"),
    Gate("Sky Islands", "Pipeyard", 3, "SI_VS"),

    Gate("Chimney Canopy", "Industrial Complex", 3, "HI_CC"),
    Gate("Chimney Canopy", "Sky Islands", 2, "SI_CC"),
    Gate("Chimney Canopy", "The Exterior", 4, "CC_UW"),
    Gate("Chimney Canopy", "Drainage System", 3, "DS_CC"),

    Gate("The Exterior", "Chimney Canopy", 1, "CC_UW"),
    Gate("The Exterior", "Shaded Citadel", 1, "SH_UW"),
    Gate("The Exterior", "Five Pebbles above puppet", 1, "SS_UW"),
    Gate("The Exterior", "Five Pebbles", 5, "UW_SS"),

    Gate("Shaded Citadel", "Industrial Complex", 1, "HI_SH"),
    Gate("Shaded Citadel", "Shoreline", 3, "SH_SL"),
    Gate("Shaded Citadel", "The Exterior", 1, "SH_UW"),
    Gate("Shaded Citadel", "Garbage Wastes", 2, "GW_SH"),

    Gate("Shoreline", "Garbage Wastes", 2, "GW_SL"),
    Gate("Shoreline", "Shaded Citadel", 2, "GW_SH"),
    Gate("Shoreline", "Subterranean", 5, "SB_SL"),
    Gate("Shoreline", "Pipeyard", 3, "SL_VS"),
    Gate("Shoreline", "Submerged Superstructure", 5, "SL_MS"),
    # Gate("Shoreline", "Bitter Aerie", 6, "MS_SL"),
    ConnectionData("Shoreline above Moon", "Shoreline"),

    Gate("Pipeyard", "Industrial Complex", 2, "HI_VS"),
    Gate("Pipeyard", "Shoreline", 3, "SL_VS"),
    Gate("Pipeyard", "Subterranean", 5, "SB_VS"),
    Gate("Pipeyard", "Sky Islands", 4, "SI_VS"),

    Gate("Five Pebbles", "The Exterior", 1, "UW_SS"),
    Gate("Five Pebbles above puppet", "The Exterior", 1, "SS_UW"),
    ConnectionData("Five Pebbles", "Five Pebbles above puppet"),

    Gate("Outer Expanse", "Subterranean", 5, "SB_OE"),
    ConnectionData("Outer Expanse", "Outer Expanse filtration"),
    Gate("Outer Expanse filtration", "Outskirts filtration", 1, "OE_SU"),

    Gate("Bitter Aerie", "Shoreline above Moon", 5, "SL_MS"),
    Gate("Shoreline above Moon", "Bitter Aerie", 6, "SL_MS"),
    Gate("Submerged Superstructure", "Shoreline", 1, "MS_SL"),

    ConnectionData("Subterranean", "Void Sea", max_karma_factory_factory(10))
]
