# Rain World player settings

The meanings and implications of the more nuanced player settings are discussed here.

### Extra karma cap increases
How many extra karma cap items are placed into the pool.
When set to `0`, there are exactly enough karma items to raise max karma to 10,
regardless of the selected victory condition.

### Passage progress without Survivor
`Passage progress without Survivor` (PPwS) is a setting in the Rain World Remix settings
which affects when The Dragon Slayer, The Friend, and The Wanderer can be earned.
Enabling PPwS makes it possible to earn these passages without first earning The Survivor.

The Randomizer mod will override the behavior in-game to match your player YAML setting.

### Victory condition
The default victory condition, ascension, logically requires raising max karma to 10
(which requires 8 karma items) and accessing Subterranean (or, for Saint, Rubicon).
The alternate victory condition varies by slugcat, and is only applicable if MSC is enabled.
Each victory condition requires certain items that are placed into the item pool,
as well as certain additional actions that must be taken to actually reach the ending:

| Slugcat          | Items                                                                                             | Actions                                                                                          |
|------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Monk or Survivor |                                                                                                   | - Reach Journey's End (Outer Expanse)                                                            |
| Gourmand         | - Mark of Communication                                                                           | - Meet Five Pebbles to unlock the OE gate<br/>- Reach Journey's End (Outer Expanse)              |
| Artificer        | - Mark of Communication<br/>- Citizen ID drone                                                    | - Kill the chieftain scavenger in Metropolis                                                     |
| Rivulet          | - Increased cycle duration (unless **Late Submerged** setting is disabled)<br/>- Rarefaction cell | - Install the rarefaction cell in Submerged Superstructure<br/>- Reunite with Looks the the Moon |
| Spearmaster      | - Mark of Communication<br/>- Spearmaster's pearl<br/>- Moon's message                            | - Deliver the pearl to Communications Array                                                      |

Hunter, Saint, and Sofanthiel do not have an alternate victory condition.
