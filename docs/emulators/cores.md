# Cores & BIOS Files

Every system below runs on a bundled libretro core. BIOS files go in the
matching folder under `Bios/` on the SD card — the folder name is the tag
in parentheses after the system name (e.g. Game Boy Advance (GBA) →
`Bios/GBA/`), and file names must match exactly.

!!! warning "No BIOS files are included"
    BIOS files are copyrighted and do **not** ship with NX Redux — the
    `Bios` folders are created empty. Dump the files you need from your own
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
| Sega Game Gear (GG) | PicoDrive | None |
| Sega Genesis (MD) | PicoDrive | None |
| Sega Master System (SMS) | PicoDrive | None |
| Sega SG-1000 (SG1000) | PicoDrive | None |
| Sony PlayStation (PS) | PCSX-ReARMed | Recommended — `psxonpsp660.bin` or `scph1001.bin` (an HLE fallback exists; a real BIOS is strongly recommended for compatibility) |
| Super Nintendo ES (SFC) | Snes9x | None |
| Super Nintendo ES (SUPA) | Mednafen Supafaust | None |
| TurboGrafx-16 (PCE) | Mednafen PCE Fast | HuCards: none; CD games: **`syscard3.pce` required** |
| Virtual Boy (VB) | Mednafen VB | None |

Two systems appear twice on purpose: **Game Boy Advance** ships both gpSP
(GBA — faster) and mGBA (MGBA — more accurate), and **Super Nintendo**
ships both Snes9x (SFC) and Supafaust (SUPA) — pick per game by which
`Roms` folder you use.

## Standalone emulators

[Nintendo 64](nintendo-64.md) (Mupen64Plus) and
[Nintendo DS](nintendo-ds.md) (Drastic) need no BIOS files.
[Sega Dreamcast](dreamcast.md) (Flycast) boots without one via HLE; a real
`dc_boot.bin` in `Bios/DC/` is optional.
