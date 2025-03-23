from BaseClasses import Item, ItemClassification
from typing import Optional, Dict
from . import constants, game_data
from .regions.gates import gates
from .game_data.general import region_code_to_name, alternate_regions


class RainWorldItem(Item):
    game: str = "Rain World"


class RainWorldItemData:
    def __init__(self, name: str, code: Optional[int], item_type: ItemClassification = ItemClassification.filler):
        self.name = name
        self.hints: list[str] = []
        self.code = code
        self.item_type = item_type

    def generate_item(self, player: int) -> RainWorldItem:
        return RainWorldItem(self.name, self.item_type, self.code, player)


class GateKeyItemData(RainWorldItemData):
    def __init__(self, names: list[str], code: Optional[int]):
        super().__init__(names[0], code, ItemClassification.progression)
        self.hints = names[1:]


class FillerItemData(RainWorldItemData):
    def __init__(self, name: str, code: Optional[int], gamestate: Optional[list[str]] = None):
        super().__init__(name, code, ItemClassification.filler)
        self.gamestate = gamestate or []


class TrapItemData(RainWorldItemData):
    def __init__(self, name: str, code: Optional[int], gamestate: Optional[list[str]] = None):
        super().__init__(name, code, ItemClassification.trap)
        self.gamestate = gamestate or []


offset: int = constants.FIRST_ID

