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
    "Ascension": RainWorldItemData("Ascension", None, ItemClassification.progression_skip_balancing, 0),
    "Karma": RainWorldItemData("Karma", offset, ItemClassification.progression, 8),

    #################################################################
    # GAMESTATE
    "MSC": RainWorldItemData("MSC", offset + 100, ItemClassification.progression, 0),
    "Scug-Yellow": RainWorldItemData("Scug-Yellow", offset + 110, ItemClassification.progression, 0),
    "Scug-White": RainWorldItemData("Scug-White", offset + 111, ItemClassification.progression, 0),
    "Scug-Red": RainWorldItemData("Scug-Red", offset + 112, ItemClassification.progression, 0),
    "Scug-Gourmand": RainWorldItemData("Scug-Gourmand", offset + 113, ItemClassification.progression, 0),
    "Scug-Artificer": RainWorldItemData("Scug-Artificer", offset + 114, ItemClassification.progression, 0),
    "Scug-Rivulet": RainWorldItemData("Scug-Rivulet", offset + 115, ItemClassification.progression, 0),
    "Scug-Spear": RainWorldItemData("Scug-Spear", offset + 116, ItemClassification.progression, 0),
    "Scug-Saint": RainWorldItemData("Scug-Saint", offset + 117, ItemClassification.progression, 0),
    "Scug-Inv": RainWorldItemData("Scug-Inv", offset + 118, ItemClassification.progression, 0),

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
