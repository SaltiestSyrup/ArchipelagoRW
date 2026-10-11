from .bases import RainWorldTestBase

if RUN_GENERAL_AP_UNITTESTS := False:
    # Simply importing this runs the tests.
    from .bases import RainWorldGeneralTestBase

# Ensure rotted regions don't generate at all if the option is off
class TestWatcherRotRegionsOff(RainWorldTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "logic_rotted_generation": "none"
    }

    def test_regions_populated(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertNotIn("Crumbling Fringes", regions)
        self.assertNotIn("Corrupted Factories", regions)
        self.assertNotIn("Decaying Tunnels", regions)
        self.assertNotIn("Infested Wastes", regions)
        self.assertIn("Outer Rim", regions)


# Same for passthrough. The regions should not be generated but logic should allow "direct" bad warping to Outer Rim.
class TestWatcherRotRegionsPassthrough(RainWorldTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "logic_rotted_generation": "passthrough"
    }

    def test_regions_populated(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        self.assertNotIn("Crumbling Fringes", regions)
        self.assertNotIn("Corrupted Factories", regions)
        self.assertNotIn("Decaying Tunnels", regions)
        self.assertNotIn("Infested Wastes", regions)
        self.assertIn("Outer Rim", regions)


# Ensure that rotted region checks *are* generated when option is set to full
class TestWatcherRotRegionsFull(RainWorldTestBase):
    options = {
        "is_watcher_enabled": True,
        "which_campaign": "watcher",
        "logic_rotted_generation": "full"
    }

    def test_regions_populated(self):
        regions = [region.name for region in self.multiworld.get_regions(self.player)]
        rot_locs = [
            loc.name for loc in self.multiworld.get_locations(self.player)
            if loc.name.startswith(
                ("Crumbling Fringes - ",
                 "Corrupted Factories - ",
                 "Decaying Tunnels -",
                 "Infested Wastes -"))
        ]
        self.assertIn("Crumbling Fringes", regions)
        self.assertIn("Corrupted Factories", regions)
        self.assertIn("Decaying Tunnels", regions)
        self.assertIn("Infested Wastes", regions)
        self.assertIn("Outer Rim", regions)
        self.assertTrue(any(rot_locs))