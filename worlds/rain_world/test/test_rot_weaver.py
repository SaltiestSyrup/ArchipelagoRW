from .bases import RainWorldTestBase

if RUN_GENERAL_AP_UNITTESTS := False:
    # Simply importing this runs the tests.
    from .bases import RainWorldGeneralTestBase

# Test every combination of victory condition, rot spreading checks, and randomized weaver options to ensure they are behaving correctly
class RotWeaverTestBase(RainWorldTestBase):
    def assertRotChecks(self):
        self.assertIn("Spread the Rot - Region #1", [loc.name for loc in self.multiworld.get_locations(self.player)])

    def assertNoRotChecks(self):
        self.assertNotIn("Spread the Rot - Region #1", [loc.name for loc in self.multiworld.get_locations(self.player)])

    def assertWeaverChecks(self):
        self.assertIn("Weaver Encounter #1", [loc.name for loc in self.multiworld.get_locations(self.player)])

    def assertNoWeaverChecks(self):
        self.assertNotIn("Weaver Encounter #1", [loc.name for loc in self.multiworld.get_locations(self.player)])

    def assertWeaverItems(self):
        self.assertIn("Progressive Weaver", [item.name for item in self.multiworld.get_items()])

    def assertNoWeaverItems(self):
        self.assertNotIn("Progressive Weaver", [item.name for item in self.multiworld.get_items()])


class TestRotEndingRotChecksWeaverOn(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "prince",
        "checks_spread_rot": "true",
        "randomize_weaver": "true"
    }

    def test_logic(self):
        self.assertRotChecks()
        self.assertNoWeaverItems()
        self.assertNoWeaverChecks()


class TestRotEndingRotChecksWeaverOff(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "prince",
        "checks_spread_rot": "true",
        "randomize_weaver": "false"
    }

    def test_logic(self):
        self.assertRotChecks()
        self.assertNoWeaverItems()
        self.assertNoWeaverChecks()


class TestRotEndingNoRotChecksWeaverOn(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "prince",
        "checks_spread_rot": "false",
        "randomize_weaver": "true"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertNoWeaverItems()
        self.assertNoWeaverChecks()


class TestRotEndingNoRotChecksWeaverOff(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "prince",
        "checks_spread_rot": "false",
        "randomize_weaver": "false"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertNoWeaverItems()
        self.assertNoWeaverChecks()


class TestWeaverEndingRotChecksWeaverOn(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "weaver",
        "checks_spread_rot": "true",
        "randomize_weaver": "true"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertWeaverItems()
        self.assertWeaverChecks()


class TestWeaverEndingRotChecksWeaverOff(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "weaver",
        "checks_spread_rot": "true",
        "randomize_weaver": "false"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertNoWeaverItems()
        self.assertWeaverChecks()


class TestWeaverEndingNoRotChecksWeaverOn(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "weaver",
        "checks_spread_rot": "false",
        "randomize_weaver": "true"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertWeaverItems()
        self.assertWeaverChecks()


class TestWeaverEndingNoRotChecksWeaverOff(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "weaver",
        "checks_spread_rot": "false",
        "randomize_weaver": "false"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertNoWeaverItems()
        self.assertWeaverChecks()


class TestTopEndingRotChecksWeaverOn(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "spinning_top",
        "checks_spread_rot": "true",
        "randomize_weaver": "true"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertWeaverItems()
        self.assertNoWeaverChecks()


class TestTopEndingRotChecksWeaverOff(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "spinning_top",
        "checks_spread_rot": "true",
        "randomize_weaver": "false"
    }

    def test_logic(self):
        self.assertRotChecks()
        self.assertNoWeaverItems()
        self.assertNoWeaverChecks()


class TestTopEndingNoRotChecksWeaverOn(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "spinning_top",
        "checks_spread_rot": "false",
        "randomize_weaver": "true"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertWeaverItems()
        self.assertNoWeaverChecks()


class TestTopEndingNoRotChecksWeaverOff(RotWeaverTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "which_victory_condition": "spinning_top",
        "checks_spread_rot": "false",
        "randomize_weaver": "false"
    }

    def test_logic(self):
        self.assertNoRotChecks()
        self.assertNoWeaverItems()
        self.assertNoWeaverChecks()