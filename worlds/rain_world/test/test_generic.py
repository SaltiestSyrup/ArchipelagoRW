from . import RainWorldTestBase


class TestMonkVanilla(RainWorldTestBase):
    options = {"which_gamestate": "monk_vanilla"}


class TestSurvivorVanilla(RainWorldTestBase):
    options = {"which_gamestate": "survivor_vanilla"}


class TestHunterVanilla(RainWorldTestBase):
    options = {"which_gamestate": "hunter_vanilla"}


class TestMonkMSC(RainWorldTestBase):
    options = {"which_gamestate": "monk_msc"}


class TestSurvivorMSC(RainWorldTestBase):
    options = {"which_gamestate": "survivor_msc"}


class TestHunterMSC(RainWorldTestBase):
    options = {"which_gamestate": "hunter_msc"}


class TestGourmand(RainWorldTestBase):
    options = {"which_gamestate": "gourmand"}


class TestArtificer(RainWorldTestBase):
    options = {"which_gamestate": "artificer"}


class TestRivulet(RainWorldTestBase):
    options = {"which_gamestate": "rivulet"}


class TestSpearMSC(RainWorldTestBase):
    options = {"which_gamestate": "spearmaster"}


class TestSaint(RainWorldTestBase):
    options = {"which_gamestate": "saint"}
