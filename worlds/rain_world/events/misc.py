from .. import game_data, RainWorldOptions
from .classes import EventData
from ..locations.echoes import locations


def generate_events(options: RainWorldOptions):
    ret = [EventData(f"Access-{short}", f"Access-{short}", full)
           for short, full in game_data.general.region_code_to_name.items() if "^" not in short]

    if not options.checks_echoes:
        ret.extend([EventData(e.full_name, e.full_name, e.region, condition=e.access_condition)
                   for r, e in locations.items()])

    return ret
