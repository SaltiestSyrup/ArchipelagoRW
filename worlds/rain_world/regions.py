from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING, Any

from .classes import RegionData, TokenData


#################################################################
# VANILLA REGIONS TODO
actual_regions: Dict[str, RegionData] = {
    "SU": RegionData(
        "Outskirts", "SU",
        [
            TokenData("SU", "", 0, "gold"),
            TokenData("SU", "", 1, "red"),
            TokenData("PoleMimic", "", 2, "blue"),
            TokenData("DangleFruit", "", 3, "blue"),
            TokenData("CicadaA", "", 4, "blue"),
        ]
    ),
    "HI": RegionData(
        "Industrial Complex", "HI",
        [
            TokenData("HI", "", 100, "gold"),
            TokenData("HI", "", 101, "red"),
            TokenData("FirecrackerPlant", "", 102, "blue"),
            TokenData("BlueLizard", "", 103, "blue"),
            TokenData("SmallCentipede", "", 104, "blue"),
            TokenData("VultureGrub", "", 105, "blue"),
        ]
    ),
    "DS": RegionData(
        "Drainage System", "DS",
        [
            TokenData("DS", "B10", 200, "gold"),
            TokenData("DS", "A01", 201, "red"),
            TokenData("Snail", "B06", 202, "blue"),
            TokenData("Salamander", "B04", 203, "blue"),
            TokenData("Leech", "A05", 204, "blue"),
            TokenData("BubbleGrass", "A25", 205, "blue"),
            TokenData("Hazer", "A21", 206, "blue"),
        ]
    ),
    "GW": RegionData(
        "Garbage Wastes", "GW",
        [
            TokenData("GW", "C10", 300, "gold"),
            TokenData("GW", "A25", 301, "red"),
            TokenData("WaterNut", "D02", 302, "blue"),
            TokenData("RedLizard", "A14", 303, "blue"),
            TokenData("BrotherLongLegs", "C09", 304, "blue"),
            # TokenData("ScavengerBomb", "A21", 305, "blue"),
            TokenData("FireSpear", "A24", 306, "blue"),
        ]
    ),
    "SL": RegionData(
        "Shoreline", "SL",
        [
            TokenData("SL", "I01", 401, "red"),
            TokenData("SeaLeech", "A06", 402, "blue"),
            TokenData("BigEel", "E01", 403, "blue"),
            TokenData("JetFish", "F02", 404, "blue"),
            TokenData("JellyFish", "C01", 405, "blue"),
        ]
    ),
    "VS": RegionData(
        "Pipeyard", "VS",
        [
            TokenData("VS", "C04", 500, "gold"),
            TokenData("VS", "E02", 501, "red"),
            TokenData("Pearl", "A14", 502, "blue"),
            TokenData("LillyPuck", "C03", 503, "blue"),
        ]
    ),
    "SH": RegionData(
        "Shaded Citadel", "SH",
        [
            TokenData("SH", "B04", 600, "gold"),
            TokenData("SH", "KELP", 601, "red"),
            TokenData("BigSpider", "A13", 602, "blue"),
            TokenData("Spider", "C03", 603, "blue"),
            TokenData("Lantern", "B05", 604, "blue"),
            TokenData("LanternMouse", "B05", 605, "blue"),
            TokenData("MirosBird", "E01", 606, "blue"),
            TokenData("FlareBomb", "D03", 607, "blue"),
        ]
    ),
    "UW": RegionData(
        "The Exterior", "UW",
        [
            TokenData("UW", "D06", 701, "red"),
            TokenData("YellowLizard", "C02", 702, "blue"),
            TokenData("SlimeMold", "J01", 703, "blue"),
            TokenData("TubeWorm", "B01", 704, "blue"),
        ]
    ),
    "SS": RegionData(
        "Five Pebbles", "SS",
        [
            TokenData("SS", "E06", 801, "red"),
            TokenData("Inspector", "C03", 802, "blue"),
        ]
    ),
    "CC": RegionData(
        "Chimney Canopy", "CC",
        [
            TokenData("CC", "STRAINER01", 900, "gold"),
            TokenData("CC", "OUTPUT", 901, "red"),
            TokenData("DropBug", "F01", 902, "blue"),
            TokenData("WhiteLizard", "A10", 903, "blue"),
            TokenData("CyanLizard", "C13", 904, "blue"),
            TokenData("Vulture", "C04", 905, "blue"),
        ]
    ),
    "SI": RegionData(
        "Sky Islands", "SI",
        [
            TokenData("SI", "C07", 1000, "gold"),
            TokenData("SI", "B09", 1001, "red"),
            TokenData("VultureMask", "B07x", 1002, "blue"),
            TokenData("KingVulture", "A07", 1003, "blue"),
            TokenData("Centiwing", "A18", 1004, "blue"),
            TokenData("EggBug", "D05", 1005, "blue"),
            TokenData("DandelionPeach", "C04", 1006, "blue"),
        ]
    ),
    "LF": RegionData(
        "Farm Arrays", "LF",
        [
            TokenData("LF", "B04", 1100, "gold"),
            TokenData("LF", "D09", 1101, "red"),
            TokenData("ScavengerBomb", "A17", 1102, "blue"),
            TokenData("SpitterSpider", "B04", 1103, "blue"),
            TokenData("Deer", "C03", 1104, "blue"),
            TokenData("FlyLure", "D06", 1105, "blue"),
            TokenData("SporePlant", "D02", 1106, "blue"),
            TokenData("BigNeedleWorm", "A02", 1107, "blue"),
            TokenData("PuffBall", "F02", 1108, "blue"),
        ]
    ),
    "SB": RegionData(
        "Subterranean", "SB",
        [
            TokenData("SB", "F01", 1200, "gold"),
            TokenData("Filtration", "G04", 1201, "gold"),
            TokenData("SB", "J01", 1202, "red"),
            TokenData("BigCentipede", "G02", 1203, "blue"),
            TokenData("TentaclePlant", "J03", 1204, "blue"),
            TokenData("BlackLizard", "D04", 1205, "blue"),
            TokenData("Mushroom", "E04", 1206, "blue"),
            TokenData("RedCentipede", "H02", 1207, "blue"),
        ]
    ),
    "MS": RegionData(
        "Submerged Superstructure", "MS",
        []
    ),
    "OE": RegionData(
        "Outer Expanse", "OE",
        []
    ),
    "LC": RegionData(
        "Metropolis", "LC",
        []
    ),
    "DM": RegionData(
        "Looks to the Moon", "DM",
        []
    ),
}


