from BaseClasses import Item, ItemClassification
from typing import Optional, Dict
from . import constants
from .regions import all_gate_short_names


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
    # FILLER - NON-CREATURE TRAPS
    "Trap-Stun": FillerItemData("Trap-Stun", 300 + offset),
    "Trap-Zoomies": FillerItemData("Trap-Zoomies", 301 + offset),
    "Trap-Timer": FillerItemData("Trap-Timer", 302 + offset),
    "Trap-Flood": FillerItemData("Trap-Flood", 303 + offset),
    "Trap-Rain": FillerItemData("Trap-Rain", 304 + offset),
    "Trap-Gravity": FillerItemData("Trap-Gravity", 305 + offset),
    "Trap-Fog": FillerItemData("Trap-Fog", 306 + offset),
    "Trap-KillSquad": FillerItemData("Trap-KillSquad", 307 + offset),
    "Trap-Alarm": FillerItemData("Trap-KillSquad", 308 + offset),

    #################################################################
    # FILLER - CREATURE TRAPS
    "Trap-RedLizard": FillerItemData("Trap-RedLizard", 330 + offset),
    "Trap-RedCentipede": FillerItemData("Trap-RedCentipede", 331 + offset),
    "Trap-SpitterSpider": FillerItemData("Trap-SpitterSpider", 332 + offset),
    "Trap-BrotherLongLegs": FillerItemData("Trap-BrotherLongLegs", 333 + offset),
    "Trap-DaddyLongLegs": FillerItemData("Trap-DaddyLongLegs", 334 + offset),
}

#################################################################
# GATES
for i, gate in enumerate(all_gate_short_names):
    all_items[f"GATE_{gate}"] = RainWorldItemData(f"GATE_{gate}", 500 + i, ItemClassification.progression)

#################################################################
item_name_to_id: Dict[str, int] = {
    k: v.code for k, v in all_items.items()
}
