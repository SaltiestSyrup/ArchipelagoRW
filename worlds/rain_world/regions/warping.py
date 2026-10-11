from rule_builder.options import OptionFilter
from rule_builder.rules import Filtered
from .classes import RegionData, ConnectionData
from ..options import RainWorldOptions, LogicRottedGeneration
from ..conditions.classes import Simple, AnyOf

cond_can_dynamic_warp = AnyOf(Simple("Ripple", 2), Simple("Dial Warp Ability"), Simple("Progressive Weaver", 4))

def generate(options: RainWorldOptions):
    if options.starting_scug != "Watcher":
        return []

    cond_can_rotted_warp = Filtered(cond_can_dynamic_warp.get_rule(),
                                    options=[OptionFilter(LogicRottedGeneration, 2)])

    ret = [
        RegionData("From any normal region"),

        ConnectionData("Menu", "From any normal region", "Create a dynamic warp",
                       cond_can_dynamic_warp),
        ConnectionData("From any normal region", "Crumbling Fringes", "Bad dynamic warp to Crumbling Fringes",
                       cond_can_rotted_warp),
        ConnectionData("From any normal region", "Corrupted Factories", "Bad dynamic warp to Corrupted Factories",
                       cond_can_rotted_warp),
        ConnectionData("From any normal region", "Decaying Tunnels", "Bad dynamic warp to Decaying Tunnels",
                       cond_can_rotted_warp),
        ConnectionData("From any normal region", "Infested Wastes", "Bad dynamic warp to Infested Wastes",
                       cond_can_rotted_warp),
        # Logical connection is directly to Outer Rim if rotted regions are passthrough
        ConnectionData("From any normal region", "Western Outer Rim", "Bad dynamic warp to Outer Rim",
                       Filtered(cond_can_dynamic_warp.get_rule(), options=[OptionFilter(LogicRottedGeneration, 1)]))
    ]

    return ret



