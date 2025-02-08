from .classes import LocationData
from ..game_data.files import white_tokens
from ..game_data.general import region_code_to_name
from ..conditions import generate

locations = [
    LocationData(
        f"Broadcast-{name}", f"Broadcast-{name}", region_code_to_name[data["room"].split("_")[0]], 5350 + offset,
        generation_condition=generate.whitelist_scugs(["Spear"], True)
    )
    for offset, (name, data) in enumerate(white_tokens.items())
]
