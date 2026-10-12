# Bundled Emulators

NX Redux ships with emulators for a wide range of systems. They run from
Atari and Commodore through the Game Boy line, NES/SNES, Genesis,
[PlayStation](playstation.md), TurboGrafx-16, [Sega Dreamcast](dreamcast.md) and
[PlayStation Portable](psp.md) and [Nintendo 64](nintendo-64.md), up to the
bundled standalone emulator for [Nintendo DS](nintendo-ds.md).

| Put this | Here |
| --- | --- |
| Games | Each system's own folder under `Roms/` on the SD card (e.g. `Roms/Game Boy Advance (GBA)/`) |
| BIOS files (for systems that need them) | The matching folder under `Bios/` |

Each system's page lists its folder, core, BIOS and controls. Systems
without a page of their own are on [Other Systems](other-systems.md).
[ROM File Formats](rom-formats.md) lists which file types each system accepts
(including zipped ROMs).

## BIOS checklist

These systems **won't run without a BIOS file**. Put each file in the folder
shown, named exactly as listed. Systems not listed need no BIOS, or have one
built in; their pages say when a real one helps.

| System | File | Folder |
| --- | --- | --- |
| [Amiga](other-systems.md#amiga) | Kickstart ROMs (`Bios/PUAE/readme.txt` lists known-good files) | `Bios/PUAE/` |
| [Arcade](arcade.md#bios-sets-neogeozip-and-friends), BIOS-based boards | The board's BIOS zip, e.g. `neogeo.zip` | Next to the game, in `Roms/Arcade (FBN)/` |
| [Atari 5200](other-systems.md#atari-2600-5200-7800-and-lynx) | `5200.rom` | `Bios/A5200/` |
| [Atari Lynx](other-systems.md#atari-2600-5200-7800-and-lynx) | `lynxboot.img` | `Bios/LYNX/` |
| [ColecoVision](other-systems.md#colecovision) | `colecovision.rom` | `Bios/COLECO/` |
| [Doom](other-systems.md#doom) | `prboom.wad` | `Bios/PRBOOM/` |
| [Famicom Disk System](other-systems.md#nes-and-famicom-disk-system) | `disksys.rom` | `Bios/FDS/` |
| [Microsoft MSX](other-systems.md#microsoft-msx) | The blueMSX `Databases/` and `Machines/` folders | `Bios/MSX/` |
| [Sega CD](other-systems.md#sega-genesis-sega-cd-32x-master-system-game-gear-and-sg-1000) | `bios_CD_U.bin`, `bios_CD_E.bin`, `bios_CD_J.bin` | `Bios/SEGACD/` (`Bios/GPGX/` for the GPGX folder) |
| [Sega Naomi / Atomiswave](dreamcast.md#arcade-games-naomi-atomiswave) | `naomi.zip` / `awbios.zip` | `Bios/DC/` (`Bios/DCX/` for Dreamcast Lite) |
| [TurboGrafx-16](other-systems.md#turbografx-16), CD games only | `syscard3.pce` | `Bios/PCE/` |

!!! warning "No BIOS files are included"
    BIOS files are copyrighted and do **not** ship with NX Redux. The `Bios`
    folders are created empty. Dump the files you need from your own
    hardware.

## Systems with a choice of core

Some systems appear more than once on purpose. Pick per game by which `Roms`
folder you use:

| System | Faster, lighter | More accurate |
| --- | --- | --- |
| [Game Boy Advance](game-boy-advance.md) | gpSP (`GBA`), the only GBA core with [Netplay](../netplay.md#supported-systems) | mGBA (`MGBA`), better for ROM hacks, no netplay |
| [Super Nintendo](super-nintendo.md) | Snes9x (`SFC`), the default | Supafaust (`SUPA`), but heavier |
| [The Sega systems](other-systems.md#sega-genesis-sega-cd-32x-master-system-game-gear-and-sg-1000) | PicoDrive | Genesis Plus GX (`GPGX`) |
| [PlayStation](playstation.md) | PCSX-ReARMed (`PS`), the default | SwanStation (`PSX`, [details](playstation.md#swanstation)), heavier |
| [Dreamcast](dreamcast.md) | Flycast 2022 (`DCX`, [Dreamcast Lite](dreamcast.md#dreamcast-lite)), no netplay | Flycast v2.7 (`DC`), the default |

## Which device plays it best

Every device runs the older systems (Atari to Genesis, the Game Boy line,
PlayStation) at full speed. The differences show in the heaviest systems,
where the **Smart Pro S** has a faster chip and more headroom. The Brick,
Brick Hammer, Brick Pro and Smart Pro share one slower chip.

| System | Smart Pro S | Brick, Brick Hammer, Brick Pro, Smart Pro |
| --- | --- | --- |
| [PlayStation Portable](psp.md#performance) | **Recommended.** Full speed in every game tested, also at 2× resolution | Most games at full speed; the heaviest 3D games (Tekken 6) run slower |
| [Dreamcast](dreamcast.md) | More headroom: 960×720 in lighter games | Keep the native 640×480; little to spare |
| [Nintendo 64](nintendo-64.md) | GLideN64 plugin; 3–4-player netplay | Rice plugin for speed; netplay up to 2 players |

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
