"""
Static data summarizing the contents of the game world, such as the locations of creature spawns.
"""

from . import general
from .data import data as static_data
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
