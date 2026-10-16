from BaseClasses import Region
from rule_builder.rules import True_, Has, False_, HasAll, Rule
from .classes import room_to_region
from ..options import RainWorldOptions
from ..game_data.general import scugs_all, accessible_gates, region_code_to_name, direct_alternate_regions
from ...AutoWorld import World


class GateData:
    def __init__(self, name: str, left: int, right: int, was_swapped: bool = False):
        self.name = name
        self.left = left
        self.right = right
        self.was_swapped = was_swapped

    def make(self, world: World, options: RainWorldOptions, regions: dict[str, Region]):
        dlcstate = "MSC" if options.msc_enabled else "Vanilla"
        if self.name[5:] not in accessible_gates[dlcstate][options.starting_scug]:
            return

        for effective_name, scugs in self.effective_names(options).items():
            _, left_name, right_name = effective_name.split("_")
            key_rule = True_() if self.item_name is None else Has(self.item_name)
            karma_rule_left = Has("Karma", self.left - 1 if self.left < 6 else 2)
            karma_rule_right = Has("Karma", self.right - 1 if self.right < 6 else 2)

            left_reg = regions[room_to_region[f'{self.name}[{left_name}]']]
            right_reg = regions[room_to_region[f'{self.name}[{right_name}]']]

            if not left_reg or not right_reg:
                continue

            match options.which_gate_behavior:
                case "karma_only":
                    left_cost = karma_rule_left
                    right_cost = karma_rule_right
                case "key_only":
                    left_cost = key_rule
                    right_cost = key_rule
                case "key_and_karma":
                    left_cost = key_rule & karma_rule_left
                    right_cost = key_rule & karma_rule_right
                case "key_or_karma":
                    left_cost = key_rule | karma_rule_left
                    right_cost = key_rule | karma_rule_right
                case _:
                    raise ValueError(f"invalid setting: {options.which_gate_behavior=}")

            # Some gates are always open to prevent softlocks
            if self.left < 0:
                left_cost = True_()
            if self.right < 0:
                right_cost = True_()

            _l, _r = self.additional_conditions(options)
            left_condition = _l & left_cost
            right_condition = _r & right_cost

            if left_reg.populate and right_reg.populate and options.starting_scug in scugs:
                world.create_entrance(left_reg, right_reg, left_condition, self.entrance_names[0])
                world.create_entrance(right_reg, left_reg, right_condition, self.entrance_names[1])

    @property
    def item_name(self) -> str | None:
        if self in gates_no_item:
            return None
        return self.names[0]

    @property
    def entrance_names(self) -> tuple[str, str]:
        return (f"{'West' if self.was_swapped else 'East'} through {self.name}",
                f"{'East' if self.was_swapped else 'West'} through {self.name}")


    @property
    def names(self) -> list[str]:
        _, left_code, right_code = self.name.split("_")
        left_name, right_name = region_code_to_name[left_code], region_code_to_name[right_code]

        if self.name == "GATE_SS_UW": right_name = "The Wall"
        if self.name == "GATE_UW_SS": left_name = "Underhang"
        if self.name == "GATE_SL_MS": right_name = "Bitter Aerie"
        if self.name == "GATE_SL_DM": left_name = "The Precipice"
        if self.name == "GATE_DM_SL": left_name, right_name = "The Struts", "Waterfront Facility"

        ret = [f'Gate: {left_name} to {right_name}', f'Gate: {right_name} to {left_name}']

        for alt in direct_alternate_regions.get(left_code, []):
            left_alt = region_code_to_name[alt]
            ret += [f'Gate: {left_alt} to {right_name}', f'Gate: {right_name} to {left_alt}']

        for alt in direct_alternate_regions.get(right_code, []):
            right_alt = region_code_to_name[alt]
            ret += [f'Gate: {left_name} to {right_alt}', f'Gate: {right_alt} to {left_name}']

        # HARDCODE: gross bandaid fix for item group name collision with GATE_SL_CL
        if self.name == "GATE_SH_SL":
            ret = [r for r in ret if "Silent Construct" not in r]

        return ret + [self.name]

    def is_accessible(self, options: RainWorldOptions):
        return self.name[5:] in accessible_gates[options.dlcstate][options.starting_scug]

    def additional_conditions(self, options: RainWorldOptions) -> tuple[Rule, Rule]:
        left, right, gg = True_(), True_(), self.name[5:]

        if options.difficulty_glow:
            if gg in ("HI_SH", "GW_SH", "DS_SB"):
                left = Has("The Glow")
            elif gg in ("SH_UW", "SH_SL", "SB_VS"):
                right = Has("The Glow")

        if gg == "SB_OE":
            if not options.msc_enabled or options.starting_scug not in ("White", "Yellow", "Gourmand"):
                left = False_()
            if options.starting_scug == "Gourmand":
                left = Has("The Mark")

        if gg == "UW_LC":
            if not (options.msc_enabled and options.starting_scug == "Artificer"):
                left = False_()
            else:
                left = HasAll("The Mark", "Citizen ID Drone")

        if gg == "MS_SL":
            if not options.submerged_should_populate:
                left = False_()
                right = False_()
            elif options.starting_scug == "Rivulet" and options.difficulty_submerged == 2:
                left = Has("Disconnect_FP")

        if gg == "SL_MS":
            left = False_()
            right = True_()

        return left, right

    def effective_names(self, options: RainWorldOptions) -> dict[str, set[str]]:
        ret = {self.name: set(scugs_all)}

        if not options.msc_enabled:
            return ret

        if "DS" in self.name:
            ret[self.name.replace("DS", "UG")] = {"Saint"}
            ret[self.name].remove("Saint")

        if self.name in ["GATE_HI_SH", "GATE_GW_SH"]:
            ret[self.name.replace("SH", "CL")] = {"Saint"}
            ret[self.name].remove("Saint")

        if "SL" in self.name and "CL" not in self.name and "MS" not in self.name:
            ret[self.name.replace("SL", "LM")] = {"Artificer", "Spear"}
            # DM_SL and SL_DM don't have SL counterparts and so should be processed exclusively as DM_LM and LM_DM.
            if "DM" in self.name:
                del ret[self.name]
            else:
                ret[self.name].remove("Artificer")
                ret[self.name].remove("Spear")

        if "SS" in self.name:
            ret[self.name.replace("SS", "RM")] = {"Rivulet"}
            ret[self.name].remove("Rivulet")

        return ret


