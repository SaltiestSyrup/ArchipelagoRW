from typing import Dict, List, NamedTuple, Optional, TYPE_CHECKING, Any, Callable

from BaseClasses import CollectionState, Location, Region, MultiWorld
from worlds.rain_world.constants import FIRST_ID, REGION_CODE_DICT

location_map: dict[str, int] = {}


class LocationData:
    def __init__(self, full_name: str, short_name: str, region: str, offset: Optional[int]):
        self.full_name = full_name
        self.short_name = short_name
        self.region = region
        self.id = None
        self.rules: list[Callable[[CollectionState], bool]] = []
        if offset is not None:
            self.id = offset + FIRST_ID
            location_map[full_name] = self.id

    def make(self, player: int, multiworld: MultiWorld) -> Location:
        region = multiworld.get_region(self.region, player)
        loc = Location(player, self.short_name, self.id, region)
        region.locations.append(loc)
        return loc


class PhysicalLocation(LocationData):
    def __init__(self, full_name: str, short_name: str, region: str, offset: int, room: str):
        super().__init__(full_name, short_name, region, offset)
        self.room = room


class Token(PhysicalLocation):
    def __init__(self, name: str, color: str, region: str, offset: int, room: str):
        super().__init__(f"CT|{color}|{name}", f"CT|{color}|{name}", region, offset, room)


class Pearl(PhysicalLocation):
    def __init__(self, name: str, color: str, region: str, offset: int, room: str):
        super().__init__(f"Pe|{name}", f"Pe|{name}", region, offset, room)


class Echo(PhysicalLocation):
    def __init__(self, ghost: str, region: str, offset: int, room: str):
        super().__init__(f"Ec|{ghost}", f"Ec|{ghost}", region, offset, room)


class Passage(LocationData):
    def __init__(self, name: str, region: str, offset: int):
        super().__init__(f"Pa|{name}", f"Pa|{name}", region, offset)


