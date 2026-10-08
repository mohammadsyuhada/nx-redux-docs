# Bundled Emulators

Every core is bundled in the app. There is nothing to download. Folder and
tag names match NX Redux on the handheld.

The systems with their own controls or settings have a page each:
[Arcade (FBNeo)](arcade.md), [Nintendo 64](nintendo-64.md),
[Sega Dreamcast](dreamcast.md), [PlayStation](playstation.md),
[PlayStation Portable](psp.md), [Nintendo DS](nintendo-ds.md) and
[Nintendo 3DS](nintendo-3ds.md). The
smaller differences of the others, such as the Sega `Mode` button or the
Neo Geo Pocket's `Option`, are on [Other Systems](other-systems.md).

| Put this | Here |
| --- | --- |
| Games | Each system's own folder under `Roms/`, such as `Roms/Game Boy Advance (GBA)/` |
| BIOS files (for systems that need them) | `Bios/<TAG>/`, such as `Bios/DC/` |

| System | Tag(s) | Core |
| --- | --- | --- |
| [Nintendo DS](nintendo-ds.md) | `NDS` | melonDS DS |
| [Nintendo 3DS](nintendo-3ds.md) | `3DS` | Azahar |
| [Nintendo 64](nintendo-64.md) | `N64` | Mupen64Plus-Next |
| [PlayStation Portable](psp.md) | `PSP` | PPSSPP |
| Game Boy / Game Boy Color | `GB`, `GBC` | Gambatte |
| Game Boy Advance | `GBA` | gpSP |
| Game Boy Advance, Super Game Boy | `MGBA`, `SGB` | mGBA |
| NES / Famicom Disk System | `FC`, `FDS` | FCEUmm |
| Super Nintendo | `SFC` | Snes9x |
| Super Nintendo | `SUPA` | Supafaust |
| Genesis / Mega Drive, Master System, Game Gear, SG-1000, Sega CD | `MD`, `SMS`, `GG`, `SG1000`, `SEGACD` | Genesis Plus GX |
| Sega 32X | `32X` | PicoDrive |
| [Dreamcast, NAOMI, Atomiswave](dreamcast.md) | `DC` | Flycast |
| [PlayStation](playstation.md) | `PS` | PCSX-ReARMed |
| Neo Geo Pocket / Color | `NGP`, `NGPC` | RACE |
| PC Engine / TurboGrafx-16 | `PCE` | Beetle PCE Fast |
| Virtual Boy | `VB` | Beetle VB |
| Atari Lynx | `LYNX` | Handy |
| Atari 2600 | `A2600` | Stella 2014 |
| Atari 5200 | `A5200` | a5200 |
| Atari 7800 | `A7800` | ProSystem |
| Pokémon Mini | `PKM` | PokeMini |
| WonderSwan Color | `WSC` | Beetle WonderSwan |
| PICO-8 | `P8` | fake-08 |
| Doom | `PRBOOM` | PrBoom |
| ColecoVision | `COLECO` | Gearcoleco |
| [Arcade](arcade.md) | `FBN` | FinalBurn Neo |
| Android | none | The game's own app (see [Launcher Mode & Android Games](../launcher.md)) |

**Android** shows as a console once you add Android games. They are apps
installed on your phone, and the app starts them for you. They have no core
and no folder.

## Choosing an emulator

Two consoles have a second emulator, each with its own tag:

| Console | Tags |
| --- | --- |
| Game Boy Advance | `GBA` (gpSP), `MGBA` (mGBA) |
| Super Nintendo ES | `SFC` (Snes9x), `SUPA` (Supafaust) |

- A folder named with a tag, such as `Game Boy Advance (MGBA)`, uses that
  tag.
- For folders without a tag, pick the emulator in **Tools → Settings →
  Emulators → Default emulators**.
- For one game, press `MENU` on it in a game list and pick **Emulator**. This
  choice wins over both.

The tag is where saves and settings are kept. To set a core's options outside
a game, for a whole console or for one game, see
[Emulator Settings](../emulator-settings.md).

## BIOS files

Put BIOS files in `Bios/<TAG>/`.

- These systems need their BIOS: Famicom Disk System, Sega CD, PC Engine CD,
  ColecoVision (`Bios/COLECO/colecovision.rom`) and Dreamcast
  ([Sega Dreamcast](dreamcast.md#bios)).
- The app checks for it before launch and names the missing file, such as
  **Sega CD needs a BIOS: put bios_CD_U.bin (or bios_CD_E.bin,
  bios_CD_J.bin) in Bios/SEGACD/**.
- PlayStation has a BIOS built in, and uses a real one when present.

??? info "More detail"
    A launch also reads the folders of tags that share its core. So a
    handheld's layout (`Bios/FC/disksys.rom`, `Bios/MD/bios_CD_*.bin`,
    `Bios/PS/psxonpsp660.bin`) works unchanged.

## Zip and 7z files

An archive holding one game plays on every core. An archive with one game
beside extras, such as a readme, plays too.

Archives with several games, a password, or a game the chosen core can't run
are refused with a message.

??? info "More detail"
    The app unpacks the archive on first launch. Saves use the archive's name,
    as on the handheld. The unpacked copies are trimmed automatically; see
    [Unpacked games cache](../library.md#unpacked-games-cache).

    Arcade sets are the exception. For FinalBurn Neo, NAOMI and Atomiswave the
    zip *is* the game, and it is never unpacked.

## Multi-disc games

A multi-file disc (`.cue`, `.gdi`) or a disc list (`.m3u`) loads as one game.

To change disc, open the [in-game menu](../in-game-menu.md#the-first-page). For a
game with more than one disc it shows a **Disc** row under **Continue**, with
the disc in the drive, such as `1/2`. `LEFT` / `RIGHT` change the disc, as
opening the lid and swapping it would. The disc choice is not saved.

## Limits

- **PlayStation `.exe` homebrew** doesn't load.
- **PICO-8** games have no save states, and don't resume where you left off.
