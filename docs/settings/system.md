# System

Power behavior, clock, save formats and system maintenance. Options marked
*device-dependent* appear only where the hardware calls for them.

![System settings](../assets/screenshots/set-system.png)

## Screen timeout

Period of inactivity before the screen turns off, `0`–`600` s.

## Suspend timeout

Time before the device goes to sleep after the screen is off, `5`–`600` s.

## Haptic feedback

Enable or disable haptic feedback on certain actions in the OS.

## Default view

The initial view to show on boot — the content list or the
[Game Switcher](../guide/game-switcher.md).

## Game Switcher games

Which recently played games appear in the Game Switcher — `Resumable only`
(the default) or all recent games.

## Show 24h time format

Show the clock in 24-hour format.

## Show clock

Show the clock in the status pill.

## Set time and date automatically

Sync time via NTP (requires internet).

## Set time and date manually

Adjust the date and time with the clock editor.

## Time zone

Your time zone.

## Save format

Format for battery saves in `Saves/<TAG>/`: `MinUI` (`.sav`),
`Retroarch (compressed)` / `Retroarch (uncompressed)` (`.srm`), or
`Generic`. Default: **Retroarch (uncompressed)** — directly compatible
with RetroArch on other devices.

## Save state format

Naming/format for save states: `MinUI` (`.st0`…), `Retroarch-ish` or
`Retroarch` (`.state`, `.state1`…), each compressed or uncompressed.
Default: **Retroarch (uncompressed)**.

## Use extracted file name

For zipped ROMs, use the extracted file's name instead of the archive
name (affects save/state matching).

## Safe poweroff

Bypasses the stock shutdown procedure to avoid the "limbo bug".
*(TrimUI devices.)*

## Restore stock files

Restores the console's factory OSD files and reverts NX boot patches, if
any — the NX OSD is unaffected. *(Device-dependent.)*

## Fan Speed

Fan speed: Quiet / Normal / Performance or a percentage. *(Devices with
active cooling — Smart Pro S.)*

## Refresh emulator/roms list

Clears the cached emulator/ROMs list so it rescans on the next launch.

## Reset to defaults

Resets all options on this page to their default values.
