from BaseClasses import Region
from rule_builder.rules import True_, Has
from .classes import ConnectionData
from ..game_data.watcher import portals, PortalData
from ..options import RainWorldOptions
from ..regions.classes import room_to_region
from ...AutoWorld import World


class PortalConnection(ConnectionData):
    def __init__(self, data: PortalData):
        self.data = data
        s = "Spinning Top" if data.spinning_top else "Fixed warp"
        super().__init__(data.source_room, data.target_room, f"{s} in {data.source_room}")

    def make(self, world: World, options: RainWorldOptions, regions: dict[str, Region]):
        self.source, self.dest = room_to_region[self.data.source_room], room_to_region[self.data.target_room]
        self.condition = True_()

        if self.data.source_room[:4] in ["WHIR", "WDSR", "WGWR", "WSUR"]:
            # Warps to WORA need specifically Ripple 3 (In case dynamic warp ability was acquired another way)
            self.condition &= Has("Ripple", 2)

        if (self.data.should_have_key
                and (not self.data.spinning_top or options.spinning_top_keys)
                and ("Daemon" not in self.data.key_name or options.daemon_keys)):
            self.condition &= Has(self.data.key_name)
        if self.data.ripple:
            self.condition &= Has("Ripple", 3 + options.logic_ripplespace_min_req)

        super().make(world, options, regions)


def generate(options: RainWorldOptions) -> list[PortalConnection]:
    if options.starting_scug != "Watcher":
        return []

    return [PortalConnection(data) for data in portals]

