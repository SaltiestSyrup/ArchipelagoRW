from .classes import LocationData
from ..game_data.files import white_tokens
from ..game_data.general import REGION_CODE_DICT
from ..conditions import generate

locations = [
    LocationData(
        f"Broadcast-{name}", f"Broadcast-{name}", REGION_CODE_DICT[data["room"].split("_")[0]], 5350 + offset,
        generation_condition=generate.whitelist_scugs(["Spear"], True)
    )
    for offset, (name, data) in enumerate(white_tokens.items())
]
