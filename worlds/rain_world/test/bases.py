from test.bases import WorldTestBase
from test.general.test_items import TestBase as TestItems
from test.general.test_locations import TestBase as TestLocations
from test.general.test_reachability import TestBase as TestReachability


class RainWorldTestBase(WorldTestBase):
    game = "Rain World"


class RainWorldGeneralTestBase(TestReachability, TestItems, TestLocations):
    game = "Rain World"