all_locations: list[LocationData] = [
    Token("SU", "gold", "Outskirts", 0, ""),
    Token("SU", "red", "Outskirts", 1, ""),
    Token("PoleMimic", "blue", "Outskirts", 2, ""),
    Token("DangleFruit", "blue", "Outskirts", 3, ""),
    Token("CicadaA", "blue", "Outskirts", 4, ""),
    Pearl("SU", "", "Outskirts", 20, ""),
    Pearl("SU_filt", "", "Outskirts filtration", 21, ""),

    Token("HI", "gold", "Industrial Complex", 100, ""),
    Token("HI", "red", "Industrial Complex", 101, ""),
    Token("FirecrackerPlant", "blue", "Industrial Complex", 102, ""),
    Token("BlueLizard", "blue", "Industrial Complex", 103, ""),
    Token("SmallCentipede", "blue", "Industrial Complex", 104, ""),
    Token("VultureGrub", "blue", "Industrial Complex", 105, ""),
    Pearl("HI", "", "Industrial Complex", 120, ""),

    Token("DS", "gold", "Drainage System", 200, "B10"),
    Token("DS", "red", "Drainage System", 201, "A01"),
    Token("Snail", "blue", "Drainage System", 202, "B06"),
    Token("Salamander", "blue", "Drainage System", 203, "B04"),
    Token("Leech", "blue", "Drainage System", 204, "A05"),
    Token("BubbleGrass", "blue", "Drainage System", 205, "A25"),
    Token("Hazer", "blue", "Drainage System", 206, "A21"),
    Pearl("DS", "", "Drainage System", 220, ""),

    Token("GW", "gold", "Garbage Wastes", 300, "C10"),
    Token("GW", "red", "Garbage Wastes", 301, "A25"),
    Token("WaterNut", "blue", "Garbage Wastes", 302, "D02"),
    Token("RedLizard", "blue", "Garbage Wastes", 303, "A14"),
    Token("BrotherLongLegs", "blue", "Garbage Wastes", 304, "C09"),
    Token("ScavengerBomb", "blue", "Garbage Wastes", 305, "A21"),
    Token("FireSpear", "blue", "Garbage Wastes", 306, "A24"),
    Pearl("GW", "", "Garbage Wastes", 320, ""),

    Token("SL", "red", "Shoreline", 401, "I01"),
    Token("SeaLeech", "blue", "Shoreline", 402, "A06"),
    Token("BigEel", "blue", "Shoreline", 403, "E01"),
    Token("JetFish", "blue", "Shoreline", 404, "F02"),
    Token("JellyFish", "blue", "Shoreline", 405, "C01"),
    Pearl("SL", "", "Shoreline", 420, ""),
    Pearl("SL_chimney", "", "Shoreline", 421, ""),
    Pearl("SL_moon", "", "Shoreline", 422, ""),

    Token("VS", "gold", "Pipeyard", 500, "C04"),
    Token("VS", "red", "Pipeyard", 501, "E02"),
    Token("Pearl", "blue", "Pipeyard", 502, "A14"),
    Token("LillyPuck", "blue", "Pipeyard", 503, "C03"),
    Pearl("VS", "", "Pipeyard", 520, ""),

    Token("SH", "gold", "Shaded Citadel", 600, "B04"),
    Token("SH", "red", "Shaded Citadel", 601, "KELP"),
    Token("BigSpider", "blue", "Shaded Citadel", 602, "A13"),
    Token("Spider", "blue", "Shaded Citadel", 603, "C03"),
    Token("Lantern", "blue", "Shaded Citadel", 604, "B05"),
    Token("LanternMouse", "blue", "Shaded Citadel", 605, "B05"),
    Token("MirosBird", "blue", "Shaded Citadel", 606, "E01"),
    Token("FlareBomb", "blue", "Shaded Citadel", 607, "D03"),
    Pearl("SH", "", "Shaded Citadel", 620, "A19"),

    Token("UW", "red", "The Exterior", 701, "D06"),
    Token("YellowLizard", "blue", "The Exterior", 702, "C02"),
    Token("SlimeMold", "blue", "The Exterior", 703, "J01"),
    Token("TubeWorm", "blue", "The Exterior", 704, "B01"),
    Pearl("UW", "", "The Exterior", 720, "H01"),

    Token("SS", "red", "Five Pebbles", 801, "E06"),
    Token("Inspector", "blue", "Five Pebbles", 802, "C03"),

    Token("CC", "gold", "Chimney Canopy", 900, "STRAINER01"),
    Token("CC", "red", "Chimney Canopy", 901, "OUTPUT"),
    Token("DropBug", "blue", "Chimney Canopy", 902, "F01"),
    Token("WhiteLizard", "blue", "Chimney Canopy", 903, "A10"),
    Token("CyanLizard", "blue", "Chimney Canopy", 904, "C13"),
    Token("Vulture", "blue", "Chimney Canopy", 905, "C04"),
    Pearl("CC", "", "Chimney Canopy", 920, ""),

    Token("SI", "gold", "Sky Islands", 1000, "C07"),
    Token("SI", "red", "Sky Islands", 1001, "B09"),
    Token("VultureMask", "blue", "Sky Islands", 1002, "B07x"),
    Token("KingVulture", "blue", "Sky Islands", 1003, "A07"),
    Token("Centiwing", "blue", "Sky Islands", 1004, "A18"),
    Token("EggBug", "blue", "Sky Islands", 1005, "D05"),
    Token("DandelionPeach", "blue", "Sky Islands", 1006, "C04"),
    Pearl("SI_top", "", "Sky Islands", 1020, "A07"),
    Pearl("SI_west", "", "Sky Islands", 1021, "B12"),
    Pearl("SI_chat3", "", "Sky Islands", 1022, "C02"),
    Pearl("SI_chat4", "", "Sky Islands", 1023, "C08"),
    Pearl("SI_chat5", "", "Sky Islands", 1024, "B10"),

    Token("LF", "gold", "Farm Arrays", 1100, "B04"),
    Token("LF", "red", "Farm Arrays", 1101, "D09"),
    # Token("ScavengerBomb", "blue", "Farm Arrays", 1102, "A17"),  TODO verify that this exists
    Token("SpitterSpider", "blue", "Farm Arrays", 1103, "B04"),
    Token("Deer", "blue", "Farm Arrays", 1104, "C03"),
    Token("FlyLure", "blue", "Farm Arrays", 1105, "D06"),
    Token("SporePlant", "blue", "Farm Arrays", 1106, "D02"),
    Token("BigNeedleWorm", "blue", "Farm Arrays", 1107, "A02"),
    Token("PuffBall", "blue", "Farm Arrays", 1108, "F02"),
    Pearl("LF_west", "", "Farm Arrays", 1120, "D06"),
    Pearl("LF_bottom", "", "Farm Arrays", 1121, "D07"),

    Token("SB", "gold", "Subterranean", 1200, "F01"),
    Token("SB", "red", "Subterranean", 1201, "J01"),
    Token("Filtration", "gold", "Subterranean", 1202, "G04"),
    Token("BigCentipede", "blue", "Subterranean", 1203, "G02"),
    Token("TentaclePlant", "blue", "Subterranean", 1204, "J03"),
    Token("BlackLizard", "blue", "Subterranean", 1205, "D04"),
    Token("Mushroom", "blue", "Subterranean", 1206, "E04"),
    Token("RedCentipede", "blue", "Subterranean", 1207, "H02"),
    Pearl("SB_ravine", "", "Subterranean ravine", 1220, "F03"),
    # Pearl("Misc2", "", "Subterranean", 1221, "E07"),  TODO verify that this actually a unique pearl
    Pearl("SB_filtration", "", "Subterranean", 1222, "J03"),

    Token("MS", "gold", "Submerged Superstructure", 1300, "FARSIDE"),
    Token("MS", "red", "Bitter Aerie", 1301, "bittermironest"),
    Token("BigJelly", "blue", "Submerged Superstructure", 1302, "MEMOUTSIDE"),
    Token("GlowWeed", "blue", "Submerged Superstructure", 1303, "VENT15"),
    Token("AquaCenti", "blue", "Submerged Superstructure", 1304, "VENT10"),

    Token("OE", "gold", "Outer Expanse", 1400, "WORMPIT"),
    Token("OE", "red", "Outer Expanse", 1401, "TREETOP"),
    Token("SlugNPC", "blue", "Outer Expanse filtration", 1402, "PUMP04"),
    Token("Spit Lizard", "blue", "Outer Expanse", 1403, "RUIN25"),
    Token("Yeek", "blue", "Outer Expanse", 1404, "RUIN21"),
    Token("GooieDuck", "blue", "Outer Expanse", 1405, "JUNGLE04"),
    Token("JungleLeech", "blue", "Outer Expanse", 1406, "RUIN06"),
    Pearl("OE", "", "Outer Expanse", 1420, "SPIRE"),

    Passage("Martyr", "Early Passages", 5000),
    Passage("Mother", "Early Passages", 5001),
    Passage("Pilgrim", "Early Passages", 5002),
    Passage("Survivor", "Early Passages", 5003),

    Passage("DragonSlayer", "PPwS Passages", 5020),
    Passage("Friend", "PPwS Passages", 5021),
    # Passage("Wanderer", "PPwS Passages", 5022),

    Passage("Chieftain", "Late Passages", 5040),
    Passage("Hunter", "Late Passages", 5041),
    Passage("Monk", "Late Passages", 5042),
    # Passage("Nomad", "Late Passages", 5043),  # TODO who was responsible for making this one honestly
    Passage("Outlaw", "Late Passages", 5044),
    Passage("Saint", "Late Passages", 5045),
    # Passage("Scholar", "Late Passages", 5046),  # TODO

    Echo("CC", "Chimney Canopy", 5070, ""),
    Echo("SH", "Shaded Citadel", 5071, ""),
    Echo("LF", "Farm Arrays", 5072, ""),
    Echo("UW", "The Exterior", 5073, ""),
    Echo("SI", "Sky Islands", 5074, ""),
    Echo("SB", "Subterranean ravine", 5075, ""),

    LocationData("Ascension", "Ascension", "Void Sea", None),
]

# food quest, 5101 - 5123
all_locations += [LocationData(f"FQ|{n:0>2}", f"FQ|{n:0>2}", "Food Quest", 5100 + n) for n in range(1, 23)]
# wanderer pips, 5151 - 5164
all_locations += [LocationData(f"Wa|{n:0>2}", f"Wa|{n:0>2}", "PPwS Passages", 5150 + n) for n in range(1, 14)]
