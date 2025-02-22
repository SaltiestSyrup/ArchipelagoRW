from .classes import StaticWorldEvent
from ..options import RainWorldOptions

from ..game_data.general import scugs_all
from ..game_data import static_data
from ..regions.classes import RainWorldRegion, room_to_region
from ..utils import effective_blacklist


def generate_events_for_one_gamestate(options: RainWorldOptions,
                                      regions: list[RainWorldRegion]) -> list[StaticWorldEvent]:
    ret = []

    for region in regions:
        if (rooms := region.rooms) and len(rooms) > 0:
            if region_data := static_data[options.dlcstate].get(region.code[:2], {}):
                events = {}

                for room in rooms:
                    if room_data := region_data.get(room, {}):
                        for obj_type, obj_data in room_data.get("objects", {}).items():
                            if len(current := events.get(obj_type, set(scugs_all))) > 0:
                                incoming = effective_blacklist(
                                    obj_data.get("filter", None), obj_data.get("whitelist", None), room_data
                                )
                                events[obj_type] = current.intersection(incoming)

                        for crit_type, crit_data in room_data.get("spawners", {}).get("normal", {}).items():
                            if len(current := events.get(crit_type, set(scugs_all))) > 0:
                                events[crit_type] = current.intersection(set(scugs_all).difference(crit_data))

                        if room_tags := room_data.get("tags", []):
                            if "SWARMROOM" in room_tags:
                                events["Fly"] = set()
                            if "SCAVOUTPOST" in room_tags:
                                events["Toll"] = set()
                            if "SHELTER" in room_tags:
                                events["Shelter"] = set()

                for event_type, event_blacklist in events.items():
                    ret.append(StaticWorldEvent(
                        event_type, f'{region.name} {event_type}', region.name,
                        scugs=set(scugs_all).difference(event_blacklist)
                    ))

    # HARDCODE
    for room in ("SS_E07", "SL_AI", "RM_AI", "DM_AI", "LC_LAB01"):
        ret.append(StaticWorldEvent("SSOracleSwarmer", f'{room} SSOracleSwarmer',
                                    room_to_region[room]))

    if options.starting_scug in {"Yellow", "White", "Red", "Gourmand", "Rivulet", "Saint"}:
        ret.append(StaticWorldEvent("Meet LttM", f'{room} LttM', room_to_region["SL_AI"]))

    return ret