class RainWorldRegionConnection(NamedTuple):
    left_region: str
    right_region: str
    left_cost: int
    right_cost: int


vanilla_connections = [
    RainWorldRegionConnection('SI', 'CC', 3, 2),
    RainWorldRegionConnection('CC', 'UW', 4, 1),
    RainWorldRegionConnection('UW', 'SS', 1, 1),
    RainWorldRegionConnection('HI', 'VS', 4, 2),
    RainWorldRegionConnection('SL', 'MS', 5, 1),
    RainWorldRegionConnection('GW', 'SL', 3, 2),

    # Horizontal long
    RainWorldRegionConnection('UW', 'LC', 20, 5),
    RainWorldRegionConnection('HI', 'SH', 5, 1),
    RainWorldRegionConnection('SB', 'SL', 2, 5),

    # Vertical short
    RainWorldRegionConnection('SI', 'LF', 3, 3),
    RainWorldRegionConnection('LF', 'SB', 4, 5),
    RainWorldRegionConnection('SB', 'OE', 1, 5),
    RainWorldRegionConnection('CC', 'HI', 3, 3),
    RainWorldRegionConnection('HI', 'SU', 2, 3),
    RainWorldRegionConnection('SU', 'DS', 4, 2),
    RainWorldRegionConnection('SH', 'SL', 3, 2),

    # Vertical long
    RainWorldRegionConnection('CC', 'DS', 3, 5),

    # Diagonal short
    RainWorldRegionConnection('LF', 'SU', 2, 5),
    RainWorldRegionConnection('SB', 'DS', 1, 4),
    RainWorldRegionConnection('HI', 'GW', 2, 2),
    RainWorldRegionConnection('VS', 'SL', 3, 3),
    RainWorldRegionConnection('UW', 'SH', 1, 1),
    RainWorldRegionConnection('SL', 'DM', 1, 1),

    #
    RainWorldRegionConnection('SI', 'VS', 3, 4),
]