gates = [
    GateData("GATE_SU_DS", 4, 2),
    GateData("GATE_SU_HI", 3, 2),
    GateData("GATE_LF_SU", 2, 5),
    GateData("GATE_CC_UW", 4, 1),
    GateData("GATE_DS_GW", 1, 3),
    GateData("GATE_DS_SB", 4, 1, True),
    GateData("GATE_GW_SL", 3, 2),
    GateData("GATE_HI_CC", 3, 3, True),
    GateData("GATE_HI_GW", 2, 2),
    GateData("GATE_HI_SH", 5, 1),
    GateData("GATE_LF_SB", 4, 5, True),
    GateData("GATE_SB_SL", 2, 5),
    GateData("GATE_SH_UW", 1, 1),
    GateData("GATE_SH_SL", 3, 2),
    GateData("GATE_SI_CC", 3, 2),
    GateData("GATE_SI_LF", 3, 3),
    GateData("GATE_SS_UW", 1, 1),
    GateData("GATE_UW_SS", 5, 1),
    GateData("GATE_MS_SL", 1, 5, True),
    GateData("GATE_SB_OE", 1, 5, True),
    GateData("GATE_UW_LC", 0, 5),
    GateData("GATE_SL_DM", 5, 1),
    GateData("GATE_UW_SL", 1, 1),
    GateData("GATE_GW_SH", 4, 2),
    GateData("GATE_DS_CC", 5, 3),
    GateData("GATE_SL_CL", 5, 1),
    GateData("GATE_HI_VS", 4, 2),
    GateData("GATE_SL_VS", 3, 3),
    GateData("GATE_SB_VS", 3, 5),
    GateData("GATE_SI_VS", 3, 4, True),
    GateData("GATE_DM_SL", 1, 1),
]

# These gates are always open, and should not have an item associated with them
gates_no_item = [
    GateData("GATE_SL_MS", 999, -1),
    GateData("GATE_OE_SU", -1, -1),
]


def generate(_: RainWorldOptions) -> list[GateData]:
    return [*gates, *gates_no_item]
