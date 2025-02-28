from .classes import RainWorldRegion, RegionData, ConnectionData
from ..options import RainWorldOptions
from ..conditions.classes import Simple


def generate(options: RainWorldOptions):
    ret = [
        RegionData("Menu"),
        RegionData("Events"),
        RegionData("Early Passages"),
        RegionData("PPwS Passages"),
        RegionData("Late Passages"),
        RegionData("Food Quest",
                   options.msc_enabled and (options.checks_foodquest.value > 0 or options.starting_scug == "Gourmand")),

        ConnectionData("Menu", "Events"),
        ConnectionData("Menu", "Early Passages"),
        ConnectionData("Early Passages", "Late Passages", Simple("Passage-Survivor", locations=True)),
        ConnectionData("Late Passages", "PPwS Passages"),
        ConnectionData("Menu", "Food Quest"),
    ]

    if options.passage_progress_without_survivor:
        ret.append(ConnectionData("Menu", "PPwS Passages"))

    return ret



