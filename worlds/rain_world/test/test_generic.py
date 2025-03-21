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


class TestHunterMSCShadedCitadel(RainWorldTestBase):
    options = {"which_gamestate": "hunter_msc", "random_starting_shelter": "shaded_citadel",
               "difficulty_echo_low_karma": 1}

    def test_karma_flower_absence(self):
        self.assertAccessDependency(["Echo-SH"], [["Karma", "Karma", "Karma", "Karma"]], True)


class TestGourmand(RainWorldTestBase):
    options = {"which_gamestate": "gourmand"}


class TestArtificer(RainWorldTestBase):
    options = {"which_gamestate": "artificer"}

    def test_check_generation(self):
        locs = [loc.name for loc in self.multiworld.get_locations(self.player)]
        self.assertNotIn("Token-BrotherLongLegs-GW", locs)


class TestRivulet(RainWorldTestBase):
    options = {"which_gamestate": "rivulet"}

    def test_86(self):
        # https://github.com/alphappy/ArchipelagoRW/issues/86
        locs = [loc.name for loc in self.multiworld.get_locations(self.player)]
        self.assertIn("Token-MirosBird-SH", locs)


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


class TestSofanthiel(RainWorldTestBase):
    options = {"which_gamestate": "sofanthiel"}


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
