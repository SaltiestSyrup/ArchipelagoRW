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


class TestSpear(RainWorldTestBase):
    options = {"which_gamestate": "spearmaster"}


class TestSaint(RainWorldTestBase):
    options = {"which_gamestate": "saint"}


class TestMonkVanillaAlternate(RainWorldTestBase):
    options = {"which_gamestate": "monk_vanilla", "which_victory_condition": "alternate"}


class TestSurvivorVanillaAlternate(RainWorldTestBase):
    options = {"which_gamestate": "survivor_vanilla", "which_victory_condition": "alternate"}


class TestHunterVanillaAlternate(RainWorldTestBase):
    options = {"which_gamestate": "hunter_vanilla", "which_victory_condition": "alternate"}


class TestMonkMSCAlternate(RainWorldTestBase):
    options = {"which_gamestate": "monk_msc", "which_victory_condition": "alternate"}


class TestSurvivorMSCAlternate(RainWorldTestBase):
    options = {"which_gamestate": "survivor_msc", "which_victory_condition": "alternate"}


class TestHunterMSCAlternate(RainWorldTestBase):
    options = {"which_gamestate": "hunter_msc", "which_victory_condition": "alternate"}


class TestGourmandAlternate(RainWorldTestBase):
    options = {"which_gamestate": "gourmand", "which_victory_condition": "alternate"}


class TestArtificerAlternate(RainWorldTestBase):
    options = {"which_gamestate": "artificer", "which_victory_condition": "alternate"}


class TestRivuletAlternate(RainWorldTestBase):
    options = {"which_gamestate": "rivulet", "which_victory_condition": "alternate"}


class TestSpearAlternate(RainWorldTestBase):
    options = {"which_gamestate": "spearmaster", "which_victory_condition": "alternate"}


class TestSaintAlternate(RainWorldTestBase):
    options = {"which_gamestate": "saint", "which_victory_condition": "alternate"}
