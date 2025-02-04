from .classes import Simple, AnyOf, LocationAccessRule

cond_normal = AnyOf(Simple("Karma", 4), Simple(["Scug-Artificer", "Scug-Saint"], 1))
cond_no_saint = AnyOf(Simple("Karma", 4), Simple("Scug-Artificer"))

all_rules = [
    LocationAccessRule("Echo-SI", cond_normal),
    LocationAccessRule("Echo-LF", cond_normal),
    LocationAccessRule("Echo-SB", cond_normal),
    LocationAccessRule("Echo-CC", cond_normal),
    LocationAccessRule("Echo-UW", cond_no_saint),
    LocationAccessRule("Echo-SH", cond_no_saint),
    LocationAccessRule("Echo-LC", Simple("Scug-Artificer")),
    LocationAccessRule("Echo-UG", Simple("Scug-Saint")),
    LocationAccessRule("Echo-SL", Simple("Scug-Saint")),
    LocationAccessRule("Echo-CL", Simple("Scug-Saint")),
]
