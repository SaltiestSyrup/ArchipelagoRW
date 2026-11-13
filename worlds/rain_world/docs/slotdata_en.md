# Rain World slot data

## Integral
These fields can only contain an integer.

### Boolean
These fields can only be `0` (false) or `1` (true).

| Field                        | Description                                                                   |
|------------------------------|-------------------------------------------------------------------------------|
| `is_msc_enabled`             | Whether More Slugcats Expansion (Downpour) is enabled.                        |
| `is_watcher_enabled`         | Whether The Watcher is enabled.                                               |
| `death_link`                 | Whether the client default Death Link to on.                                  |
| `checks_passages`            | Whether passages are randomized.                                              |
| `randomize_passage_tokens`   | Whether passage token items are in the item pool.                             |
| `checks_sheltersanity`       | Whether shelter checks are in the pool.                                       |
| `checks_flowersanity`        | Whether karma flower checks are in the pool.                                  |
| `checks_devtokens`           | Whether developer commentary token checks are in the pool.                    |
| `checks_foodquest_expanded`  | Whether food quest should use expanded food pool (if enabled)                 |
| `difficulty_chieftain`       | Whether a Scavenger Toll must be accessible for The Chieftain to be in logic. |
| `difficulty_glow`            | Whether The Glow is required for dark places.                                 |
| `difficulty_extreme_threats` | Whether especially difficult creatures should be used in logic.               |
| `spinning_top_keys`          | Whether Spinning Top warps need keys to open.                                 |
| `daemon_keys`                | Whether Daemon warps need keys to open.                                       |
| `sparse_gates`               | Whether the amount of gates in the item pool is minimized.                    |
| `artificer_scavenger_karma`  | Whether Artificer's scavenger karma is randomized.                            |
| `checks_tokens_pearls`       | Currently unused.                                                             |
| `checks_broadcasts`          | Currently unused.                                                             |

### Normal enumeration
These fields can only contain specific integers,
each with a meaning that is not necessarily intrinsic to the number itself.
Cells without a description are not valid values for that setting.

| Field                               | Description                                                       | `0`                      | `1`                 | `2`             | `3`        | `4`                    | `5`           | `6`                             |
|-------------------------------------|-------------------------------------------------------------------|--------------------------|---------------------|-----------------|------------|------------------------|---------------|---------------------------------|
| `which_victory_condition`           | The win condition for the seed.                                   | Ascension / Spinning Top | Story / Prince      | Echoes / Weaver | Food Quest | Watcher True Ending    |               |                                 |
| `which_gate_behavior`               | The requirement for a gate to be unlocked.                        | Key only                 | Key and karma       | Key or karma    | Karma only |                        |               |                                 |
| `checks_foodquest`                  | Whether food quest checks are in the pool.                        | Off                      | Gourmand only       | All slugcats    |            |                        |               |                                 |
| `checks_submerged`                  | Whether Submerged Superstructure checks are generated.            | Off                      | Aquatic only        | All slugcats    |            |                        |               |                                 |
| `difficulty_submerged`              | The condition needed to logically enter Submerged Superstructure. | None                     | Aquatic             | Longer Cycles   |            |                        |               |                                 |
| `difficulty_echo_low_karma`         | The spawn condition for Echoes below Karma 5.                     | Never                    | With flower         | Without flower  | Unaltered  |                        |               |                                 |
| `passage_progress_without_survivor` | Passage progress without Survivor behavior.                       | None                     | Disabled            | Enabled         | Bypassed   |                        |               |                                 |
| `checks_spread_rot`                 | Whether spreading rot should give checks.                         | False                    | Related Ending Only | True            |            |                        |               |                                 |
| `checks_weaver_encounters`          | Whether encountering the Weaver should give checks.               | False                    | Related Ending Only | True            |            |                        |               |                                 |
| `randomize_weaver`                  | Whether the Weaver ability is randomized.                         | False                    | Related Ending Only | True            |            |                        |               |                                 |
| `logic_rotted_generation`           | How the rotted vanilla regions should be generated.               | None                     | Passthrough         | Full            |            |                        |               |                                 |

### Other numeric
These fields can only contain an integer between two limits,
or only specific integers that aren't a normal enumeration.

| Field                            | Description                                                                        | Valid values                          |
|----------------------------------|------------------------------------------------------------------------------------|---------------------------------------|
| `difficulty_hunter`              | Number of accessible foods for The Hunter to be in logic.                          | `1` to `4`                            |
| `difficulty_monk`                | Number of accessible foods for The Monk to be in logic.                            | `1` to `4`                            |
| `difficulty_nomad`               | Number of accessible reigons for The Nomad to be in logic.                         | `3` to `8`                            |
| `difficulty_outlaw`              | Number of accessible creatures for The Outlaw to be in logic.                      | `1` to `8`                            |
| `rotted_region_target`           | How many regions must be rotted to trigger Prince ending.                          | `2` to `21`                           |
| `logic_ripplespace_min_req`      | The lowest that minimum Ripple can be before Ripplespace is considered accessible. | `5` to `9`                            |
| `checks_foodquest_accessibility` | A bitflag indicating which food quest checks are accessible.                       | `0` to `2251799813685248` (2**51 - 1) |

## String
These fields can only contain a string.

| Field             | Description                                              | Valid values                                                                                     |
|-------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| `starting_room`   | The room that the player will start in.                  | The full name of a shelter room, or the empty string for the default starting point.             |
| `which_campaign`  | The name of the slugcat whose campaign is selected.      | `Yellow`, `White`, `Red`, `Gourmand`, `Artificer`, `Rivulet`, `Spear`, `Saint`, `Inv`, `Watcher` |
| `apworld_version` | The version of the APWorld this seed was generated with. |                                                                                                  |

## List
These fields can only contain a list/array.
The values contained within that list are described in the third column.

| Field             | Description                                               | Valid contained values                         |
|-------------------|-----------------------------------------------------------|------------------------------------------------|
| `expediton_perks` | Expedition perks included in the item pool. May be empty. | The direct item names of the expedition perks. |