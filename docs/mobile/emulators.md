# Emulators

Every core is bundled in the app. Folder and tag names match NX Redux on the
handheld.

| System | Tag(s) | Core |
| --- | --- | --- |
| Nintendo DS | `NDS` | melonDS DS |
| Nintendo 64 | `N64` | mupen64plus-next |
| PlayStation Portable | `PSP` | PPSSPP |
| Game Boy / Game Boy Color | `GB`, `GBC` | Gambatte |
| Game Boy Advance | `GBA` | gpSP |
| Game Boy Advance, Super Game Boy | `MGBA`, `SGB` | mGBA |
| NES / Famicom Disk System | `FC`, `FDS` | FCEUmm |
| Super Nintendo | `SFC` | Snes9x |
| Super Nintendo | `SUPA` | Mednafen Supafaust |
| Genesis / Mega Drive, Master System, Game Gear, SG-1000, Sega CD | `GPGX`, `MD`, `SMS`, `GG`, `SG1000`, `SEGACD` | Genesis Plus GX |
| PlayStation | `PS` | PCSX ReARMed |
| Neo Geo Pocket / Color | `NGP`, `NGPC` | RACE |
| PC Engine | `PCE` | Mednafen PCE Fast |
| Virtual Boy | `VB` | Mednafen VB |
| Atari Lynx | `LYNX` | Handy |
| Atari 2600 | `A2600` | Stella 2014 |
| Atari 5200 | `A5200` | a5200 |
| Atari 7800 | `A7800` | ProSystem |
| Pokémon Mini | `PKM` | PokeMini |
| WonderSwan Color | `WSC` | Mednafen WonderSwan |
| PICO-8 | `P8` | fake-08 |
| Doom | `PRBOOM` | PrBoom |
| Sega 32X | `32X` | PicoDrive |
| ColecoVision | `COLECO` | Gearcoleco |
| Arcade | `FBN` | FinalBurn Neo |

Sega Genesis uses `GPGX` by default, like the handheld, with `MD` as a second
tag on the same core.

## BIOS files

Put BIOS files in `Bios/<TAG>/`. A launch also reads the folders of tags that
share its core, so a handheld's layout (`Bios/FC/disksys.rom`,
`Bios/MD/bios_CD_*.bin`, `Bios/PS/psxonpsp660.bin`) works unchanged.
Famicom Disk System, Sega CD, PC Engine CD and ColecoVision
(`Bios/COLECO/colecovision.rom`) need their BIOS, which is checked before
launch. PlayStation has a BIOS built in and uses a real one when present.

## Zip and 7z files

An archive holding one game plays on every core. The app unpacks it on first
launch, and saves use the archive's name, as on the handheld. Archives with
several games or a password are refused with a message. Arcade (`FBN`) zips
are the game itself and are never unpacked; parent and BIOS sets such as
`neogeo.zip` are found in the same folder or in `Bios/FBN/`.

## Nintendo DS

The two screens can be stacked, side by side, picture in picture or single
screen, set separately for portrait and landscape in
**Options → Console Settings**. With a controller, `R2` swaps the big screen,
`SELECT` + `LEFT` / `RIGHT` cycles the layout, and `L2` toggles stylus mode.
3D runs on the GPU at 2× internal resolution by default (1×–8× in
**Core Options → Video**).

## Not available yet

- **Sega Dreamcast** is not in the first release.
- **PlayStation `.exe` homebrew** does not load yet.
- **PICO-8** save states and auto-resume do not work yet.
