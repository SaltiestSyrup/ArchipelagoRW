from typing import Callable, Optional

from BaseClasses import CollectionState, MultiWorld
from worlds.generic.Rules import add_rule


class Condition:
    def __call__(self):
        return self.check

    def check(self, player: int) -> Callable[[CollectionState], bool]:
        return lambda state: True


class Simple(Condition):
    """Represents a simple check against a CollectionState."""
    def __init__(self, items: list[str] | str, count: Optional[int] = None,
                 unique: Optional[bool] = None, negative: bool = False,
                 locations: bool = False):
        """
        :param items:  The item or list of items to check against.
        :param count:  The number of items that must be found in the CollectionState.
        If unspecified, all items must be found (`count == len(items)` if `items` is a list, or 1 otherwise).
        :param unique:  Whether duplicate items should be ignored.
        If unspecified, `unqiue` is `False` if `items` is a string and `True` if it's a list.
        :param negative:  Whether the condition should be negated.
        """
        self.unique: bool = unique or (type(items) == list)
        self.items: list[str] = [items] if type(items) == str else items
        self.count: int = count or len(self.items)
        self.negative: bool = negative
        self.locations: bool = locations

    def check(self, player: int) -> Callable[[CollectionState], bool]:
        def inner(state: CollectionState) -> bool:
            if len(self.items) == 0:
                return True
            if self.locations:
                ret = sum(state.can_reach_location(item, player) for item in self.items) >= self.count
            elif self.unique:
                ret = state.has_from_list_unique(self.items, player, self.count)
            else:
                ret = state.has_from_list(self.items, player, self.count)

            return (not ret) if self.negative else ret
        return inner


class Compound(Condition):
    """Represents multiple checks against a CollectionState, some specified number of which must be satsified."""
    def __init__(self, count: int, *conditions: Condition):
        self.conditions = conditions
        self.count = count

    def check(self, player: int) -> Callable[[CollectionState], bool]:
        def inner(state: CollectionState) -> bool:
            if self.count > len(self.conditions):
                return False
            elif self.count == len(self.conditions):
                return all(c.check(player)(state) for c in self.conditions)
            elif self.count == 1:
                return any(c.check(player)(state) for c in self.conditions)
            else:
                return sum(c.check(player)(state) for c in self.conditions) >= self.count
        return inner


class AnyOf(Compound):
    def __init__(self, *conditions: Condition):
        super().__init__(1, *conditions)


class AllOf(Compound):
    def __init__(self, *conditions: Condition):
        super().__init__(len(conditions), *conditions)


ConditionBlank = Condition()


class LocationAccessRule:
    def __init__(self, name: str, condition: Condition):
        self.name: str = name
        self.condition: Condition = condition

    def make(self, player: int, multiworld: MultiWorld):
        add_rule(multiworld.get_location(self.name, player), self.condition.check(player))
