# Rain World Setup Guide

## 0. Add the Rain World APWorld

The APWorld for Rain World is self-contained in `worlds/rain_world`.
You can either clone this fork or copy `worlds/rain_world`
to an existing Archipelago source.

## 1. Create a YAML settings file
### What is a YAML and why do I need one?
You can see the [basic multiworld setup guide](/tutorial/Archipelago/setup/en) here on the Archipelago website to learn 
about why Archipelago uses YAML files and what they're for.

### Where do I get a YAML?
You can use the [game options page](/games/Risk%20of%20Rain%202/player-options) here on the Archipelago 
website to generate a YAML using a graphical interface.
You can also edit this file directly if you understand the format.

## 2. Enable the Dev Console and Archipelago mods

### Option A: Install via Steam Workshop

1. Subscribe to the Dev Console mod
[on the Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=2920528044).
2. Subscribe to the Archipelago mod on the Workshop (TODO).
3. Enable both in the in-game Remix menu.
4. Restart Rain World.

### Option B: Install as local mods

1. Download Dev Console [from GitHub](https://github.com/SlimeCubed/DevConsole).
2. From that repository, copy the folder `Remix\slime-cubed.devconsole`
to `Rain World\RainWorld_Data\StreamingAssets\mods\slime-cubed.devconsole`.
3. Download the Archipelago mod [from GitHub](https://github.com/alphappy/ArchipelagoRWMod).
4. From that repository, copy the folder `mod`
to `Rain World\RainWorld_Data\StreamingAssets\mods\archipelago`.
5. Enable both in the in-game Remix menu.
6. Restart Rain World.

## 3. Test that the mods are working

There are three things that should always happen when the mod is working as intended:
1. The Dev Console should open when its keybind is pressed.
By default, it is <code>`</code> (backtick / backquote),
but this can be changed in its Remix menu.
2. (UNIMPLEMENTED) Clicking on Archipelago in the Remix menu should open its Remix interface
(as opposed to warning that the mod does not define a Remix interface).
3. Dev Console autocomplete should recommend the commands `apconnect` and `apdisconnect` as you type them.

## 4. Set Remix settings

There are two Rain World Remix settings that affect logic and may be specified in your YAML:
`Passage progress without Survivor` (enabled by default in the YAML)
and `Disable all karma requirements` (disabled by default).
They must also be set accordingly in your game's Rain World Remix settings.

For all other Rain World Remix settings, the choice is yours.

## 5. Join an Archipelago room

When the Archipelago room is open, open the Dev Console and connect by sending the command
`apconnect <HOST> <NAME> <PASSWORD>`.
- `<HOST>` should include the port number.
- `<NAME>` must *exactly* match the name in your settings YAML.
- `<PASSWORD>` must *exactly* match the room password, but can be omitted if no password was set.

For instance, the command might look like `apconnect localhost:38281 hunter`
or `apconnect archipelago.gg:22222 monk ErraticPulse5`.

A message should be returned indicating a successful connection.
At that point, you can start a Story campaign to begin.

The client will remain connected if you go back out to the main menu or any other menu.
It may not remain connected if you close or hot-reload the game (e.g., via Rain Reloader),
or if the host address or port number changes.
To disconnect, run the command `apdisconnect`.

You can use `apsay` to send a text message to the room.
This works like the regular text client;
for instance, you can `!hint` an item by sending, e.g.,
`apsay !hint key to outskirts`.

For details on everything that gets randomized,
see the [game description page](en_Rain%20World.md).