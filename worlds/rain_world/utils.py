from typing import TypeVar


def flatten(lol):
    return [item for sublist in lol for item in sublist]


T = TypeVar("T")


def normalize(d: dict[T, float]) -> dict[T, float]:
    """Normalizes a dictionary of weights so that all its weights add to 1."""
    total = sum(list(d.values()))
    return {k: v / total for k, v in d.items()}


def flounder(weights, count):
    current_credits = 0.1
    credit_values = {k: v * count for k, v in normalize(weights).items()}

    ret = []
    for item, credit_count in credit_values.items():
        current_credits += credit_count
        ret += [item] * int(current_credits)
        current_credits -= int(current_credits)
    return ret


def flounder2(weights: dict[T, float], count: int) -> list[T]:
    """Given a dictionary of weights, constructs a list of items of a given size
    built whose proportions approximate the dictionary of weights."""
    # Compute roughly how many entries each item should have.  The total number of credits is the `count`.
    credit = {k: v * count for k, v in normalize(weights).items()}
    # Compute the remainders for each credit value.
    remainders = {k: v - int(v) for k, v in credit.items()}

    ret = []
    # Each item is added to the list once for each *full* credit.
    for item, proportion in credit.items():
        ret += [item] * int(proportion)
    # Then, sort the credit values by their remainders and assign extras starting with the largest remainders
    # until the list reaches the appropriate size.
    for item, remainder in sorted(remainders.items(), key=lambda i: -i[1]):
        ret.append(item)
        if len(ret) >= count:
            break

    return ret
