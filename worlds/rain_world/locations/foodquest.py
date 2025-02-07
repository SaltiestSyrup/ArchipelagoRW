from .classes import LocationData
from ..conditions.classes import Simple
from ..conditions import generate
from ..game_data.general import food_quest_items, alt_food_quest_items

locations = [
    LocationData(
        f"FoodQuest-{food}", f"FoodQuest-{food}", "Food Quest", i,
        Simple(alt_food_quest_items[food], 1) if food in alt_food_quest_items.keys() else Simple(food),
        generate.msc(True)
    )
    for i, food in enumerate(food_quest_items)
]
