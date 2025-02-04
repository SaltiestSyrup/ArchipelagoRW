from typing import Callable

from BaseClasses import CollectionState
from . import game_data


def ascension(player: int) -> Callable[[CollectionState], bool]:
    def ascension_inner(state: CollectionState) -> bool:
        return state.has("Ascension", player)
    return ascension_inner


def wanderer_factory_factory(count: int):
    def wanderer_factory(player: int):
        def wanderer_inner(state: CollectionState) -> bool:
            # TODO only story regions
            return state.has_from_list_unique(
                [f"Access-{region}" for region in game_data.general.REGION_CODE_DICT.keys()],
                player, count
            )
        return wanderer_inner
    return wanderer_factory


def pilgrim_factory(player: int):
    def pilgrim_inner(state: CollectionState) -> bool:
        return all(state.can_reach_location(f'Echo-{r}', player) for r in ['CC', 'SI', 'LF', 'SB', 'SH', 'UW'])
    return pilgrim_inner


def has(item: str) -> Callable[[int], Callable[[CollectionState], bool]]:
    def has_inner(player: int) -> Callable[[CollectionState], bool]:
        def has_inner_inner(state: CollectionState) -> bool:
            return state.has(item, player)
        return has_inner_inner
    return has_inner

