# Bundled Emulators

NX Redux ships with emulators for a wide range of systems — from Atari and
Commodore through the Game Boy line, NES/SNES, Genesis, PlayStation and
TurboGrafx-16, up to the bundled standalone emulators for
[Nintendo 64](nintendo-64.md), [Nintendo DS](nintendo-ds.md) and
[Sega Dreamcast](dreamcast.md). Each system has its own folder under `Roms/`
on the SD card (e.g. `Roms/Game Boy Advance (GBA)/`); systems that need BIOS
files read them from the matching folder under `Bios/` — see
[Cores & BIOS Files](cores.md) for the full list of included cores and what
each one needs, and [ROM File Formats](rom-formats.md) for which file types
each system accepts (including zipped ROMs).

## Shared features

Every emulator — built-in cores and standalones alike — supports:

- A custom [in-game menu](../guide/playing-games.md#the-in-game-menu) with UI
  styling consistent with the system.
- **Save states with screenshots.**
- **Auto-save on quit** to a hidden slot, so the
  [Game Switcher](../guide/game-switcher.md) always resumes where you left
  off.
- **USB-C and Bluetooth audio** with automatic rerouting.
- **Sleep** by pressing the power button.
- Per-game **emulator options**, editable in-game (Options), from the game's
  [context menu](../guide/context-menu.md), or in **Tools → Emulator
  Settings**.

## Enhancements

- **Shaders and overlays** — the SD card ships with `Shaders` and `Overlays`
  folders; apply them per system or per game from the emulator options.
- **Cheats** — place cheat files in the `Cheats` folder.

## Netplay

Many built-in cores support local wireless [Netplay](../netplay.md), including
Game Boy link cable (gambatte) and Game Boy Advance link (gpSP) games.
