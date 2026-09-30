# Bundled Emulators

NX Redux ships with emulators for a wide range of systems. They run from
Atari and Commodore through the Game Boy line, NES/SNES, Genesis,
PlayStation, TurboGrafx-16, [Sega Dreamcast](dreamcast.md) and
[PlayStation Portable](psp.md), up to the
bundled standalone emulators for [Nintendo 64](nintendo-64.md) and
[Nintendo DS](nintendo-ds.md).

| Put this | Here |
| --- | --- |
| Games | Each system's own folder under `Roms/` on the SD card (e.g. `Roms/Game Boy Advance (GBA)/`) |
| BIOS files (for systems that need them) | The matching folder under `Bios/` |

- [Cores & BIOS Files](cores.md) lists the included cores and what each one
  needs.
- [ROM File Formats](rom-formats.md) lists which file types each system
  accepts (including zipped ROMs).

## Shared features

Every emulator, built-in cores and standalones alike, supports:

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

- **Shaders and overlays:** the SD card ships with `Shaders` and `Overlays`
  folders. Apply them per system or per game from the emulator options.
- **Cheats:** place cheat files in the `Cheats` folder.

## Netplay

Many built-in cores support local wireless [Netplay](../netplay.md). That
includes Game Boy link cable (gambatte) and Game Boy Advance link (gpSP)
games.

!!! note "Game Boy Advance: use the GBA folder"
    For Game Boy Advance, only the `GBA` (gpSP) folder supports netplay, not
    `MGBA`. The [Netplay page](../netplay.md#supported-systems) lists exactly
    which cores and `Roms` folders are netplay-capable.
