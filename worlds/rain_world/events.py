from typing import NamedTuple

from BaseClasses import MultiWorld, Item, ItemClassification, Location
from worlds.rain_world.constants import REGION_CODE_DICT
from worlds.rain_world.utils import flatten


class EventData(NamedTuple):
    item_name: str
    location_item: str
    region: str
    classification: ItemClassification = ItemClassification.progression

    def make(self, player: int, multiworld: MultiWorld):
        item = Item(self.item_name, self.classification, None, player)
        region = multiworld.get_region(self.region, player)
        location = Location(player, self.location_item, None, region)
        region.locations.append(location)
        location.place_locked_item(item)


all_events: list[EventData] = [
    ########################################################################
    # Events tracking what Lizards are accessible for things like Dragon Slayer
    # EventData("Blue Liz", "SU Blue", "Outskirts"),
    # EventData("Green Liz", "SU Green", "Outskirts"),
    # EventData("Pink Liz", "SU Pink", "Outskirts"),
    # EventData("Red Liz", "SU Red", "Outskirts"),
    # EventData("White Liz", "SU White", "Outskirts"),
    #
    # EventData("Blue Liz", "HI Blue", "Industrial Complex"),
    # EventData("Cyan Liz", "HI Cyan", "Industrial Complex"),
    # EventData("Pink Liz", "HI Pink", "Industrial Complex"),
    # EventData("Red Liz", "HI Red", "Industrial Complex"),
    # EventData("White Liz", "HI White", "Industrial Complex"),
]

########################################################################
# Events tracking what Lizards are accessible for things like Dragon Slayer
lizzies = {
    'SU': ['Blue', 'Green', 'Pink', 'Red', 'White'],
    'HI': ['Blue', 'Cyan', 'Pink', 'Red', 'White'],
    'GW': ['Caramel', 'Cyan', 'Green', 'Pink'],
    'SL': ['Cyan', 'White', 'Salamander'],
    'SH': ['Black'],
    'UW': ['Blue', 'Cyan', 'White', 'Yellow'],
    'CC': ['Blue', 'Caramel', 'Cyan', 'Eel', 'Pink', 'White'],
    'SI': ['Blue', 'Cyan', 'Pink', 'White', 'Yellow'],
    'LF': ['Blue', 'Caramel', 'Green', 'Pink'],
    'SB': ['Black', 'Blue', 'Caramel', 'Cyan', 'Salamander'],
    'DS': ['Cyan', 'Green', 'Salamander'],
    'VS': ['Black', 'Cyan', 'Salamander'],
    # 'MS': ['Blue', 'Eel', 'White', 'Yellow'],
    'OE': [],
}

all_events += flatten([
    [EventData(f'{color} Liz', f'{k} {color} Liz', REGION_CODE_DICT[k])
     for color in colors]
    for k, colors in lizzies.items()
])

########################################################################
# Events tracking region access for Wanderer
all_events += [EventData("Wanderer pip", f"{k} any shelter", v) for k, v in REGION_CODE_DICT.items()]

########################################################################
# Events tracking food items for Food Quest
foods = {
    "Slime Mold": ["SH", "UW"],
    "Blue Fruit": ["SL", "SB", "UW", "SU", "HI", "SH", "CC", "DS", "GW", "SI", "LF"],
    "Batfly": ["SU", "HI", "DS", "GW", "SL", "SH", "UW", "CC", "SI", "LF", "SB", "VS", "MS"],
    "Mushroom": ["SB", "DS", "SU", "LF", "SH", "CC", "UW", "GW", "HI", "SI", "VS", "OE"],
    "Black Lizard": ["SH", "SB", "VS"],
    "Bubble Fruit": ["GW", "DS", "SL", "SB", "SH", "HI", "LF"],
    "Jellyfish": ["MS", "SL"],
    "Jetfish": ["SL", "SB", "MS", "VS"],
    "Glow Weed": ["SL", "SB", "MS"],
    "Aquatic Lizard": ["DS", "SL", "SB", "VS", "CC", "MS"],
    "Snail": ["DS", "SL", "CC", "MS", "GW", "VS"],
    "Hazer": ["HI", "GW", "SL", "DS", "LF", "SU"],
    "Eggbug": ["SU", "SH", "SI", "LF", "HI", "GW", "CC", "SB", "VS"],
    "Lilypuck": ["DS", "VS"],
    "Yellow Lizard": ["UW", "SI", "MS"],
    "Grappling Worm": ["UW", "CC"],
    "Neuron Fly": ["SL", "SS"],
    "Centiwing": ["SI"],
    "Dandelion Peach": ["SI"],
    "Cyan Lizard": ["HI", "DS", "GW", "UW", "CC", "SI", "SB", "VS"],
    "Gooieduck": ["LF", "SB", "OE"],
    "Aquapede or Redpede": ["SL", "MS", "GW", "SB", "VS"],
}

for food, region_codes in foods.items():
    for code in region_codes:
        all_events.append(EventData(f"Eat {food}", f"{code} {food}", REGION_CODE_DICT[code]))

