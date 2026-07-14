from rule_builder.options import OptionFilter
from rule_builder.rules import Has, True_, False_
from worlds.rain_world.options import WhichCampaign, DifficultyGlow, ChecksSubmerged, ExpeditionPerks

survivor = True_() & OptionFilter(WhichCampaign, WhichCampaign.option_survivor)
monk = True_() & OptionFilter(WhichCampaign, WhichCampaign.option_monk)
hunter = True_() & OptionFilter(WhichCampaign, WhichCampaign.option_hunter)
gourmand = True_() & OptionFilter(WhichCampaign, WhichCampaign.option_gourmand)
artificer = True_() & OptionFilter(WhichCampaign, WhichCampaign.option_artificer)
rivulet = True_() & OptionFilter(WhichCampaign, WhichCampaign.option_rivulet)
spearmaster = True_() & OptionFilter(WhichCampaign, WhichCampaign.option_spearmaster)
saint = True_() & OptionFilter(WhichCampaign, WhichCampaign.option_saint)

can_explosive_jump = Has("Explosive Jump Perk") | artificer
is_aquatic = Has("Aquatic Perk") | rivulet
glow_logic = [OptionFilter(DifficultyGlow, DifficultyGlow.option_true)]
submerged_should_populate = ((True_() & OptionFilter(ChecksSubmerged, 2))
                             | ((False_()
                                 | OptionFilter(WhichCampaign, WhichCampaign.option_rivulet)
                                 | OptionFilter(ExpeditionPerks, "Aquatic Perk", operator="contains"))
                                & OptionFilter(ChecksSubmerged, 1)))