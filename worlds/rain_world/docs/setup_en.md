# Rain World Setup Guide

## 1. Add the Rain World APWorld

Add the APWorld to your AP installation by doing one of the following:
- Grab an `.apworld` from [the releases page](https://github.com/alphappy/ArchipelagoRW/releases)
and place it in the `worlds` folder of your AP installation.
- Clone this repository and either use it directly or copy `worlds/rain_world`
to the `worlds` folder of your AP installation.

## 2. Create a player YAML settings file

Player YAML settings files are used to tweak logic, determine start state and victory condition, and more.
You can see the [basic multiworld setup guide](/tutorial/Archipelago/setup/en)
for a general overview of how Archipelago uses player YAML files,
and [the settings subpage](/tutorial/Rain%20World/settings/en)
for more on the specific settings that Rain World uses.
You need a player YAML file even if you choose to leave all settings at their defaults.

You can generate a player YAML file by doing one of the following:
- Generate the template file.
  1. Open the Archipelago Launcher and select `Generate Template Options`.
  2. Find `Rain World.yaml` in `Players/Templates` of your AP installation.
  3. Copy and edit this file to change settings.
- Run the WebHost.
  1. Run `WebHost.py` to start the WebHost locally.
  If you haven't done this before, several Python packages will need to install first.
  2. Once the WebHost is running, navigate to `localhost` in a browser.
  3. Select `Supported Games`, then find `Rain World` in the game list.
  4. Go to the [game options page](/games/Rain%20World/player-options)
  (or the [weighted options page](/games/Rain%20World/weighted-options))
  and adjust settings as desired.
  5. Click `Export Options` at the bottom.

## 3. Enable the Randomizer mod

Install an Archipelago release of the Randomizer mod by doing the following:
1. Download a release [from GitHub](https://github.com/SaltiestSyrup/RWRandomizer/releases).
   If you downloaded a specific release on the APWorld,
   that release page should point to the version(s) of the Randomizer mod that it is designed for.
2. Unzip it and place the `rwrandomizer` folder in your mods folder
   (`Rain World\RainWorld_Data\StreamingAssets\mods`).
3. (Re)start Rain World.
4. Go to the Remix menu and enable `Check Randomizer` and `Rain World Remix`.
5. Restart Rain World.
6. Go to the Remix menu and verify that the mod has loaded correctly
by clicking on the `Check Randomizer` to open its Remix interface.
You should an `Archipelago` tab in this interface.

## 4. Set Remix and mod settings

There are a few mod settings that must be adjusted according to your player YAML file:
- _Rain World Remix_ must be enabled.
- If the `Game state` setting is not a `Vanilla` state, then _More Slugcats Expansion_ must be enabled.
- The `Passage progress without Survivor` setting should match what is set in your _Rain World Remix_ settings.
- If the `Gate Behavior` setting is not set to `Key Only`,
then `Monk-style karma gates` in your _Rain World Remix_ settings should be enabled.

## 5. Join an Archipelago room

When the Archipelago room is open, the Randomizer mod Remix menu interface 
may be used to connect to a room (under the `Archipelago` tab).
The name entered here must exactly match the name specified in the YAML.

A message should be returned indicating a successful connection
and including key pieces of information from your player YAML file.

The client will remain connected if you go back out to the main menu or any other menu.
It may not remain connected if you close or hot-reload the game (e.g., via Rain Reloader),
or if the host address or port number changes.

## 6. Start the game

Once you are connected to a room, the matching Story campaign may be started.
A fresh campaign should be used - not necessarily a fresh save file,
but use alternate save files or backups to avoid deleting other campaign data.

For details on everything that gets randomized,
see the [game description page](/games/Rain%20World/info/en).