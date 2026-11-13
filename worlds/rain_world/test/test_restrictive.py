from .bases import RainWorldTestBase

if RUN_GENERAL_AP_UNITTESTS := False:
    # Simply importing this runs the tests.
    from .bases import RainWorldGeneralTestBase

item_options = {
    "which_gate_behavior": "key_and_karma",
    "extra_karma_cap_increases": 15,
    "damage_upgrades": 10,
    "expedition_perks": [
        "Back Spear Perk", 
        "Dual Wielding Perk", 
        "Blast Resistance Perk", 
        "Explosive Parry Perk", 
        "Explosive Jump Perk", 
        "Crafting Perk", 
        "Aquatic Perk", 
        "Agility Perk"
    ]
}

check_options = {
    "checks_passages": False,
    "checks_tokens": False,
    "checks_pearls": False,
    "checks_echoes": False,
    "checks_broadcasts": False,
    "checks_foodquest": False,
    "checks_foodquest_expanded": False,
    "checks_shelters": False,
    "checks_flowers": False,
    "checks_devtokens": False,
}

class TestOnlyTokensMonk(RainWorldTestBase):
    options = {
        "which_campaign": "monk",
        **check_options,
        **item_options,
        "checks_tokens": True
    }

class TestOnlyTokensSurvivor(RainWorldTestBase):
    options = {
        "which_campaign": "survivor",
        **check_options,
         "checks_tokens": True
    }

class TestOnlyTokensHunter(RainWorldTestBase):
    options = {
        "which_campaign": "hunter",
        **check_options,
        "checks_tokens": True
    }

class TestOnlyTokensGourmand(RainWorldTestBase):
    options = {
        "which_campaign": "gourmand",
        "is_msc_enabled": True,
        **check_options,
        **item_options,
        "checks_tokens": True
    }

class TestOnlyTokensArtificer(RainWorldTestBase):
    options = {
        "which_campaign": "artificer",
        "is_msc_enabled": True,
        **check_options,
        **item_options,
        "checks_tokens": True
    }

class TestOnlyTokensRivulet(RainWorldTestBase):
    options = {
        "which_campaign": "rivulet",
        "is_msc_enabled": True,
        **check_options,
        **item_options,
        "checks_tokens": True
    }

class TestOnlyTokensSpearmaster(RainWorldTestBase):
    options = {
        "which_campaign": "spearmaster",
        "is_msc_enabled": True,
        **check_options,
        **item_options,
        "checks_tokens": True
    }

class TestOnlyTokensSaint(RainWorldTestBase):
    options = {
        "which_campaign": "saint",
        "is_msc_enabled": True,
        **check_options,
        **item_options,
        "checks_tokens": True
    }

class TestOnlyTokensInv(RainWorldTestBase):
    options = {
        "which_campaign": "sofanthiel",
        "is_msc_enabled": True,
        **check_options,
        **item_options,
        "checks_tokens": True
    }

class TestOnlyTokensWatcher(RainWorldTestBase):
    options = {
        "which_campaign": "watcher",
        "is_watcher_enabled": True,
        **check_options,
        **item_options,
        "checks_tokens": True
    }
