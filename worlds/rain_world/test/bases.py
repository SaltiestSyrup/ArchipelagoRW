from test.bases import WorldTestBase

RUN_GENERAL_AP_UNITTESTS = False

if RUN_GENERAL_AP_UNITTESTS:
    # Simply importing these runs the tests.
    from test.general.test_items import TestBase as TestItems
    from test.general.test_locations import TestBase as TestLocations
    from test.general.test_reachability import TestBase as TestReachability


class RainWorldTestBase(WorldTestBase):
    game = "Rain World"
