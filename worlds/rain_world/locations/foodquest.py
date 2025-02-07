from .classes import LocationData
from ..conditions.classes import Simple
from ..conditions import generate
from ..game_data.general import (food_quest_items, alt_food_quest_items, food_quest_saint_inedible,
                                 food_quest_spearmaster_inedible, food_quest_survivor_inedible, scugs_msc)


def edible_for_which_scugs(food: str) -> list[str]:
    return list(
        set(scugs_msc)
        .difference({"Spear" if food in food_quest_spearmaster_inedible else ""})
        .difference({"Saint" if food in food_quest_saint_inedible else ""})
        .difference({"Yellow", "White", "Rivulet"} if food in food_quest_survivor_inedible else {})
        .difference({"Yellow", "White"} if food == "RedCentipede" else {})
    )


locations = [
    LocationData(
        f"FoodQuest-{food}", f"FoodQuest-{food}", "Food Quest", 5250 + i,
        Simple(alt_food_quest_items[food], 1) if food in alt_food_quest_items.keys() else Simple(food),
        generate.whitelist_scugs(edible_for_which_scugs(food), True)
    )
    for i, food in enumerate(food_quest_items)
]
