from rule_builder.options import OptionFilter
from .classes import RegionData, ConnectionData
from ..locations.passages import cond_survivor
from ..options import RainWorldOptions, PassageProgressWithoutSurvivor as PPwS



def generate(options: RainWorldOptions) -> list[RegionData | ConnectionData]:
    ret = [
        RegionData("Menu"),
        RegionData("Events"),
        RegionData("Early Passages"),
        RegionData("PPwS Passages"),
        RegionData("Late Passages"),
        RegionData("Food Quest",
                   options.msc_enabled and (options.checks_foodquest.value > 0 or options.starting_scug == "Gourmand")),

        ConnectionData("Menu", "Events", "Unique event checks"),
        # Require Survivor for early passages if PPwS is nothing
        ConnectionData("Menu", "Early Passages", "Early Passages",
                       cond_survivor | [OptionFilter(PPwS, PPwS.option_disabled, operator="ge")]),
        # Require Survivor for PPwS passages if PPwS is < enabled
        ConnectionData("Menu", "PPwS Passages", "Passage progress without Survivor",
                       cond_survivor | [OptionFilter(PPwS, PPwS.option_enabled, operator="ge")]),
        # Require Survivor for Late passages if PPwS is < bypassed
        ConnectionData("Menu", "Late Passages", "Bypass Survivor requirement",
                       cond_survivor | [OptionFilter(PPwS, PPwS.option_bypassed)]),
        ConnectionData("Menu", "Food Quest", "Food Quest"),
    ]

    return ret



