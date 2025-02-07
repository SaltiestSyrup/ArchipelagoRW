from . import RainWorldTestBase


class TestSurvivorVanilla(RainWorldTestBase):
    options = {"which_gamestate": "survivor_vanilla"}


class TestSurvivorMSC(RainWorldTestBase):
    options = {"which_gamestate": "survivor_msc"}


class TestSpearMSC(RainWorldTestBase):
    options = {"which_gamestate": "spearmaster"}
