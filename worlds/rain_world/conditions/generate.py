"""
Methods which decide whether something should generate based on the current settings.
Everything here should be (*args, **kwargs) -> (RainWorldOptions) -> bool.
"""
from typing import Callable

from ..options import RainWorldOptions


def msc(enabled: bool) -> Callable[[RainWorldOptions], bool]:
    def inner(options: RainWorldOptions) -> bool:
        return options.msc_enabled == enabled
    return inner


def blacklist_scugs(scugs: list[str], msc_enabled: bool = None) -> Callable[[RainWorldOptions], bool]:
    def inner(options: RainWorldOptions) -> bool:
        if msc_enabled is not None and options.msc_enabled != msc_enabled:
            return False
        return options.starting_scug not in scugs
    return inner


def whitelist_scugs(scugs: list[str], msc_enabled: bool = None) -> Callable[[RainWorldOptions], bool]:
    def inner(options: RainWorldOptions) -> bool:
        if msc_enabled is not None and options.msc_enabled != msc_enabled:
            return False
        return options.starting_scug in scugs
    return inner


def no_monk_vanilla() -> Callable[[RainWorldOptions], bool]:
    def inner(options: RainWorldOptions) -> bool:
        return options.starting_scug != "Yellow" or options.msc_enabled
    return inner
