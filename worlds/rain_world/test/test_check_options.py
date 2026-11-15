from BaseClasses import CollectionState
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


class TestChecksSubmergedLongerCycles(RainWorldTestBase):
    options = {"checks_submerged": "all_slugcats", "difficulty_submerged": "longer_cycles",
               "is_msc_enabled": True, "which_campaign": "Rivulet", "which_victory_conditon": "story"}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertIn("Submerged Superstructure", regions)
        self.assertIn("Shoreline near gate to Submerged", regions)
        self.assertAccessDependency(["Access-MS"],[["Longer Cycles"]], True)


class TestChecksMetropolisAllSlugcats(RainWorldTestBase):
    options = {"checks_metropolis": "all_slugcats", "is_msc_enabled": True, "which_campaign": "survivor"}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertIn("Metropolis", regions)


class TestChecksMetropolisExpJump(RainWorldTestBase):
    options = {"checks_metropolis": "only_explosive_jump", "is_msc_enabled": True, "which_campaign": "survivor",
               "expedition_perks": ["Explosive Jump Perk"]}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertIn("Metropolis", regions)
        self.assertAccessDependency(["Access-LC"], [["Explosive Jump Perk"]], True)


class TestChecksMetropolisExpJumpArty(RainWorldTestBase):
    options = {"checks_metropolis": "only_explosive_jump", "is_msc_enabled": True, "which_campaign": "artificer",
               "expedition_perks": ["Explosive Jump Perk"]}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertIn("Metropolis", regions)
        # Assert that Metropolis can be reached without the Explosive Jump Perk (because Arty has it innately)
        state = CollectionState(self.multiworld)
        self.collect_all_but("Explosive Jump Perk", state)
        self.assertTrue(state.can_reach("Access-LC", "Location", self.player))


class TestChecksMetropolisOnlyArty(RainWorldTestBase):
    options = {"checks_metropolis": "only_artificer", "is_msc_enabled": True, "which_campaign": "survivor"}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertNotIn("Metropolis", regions)


class TestChecksMetropolisOnlyArtyArty(RainWorldTestBase):
    options = {"checks_metropolis": "only_artificer", "is_msc_enabled": True, "which_campaign": "artificer"}

    def test_check_generation(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertIn("Metropolis", regions)