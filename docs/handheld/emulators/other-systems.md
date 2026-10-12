# Other Systems

The systems without a page of their own play as you would expect. This page
lists each one's folder, core and BIOS, and the controls that do something
more than the console's own pad. File types are on
[ROM File Formats](rom-formats.md).

!!! warning "No BIOS files are included"
    BIOS files are copyrighted and do **not** ship with NX Redux. The `Bios`
    folders are created empty. Dump the files you need from your own
    hardware. File names must match exactly.

Button tables name the device buttons by the letter printed on the cap, as
they work under the default Nintendo
[Button Layout](../guide/button-layout.md). With the Xbox layout, each
assignment moves with its letter. Remap anything in the in-game menu under
[Options → Controls](../guide/in-game-options.md#controls).

## Amiga

| | |
| --- | --- |
| Folder | `Roms/Amiga (PUAE)/` |
| Core | PUAE (puae2021) |
| BIOS | **Required** — Kickstart ROMs in `Bios/PUAE/`; `Bios/PUAE/readme.txt` lists known-good files |

## Amstrad CPC

| | |
| --- | --- |
| Folder | `Roms/Amstrad CPC (CPC)/` |
| Core | cap32 |
| BIOS | None |

## Atari 2600, 5200, 7800 and Lynx

| System | Folder tag | Core | BIOS |
| --- | --- | --- | --- |
| Atari 2600 | `A2600` | Stella 2014 | None |
| Atari 5200 | `A5200` | a5200 | **Required** — `5200.rom` in `Bios/A5200/` |
| Atari 7800 | `A7800` | ProSystem | Optional — `7800 BIOS (U).rom` in `Bios/A7800/` |
| Atari Lynx | `LYNX` | Handy | **Required** — `lynxboot.img` in `Bios/LYNX/` |

## ColecoVision

| | |
| --- | --- |
| Folder | `Roms/Colecovision (COLECO)/` |
| Core | Gearcoleco |
| BIOS | **Required** — `colecovision.rom` in `Bios/COLECO/` |

## Commodore 64, 128, PET, Plus/4 and VIC-20

All five run on VICE, one core per machine, with the system ROMs built in.

| System | Folder tag | BIOS |
| --- | --- | --- |
| Commodore 64 | `C64` | None |
| Commodore 128 | `C128` | None |
| Commodore PET | `PET` | None |
| Commodore Plus/4 | `PLUS4` | None |
| Commodore VIC-20 | `VIC` | None |

## Doom

| | |
| --- | --- |
| Folder | `Roms/Doom (PRBOOM)/` |
| Core | PrBoom |
| BIOS | **Required** — `prboom.wad` in `Bios/PRBOOM/`; the game won't start without it |

## Game Boy and Game Boy Color

| System | Folder tag | Core | BIOS |
| --- | --- | --- | --- |
| Game Boy | `GB` | Gambatte | Optional — `gb_bios.bin` in `Bios/GB/` |
| Game Boy Color | `GBC` | Gambatte | Optional — `gbc_bios.bin` in `Bios/GBC/` |

`A`, `B`, the D-pad, `SELECT` and `START` play as on the console. **A Turbo**,
**B Turbo** and **Prev. / Next Palette** (colour palettes for original Game
Boy games) have no button out of the box.

Game Boy Advance and Super Game Boy have their own page:
[Game Boy Advance](game-boy-advance.md).

## Microsoft MSX

| | |
| --- | --- |
| Folder | `Roms/Microsoft MSX (MSX)/` |
| Core | blueMSX |
| BIOS | **Required** — the blueMSX system files: the `Databases/` and `Machines/` folders in `Bios/MSX/` |

## NES and Famicom Disk System

| System | Folder tag | Core | BIOS |
| --- | --- | --- | --- |
| NES / Famicom | `FC` | FCEUmm | None |
| Famicom Disk System | `FDS` | FCEUmm | **Required** — `disksys.rom` in `Bios/FDS/` |

The Famicom Disk System was a disk drive add-on for the Famicom, released only
in Japan. Its games came on two-sided disk cards.

### Controls

| Device button | NES | Famicom Disk System |
| --- | --- | --- |
| `A` / `B` | A / B | A / B |
| D-pad (and the left stick, on devices that have one) | D-pad | D-pad |
| `SELECT` / `START` | Select / Start | Select / Start |
| `R1` | — | **Insert Disk**: eject the disk, or put it back in |
| `L1` | — | **Change Disk**: switch to the next side (only while the disk is ejected) |

**A Turbo**, **B Turbo** and **Insert Coin** have no button out of the box on
either. On the NES, **Change Disk** and **Insert Disk** are unbound too.

### Flipping disk sides

Many FDS games ask you to flip the disk partway through (*"Set side B"*), for
example when you start a new game or load a save. To flip to side B, press
`R1` (eject), `L1` (side B), then `R1` (insert). A game on more than one disk
card steps through every side in order (disk 1 side A, side B, disk 2
side A…).

!!! warning "Keep shortcuts off L1 and R1 in FDS"
    The disk buttons work without `MENU`, so a
    [shortcut](../guide/in-game-options.md#shortcuts) on the same button does
    both. A fast-forward shortcut on `R1` also ejects the disk, and the game
    then sits on its loading screen as if fast-forward had stopped working.
    Bind FDS shortcuts to another button or a `MENU` + button combination, or
    move **Change Disk** / **Insert Disk** under
    [Options → Controls](../guide/in-game-options.md#controls).

    Stuck on a loading screen? Press `R1` once to put the disk back in.

## Neo Geo Pocket and Neo Geo Pocket Color

| | |
| --- | --- |
| Folders | `Roms/Neo Geo Pocket (NGP)/`, `Roms/Neo Geo Pocket Color (NGPC)/` |
| Core | RACE |
| BIOS | None |

| Device button | Neo Geo Pocket |
| --- | --- |
| `B` (bottom) | A |
| `A` (right) | B |
| `START` | Option |

## PICO-8

| | |
| --- | --- |
| Folder | `Roms/Pico-8 (P8)/` |
| Core | fake-08 |
| BIOS | None; plays `.p8` and `.p8.png` carts |

## Pokémon mini

| | |
| --- | --- |
| Folder | `Roms/Pokémon mini (PKM)/` |
| Core | PokeMini |
| BIOS | Optional — `bios.min` in `Bios/PKM/` (a free BIOS is built in) |

| Device button | Pokémon mini |
| --- | --- |
| `A` / `B` | A / B |
| `R1` | C |
| `L1` | Shake |
| `SELECT` | Power |

## Sega Genesis, Sega CD, 32X, Master System, Game Gear and SG-1000

| System | Folder tag | Core | BIOS |
| --- | --- | --- | --- |
| Sega Genesis / Mega Drive | `MD` | PicoDrive | None |
| Sega CD | `SEGACD` | PicoDrive | **Required** — `bios_CD_U.bin`, `bios_CD_E.bin`, `bios_CD_J.bin` in `Bios/SEGACD/` |
| Sega 32X | `32X` | PicoDrive | None |
| Sega Master System | `SMS` | PicoDrive | None |
| Sega Game Gear | `GG` | PicoDrive | None |
| Sega SG-1000 | `SG1000` | PicoDrive | None |
| Any of the above, except 32X | `GPGX` | Genesis Plus GX | Sega CD: **required**, the same three files in `Bios/GPGX/` |

PicoDrive is the default and the lighter of the two. To use Genesis Plus GX,
name a `Roms` folder with the `(GPGX)` tag, for example
`Sega Genesis (GPGX)`.

??? info "More detail: Genesis Plus GX"
    A single `GPGX` tag, pak and core plays Genesis/Mega Drive, Master System,
    Game Gear, SG-1000 **and** Sega CD. It picks the system from each ROM's
    file extension.

    That also lets [RetroAchievements](../apps/retroachievements.md) identify
    every game with the correct console, so you can keep all your Sega games
    under `(GPGX)` folders.

    Because they share one tag, GPGX saves, BIOS, cheats and overlays all
    live under the `GPGX` name (e.g. Sega CD BIOS goes in `Bios/GPGX/`, not
    `Bios/SEGACD/`).

### Controls

Genesis, Sega CD and 32X games get the six-button pad. The top row sits on
the face buttons and the bottom row on `B`, `L1` and `R1`:

| Device button | Genesis button |
| --- | --- |
| `Y` (left) | A |
| `X` (top) | B |
| `A` (right) | C |
| `B` (bottom) | X |
| `L1` | Y |
| `R1` | Z |
| `SELECT` | Mode |
| `START` | Start |

Master System, Game Gear and SG-1000:

| Device button | Button |
| --- | --- |
| `B` (bottom) | 1 |
| `A` (right) | 2 |
| `START` | Pause / Start |

## TurboGrafx-16

| | |
| --- | --- |
| Folder | `Roms/TurboGrafx-16 (PCE)/` |
| Core | Mednafen PCE Fast |
| BIOS | HuCards: none. CD games: **required** — `syscard3.pce` in `Bios/PCE/` |

| Device button | TurboGrafx-16 |
| --- | --- |
| `A` / `B` | I / II |
| `Y` / `X` | III / IV |
| `L1` / `R1` | V / VI |
| `L2` | Mode (switches between the 2- and 6-button pad) |
| `SELECT` / `START` | Select / Run |

## Virtual Boy

| | |
| --- | --- |
| Folder | `Roms/Virtual Boy (VB)/` |
| Core | Mednafen VB |
| BIOS | None |

The D-pad is the left D-pad, with `A`, `B`, `L1` / `R1`, `SELECT` and `START`
as on the console. The **right D-pad** and **Low Battery** have no button out
of the box; assign them under
[Options → Controls](../guide/in-game-options.md#controls) for games that
use the right pad.

## WonderSwan and WonderSwan Color

| | |
| --- | --- |
| Folder | `Roms/Wonderswan Color (WSC)/` (WonderSwan and WonderSwan Color games share it) |
| Core | Mednafen WonderSwan |
| BIOS | None |
