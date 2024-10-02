# Rain World Setup Guide

## 1. Create a YAML settings file
### What is a YAML and why do I need one?
You can see the [basic multiworld setup guide](/tutorial/Archipelago/setup/en) here on the Archipelago website to learn 
about why Archipelago uses YAML files and what they're for.

### Where do I get a YAML?
You can use the [game options page](/games/Risk%20of%20Rain%202/player-options) here on the Archipelago 
website to generate a YAML using a graphical interface.
You can also edit this file directly if you understand the format.

## 2. Enable the Archipelago mod

### Option A: Install via Steam Workshop

Subscribe to the Archipelago mod on the Workshop (LINK TODO),
enable the mod in the Remix menu, then restart Rain World.

The mod can be automatically updated through the Workshop.

### Option B: Install as a local mod

Download the mod folder from the GitHub repository (LINK TODO)
and place it in `Rain World\RainWorld_Data\StreamingAssets\mods`.
Enable the mod in the Remix menu, then restart Rain World.

The mod will not be automatically updated.
Updates will require you to re-download from the GitHub repository.

## 3. Test that the mod is working

There are three things that should always happen when the mod is working as intended:
1. Clicking on Archipelago in the Remix menu should open its Remix interface
(as opposed to warning that the mod does not define a Remix interface).
2. Opening the Story select menu should show the interface for connecting to an Archipelago room.
3. `Rain World\BepInEx\LogOutput.log` should contain a line that reads
`[Debug  :Archipelago] Initialization completed without exception`.

## 4. Set Remix settings

There are two Rain World Remix settings that affect logic and may be specified in your YAML:
`Passage progress without Survivor` (enabled by default in the YAML)
and `Disable all karma requirements` (disabled by default).
They must also be set accordingly in your game's Rain World Remix settings.

For all other Rain World Remix settings, the choice is yours.

## 5. Join an Archipelago room

On the Story select screen, you should see an interface
for entering the information necessary to connect to an Archipelago room (IMAGE TODO):
 - Name: your name in the multiworld. This must match the name in the YAML.
 - Password: the password for the room.  Leave blank if the room has no password.
 - Server: URL to the room's host, including port number.
This usually looks something like `archipelago.gg:12345` or `localhost:38281`.

Click `CONNECT` and the status text should change to the room.
At that point, you can start the Story campaign to begin.

The client will remain connected if you go back out to the main menu or any other menu.
It will not remain connected if you close or hot-reload the game (e.g., via Rain Reloader).

For details on everything that gets randomized,
see the [game description page](en_Rain%20World.md).