from BaseClasses import Item, ItemClassification
from typing import Optional, Dict
from . import constants


class RainWorldItem(Item):
    game: str = "Rain World"


class RainWorldItemData:
    def __init__(self, name: str, code: Optional[int], item_type: ItemClassification = ItemClassification.filler,
                 count: int = 1, precollect: int = 0):
        self.name = name
        self.code = code
        self.item_type = item_type
        self.count = count
        self.precollect = precollect

    def generate_item(self, player: int) -> RainWorldItem:
        return RainWorldItem(self.name, self.item_type, self.code, player)


offset: int = constants.FIRST_ID

all_items: Dict[str, RainWorldItemData] = {
    #################################################################
    # PROGRESSION
    "Karma": RainWorldItemData("Karma", offset, ItemClassification.progression, 8),
    "Ascension": RainWorldItemData("Ascension", None, ItemClassification.progression_skip_balancing, 0),

    #################################################################
    # REGION KEYS
    # "Key to SU": RainWorldItemData("Key to Outskirts", 1 + offset, ItemClassification.progression),
    # "Key to HI": RainWorldItemData("Key to Industrial Complex", 2 + offset, ItemClassification.progression),
    # "Key to DS": RainWorldItemData("Key to Drainage System", 3 + offset, ItemClassification.progression),
    # "Key to GW": RainWorldItemData("Key to Garbage Wastes", 4 + offset, ItemClassification.progression),
    # "Key to SL": RainWorldItemData("Key to Shoreline", 5 + offset, ItemClassification.progression),
    # "Key to VS": RainWorldItemData("Key to Pipeyard", 6 + offset, ItemClassification.progression),
    # "Key to SH": RainWorldItemData("Key to Shaded Citadel", 7 + offset, ItemClassification.progression),
    # "Key to UW": RainWorldItemData("Key to The Exterior", 8 + offset, ItemClassification.progression),
    # "Key to SS": RainWorldItemData("Key to Five Pebbles", 9 + offset, ItemClassification.progression),
    # "Key to CC": RainWorldItemData("Key to Chimney Canopy", 10 + offset, ItemClassification.progression),
    # "Key to SI": RainWorldItemData("Key to Sky Islands", 11 + offset, ItemClassification.progression),
    # "Key to LF": RainWorldItemData("Key to Farm Arrays", 12 + offset, ItemClassification.progression),
    # "Key to SB": RainWorldItemData("Key to Subterranean", 13 + offset, ItemClassification.progression),
    # "Key to MS": RainWorldItemData("Key to Submerged Superstructure", 14 + offset, ItemClassification.progression),
    # "Key to OE": RainWorldItemData("Key to Outer Expanse", 15 + offset, ItemClassification.progression),

    #################################################################
    # FILLER
    "Rock": RainWorldItemData("Rock", 200 + offset, ItemClassification.filler, 0),
    "Spear": RainWorldItemData("Spear", 201 + offset, ItemClassification.filler, 0),
    "Grenade": RainWorldItemData("Grenade", 202 + offset, ItemClassification.filler, 0),
    "Fuit": RainWorldItemData("Fuit", 203 + offset, ItemClassification.filler, 0),

    #################################################################
    # TRAPS
    "Stun Trap": RainWorldItemData("Stun Trap", 300 + offset, ItemClassification.trap, 0),
    "Zoomies Trap": RainWorldItemData("Zoomies Trap", 301 + offset, ItemClassification.trap, 0),
    "Timer Trap": RainWorldItemData("Timer Trap", 302 + offset, ItemClassification.trap, 0),
    "Red Lizard Trap": RainWorldItemData("Red Lizard Trap", 303 + offset, ItemClassification.trap, 0),
    "Red Centipede Trap": RainWorldItemData("Red Centipede Trap", 304 + offset, ItemClassification.trap, 0),
    "Spitter Spider Trap": RainWorldItemData("Spitter Spider Trap", 305 + offset, ItemClassification.trap, 0),
}

#################################################################
# GATES
gate_shorts = [
    "LF_SU", "SU_DS", "OE_SU", "SU_HI",
    "HI_VS", "HI_CC", "HI_GW", "HI_SH",
    "DS_SB", "DS_CC", "DS_GW",
    "SI_CC", "CC_UW",
    "GW_SL", "GW_SH",
    "SH_SL", "SH_UW",
    "SB_VS", "SI_VS", "SL_VS",
    "UW_SL", "MS_SL", "SL_MS", "SB_SL",
    "SI_LF",
    "LF_SB", "SB_OE",
    "UW_SS", "SS_UW", "UW_LC",
]
for i, gate in enumerate(gate_shorts):
    all_items[f"GATE_{gate}"] = RainWorldItemData(f"GATE_{gate}", 500 + i, ItemClassification.progression)

#################################################################
item_name_to_id: Dict[str, int] = {
    k: v.code for k, v in all_items.items()
}
