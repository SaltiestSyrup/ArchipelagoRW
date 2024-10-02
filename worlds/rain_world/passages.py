"""
DEPRECATED.
"""

from typing import Dict

from BaseClasses import Location, Region, MultiWorld
from . import constants, state_helpers
from ..generic.Rules import set_rule
from .classes import LocationData


class PassageLocation(Location):
    def __init__(self, player: int, name: str, address: int, parent: Region):
        super().__init__(player, name, address, parent)


def create_passage_regions(player: int, multiworld: MultiWorld):
    region = Region("Passages", player, multiworld)
    region2 = Region("Passages 2", player, multiworld)

    multiworld.get_region("Menu", player).connect(region)
    region.connect(region2, rule=lambda state: state.has("The Survivor", player))

    region.locations.extend([
        Location(player, "The Survivor", constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Dragon Slayer", 1 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Friend", 2 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Martyr", 3 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Mother", 4 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Pilgrim", 5 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Wanderer", 6 + constants.FIRST_ID_PASSAGES, region),
    ])

    region2.locations.extend([
        Location(player, "The Chieftain", 7 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Hunter", 8 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Monk", 9 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Nomad", 10 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Outlaw", 11 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Saint", 12 + constants.FIRST_ID_PASSAGES, region),
        Location(player, "The Scholar", 13 + constants.FIRST_ID_PASSAGES, region),
    ])


def set_passage_rules(player: int, multiworld: MultiWorld):
    set_rule(multiworld.get_location("The Survivor", player), state_helpers.max_karma_at_least(5, player))
