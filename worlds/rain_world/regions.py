from typing import NamedTuple

from BaseClasses import Region, CollectionState, MultiWorld
from .conditions.classes import Condition, Simple, Compound, ConditionBlank
from .game_data.general import scug_names


class ConnectionData:
    """
    Represents a connection between Archi regions.
    """
    def __init__(self, source: str, dest: str, condition: Condition = ConditionBlank):
        self.source = source
        self.dest = dest
        self.condition = condition

    def make(self, player: int, multiworld: MultiWorld):
        source = multiworld.get_region(self.source, player)
        dest = multiworld.get_region(self.dest, player)
        source.connect(dest, rule=self.condition.check(player))


class Gate(ConnectionData):
    """
    Represents a karma gate connection between actual regions.
    """
    def __init__(self, source: str, dest: str, cost: int, gate_name: str, condition: Condition = ConditionBlank):
        super().__init__(source, dest)
        self.cost = cost
        self.gate_name = gate_name
        self.condition = condition

    def make(self, player: int, multiworld: MultiWorld):
        source = multiworld.get_region(self.source, player)
        dest = multiworld.get_region(self.dest, player)
        conditions = [
            Simple("Karma", self.cost - (1 if self.cost < 6 else 2)),
            Simple(f"GATE_{self.gate_name}"),
            self.condition
        ]
        rule = Compound(len(conditions), *conditions)
        source.connect(dest, name=f'GATE_{self.gate_name} (to {dest.name})', rule=rule.check(player))


class RegionData(NamedTuple):
    full_name: str
    short_name: str

    def make(self, player: int, multiworld: MultiWorld):
        multiworld.regions.append(Region(self.full_name, player, multiworld))


def any_scug_except(scugs: list[str]) -> Simple:
    return Simple([f"Scug-{s}" for s in set(scug_names.values()).difference(set(scugs))], 1)


def one_of_these_scugs(scugs: list[str]) -> Simple:
    return Simple([f"Scug-{s}" for s in scugs], 1)


all_regions = [
    RegionData("Menu", "Menu"),
    RegionData("Early Passages", "(P1)"),
    RegionData("PPwS Passages", "(P2)"),
    RegionData("Late Passages", "(P3)"),
    RegionData("Food Quest", "(FQ)"),
    RegionData("Starting region", "START"),
    RegionData("Events", "(EV)"),

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
    RegionData("The Rot", "RM"),
    RegionData("Undergrowth", "UG"),
    RegionData("Silent Construct", "CL"),
    RegionData("Waterfront Facility", "LM"),
    RegionData("Rubicon", "HR"),
    RegionData("Void Sea", "(Vo)")
]


