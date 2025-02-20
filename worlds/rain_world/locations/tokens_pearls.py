from typing import Callable

from BaseClasses import MultiWorld
from .classes import LocationData
from ..options import RainWorldOptions
from ..game_data import static_data
from ..game_data.general import region_code_to_name, scugs_all, scugs_vanilla
from ..conditions.classes import AnyOf, AllOf, Simple, Condition

locations = {}
next_offset = 0


class TokenOrPearl(LocationData):
    def __init__(self, name: str, region: str, offset: int,
                 msc_blacklist: list[str] | None = None,
                 vanilla_blacklist: list[str] | None = None):
        super().__init__(name, name, region, offset)
        self.msc_blacklist = msc_blacklist
        self.vanilla_blacklist = vanilla_blacklist

    def make(self, player: int, multiworld: MultiWorld, options: RainWorldOptions) -> bool:
        # HARDCODE: This pearl only appears in a past-GW room.
        if self.full_name == "Pearl-MS-GW":
            self.msc_blacklist = set(scugs_all).difference({"Artificer", "Spear"})
        # HARDCODE: This pearl isn't accessible from SU proper.
        if self.full_name == "Pearl-SU_filt-SU":
            self.region = "Outskirts filtration"

        self.generation_condition = self._gen()
        # self.access_condition = self._acc()
        return super().make(player, multiworld, options)

    def _gen(self) -> Callable[[RainWorldOptions], bool]:
        def inner(options: RainWorldOptions) -> bool:
            if self.full_name.startswith("DevToken"):
                return False
            # HARDCODE: This pearl only appears in a past-GW room.
            if options.checks_tokens_pearls and self.full_name != "Pearl-MS-GW":
                return True
            if options.msc_enabled and options.starting_scug not in (self.msc_blacklist or []):
                return True
            if not options.msc_enabled and options.starting_scug not in (self.vanilla_blacklist or []):
                return True
            return False
        return inner

    def _acc(self, options: RainWorldOptions) -> Condition:
        return \
            AnyOf(
                AllOf(
                    Simple("MSC"),
                    Simple([f'Scug-{scug}' for scug in set(scugs_all).difference(set(self.msc_blacklist))], 1)
                ),
                AllOf(
                    Simple("MSC", negative=True),
                    Simple([f'Scug-{scug}' for scug in set(scugs_vanilla).difference(set(self.vanilla_blacklist))], 1)
                )
            )


def token_name(name: str, kind: str, _region: str) -> str:
    if kind == "GoldToken":  # arena level unlock
        return f'Token-L-{name}'
    elif kind == "RedToken":  # safari level unlock
        return f'Token-S-{name}'
    elif kind == "WhiteToken":
        return f'Broadcast-{name}-{_region}'
    elif kind == "DevToken":
        return f'DevToken-{name}-{_region}'
    elif "Token" in kind:
        return f'Token-{name}-{_region}'
    else:
        return f'Pearl-{name}-{_region}'


for region, region_data in static_data["MSC"].items():
    for room, room_data in region_data.items():
        alted: set[str] = room_data.get("alted", set())

        if "shinies" in room_data.keys():
            for shiny_name, shiny_data in room_data["shinies"].items():
                name = token_name(shiny_name, shiny_data["kind"], region)
                locations[name] = TokenOrPearl(
                    name, region_code_to_name[region], next_offset,
                    msc_blacklist=shiny_data.get("filter", set()).union(
                        alted.difference(shiny_data.get("whitelist", set()))
                    )
                )
                next_offset += 1


for region, region_data in static_data["Vanilla"].items():
    for room, room_data in region_data.items():
        alted: set[str] = room_data.get("alted", set())

        if "shinies" in room_data.keys():
            for shiny_name, shiny_data in room_data["shinies"].items():
                name = token_name(shiny_name, shiny_data["kind"], region)
                if name in locations.keys():
                    locations[name].vanilla_blacklist = shiny_data.get("filter", set())
                else:
                    locations[name] = TokenOrPearl(
                        name, region_code_to_name[region], next_offset,
                        vanilla_blacklist=shiny_data.get("filter", set()).union(
                            alted.difference(shiny_data.get("whitelist", set()))
                        )
                    )
                    next_offset += 1


def generate(_: RainWorldOptions) -> list[LocationData]:
    return list(locations.values())
