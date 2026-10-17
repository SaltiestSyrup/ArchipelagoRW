from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, False_, Filtered, Rule
from worlds.rain_world.options import WhichCampaign, DifficultyGlow, ChecksSubmerged, ExpeditionPerks


def perk_in_pool(perk: str) -> OptionFilter:
    return OptionFilter(ExpeditionPerks, perk, operator="contains")

def has_perk(perk: str) -> Rule:
    return Has(perk, options=[perk_in_pool(perk)])

survivor = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_survivor)])
monk = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_monk)])
hunter = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_hunter)])
gourmand = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_gourmand)])
artificer = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_artificer)])
rivulet = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_rivulet)])
spearmaster = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_spearmaster)])
saint = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_saint)])
watcher = Filtered(True_(), options=[OptionFilter(WhichCampaign, WhichCampaign.option_watcher)])

can_explosive_jump = has_perk("Explosive Jump Perk") | artificer
is_aquatic = Has("Aquatic Perk") | rivulet
glow_logic = [OptionFilter(DifficultyGlow, DifficultyGlow.option_true)]
submerged_should_populate = ((OptionFilter(ChecksSubmerged, 2))
                             | ((False_()
                                 | OptionFilter(WhichCampaign, WhichCampaign.option_rivulet)
                                 | perk_in_pool("Aquatic Perk"))
                                & OptionFilter(ChecksSubmerged, 1)))