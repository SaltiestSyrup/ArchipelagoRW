from .classes import StaticWorldEvent
from ..options import RainWorldOptions

from ..game_data.general import scugs_all, scugs_vanilla, region_code_to_name
from ..conditions.classes import Simple, AnyOf, AllOf
from ..game_data import static_data


def generate_events_for_one_gamestate(options: RainWorldOptions) -> list[StaticWorldEvent]:
    dlcstate = "MSC" if options.msc_enabled else "Vanilla"
    ret = []

    for region, region_data in static_data[dlcstate].items():
        region_name = region_code_to_name[region]

        for room, room_data in region_data.items():
            if "OFFSCREEN" in room:  # TODO
                continue

            if "objects" in room_data.keys():
                for objtype, blacklist in room_data["objects"].items():
                    ret.append(StaticWorldEvent(
                        objtype, f'{room} {objtype}', region_name, scugs=set(scugs_all).difference(blacklist)
                    ))

            try:
                for crittype, whitelist in room_data["spawners"]["normal"].items():
                    ret.append(StaticWorldEvent(
                        crittype, f'{room} {crittype}', region_name, scugs=whitelist
                    ))
            except KeyError:
                pass

            try:
                if "SWARMROOM" in room_data["tags"]:
                    ret.append(StaticWorldEvent("Fly", f'{room} Fly', region_name))
                if "SCAVOUTPOST" in room_data["tags"]:
                    ret.append(StaticWorldEvent("Toll", f'{room} Toll', region_name))
                # HARDCODE
                if "SHELTER" in room_data["tags"] and room not in ("GW_S08", "SL_S04"):
                    ret.append(StaticWorldEvent(f"{region} Shelter", f'{room} Shelter', region_name))
            except KeyError:
                pass

    # HARDCODE
    for room in ("SS_E07", "SL_AI", "RM_AI", "DM_AI", "LC_LAB01"):
        ret.append(StaticWorldEvent("SSOracleSwarmer", f'{room} SSOracleSwarmer',
                                    region_code_to_name[room.split("_")[0]]))

    if options.starting_scug in {"Yellow", "White", "Red", "Gourmand", "Rivulet", "Saint"}:
        ret.append(StaticWorldEvent("Meet LttM", f'{room} LttM', "SL_AI"))

    return ret
