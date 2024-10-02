from typing import Callable

from BaseClasses import CollectionState


def max_karma_at_least(karma: int, player: int) -> Callable[[CollectionState], bool]:
    def max_karma_at_least_inner(state: CollectionState) -> bool:
        return state.has("Karma cap increase", player, karma - (1 if karma < 6 else 2))
    return max_karma_at_least_inner


def karma_and_key(player: int, karma: int, region: str) -> Callable[[CollectionState], bool]:
    def karma_and_key_inner(state: CollectionState) -> bool:
        return (state.has("Karma cap increase", player, karma - (1 if karma < 6 else 2))
                and state.has(f"Key to {region}", player))
    return karma_and_key_inner


def ascension(player: int) -> Callable[[CollectionState], bool]:
    def ascension_inner(state: CollectionState) -> bool:
        return state.has("Ascension", player)
    return ascension_inner


def max_karma_factory_factory(karma: int) -> Callable[[int], Callable[[CollectionState], bool]]:
    def max_karma_factory(player: int):
        def max_karma_inner(state: CollectionState) -> bool:
            return state.has("Karma cap increase", player, karma - (1 if karma < 6 else 2))
        return max_karma_inner
    return max_karma_factory


def lizard_factory_factory(count: int):
    def lizard_factory(player: int):
        def lizard_inner(state: CollectionState) -> bool:
            return state.has_from_list_unique(
                ["Blue Liz", "Green Liz", "Pink Liz", "White Liz", "Red Liz", "Cyan Liz", "Black Liz", "Caramel Liz", "Yellow Liz"],
                player, count
            )
        return lizard_inner
    return lizard_factory


def wanderer_factory_factory(count: int):
    def wanderer_factory(player: int):
        def wanderer_inner(state: CollectionState) -> bool:
            return state.has("Region", player, count)
        return wanderer_inner
    return wanderer_factory


def pilgrim_factory(player: int):
    def pilgrim_inner(state: CollectionState) -> bool:
        return all(state.can_reach_location(f'Ec|{r}', player) for r in ['CC', 'SI', 'LF', 'SB', 'SH', 'UW'])
    return pilgrim_inner


def haves_survivor_factory(player: int):
    def haves_survivor_inner(state: CollectionState) -> bool:
        return state.can_reach_location('Pa|Survivor', player)
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
