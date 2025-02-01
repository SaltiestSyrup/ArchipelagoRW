from glob import glob
from os.path import join
import re

# Location of the StreamingAssets folder.
GAME_FOLDER = r"C:\Program Files (x86)\Steam\steamapps\common\Rain World\RainWorld_Data\StreamingAssets"
ALL_SCUGS = {"Yellow", "White", "Red", "Gourmand", "Artificer", "Rivulet", "Spear", "Saint", "Inv"}

data = {}

world_fps = glob(join(f'{GAME_FOLDER}', 'world', '*', 'world_*.txt'))

for fp in world_fps:
    with open(fp) as f:
        in_creatures_block = False
        for line in f:
            if line.startswith("CREATURES"):
                in_creatures_block = True
            elif in_creatures_block:

                scugs = set(ALL_SCUGS)

                if line.startswith("(X-"):  # there is a blacklist
                    scugs = ALL_SCUGS - set(line.split(")")[0][3:].split(","))

                elif line.startswith("("):  # whitelist
                    scugs = line.split(")")[0][1:].split(",")



                # Lineage with blacklist
                if match := re.match(r"\((.+)\)LINEAGE ?: ?\S+ ?: ?\d+ ?: ?(.+)", line):
                    blacklist = match.group(1)[2:].split(',')
                    creatures = match.group(2).split(',')
