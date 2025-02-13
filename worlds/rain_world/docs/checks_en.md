# Locations in Rain World Randomizer

Following is a summary of all randomized locations (checks)
along with the items that would normally be at those locations.

## Physical checks
There are several *physical checks* available in most regions.
These come in the form of tokens -
the small holograms on stalks which unlock things for Arena or Safari -
and the unique colored pearls, which count as checks when broguht to a shelter for the first time.
Not all tokens and pearls are available to every slugcat,
even if they exist in a region that every slugcat can visit.

For Spearmaster, broadcast tokens are also checks.
Although some braodcast tokens give different chatlogs before and after meeting Five Pebbles,
they are not considered two separate checks.

## Echoes
Visiting an echo is a check, and the karma cap increases they would normally give are placed in the item pool.
By default, echo apperance follows the same rules as the unrandomized game:
- Saint can always see echoes, regardless of current and max karma.
- For other slugcats:
  - If max karma is 7 or more, current karma must be at least 6.
  - If max karma is 5, current karma must be 5.
  - If max karma is less than 5:
    - Artificer may see echoes if current karma equals max karma
    and karma flower reinforcement is active.
    - Other slugcats cannot see echoes.

Note that current karma is not logically constrained,
so echo checks are considered accessible as soon as max karma reaches 5
or, for Artificer, as soon as a karma flower is accessible.

## Unique checks
There are several unique checks, mostly associated with the iterators:
- Eating a neuron.  The glow is placed in the item pool.
- Gifting a neuron to Looks to the Moon as Monk, Survivor, or Gourmand.
- Meeting Five Pebbles.  The Mark of Communication (and, in Spearmaster's case, their embedded pearl)
is placed in the item pool.
- Meeting Looks to the Moon.
- Reviving Looks to the Moon with the green neuron as Hunter.
- Removing the rarefaction cell from The Rot as Rivulet.  The rarefaction cell is placed in the item pool.
- Ascending Looks to the Moon and Five Pebbles as Saint.

## Passages
Completing a passage is a check, and the passage tokens (which allow for fast-travel)
that they would normally give are placed in the item pool.
The logical requirement for each passage varies.
There are four passages that may be earned before The Survivor is earned:

| Passage           | Eligibility                                 | Requirements                                                                                 |
|-------------------|---------------------------------------------|----------------------------------------------------------------------------------------------|
| The Martyr        | Any; MSC enabled                            | None                                                                                         |
| The Mother        | Survivor, Hunter, or Gourmand; MSC enabled  | Access to a region which spawns slugpups normally<sup>b</sup>                                |
| The Pilgrim       | Any; MSC enabled                            | Access to all eligible echoes                                                                |
| The Survivor      | Any                                         | Max karma at least 5                                                                         |

There are three passages that may be earned before The Survivor,
but if and only if the `Passage progress without survivor` setting is enabled:

| Passage           | Eligibility                                 | Requirements                                                                            |
|-------------------|---------------------------------------------|-----------------------------------------------------------------------------------------|
| The Dragon Slayer | Any                                         | Access to six eligibile lizard types<sup>c</sup>                                        |
| The Friend        | Any                                         | Access to one lizard                                                                    |
| The Wanderer      | Any                                         | Access to every story region for the given slugcat; each individual pip is also a check |

The remaining seven passages can only be earned after The Survivor has been earned:

| Passage       | Eligibility                                 | Requirements                                                                                                                         |
|---------------|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| The Chieftain | Not Artificer                               | Access to a Scavenger (or Scavenger Outpost/Toll)<sup>a</sup>                                                                        |
| The Hunter    | Not Saint                                   | Access to 3<sup>a</sup> types of meat                                                                                                |
| The Monk      | Any                                         | Access to 3<sup>a</sup> types of non-meat foods                                                                                      |
| The Nomad     | Any; MSC enabled                            | Access to 5<sup>a</sup> different regions                                                                                            |  
| The Outlaw    | Not Saint                                   | Access to 5<sup>a</sup> eligible creatures                                                                                           |
| The Saint     | Any                                         | None                                                                                                                                 |
| The Scholar   | Not Monk (unless MSC is enabled); Not Saint | - The Mark of Communication<br/>- Access to three colored pearls<br/>- For Monk, Survivor, and Gourmand: access to Looks to the Moon |

- <sup>a</sup> This is controlled by the player YAML settings.
- <sup>b</sup> "Normal spawning" of slugpups does not occur in Five Pebbles or Submerged Superstructure.
- <sup>c</sup> Without MSC, this requires Blue, Pink, Green, Yellow, Black, and White Lizards.
MSC allows Red, Cyan, Strawberry, and Caramel Lizards to count as well.

## Food quest
If MSC is enabled, each item of the food quest is a check when completed.
While randomized, the food quest appears for slugcats other than Gourmand.
Each slugcat has the ability to fulfill part of the food quest,
but only Hunter and Gourmand can complete it logically.

| Food                                                                                                                           | Monk<br/>Survivor | Rivulet | Hunter<br/>Gourmand | Artificer    | Spearmaster | Saint |
|--------------------------------------------------------------------------------------------------------------------------------|-------------------|---------|---------------------|--------------|-------------|-------|
| Neuron Fly                                                                                                                     | ✔                 | ✔       | ✔                   | ✔            | ✔           | ✔     |
| Glow Weed                                                                                                                      | ✔                 | ✔       | ✔                   | <sup>a</sup> |             | ✔     |
| Blue Fruit<br/>Bubble Fruit<br/>Dandelion Peach<br/>Gooieduck<br/>Lilypuck<br/>Slime Mold                                      | ✔                 | ✔       | ✔                   | ✔            |             | ✔     |
| Batfly<br/>Hazer                                                                                                               | ✔                 | ✔       | ✔                   | ✔            | ✔           |       |
| Black Lizard<br/>Salamander / Eel Lizard<br/>Yellow Lizard<br/>Cyan Lizard<br/>Jetfish<br/>Snail<br/>Eggbug<br/>Grappling Worm |                   |         | ✔                   | ✔            | ✔           |       |
| Aquapede / Red Centipede<br/>Centiwing                                                                                         | ✔<sup>b</sup>     | ✔       | ✔                   | ✔            | ✔           |       |
| Jellyfish                                                                                                                      | ✔                 | ✔       | ✔                   | ✔            |             |       |

- <sup>a</sup> Artificer does not find Glow Weed in their worldstate,
but may receive it as a filler item.  This check is not in logic.
- <sup>b</sup> Monk and Survivor can only find Red Centipedes by lineage -
which is not in logic - but Aquapedes are available without lineage.
