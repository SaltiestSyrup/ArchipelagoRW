import re
from os import path
from glob import glob

from generate_classes import Spawner
from generate_methods import parse_placed_objects, splitstrip, setdefaultchain as sdc

########################################################################################################################
ROOT_FP = "D:/RW files/1.9.15.3"
re_3 = re.compile(r'\b(\w+)><([\d.]+)><([\d.]+)><([^,]*)')
re_room_settings_filename = re_rsf = re.compile(r'((\S+)_\S+)_settings(?:-(\S+))?\.txt')
OBJECT_WHITELIST = [
    # food quest
    "SlimeMold", "DangleFruit", "Mushroom", "WaterNut", "JellyFish", "GlowWeed", "Hazer", "LillyPuck",
    "DandelionPeach", "GooieDuck",
    # physical checks
    "BlueToken", "GreenToken", "RedToken", "GoldToken", "WhiteToken", "DevToken", "UniqueDataPearl",
    "KarmaFlower",  # artificer echo logic
    "SeedCob",  # for The Monk
    "BubbleGrass",  # for waterway traversal
]
SHINY_LIST = ["BlueToken", "GreenToken", "RedToken", "GoldToken", "WhiteToken", "UniqueDataPearl"]

########################################################################################################################
data = {}
# (root)
#   dlcstate ("Vanilla" | "MSC")
#     region code
#       room name
#         "whitelist": set of whitelisted scugs
#         "blacklist": set of blacklisted scugs
#         "alted": set of scugs with alternate settings files
#         "tags": set of room tags
#         "spawners"
#           den type ("normal" | "precycle" | "lineage_start" | "lineage_mid" | "lineage_end")
#             creature type: set of whitelisted scugs
#         "shinies"
#           shiny name
#             "filter": set of filtered scugs
#             "whitelist": set of whitelisted scugs
#             "kind": token/pearl type
#         "objects"
#           object type
#             "filter": set of filtered scugs
#             "whitelist": set of whitelisted scugs


########################################################################################################################
scugs_vanilla = {"Yellow", "White", "Red"}
scugs_msc = {"Yellow", "White", "Red", "Gourmand", "Artificer", "Rivulet", "Spear", "Saint", "Inv"}

for dlcstate, all_scugs in zip(("Vanilla", "MSC"), (scugs_vanilla, scugs_msc)):
    data[dlcstate] = {}

    for fp in glob(path.join(ROOT_FP, dlcstate, 'world', '*', 'world_*.txt')):
        region = path.basename(fp).split("_")[1].split(".")[0].upper()
        region_data = data[dlcstate].setdefault(region, {})

        with open(fp) as f:
            block = None

            for line in f:
                line = line.strip()

                if line.startswith("ROOMS"):
                    block = "ROOMS"
                elif line.startswith("END ROOMS"):
                    block = None
                elif line.startswith("CONDITIONAL LINKS"):
                    block = "LINKS"
                elif line.startswith("END CONDITIONAL LINKS"):
                    block = None
                elif line.startswith("CREATURES"):
                    block = "CREATURES"
                elif line.startswith("END CREATURES"):
                    block = None
                elif block is None or line.startswith("//") or len(line) == 0:
                    continue

########################################################################################################################
                elif block == "LINKS":
                    parts = splitstrip(line, ":")

                    match parts:
                        case [scugname, "EXCLUSIVEROOM", roomname]:
                            sdc(region_data, {scugname}, roomname.upper(), "whitelist")

                        case [scugname, "HIDEROOM", roomname]:
                            sdc(region_data, {scugname}, roomname.upper(), "blacklist")

                        case [scugname, sourcename, old_destname, new_destname]:
                            pass

                        case _:
                            raise ValueError(f"Unrecognized conditional link: '{line}'")

