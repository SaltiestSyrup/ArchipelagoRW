from .classes import LocationData
from ..options import RainWorldOptions
from ..conditions.classes import Simple, ConditionBlank

locations = {
    "Eat_Neuron": LocationData("Eat_Neuron", "Eat_Neuron", "Events", 4900, Simple("SSOracleSwarmer")),
    "Gift_Neuron": LocationData("Gift_Neuron", "Gift_Neuron", "Events", 4901, Simple(["Access-SL", "Access-SS"])),
    "Meet_FP": LocationData(
        "Meet_FP", "Meet_FP", "Five Pebbles above puppet", 4902,
        access_condition_generator=lambda opt: ConditionBlank if opt.starting_scug == "Inv" else Simple("The Mark")
    ),
    "Meet_LttM": LocationData("Meet_LttM", "Meet_LttM", "Shoreline", 4903, Simple("The Mark")),
    "Meet_LttM_Spear": LocationData("Meet_LttM_Spear", "Meet_LttM_Spear", "Looks to the Moon", 4904),
    "Kill_FP": LocationData("Kill_FP", "Kill_FP", "The Rot", 4905),
    "Save_LttM": LocationData("Save_LttM", "Save_LttM", "Shoreline", 4906, Simple("Object-NSHSwarmer")),
    "Ascend_FP": LocationData("Ascend_FP", "Ascend_FP", "Silent Construct", 4907, Simple("Karma", 8)),
    "Ascend_LttM": LocationData("Ascend_LttM", "Ascend_LttM", "Shoreline", 4908, Simple("Karma", 8)),
}


def generate(options: RainWorldOptions) -> list[LocationData]:
    keys = ["Eat_Neuron"]

    if options.starting_scug in ["Yellow", "White", "Gourmand"]:
        keys.append("Gift_Neuron")

    if options.starting_scug in ["Yellow", "White", "Red", "Gourmand", "Artificer", "Spear", "Inv"]:
        keys.append("Meet_FP")

    if options.starting_scug in ["Yellow", "White", "Red", "Gourmand", "Rivulet", "Saint"]:
        keys.append("Meet_LttM")

    if options.starting_scug == "Red":
        keys.append("Save_LttM")

    if options.starting_scug == "Spear":
        keys.append("Meet_LttM_Spear")

    if options.starting_scug == "Rivulet":
        keys.append("Kill_FP")

    if options.starting_scug == "Saint":
        keys += ["Ascend_FP", "Ascend_LttM"]

    return [locations[key] for key in keys]
