# Cores & BIOS Files

This page lists the core each system runs on and the BIOS files it needs.
Every system below runs on a bundled libretro core.

To add a BIOS file, put it in the matching folder under `Bios/` on the SD
card. The folder name is the tag in parentheses after the system name (e.g.
Game Boy Advance (GBA) → `Bios/GBA/`). File names must match exactly.

!!! warning "No BIOS files are included"
    BIOS files are copyrighted and do **not** ship with NX Redux. The `Bios`
    folders are created empty. Dump the files you need from your own
    hardware.

## Systems and cores

| System | Core | BIOS |
| --- | --- | --- |
| Amiga (PUAE) | puae2021 | **Required** — Kickstart ROMs; `Bios/PUAE/readme.txt` lists known-good files |
| Amstrad CPC (CPC) | cap32 | None |
| Arcade (FBN) | fbneo | No system BIOS; BIOS-based boards (e.g. Neo Geo) need the BIOS zip (`neogeo.zip`) with the ROM set — see the [Arcade page](arcade.md) |
| Atari 2600 (A2600) | stella2014 | None |
| Atari 5200 (A5200) | a5200 | **Required** — `5200.rom` |
| Atari 7800 (A7800) | prosystem | Optional — `7800 BIOS (U).rom` |
| Atari Lynx (LYNX) | handy | **Required** — `lynxboot.img` |
| Colecovision (COLECO) | gearcoleco | **Required** — `colecovision.rom` |
| Commodore 64 (C64) | vice_x64 | None (system ROMs built in) |
| Commodore 128 (C128) | vice_x128 | None (system ROMs built in) |
| Commodore PET (PET) | vice_xpet | None (system ROMs built in) |
| Commodore Plus4 (PLUS4) | vice_xplus4 | None (system ROMs built in) |
| Commodore VIC20 (VIC) | vice_xvic | None (system ROMs built in) |
| Doom (PRBOOM) | prboom | **Required** — `prboom.wad` (the launcher refuses to start without it) |
| Famicom Disk System (FDS) | fceumm | **Required** — `disksys.rom` |
| Game Boy (GB) | gambatte | Optional — `gb_bios.bin` |
| Game Boy Color (GBC) | gambatte | Optional — `gbc_bios.bin` |
| Game Boy Advance (GBA) | gpSP | Recommended — `gba_bios.bin` (a built-in replacement exists; the real BIOS improves compatibility) |
| Game Boy Advance (MGBA) | mGBA | Optional — `gba_bios.bin` |
| Super Game Boy (SGB) | mGBA | Optional — `sgb_bios.bin` for full Super Game Boy accuracy |
| Microsoft MSX (MSX) | blueMSX | **Required** — blueMSX system files: the `Databases/` and `Machines/` folders |
| Neo Geo Pocket (NGP) | RACE | None |
| Neo Geo Pocket Color (NGPC) | RACE | None |
| Nintendo ES (FC) | FCEUmm | None |
| Pico-8 (P8) | fake-08 | None (plays `.p8` / `.p8.png` carts) |
| Pokémon mini (PKM) | PokeMini | Optional — `bios.min` (FreeBIOS built in) |
| Sega 32X (32X) | PicoDrive | None |
| Sega CD (SEGACD) | PicoDrive | **Required** — `bios_CD_U.bin`, `bios_CD_E.bin`, `bios_CD_J.bin` |
| Sega Dreamcast (DC) | Flycast | Optional — `dc_boot.bin` (a built-in HLE BIOS is used without it). Naomi / Atomiswave arcade games **require** `naomi.zip` / `awbios.zip` — see the [Dreamcast page](dreamcast.md#arcade-games-naomi-atomiswave) |
| Dreamcast Lite (DCX) | Flycast (2022 libretro build) | Same files as Dreamcast, in `Bios/DCX/` — see [Dreamcast Lite](dreamcast.md#dreamcast-lite) |
| Sega Game Gear (GG) | PicoDrive | None |
| Sega Genesis (MD) | PicoDrive | None |
| Sega Master System (SMS) | PicoDrive | None |
| Sega SG-1000 (SG1000) | PicoDrive | None |
| Sega Genesis (GPGX) | Genesis Plus GX | None |
| Sega Master System (GPGX) | Genesis Plus GX | None |
| Sega Game Gear (GPGX) | Genesis Plus GX | None |
| Sega CD (GPGX) | Genesis Plus GX | **Required** — `bios_CD_U.bin`, `bios_CD_E.bin`, `bios_CD_J.bin` in `Bios/GPGX/` |
| Sony PlayStation (PS) | PCSX-ReARMed | Recommended — `psxonpsp660.bin` or `scph1001.bin` (an HLE fallback exists; a real BIOS is strongly recommended for compatibility) — see the [PlayStation page](playstation.md) |
| Sony PlayStation (PSX) | SwanStation | Recommended — `scph5500.bin` (Japan), `scph5501.bin` (USA), `scph5502.bin` (Europe) in `Bios/PSX/` (a built-in OpenBIOS is used without them) — see [SwanStation](playstation.md#swanstation) |
| Sony PlayStation Portable (PSP) | PPSSPP | None — see the [PSP page](psp.md) |
| Super Nintendo ES (SFC) | Snes9x | None |
| Super Nintendo ES (SUPA) | Mednafen Supafaust | None |
| TurboGrafx-16 (PCE) | Mednafen PCE Fast | HuCards: none; CD games: **`syscard3.pce` required** |
| Virtual Boy (VB) | Mednafen VB | None |
| Wonderswan Color (WSC) | Mednafen WonderSwan | None (plays WonderSwan and WonderSwan Color games) |

## Systems with a choice of core

Some systems appear more than once on purpose. Pick per game by which `Roms`
folder you use:

| System | Faster, lighter | More accurate |
| --- | --- | --- |
| **Game Boy Advance** | gpSP (`GBA`), the only GBA core with [Netplay](../netplay.md#supported-systems) | mGBA (`MGBA`), better for ROM hacks, no netplay |
| **Super Nintendo** | Snes9x (`SFC`), the default | Supafaust (`SUPA`), but heavier |
| **The Sega systems** | PicoDrive | Genesis Plus GX (`GPGX`) |
| **PlayStation** | PCSX-ReARMed (`PS`), the default | SwanStation (`PSX`, [details](playstation.md#swanstation)), sharper 3D but heavier |
| **Dreamcast** | Flycast 2022 (`DCX`, [Dreamcast Lite](dreamcast.md#dreamcast-lite)), no netplay | Flycast v2.7 (`DC`), the default |

See [Game Boy Advance](game-boy-advance.md) and
[Super Nintendo](super-nintendo.md) for which to use.

To use Genesis Plus GX, name a `Roms` folder for the system with the
`(GPGX)` tag, for example `Sega Genesis (GPGX)`. It works the same way the
default `Sega Genesis (MD)` folder uses PicoDrive.

??? info "More detail: Genesis Plus GX"
    Genesis Plus GX is special: a single `GPGX` tag, pak and core plays
    Genesis/Mega Drive, Master System, Game Gear, SG-1000 **and** Sega CD. It
    picks the system from each ROM's file extension.

    That also lets [RetroAchievements](../apps/retroachievements.md) identify
    every game with the correct console, so you can keep all your Sega games
    under `(GPGX)` folders.

    Because they share one tag, GPGX saves, BIOS, cheats and overlays all
    live under the `GPGX` name (e.g. Sega CD BIOS goes in `Bios/GPGX/`, not
    `Bios/SEGACD/`).

## Standalone emulators

[Nintendo 64](nintendo-64.md) (Mupen64Plus) and
[Nintendo DS](nintendo-ds.md) (Drastic) run on standalone emulators and need
no BIOS files.
