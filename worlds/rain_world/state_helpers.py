from typing import Callable

from BaseClasses import CollectionState
from . import game_data


def max_karma_at_least(karma: int, player: int) -> Callable[[CollectionState], bool]:
    def max_karma_at_least_inner(state: CollectionState) -> bool:
        return state.has("Karma", player, karma - (1 if karma < 6 else 2))
    return max_karma_at_least_inner


def karma_and_key(player: int, karma: int, region: str) -> Callable[[CollectionState], bool]:
    def karma_and_key_inner(state: CollectionState) -> bool:
        return (state.has("Karma", player, karma - (1 if karma < 6 else 2))
                and state.has(f"Key to {region}", player))
    return karma_and_key_inner


def karma_and_gate(player: int, karma: int, gate_name: str) -> Callable[[CollectionState], bool]:
    def karma_and_gate_inner(state: CollectionState) -> bool:
        return (state.has("Karma", player, karma - (1 if karma < 6 else 2))
                and state.has(f"GATE_{gate_name}", player))
    return karma_and_gate_inner


def ascension(player: int) -> Callable[[CollectionState], bool]:
    def ascension_inner(state: CollectionState) -> bool:
        return state.has("Ascension", player)
    return ascension_inner


def max_karma_factory_factory(karma: int) -> Callable[[int], Callable[[CollectionState], bool]]:
    def max_karma_factory(player: int):
        def max_karma_inner(state: CollectionState) -> bool:
            return state.has("Karma", player, karma - (1 if karma < 6 else 2))
        return max_karma_inner
    return max_karma_factory


def lizard_factory_factory(count: int, dragonslayer: bool):
    def lizard_factory(player: int):
        def lizard_inner(state: CollectionState) -> bool:
            return state.has_from_list_unique(
                (game_data.dragonslayer_msc if state.has("MSC", player) else game_data.dragonslayer_vanilla)
                if dragonslayer else game_data.lizards_any,
                player, count)
        return lizard_inner
    return lizard_factory


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


def haves_survivor_factory(player: int):
    def haves_survivor_inner(state: CollectionState) -> bool:
        return state.can_reach_location('Passage-Survivor', player)
    return haves_survivor_inner


def haves_survivor_or_ppws_factory(player: int):
    def haves_survivor_inner(state: CollectionState) -> bool:
        return state.can_reach_location('Passage-Survivor', player)
    return haves_survivor_inner


def food_quest_factory_factory(count: int):
    def food_quest_factory(player: int):
        def food_quest_inner(state: CollectionState) -> bool:
            return state.has_from_list_unique(
                [f'Eat {food}' for food in
                 ['Slime Mold', 'Blue Fruit', 'Batfly', 'Mushroom', 'Black Lizard', 'Bubble Fruit', 'Jellyfish',
                  'Jetfish', 'Glow Weed', 'Aquatic Lizard', 'Snail', 'Hazer', 'Eggbug', 'Lilypuck', 'Yellow Lizard',
                  'Grappling Worm', 'Neuron Fly', 'Centiwing', 'Dandelion Peach', 'Cyan Lizard', 'Gooieduck',
                  'Aquapede or Redpede']
                 ],
                player, count
            )
        return food_quest_inner
    return food_quest_factory


def has(item: str) -> Callable[[int], Callable[[CollectionState], bool]]:
    def has_inner(player: int) -> Callable[[CollectionState], bool]:
        def has_inner_inner(state: CollectionState) -> bool:
            return state.has(item, player)
        return has_inner_inner
    return has_inner


def has_some(items: list[str], count: int) -> Callable[[int], Callable[[CollectionState], bool]]:
    def inner(player: int) -> Callable[[CollectionState], bool]:
        def inner_inner(state: CollectionState) -> bool:
            return state.has_from_list_unique(items, player, count)
        return inner_inner
    return inner


def gate_factory(gate_name: str, karma: int, gamestate: list[str] = None) -> Callable[[int], Callable[[CollectionState], bool]]:
    def inner(player: int) -> Callable[[CollectionState], bool]:
        def inner_inner(state: CollectionState) -> bool:
            return (state.has("Karma", player, karma - (1 if karma < 6 else 2))
                    and state.has(f"GATE_{gate_name}", player)
                    and state.has_all(gamestate or [], player))
        return inner_inner
    return inner

