# Rain World

## Where is the options page?

The [player options page for this game](../player-options) contains all the options you need to configure and export a
config file.

## What is the win condition?

Currently, the only goal is ascension.
Logically, this requires that you raise max karma to 10 and gain access to Subterranean.
The win condition is met once you enter the Void Sea itself.

(Technically, you could Guardian skip.  But that's boring.)

## What does randomization do to this game?

Randomization initially sets max karma to 1.
Items are required to raise max karma.

Randomization makes it necessary to obtain a "key" before entering a region
(similarly to the citizen ID drone that allows Artificer into Metropolis).

Currently, randomization assumes you are playing Survivor's campaign.

## Is the Archipelago mod compatible with other mods or DLC?

- **More Slugcats Expansion** (Downpour): (UNIMPLEMENTED)
(Currently, MSC is *required*.  This will change.)
Tokens, regions, and passages added are fully supported.
**Make sure you set the DLC setting correctly in your YAML!**

- **Room Randomizer**: Partial.
As long as Room Randomizer is set to ensure that all gates are accessible,
the game should remain logically completable.

- **Enemy Randomizer**: Minor incompatibility.
Certain checks, such as _The Dragon Slayer_ and the food quest,
assume that certain creatures will appear in certain regions.
Disabling these checks entirely is reccomended if using Enemy Randomizer.

- **Expedition** (Downpour): Unsupported.
Archipelago mode is not designed to work with Expedition mode.
Just having Expedition enabled is fine, though.

## What checks (locations) are added to the pool?

Randomization adds the following checks to the pool:
- **Unlock tokens** (the small holograms on stalks which normally unlock things for Arena or Story):
While the Archipelago mod is connected, these tokens are collectable
even if you've already collected them on the current save file.
Collecting them while connected won't affect your unlock status.

- **Colored pearls**:
Picking up a colored pearl for the first time is a check.
Though the Mark is required for the pearls to make progress towards to The Scholar,
it is not necessary for the checks.

- **Echoes**
Each Echo is its own check.
You do not need the Mark of Communication to check an Echo.
However, having the Mark will allow the Echo to impart a (partial) item hint.

- **Passages**
Completing a Passage is a check.
Note that which Passages are logically possible depends on
whether you enabled `Passage progress without Survivor` in the YAML.
_The Wanderer_ additionally awards a check for each pip (each region hibernated in).

- **Food quest**
If enabled, every point toward the food quest is a check.
The food quest can be made to appear even if not playing Gourmand's campaign.

## What items are added to the pool?

### Progression
Randomization adds the following _progression items_ to the pool:
- Karma cap increase (at least 8)
- "Keys" for each region (except the starting region)
- (UNIMPLEMENTED) The Mark of Communication

### Filler
Randomization adds the following _filler items_ to the pool:
- (UNIMPLEMENTED) A Passage token (for fast travel) for each Passage
- (UNIMPLEMENTED) Several physical objects, such as rocks, spears, grenades, singularity bombs,
vulture masks, white (non-unique) pearls, and batflies.
- (UNIMPLEMENTED) Direct increase to food
- (UNIMPLEMENTED) Direct increase to karma
- (UNIMPLEMENTED) Karma flower reinforcement

### Traps
Randomization adds the following _trap items_ to the pool.
Although they are "traps," many of them can be exploited for personal gain
(or are neutral in the first place).
The only thing that all traps have in common is that they affect the game world instantly.
- (UNIMPLEMENTED) **Stun**: Slugcat is briefly stunned.
- (UNIMPLEMENTED) **Flood**: the current room rapidly fills with water.
The water drains after some time or after the cycle ends.
- (UNIMPLEMENTED) **Creature**: a dangerous creature spawns in an adjacent room.
This may be a Red Lizard, Red Centipede, Spitter Spider, any type of Vulture, or an Elite Scavenger.
The creature is immediately aware of Slugcat's position.
- (UNIMPLEMENTED) **Timer**: the current cycle timer is shortened.
- (UNIMPLEMENTED) **Rain**: rain starts and quickly becomes deadly to anything directly exposed.
The rain ends after some time.
- (UNIMPLEMENTED) **Gravity**: Slugcat's personal gravity is reduced, possibly to zero.
Their gravity returns to normal after some time.
- (UNIMPLEMENTED) **Zoomies**: Slugcat and/or creatures around them suddenly start moving much faster.
The effect wears off after entering a pipe.
- (UNIMPLEMENTED) **Fog**: a thick fog obscures view.  The fog wears off after some time.
- (UNIMPLEMENTED) **Darkness**: the world is suddenly enveloped in darkness like that of the Shaded Citadel.
The light returns after some time.
- (UNIMPLEMENTED) **Blizzard**: a severe blizzard suddenly starts.
Exposed creatures may be pushed around by the wind and suffer hypothermia.
The blizzard ends after a long time.
- (UNIMPLEMENTED) **Warp**: Slugcat is suddenly warped to another room in the current region.
- (UNIMPLEMENTED) **Kill squad**: a Scavenger kill squad is sent after Slugcat.
- (UNIMPLEMENTED) **Alarm**: every creature in the region is made aware of Slugcat's position.