########################################################################################################################
                elif block == "ROOMS":
                    parts = splitstrip(line, ":")

                    match parts:
                        case [roomname, connections, tags]:
                            sdc(region_data, {a.upper() for a in splitstrip(tags, ",")}, roomname.upper(), "tags")

                        case [roomname, connections]:
                            sdc(region_data, None, roomname.upper())

                        case _:
                            raise ValueError(f"Unrecognized room declaration: '{line}'")

########################################################################################################################
                elif block == "CREATURES":
                    scugstring = None
                    if line.startswith('('):
                        scugstring, line = line[1:].split(')', 1)

                    parts = line.split(" : ")

                    if parts[0] == "LINEAGE":
                        room, den_number, critstring = parts[1:]
                        spawner = Spawner(scugstring, room, den_number, critstring, True, dlcstate == "Vanilla")

                        for i, crit in enumerate(spawner.crits):
                            if crit.type != "NONE":
                                dentype = "lineage_start" if i == 0 else ("lineage_end" if i == len(spawner.crits) - 1 else "lineage_mid")
                                sdc(region_data, set(spawner.scugs), room.upper(), "spawners", dentype, crit.type)

                    else:
                        room, critstrings = parts
                        for critstring in critstrings.split(', '):
                            den_number, critstring = critstring.split('-', 1)
                            spawner = Spawner(scugstring, room, den_number, critstring, False, dlcstate == "Vanilla")

                            for crit in spawner.crits:
                                if crit.type != "NONE":
                                    dentype = "precycle" if "PreCycle" in crit.attributes else "normal"
                                    sdc(region_data, set(spawner.scugs), room.upper(), "spawners", dentype, crit.type)

########################################################################################################################
    normal_settings_files = set(glob(path.join(ROOT_FP, dlcstate, 'world', '??-rooms', '??_*_settings.txt')))
    all_settings_files = set(glob(path.join(ROOT_FP, dlcstate, 'world', '??-rooms', '??_*_settings*')))

    for fp in list(normal_settings_files) + list(all_settings_files - normal_settings_files):
        if match := re_rsf.match(path.basename(fp)):
            room, region, scug = match.groups()
            room, region, scug = room.upper(), region.upper(), scug.title() if scug else None
        else:
            # settings file with an invalid name
            continue

        try:
            room_data = data[dlcstate][region][room]
        except KeyError:
            # if there isn't a dict for the room already, then it's not in a world file
            # and therefore not connected to the rest of the region - such as arti dream rooms in GW
            continue

        room_objects = parse_placed_objects(fp)
        r_data = {'shinies': {}, 'objects': {}}

        for obj in room_objects:
            custom_data = obj["data"]
            blacklist: set = obj["filtered"]

            if obj['type'] in SHINY_LIST:
                name = custom_data[4 if "Pearl" in obj['type'] else 5]
                if "Token" in obj['type']:
                    blacklist = set(custom_data[6].split("|")).union(blacklist or set())

                r_data["shinies"][name] = {"filter": blacklist, "kind": obj["type"]}

            elif obj['type'] in OBJECT_WHITELIST:
                try:
                    s = r_data['objects'][obj['type']]['filter']
                    r_data['objects'][obj['type']]['filter'] = s.intersection(blacklist or set())
                except KeyError:
                    r_data['objects'][obj['type']] = {"filter": blacklist or set()}

########################################################################################################################
        if scug is None:
            room_data.update(r_data)
        else:
            sdc(room_data, {scug}, "alted")

            for shiny_name, shiny_data in r_data['shinies'].items():
                if scug not in shiny_data["filter"]:
                    sdc(room_data, shiny_data["kind"], "shinies", shiny_name, "kind")
                    sdc(room_data, {scug}, "shinies", shiny_name, "whitelist")

            for object_name, object_data in r_data['objects'].items():
                if scug not in object_data["filter"]:
                    sdc(room_data, {scug}, "objects", object_name, "whitelist")

########################################################################################################################

with open("data.py", "w") as f:
    f.write(f'data = {data}\n')

print('script ending normally')
