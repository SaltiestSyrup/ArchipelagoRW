from .. import game_data
from .classes import EventData


def generate_events():
    return [
        EventData(f"Access-{short}", f"Access-{short}", full)
        for short, full in game_data.general.region_code_to_name.items() if "^" not in short
    ]