all_items: Dict[str, RainWorldItemData] = {
    #################################################################
    # PROGRESSION
    "Karma": RainWorldItemData("Karma", offset, ItemClassification.progression),
    "The Mark": RainWorldItemData("The Mark", offset + 1, ItemClassification.progression),
    "Citizen ID Drone": RainWorldItemData("Citizen ID Drone", offset + 2, ItemClassification.progression),
    "Rarefaction Cell": RainWorldItemData("Rarefaction Cell", offset + 3, ItemClassification.progression),
    "Spearmaster's Pearl": RainWorldItemData("Spearmaster's Pearl", offset + 4, ItemClassification.progression),
    "Moon's Final Message": RainWorldItemData("Moon's Final Message", offset + 5, ItemClassification.progression),
    "Slag Key": RainWorldItemData("Slag Key", offset + 6, ItemClassification.progression),

    #################################################################
    # PASSAGE TOKENS
    **{
        f"Passage Token - {p}": RainWorldItemData(f"Passage Token - {p}", offset + 20 + i, ItemClassification.useful)
        for i, p in enumerate(game_data.general.passage_proper_names.values())
    },

    #################################################################
    # UNIQUE
    "The Glow": RainWorldItemData("The Glow", offset + 50, ItemClassification.progression),
    "Longer cycles": RainWorldItemData("Longer cycles", offset + 51, ItemClassification.useful),

    #################################################################
    # GAMESTATE
    "MSC": RainWorldItemData("MSC", offset + 100, ItemClassification.progression),
    "Scug-Yellow": RainWorldItemData("Scug-Yellow", offset + 110, ItemClassification.progression),
    "Scug-White": RainWorldItemData("Scug-White", offset + 111, ItemClassification.progression),
    "Scug-Red": RainWorldItemData("Scug-Red", offset + 112, ItemClassification.progression),
    "Scug-Gourmand": RainWorldItemData("Scug-Gourmand", offset + 113, ItemClassification.progression),
    "Scug-Artificer": RainWorldItemData("Scug-Artificer", offset + 114, ItemClassification.progression),
    "Scug-Rivulet": RainWorldItemData("Scug-Rivulet", offset + 115, ItemClassification.progression),
    "Scug-Spear": RainWorldItemData("Scug-Spear", offset + 116, ItemClassification.progression),
    "Scug-Saint": RainWorldItemData("Scug-Saint", offset + 117, ItemClassification.progression),
    "Scug-Inv": RainWorldItemData("Scug-Inv", offset + 118, ItemClassification.progression),

    #################################################################
    # OPTIONSTATE

    "Option-Glow": RainWorldItemData("Option-Glow", offset + 170, ItemClassification.progression),

    #################################################################
    # FILLER - WEAPONS
    "Rock": FillerItemData("Rock", 200 + offset),
    "Spear": FillerItemData("Spear", 201 + offset),
    "Explosive Spear": FillerItemData("Explosive Spear", 202 + offset),
    "Electric Spear": FillerItemData("Electric Spear", 203 + offset, ["MSC"]),
    "Grenade": FillerItemData("Grenade", 204 + offset),
    "Flashbang": FillerItemData("Flashbang", 205 + offset),
    "Spore Puff": FillerItemData("Spore Puff", 206 + offset),
    "Cherrybomb": FillerItemData("Cherrybomb", 207 + offset),
    "Singularity Bomb": FillerItemData("Singularity Bomb", 208 + offset, ["MSC"]),
    "Lilypuck": FillerItemData("Lilypuck", 209 + offset, ["MSC"]),

    #################################################################
    # FILLER - FOOD
    "Blue Fruit": FillerItemData("Blue Fruit", 240 + offset),
    "Bubble Fruit": FillerItemData("Bubble Fruit", 241 + offset),
    "Eggbug Egg": FillerItemData("Eggbug Egg", 242 + offset),
    "Jellyfish": FillerItemData("Jellyfish", 243 + offset),
    "Mushroom": FillerItemData("Mushroom", 244 + offset),
    "Slime Mold": FillerItemData("Slime Mold", 245 + offset),
    "Fire Egg": FillerItemData("Fire Egg", 246 + offset, ["MSC"]),
    "Glow Weed": FillerItemData("Glow Weed", 247 + offset, ["MSC"]),
    "Seed": FillerItemData("Seed", 248 + offset, ["MSC"]),
    "Gooieduck": FillerItemData("Gooieduck", 249 + offset, ["MSC"]),
    "Dandelion Peach": FillerItemData("Dandelion Peach", 250 + offset, ["MSC"]),

    #################################################################
    # FILLER - OTHER
    "Bubble Weed": FillerItemData("Bubble Weed", 270 + offset),
    "Batnip": FillerItemData("Batnip", 271 + offset),
    "Lantern": FillerItemData("Lantern", 272 + offset),
    "Karma Flower": FillerItemData("Karma Flower", 273 + offset),
    "Vulture Mask": FillerItemData("Vulture Mask", 274 + offset),
    "Joke Rifle": FillerItemData("Joke Rifle", 275 + offset, ["MSC"]),

    #################################################################
    # FILLER - NON-CREATURE TRAPS
    "Stun trap": TrapItemData("Stun trap", 300 + offset),
    "Zoomies trap": TrapItemData("Zoomies trap", 301 + offset),
    "Timer trap": TrapItemData("Timer trap", 302 + offset),
    "Flood trap": TrapItemData("Flood trap", 303 + offset),
    "Rain trap": TrapItemData("Rain trap", 304 + offset),
    "Gravity trap": TrapItemData("Gravity trap", 305 + offset),
    "Fog trap": TrapItemData("Fog trap", 306 + offset),
    "Killsquad trap": TrapItemData("Killsquad trap", 307 + offset),
    "Alarm trap": TrapItemData("Alarm trap", 308 + offset),

    #################################################################
    # FILLER - CREATURE TRAPS
    "Red Lizard trap": TrapItemData("Red Lizard trap", 330 + offset),
    "Red Centipede trap": TrapItemData("Red Centipede trap", 331 + offset),
    "Spitter Spider trap": TrapItemData("Spitter Spider trap", 332 + offset),
    "Brother Long Legs trap": TrapItemData("Brother Long Legs trap", 333 + offset),
    "Daddy Long Legs trap": TrapItemData("Daddy Long Legs trap", 334 + offset),
}

#################################################################
# GATES
gate_keys: dict[str, GateKeyItemData] = {
    names[0]: GateKeyItemData(names, offset + 500 + i)
    for i, names in enumerate([g.names for g in gates])
}
all_items.update(gate_keys)

#################################################################
item_name_to_id: Dict[str, int] = {k: v.code for k, v in all_items.items()}

item_hints: dict[str, set[str]] = {}
for item in all_items.values():
    for hint in item.hints:
        item_hints.setdefault(hint, set()).update({item.name})
