from .classes import ObjectEventData2

from ..game_data.general import scugs_msc, scugs_vanilla
from ..classes import Simple, AnyOf, AllOf
from ..game_data.files import placed_objects, creatures


def generate_events(which: str) -> list[ObjectEventData2]:
    ret = []
    data = placed_objects if which == "placed_objects" else creatures["normal"]

    for otype, by_otype in data.items():
        condition = \
            AnyOf(
                *[AllOf(
                    Simple("MSC", negative=neg),
                    AnyOf(
                        *[AllOf(
                            Simple(f"Scug-{scug}"),
                            Simple(
                                [
                                    f"Access-{region}" for region in
                                    set(room.split("_")[0] for room in
                                        by_otype[dlcstate][scug] + by_otype[dlcstate]["*ALL"])
                                ],
                                1
                            )
                        ) for scug in scugs]
                    )
                ) for neg, dlcstate, scugs in zip((True, False), ("Vanilla", "MSC"), (scugs_vanilla, scugs_msc))]
            )

        ret.append(ObjectEventData2(otype, otype, "Events", condition))
    return ret
