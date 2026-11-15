from ..options import RainWorldOptions
from ..game_data import static_data

item_to_table_id = [
    'Rock',
    'Flashbang',
    'VultureMask',
    'PuffBall',
    'Lantern',
    'Mushroom',
    'FirecrackerPlant',
    'FlyLure',
    'ScavengerBomb',
    'SporePlant',
    'BubbleGrass',
    'NeedleEgg',
    'KarmaFlower',
    'SingularityBomb',
    'Overseer',
    'Pearl',
    'SSOracleSwarmer',
    'FireEgg',
    'DangleFruit',
    'WaterNut',
    'SlimeMold',
    'JellyFish',
    'EggBugEgg',
    'Seed',
    'GooieDuck',
    'LillyPuck',
    'GlowWeed',
    'DandelionPeach',
    'Fly',
    'SmallCentipede',
    'VultureGrub',
    'SmallNeedleWorm',
    'DeadHazer',
    'TubeWorm',
    'Snail',
    '',
    ''
]

craft_table = [
    [36, 4, 15, 9, 1, 3, 8, 6, 15, 3, 6, 28, 8, 17, 15, 36, 14, 8, 1, 21, 4, 25, 11, 28, 9, 4, 4, 3, 5, 9, 4, 3, 25],
    [4, 36, 15, 5, 26, 3, 4, 6, 4, 6, 6, 30, 4, 17, 15, 36, 14, 8, 20, 21, 4, 25, 9, 30, 4, 4, 4, 9, 5, 9, 4, 3, 26],
    [15, 15, 36, 15, 15, 15, 15, 15, 15, 15, 15, 30, 15, 17, 15, 36, 14, 8, 15, 15, 15, 15, 15, 30, 15, 15, 15, 15, 23, 23, 23, 23, 23],
    [9, 5, 15, 36, 5, 24, 8, 5, 5, 24, 24, 5, 29, 17, 15, 36, 14, 8, 5, 24, 5, 24, 24, 29, 5, 5, 24, 24, 5, 9, 6, 5, 10],
    [1, 26, 15, 5, 36, 3, 8, 6, 15, 6, 26, 30, 15, 17, 15, 36, 14, 8, 1, 26, 5, 26, 11, 30, 25, 26, 25, 26, 5, 6, 15, 11, 34],
    [3, 3, 15, 24, 3, 36, 29, 28, 9, 24, 32, 29, 11, 29, 15, 36, 14, 8, 24, 11, 31, 24, 24, 29, 3, 24, 24, 24, 24, 24, 24, 3, 10],
    [8, 4, 15, 8, 8, 29, 36, 9, 4, 8, 34, 29, 8, 17, 15, 36, 14, 8, 9, 10, 4, 7, 9, 29, 9, 9, 9, 9, 9, 9, 9, 9, 21],
    [6, 6, 15, 5, 6, 28, 9, 36, 6, 3, 5, 28, 23, 17, 15, 36, 14, 8, 24, 10, 6, 10, 24, 28, 5, 32, 29, 28, 5, 5, 5, 5, 10],
    [15, 4, 15, 5, 15, 9, 4, 6, 36, 3, 3, 29, 17, 17, 15, 36, 14, 13, 6, 34, 4, 34, 6, 29, 3, 9, 4, 3, 6, 6, 6, 3, 1],
    [3, 6, 15, 24, 6, 24, 8, 3, 3, 36, 3, 33, 8, 17, 15, 36, 14, 8, 5, 32, 6, 32, 3, 33, 3, 21, 21, 5, 7, 33, 1, 3, 21],
    [6, 6, 15, 24, 26, 32, 34, 5, 3, 3, 36, 32, 23, 17, 15, 36, 14, 8, 25, 25, 5, 25, 5, 32, 3, 21, 25, 26, 7, 21, 26, 5, 26],
    [28, 30, 30, 5, 30, 29, 29, 28, 29, 33, 32, 36, 14, 30, 15, 36, 14, 30, 28, 32, 29, 34, 31, 31, 33, 32, 32, 31, 23, 23, 23, 23, 23],
    [8, 4, 15, 29, 15, 11, 8, 23, 17, 8, 23, 14, 36, 17, 16, 36, 14, 13, 23, 23, 23, 11, 11, 14, 23, 23, 23, 23, 7, 3, 2, 11, 10],
    [17, 17, 17, 17, 17, 29, 17, 17, 17, 17, 17, 30, 17, 36, 15, 36, 14, 12, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17],
    [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 16, 15, 36, 36, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15],
    [36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 14, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36],
    [14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 14, 15, 14, 36, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 35]
]

# This function credited to M-Cool
def craftable_items(inputs : list[bool], max_steps: int = 32):
    # The input (inputs) and Output of the function is a list of 37-bool variables, where TRUE means that that item can be foraged already (input) and/or crafted (output)
    # Hard-coded crafting recipies. Source: https://rainworld.miraheze.org/wiki/Crafting#Crafting_By_Ingredients
    # The crafting table is a diagonal-symmetrical 32x32, for our use we can use only the top half. Items 0-32 are their inputs, while items 33-36 are some extra outputs

    i = 0
    total_items = []
    new_craftables = list(inputs)  # We separate the original variable in case we want to use it later (XOR to notice changes for example)

    while i < max_steps and total_items != new_craftables:  # Main Loop until the "recipe becomes too complex" (go over step value, ideally it would be between 3 and 10) or it stops gaining new outputs
        i += 1
        total_items = list(new_craftables)  # Updates old list with new values without linking both

        cur_inputs = []
        for j in range(0, 33):  # Transforms the bool list into a number list with the item IDs that are currently "True" (valid inputs). Stops at 32 (Hazer) since 33-36 are output-only items
            if total_items[j]:
                cur_inputs.append(j)

        for x in cur_inputs:  # Check each column (left to right)
            for y in range(min(x, 17)): # Check each row from the current column. Skip the bottom of the diagonal (symmetrical cells) and the bottom half of the table (repeated and/or +1 food)
                ret = craft_table[y][x]  # Check the table (y = Row [0-16] + x = Column [0-32])
                new_craftables[ret] = True  # Set to TRUE all items that any combination of current inputs (included crafted in previous loops) can craft

    return total_items

# def precompute_regions(options: RainWorldOptions):
#     for reg, reg_data in static_data[options.dlcstate].items():
#         pass
#