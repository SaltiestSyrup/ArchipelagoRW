from .classes import LocationData, Echo
from ..conditions.classes import Simple, AnyOf
from ..conditions import generate

cond_normal = AnyOf(Simple("Karma", 4), Simple(["Scug-Artificer", "Scug-Saint"], 1))
cond_no_saint = AnyOf(Simple("Karma", 4), Simple("Scug-Artificer"))

locations: list[LocationData] = [
    Echo("CC", "Chimney Canopy", 5070, "", cond_normal),
    Echo("SH", "Shaded Citadel", 5071, "", cond_no_saint),
    Echo("LF", "Farm Arrays", 5072, "", cond_normal),
    Echo("UW", "The Exterior", 5073, "", cond_no_saint),
    Echo("SI", "Sky Islands", 5074, "", cond_normal),
    Echo("SB", "Subterranean ravine", 5075, "", cond_normal),
    Echo("LC", "Metropolis", 5076, "", Simple("Scug-Artificer")),
    Echo("UG", "Undergrowth", 5077, "", Simple("Scug-Saint")),
    Echo("CL", "Silent Construct", 5078, "", Simple("Scug-Saint")),
    Echo("SL", "Shoreline", 5079, "", Simple("Scug-Saint"), generate.whitelist_scugs(["Saint"], True)),
]
