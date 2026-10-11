from test.bases import WorldTestBase
from test.general.test_items import TestBase as TestItems
from test.general.test_locations import TestBase as TestLocations
from test.general.test_reachability import TestBase as TestReachability


class RainWorldTestBase(WorldTestBase):
    game = "Rain World"

    def assertRegionsPopulated(self, regions : set[str]):
        actual_regions = [region.name for region in self.multiworld.get_regions(self.player)]
        for r in regions:
            self.assertIn(r, actual_regions)

    def assertRegionsNotPopulated(self, regions : set[str]):
        actual_regions = [region.name for region in self.multiworld.get_regions(self.player)]
        for r in regions:
            self.assertNotIn(r, actual_regions)


class RainWorldGeneralTestBase(TestReachability, TestItems, TestLocations):
    game = "Rain World"
