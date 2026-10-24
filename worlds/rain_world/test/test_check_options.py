from .bases import RainWorldTestBase

if RUN_GENERAL_AP_UNITTESTS := False:
    # Simply importing this runs the tests.
    from .bases import RainWorldGeneralTestBase


class TestPPwSNone(RainWorldTestBase):
    options = {"is_msc_enabled": True, "passage_progress_without_survivor": "none"}

    def test_passages_without_survivor(self):
        self.assertFalse(self.can_reach_region("Early Passages"))
        self.assertFalse(self.can_reach_region("PPwS Passages"))
        self.assertFalse(self.can_reach_region("Late Passages"))

        self.collect([self.get_item_by_name("Karma") for _ in range(4)])

        self.assertTrue(self.can_reach_region("Early Passages"))
        self.assertTrue(self.can_reach_region("PPwS Passages"))
        self.assertTrue(self.can_reach_region("Late Passages"))


class TestPPwSDisabled(RainWorldTestBase):
    options = {"is_msc_enabled": True, "passage_progress_without_survivor": "disabled"}

    def test_passages_without_survivor(self):
        self.assertTrue(self.can_reach_region("Early Passages"))
        self.assertFalse(self.can_reach_region("PPwS Passages"))
        self.assertFalse(self.can_reach_region("Late Passages"))

        self.collect([self.get_item_by_name("Karma") for _ in range(4)])

        self.assertTrue(self.can_reach_region("PPwS Passages"))
        self.assertTrue(self.can_reach_region("Late Passages"))



class TestPPwSEnabled(RainWorldTestBase):
    options = {"is_msc_enabled": True, "passage_progress_without_survivor": "enabled"}

    def test_passages_without_survivor(self):
        self.assertTrue(self.can_reach_region("Early Passages"))
        self.assertTrue(self.can_reach_region("PPwS Passages"))
        self.assertFalse(self.can_reach_region("Late Passages"))

        self.collect([self.get_item_by_name("Karma") for _ in range(4)])

        self.assertTrue(self.can_reach_region("Late Passages"))


class TestPPwSBypassed(RainWorldTestBase):
    options = {"is_msc_enabled": True, "passage_progress_without_survivor": "bypassed"}

    def test_passages_without_survivor(self):
        self.assertTrue(self.can_reach_region("Early Passages"))
        self.assertTrue(self.can_reach_region("PPwS Passages"))
        self.assertTrue(self.can_reach_region("Late Passages"))


class TestChecksSubmergedAquatic(RainWorldTestBase):
    options = {"checks_submerged": "only_aquatic", "is_msc_enabled": True, "expedition_perks": ["Aquatic Perk"]}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertIn("Submerged Superstructure", regions)
        self.assertIn("Shoreline near gate to Submerged", regions)


class TestChecksSubmergedAquaticFail(RainWorldTestBase):
    options = {"checks_submerged": "only_aquatic", "is_msc_enabled": True}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertNotIn("Submerged Superstructure", regions)
        self.assertNotIn("Shoreline near gate to Submerged", regions)


class TestChecksSubmergedOff(RainWorldTestBase):
    options = {"checks_submerged": "off", "is_msc_enabled": True, "which_campaign": "Rivulet"}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertNotIn("Submerged Superstructure", regions)
        self.assertNotIn("Shoreline near gate to Submerged", regions)