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

    def test_check_generation(self):
        locs = [loc.name for loc in self.multiworld.get_locations(self.player)]
        self.assertNotIn("Pearl-MS-GW", locs)
        self.assertNotIn("Broadcast-Chatlog_SI0-SI", locs)
        self.assertNotIn("Broadcast-Chatlog_SI1-SI", locs)
        self.assertIn("Token-KingVulture-SI", locs)
        self.assertIn("Pearl-SI_top-SI", locs)


class TestGourmand(RainWorldTestBase):
    options = {"which_gamestate": "gourmand"}


class TestArtificer(RainWorldTestBase):
    options = {"which_gamestate": "artificer"}


class TestRivulet(RainWorldTestBase):
    options = {"which_gamestate": "rivulet"}


class TestSpear(RainWorldTestBase):
    options = {"which_gamestate": "spearmaster"}

    def test_check_generation(self):
        locs = [loc.name for loc in self.multiworld.get_locations(self.player)]
        self.assertIn("Pearl-MS-GW", locs)
        self.assertIn("Broadcast-Chatlog_SI0-SI", locs)
        self.assertIn("Broadcast-Chatlog_SI1-SI", locs)
        self.assertNotIn("Token-KingVulture-SI", locs)
        self.assertNotIn("Pearl-SI_top-SI", locs)


class TestSaint(RainWorldTestBase):
    options = {"which_gamestate": "saint"}


class TestMonkMSCAlternate(RainWorldTestBase):
    options = {"which_gamestate": "monk_msc", "which_victory_condition": "alternate"}


class TestSurvivorMSCAlternate(RainWorldTestBase):
    options = {"which_gamestate": "survivor_msc", "which_victory_condition": "alternate"}


class TestGourmandAlternate(RainWorldTestBase):
    options = {"which_gamestate": "gourmand", "which_victory_condition": "alternate"}


class TestArtificerAlternate(RainWorldTestBase):
    options = {"which_gamestate": "artificer", "which_victory_condition": "alternate"}


class TestRivuletAlternate(RainWorldTestBase):
    options = {"which_gamestate": "rivulet", "which_victory_condition": "alternate"}


class TestSpearAlternate(RainWorldTestBase):
    options = {"which_gamestate": "spearmaster", "which_victory_condition": "alternate"}
