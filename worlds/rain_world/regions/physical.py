from ..game_data.general import region_code_to_name
from ..game_data import static_data
from ..conditions.classes import Simple, AllOf
from ..options import RainWorldOptions
from .classes import ConnectionData, PhysicalRegion


def _generate(options: RainWorldOptions) -> list[PhysicalRegion | ConnectionData]:
    ret = []
    for region, region_data in static_data["MSC"].items():
        rooms = set(region_data.keys())

        match region:
            case "SU":
                filt = {r for r in rooms if "CAVE" in r or "PUMP" in r
                        or r in ("SU_VR1", "SU_PS1", "SU_C04", "SU_A41", "SU_A42", "SU_A43", "SU_A44", "SU_S05",
                                 "SU_INTRO01", "SU_X02", "SU_S10", "GATE_OE_SU[SU]")}
                ret += [
                    PhysicalRegion("Outskirts", "SU", rooms.difference(filt)),
                    PhysicalRegion("Outskirts filtration", "SU^", filt),
                    ConnectionData("Outskirts filtration", "Outskirts", backward=Simple("Scug-Saint")),
                ]

            case "MS":
                bitter = {name for name in rooms if "BITTER" in name or "SEWER" in name or "AERIE" in name
                          or name in ("MS_WILLSNAGGING01", "MS_S07", "MS_PUMPS", "MS_SCAVTRADER", "MS_JTRAP",
                                      "MS_COMMS", "GATE_SL_MS[MS]")}
                ret += [
                    PhysicalRegion("Submerged Superstructure", "MS", rooms.difference(bitter)),
                    PhysicalRegion("Bitter Aerie", "MS^", bitter),
                    ConnectionData("Submerged Superstructure", "Bitter Aerie",
                                   forward=Simple(["Scug-Rivulet", "Object-EnergyCell"])),
                ]

            case "SB":
                ravine = {name for name in rooms if name in (
                    "SB_A10", "SB_F03", "SB_TOPSIDE", "SB_S09", "GATE_LF_SB[SB]"
                )}
                ret += [
                    PhysicalRegion("Subterranean", "SB", rooms.difference(ravine)),
                    PhysicalRegion("Subterranean ravine", "SB^", ravine),
                    ConnectionData("Subterranean ravine", "Subterranean", backward=Simple("Scug-Saint")),
                ]

            case "SS":
                above = {name for name in rooms if name in (
                    "GATE_SS_UW[SS]", "SS_D08", "SS_S04", "SS_E08", "SS_D07", "SS_AI"
                )}
                ret += [
                    PhysicalRegion("Five Pebbles", "SS", rooms.difference(above)),
                    PhysicalRegion("Five Pebbles above puppet", "SS^", above),
                    ConnectionData("Five Pebbles", "Five Pebbles above puppet")
                ]

            # case "GW":
            #     if "EDGE" in name or name in ("A24", "A25", "S09"):
            #         return "Garbage Wastes (upper east)"
            #     elif name in ("C04", "B08", "S04"):
            #         return "Garbage Wastes (lower east)"
            #     return "Garbage Wastes"
            #
            # case "SL":
            #     if name in ("EDGE02", "EDGE01", "BRIDGE01", "BRIDGEEND", "S13"):
            #         return "Shoreline (broken precipice)"
            #     return "Shoreline"

            case _:
                ret.append(PhysicalRegion(region_code_to_name[region], region, rooms))

    ret.append(ConnectionData("Subterranean", "Rubicon", AllOf(Simple("Karma", 8), Simple("Scug-Saint"))))

    return ret


def generate(options: RainWorldOptions):
    return _generate(options)
