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


class FillerItemData(RainWorldItemData):
    def __init__(self, name: str, code: Optional[int], gamestate: Optional[list[str]] = None):
        super().__init__(name, code, ItemClassification.filler, 0, 0)
        self.gamestate = gamestate or []


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
    # FILLER - WEAPONS
    "Object-Rock": FillerItemData("Object-Rock", 200 + offset),
    "Object-Spear": FillerItemData("Object-Spear", 201 + offset),
    "Object-ExplosiveSpear": FillerItemData("Object-ExplosiveSpear", 202 + offset),
    "Object-ElectricSpear": FillerItemData("Object-ExplosiveSpear", 203 + offset, ["MSC"]),
    "Object-ScavengerBomb": FillerItemData("Object-ScavengerBomb", 204 + offset),
    "Object-FlareBomb": FillerItemData("Object-FlareBomb", 205 + offset),
    "Object-PuffBall": FillerItemData("Object-PuffBall", 206 + offset),
    "Object-FirecrackerPlant": FillerItemData("Object-FirecrackerPlant", 207 + offset),
    "Object-SingularityBomb": FillerItemData("Object-SingularityBomb", 208 + offset, ["MSC"]),
    "Object-LillyPuck": FillerItemData("Object-LillyPuck", 209 + offset, ["MSC"]),

    #################################################################
    # FILLER - FOOD
    "Object-DangleFruit": FillerItemData("Object-DangleFruit", 240 + offset),
    "Object-WaterNut": FillerItemData("Object-WaterNut", 241 + offset),
    "Object-EggBugEgg": FillerItemData("Object-EggBugEgg", 242 + offset),
    "Object-JellyFish": FillerItemData("Object-JellyFish", 243 + offset),
    "Object-Mushroom": FillerItemData("Object-Mushroom", 244 + offset),
    "Object-SlimeMold": FillerItemData("Object-SlimeMold", 245 + offset),
    "Object-FireEgg": FillerItemData("Object-FireEgg", 246 + offset, ["MSC"]),
    "Object-GlowWeed": FillerItemData("Object-GlowWeed", 247 + offset, ["MSC"]),
    "Object-Seed": FillerItemData("Object-Seed", 248 + offset, ["MSC"]),
    "Object-GooieDuck": FillerItemData("Object-GooieDuck", 249 + offset, ["MSC"]),
    "Object-DandelionPeach": FillerItemData("Object-DandelionPeach", 250 + offset, ["MSC"]),

    #################################################################
    # FILLER - OTHER
    "Object-BubbleGrass": FillerItemData("Object-BubbleGrass", 270 + offset),
    "Object-FlyLure": FillerItemData("Object-FlyLure", 271 + offset),
    "Object-Lantern": FillerItemData("Object-Lantern", 272 + offset),
    "Object-KarmaFlower": FillerItemData("Object-KarmaFlower", 273 + offset),
    "Object-VultureMask": FillerItemData("Object-VultureMask", 274 + offset),
    "Object-JokeRifle": FillerItemData("Object-JokeRifle", 275 + offset, ["MSC"]),

    #################################################################
    # FILLER - TRAPS
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