all_connections = [
    ConnectionData("Menu", "Early Passages"),
    ConnectionData("Late Passages", "PPwS Passages"),  # default connect PPwS to late to require survivor
    ConnectionData("Menu", "Food Quest", Simple("MSC")),
    ConnectionData("Early Passages", "Late Passages", Simple("Passage-Survivor")),
    ConnectionData("Menu", "Starting region"),
    ConnectionData("Menu", "Events"),

    ConnectionData("Outskirts filtration", "Outskirts"),
    Gate("Outskirts", "Industrial Complex", 3, "SU_HI"),
    Gate("Outskirts", "Drainage System", 4, "SU_DS", any_scug_except(["Saint"])),
    Gate("Outskirts", "Undergrowth", 4, "SU_DS", one_of_these_scugs(["Saint"])),
    Gate("Outskirts", "Farm Arrays", 5, "LF_SU"),

    Gate("Industrial Complex", "Outskirts", 2, "SU_HI"),
    Gate("Industrial Complex", "Garbage Wastes", 2, "HI_GW"),
    Gate("Industrial Complex", "Chimney Canopy", 3, "HI_CC"),
    Gate("Industrial Complex", "Shaded Citadel", 5, "HI_SH"),
    Gate("Industrial Complex", "Pipeyard", 4, "HI_VS", Simple("MSC")),
    Gate("Industrial Complex", "Silent Construct", 4, "HI_VS", one_of_these_scugs(["Saint"])),

    Gate("Garbage Wastes", "Drainage System", 3, "DS_GW"),
    Gate("Garbage Wastes", "Industrial Complex", 2, "HI_GW"),
    Gate("Garbage Wastes", "Shoreline", 3, "GW_SL", any_scug_except(["Artificer", "Spear"])),
    Gate("Garbage Wastes", "Shaded Citadel", 4, "GW_SH", Simple("MSC")),
    Gate("Garbage Wastes", "Waterfront Facility", 3, "GW_SL", one_of_these_scugs(["Artificer", "Spear"])),
    Gate("Garbage Wastes", "Silent Construct", 4, "GW_SH", one_of_these_scugs(["Saint"])),
    Gate("Garbage Wastes", "Undergrowth", 3, "DS_GW", one_of_these_scugs(["Saint"])),

    Gate("Drainage System", "Outskirts", 2, "SU_DS"),
    Gate("Drainage System", "Garbage Wastes", 1, "DS_GW"),
    Gate("Drainage System", "Subterranean", 4, "DS_SB"),
    Gate("Drainage System", "Chimney Canopy", 5, "DS_CC", Simple("MSC")),

    Gate("Shoreline", "Garbage Wastes", 2, "GW_SL"),
    Gate("Shoreline", "Shaded Citadel", 2, "SH_SL"),
    Gate("Shoreline", "Subterranean", 5, "SB_SL"),
    Gate("Shoreline", "Pipeyard", 3, "SL_VS", Simple("MSC")),
    Gate("Shoreline", "Submerged Superstructure", 5, "SL_MS", Simple("MSC")),
    # Gate("Shoreline", "Bitter Aerie", 6, "MS_SL",  Simple("MSC")),
    Gate("Shoreline", "Silent Construct", 5, "SH_SL", one_of_these_scugs(["Saint"])),
    ConnectionData("Shoreline above Moon", "Shoreline"),

    Gate("Shaded Citadel", "Industrial Complex", 1, "HI_SH"),
    Gate("Shaded Citadel", "Shoreline", 3, "SH_SL"),
    Gate("Shaded Citadel", "The Exterior", 1, "SH_UW"),
    Gate("Shaded Citadel", "Garbage Wastes", 2, "GW_SH", Simple("MSC")),
    Gate("Shaded Citadel", "Waterfront Facility", 3, "SH_SL", one_of_these_scugs(["Artificer", "Spear"])),

    Gate("The Exterior", "Chimney Canopy", 1, "CC_UW"),
    Gate("The Exterior", "Shaded Citadel", 1, "SH_UW"),
    Gate("The Exterior", "Five Pebbles above puppet", 1, "SS_UW"),
    Gate("The Exterior", "Five Pebbles", 5, "UW_SS"),
    Gate("The Exterior", "Waterfront Facility", 3, "UW_SL", one_of_these_scugs(["Artificer", "Spear"])),
    Gate("The Exterior", "Metropolis", 5, "UW_LC", one_of_these_scugs(["Artificer"])),  # TODO
    Gate("The Exterior", "The Rot", 1, "SS_UW", one_of_these_scugs(["Rivulet"])),
    Gate("The Exterior", "The Rot", 5, "UW_SS", one_of_these_scugs(["Rivulet"])),

    Gate("Chimney Canopy", "Industrial Complex", 3, "HI_CC"),
    Gate("Chimney Canopy", "Sky Islands", 2, "SI_CC"),
    Gate("Chimney Canopy", "The Exterior", 4, "CC_UW"),
    Gate("Chimney Canopy", "Drainage System", 3, "DS_CC", Simple("MSC")),
    Gate("Chimney Canopy", "Undergrowth", 3, "DS_CC", one_of_these_scugs(["Saint"])),

    Gate("Sky Islands", "Chimney Canopy", 3, "SI_CC"),
    Gate("Sky Islands", "Farm Arrays", 3, "SI_LF"),
    Gate("Sky Islands", "Pipeyard", 3, "SI_VS", Simple("MSC")),

    Gate("Farm Arrays", "Outskirts", 2, "LF_SU"),
    Gate("Farm Arrays", "Sky Islands", 3, "SI_LF"),
    Gate("Farm Arrays", "Subterranean ravine", 4, "LF_SB"),

    ConnectionData("Subterranean ravine", "Subterranean"),
    Gate("Subterranean", "Drainage System", 1, "DS_SB"),
    Gate("Subterranean", "Shoreline", 2, "SB_SL"),
    Gate("Subterranean", "Pipeyard", 3, "SB_VS", Simple("MSC")),
    Gate("Subterranean", "Outer Expanse", 1, "OE_SB",
         Compound(2, Simple("MSC"), one_of_these_scugs(["Yellow", "White", "Gourmand"]))),
    Gate("Subterranean", "Waterfront Facility", 2, "SB_SL", one_of_these_scugs(["Artificer", "Rivulet"])),
    Gate("Subterranean", "Undergrowth", 1, "DS_SB", one_of_these_scugs(["Saint"])),
    # Gate("Subterranean", "Rubicon", 10, "DS_SB", one_of_these_scugs(["Saint"])),

    ################################################################
    # DOWNPOUR

    Gate("Pipeyard", "Industrial Complex", 2, "HI_VS", Simple("MSC")),
    Gate("Pipeyard", "Shoreline", 3, "SL_VS", Simple("MSC")),
    Gate("Pipeyard", "Subterranean", 5, "SB_VS", Simple("MSC")),
    Gate("Pipeyard", "Sky Islands", 4, "SI_VS", Simple("MSC")),
    Gate("Pipeyard", "Waterfront Facility", 3, "SL_VS", one_of_these_scugs(["Artificer", "Rivulet"])),

    Gate("Five Pebbles", "The Exterior", 1, "UW_SS"),
    Gate("Five Pebbles above puppet", "The Exterior", 1, "SS_UW"),
    ConnectionData("Five Pebbles", "Five Pebbles above puppet"),

    Gate("Outer Expanse", "Subterranean", 5, "SB_OE",  Simple("MSC")),
    ConnectionData("Outer Expanse", "Outer Expanse filtration"),
    Gate("Outer Expanse filtration", "Outskirts filtration", 1, "OE_SU",  Simple("MSC")),

    Gate("Bitter Aerie", "Shoreline above Moon", 5, "SL_MS",  Simple("MSC")),
    Gate("Shoreline above Moon", "Bitter Aerie", 6, "SL_MS",  Simple("MSC")),
    Gate("Submerged Superstructure", "Shoreline", 1, "MS_SL",  Simple("MSC")),

    ConnectionData("Subterranean", "Void Sea", Simple("Karma", 8))
]

all_gate_short_names = set(item.gate_name for item in all_connections if type(item) == Gate)
