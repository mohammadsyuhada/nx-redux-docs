# ROM File Formats

Every system folder under `Roms/` accepts the formats its emulator reads
natively — the tables below list them per system. On top of that, the
built-in cores all accept **zipped ROMs**, and most users only need one
rule of thumb: **uncompressed is best, CD games should be CHD, and
arcade zips must stay exactly as they are.**

## Compressed ROMs (.zip and .7z)

Any game launched through a built-in core can be a `.zip` or `.7z`
archive:

- Cores that read archives themselves (FBNeo, the Commodore cores, Amiga)
  get the file untouched.
- For every other core, NX Redux extracts the ROM out of the archive at
  launch and hands the core the extracted file. The copy is kept in RAM
  until the device powers off, so only the **first** launch of a session
  pays the extraction delay.

This does **not** apply to the standalone emulators —
[Nintendo 64](nintendo-64.md), [Nintendo DS](nintendo-ds.md) and
[Sega Dreamcast](dreamcast.md) get their files directly, so give them
uncompressed images (Dreamcast's `.chd` is compressed internally and is
the recommended format there anyway).

### Uncompressed vs .zip vs .7z

**Prefer uncompressed ROMs** (`.gb`, `.sfc`, `.md`, …). The only thing
compression buys is SD card space, and cartridge ROMs are tiny next to
any modern card. Uncompressed files win everything else:

- **Fastest launch** — the core reads the file directly, with no
  extraction step, every time.
- **No RAM overhead** — extracted copies of compressed ROMs live in
  RAM until the device powers off, and the Trimui devices only have
  **1 GB** shared with the emulator itself. An uncompressed ROM costs
  nothing.
- **Works everywhere** — including the standalone emulators, which do
  not get the automatic extraction.

| Format | Pros | Cons |
| --- | --- | --- |
| Uncompressed (`.gb`, `.sfc`, …) | Fastest launch, no RAM overhead, works everywhere | Largest files on the SD card |
| `.zip` | Smaller files, standard romset convention | Extraction delay on first launch; extracted copy sits in RAM all session |
| `.7z` | Smallest files | Slowest extraction of the three; same RAM cost as `.zip` |

Compressed cartridge ROMs still work fine if that is the form your
library is already in — for typical carts (up to a few dozen MB) the
extraction delay is under a second and the RAM cost is small. Just
don't bother compressing yourself, and if you keep archives, prefer
`.zip` over `.7z`: the extra space `.7z` saves is small and its
extraction is noticeably slower on these devices.

!!! warning "Never zip CD images"
    Do **not** compress CD-based games (PlayStation, Sega CD,
    TurboGrafx-CD) into `.zip`/`.7z`. A `.cue` + `.bin` pair stops
    working when archived (only one file gets extracted), and a large
    image can exhaust the device's RAM during extraction. Use **`.chd`**
    instead — it is heavily compressed *and* read directly, with no
    extraction step and no RAM cost.

!!! note "Arcade zips are not compressed ROMs"
    `Roms/Arcade (FBN)/` zips are **romsets** — the zip itself is the
    game's identity and FBNeo reads it directly. Never extract or
    re-compress them, and see the [Arcade page](arcade.md) for naming
    rules.

## Formats per system

Native formats verified against each bundled core. Remember `.zip` and
`.7z` work for all of these on top of what is listed; multi-disc games
use [`.m3u` playlists](../guide/main-menu.md#multi-disc-games).

### Cartridge & handheld systems

| System | Core | Formats |
| --- | --- | --- |
| Atari 2600 (A2600) | stella2014 | `a26` `bin` |
| Atari 5200 (A5200) | a5200 | `a52` `bin` |
| Atari 7800 (A7800) | prosystem | `a78` `bin` `cdf` |
| Atari Lynx (LYNX) | handy | `lnx` `lyx` `o` |
| Colecovision (COLECO) | gearcoleco | `col` `cv` `bin` `rom` |
| Famicom Disk System (FDS) | fceumm | `fds` |
| Game Boy (GB) / Game Boy Color (GBC) | gambatte | `gb` `gbc` `dmg` |
| Game Boy Advance (GBA) | gpsp | `gba` `bin` `agb` `gbz` |
| Game Boy Advance (MGBA) | mgba | `gba` |
| Super Game Boy (SGB) | mgba | `gb` `gbc` `sgb` |
| Neo Geo Pocket (NGP/NGPC) | race | `ngp` `ngc` `ngpc` `npc` |
| Nintendo ES (FC) | fceumm | `nes` `unf` `unif` |
| Pico-8 (P8) | fake-08 | `p8` `png` |
| Pokémon mini (PKM) | pokemini | `min` |
| Sega Genesis (MD) | picodrive | `md` `gen` `smd` `bin` `68k` `sgd` |
| Sega 32X (32X) | picodrive | `32x` `bin` |
| Sega Game Gear (GG) | picodrive | `gg` |
| Sega Master System (SMS) | picodrive | `sms` |
| Sega SG-1000 (SG1000) | picodrive | `sg` `sc` |
| Super Nintendo ES (SFC) | snes9x | `sfc` `smc` `swc` `fig` `bs` `st` |
| Super Nintendo ES (SUPA) | mednafen_supafaust | `sfc` `smc` `swc` `fig` |
| TurboGrafx-16 (PCE) | mednafen_pce_fast | `pce` + CD: `cue` `ccd` `chd` `toc` `m3u` |
| Virtual Boy (VB) | mednafen_vb | `vb` `vboy` `bin` |

### CD-based systems

| System | Core | Formats |
| --- | --- | --- |
| Sony PlayStation (PS) | pcsx_rearmed | `chd` `cue` `bin` `img` `iso` `pbp` `toc` `mdf` `cbn` `m3u` `exe` |
| Sega CD (SEGACD) | picodrive | `chd` `cue` `bin` `iso` `m3u` |

`.chd` is the recommended format for both — single file per disc,
compressed, no extraction.

### Computers & other

| System | Core | Formats |
| --- | --- | --- |
| Amiga (PUAE) | puae2021 | `adf` `adz` `dms` `fdi` `ipf` `hdf` `hdz` `lha` `slave` `info` `cue` `ccd` `iso` `chd` `uae` `m3u` (zip/7z native) |
| Amstrad CPC (CPC) | cap32 | `dsk` `sna` `tap` `cdt` `voc` `cpr` `m3u` (zip native) |
| Commodore 64 (C64) / 128 (C128) / PET / Plus4 / VIC-20 | VICE | `d64` `d71` `d81` `g64` `x64` `t64` `tap` `prg` `p00` `crt` `bin` `m3u` `vsf` and more (zip/7z/gz native) |
| Microsoft MSX (MSX) | bluemsx | `rom` `ri` `mx1` `mx2` `dsk` `cas` `m3u` |
| Doom (PRBOOM) | prboom | `wad` `iwad` `pwad` `lmp` |
| Arcade (FBN) | fbneo | `zip` `7z` romsets — see [Arcade](arcade.md) |

### Standalone emulators

| System | Emulator | Formats |
| --- | --- | --- |
| Nintendo 64 (N64) | mupen64plus | `z64` `n64` `v64` |
| Nintendo DS (NDS) | DraStic | `nds` |
| DreamCast (DC) | Flycast | `chd` `gdi` `cdi` `cue` + Naomi/Atomiswave `zip` — see [Dreamcast](dreamcast.md) |

[Additional emulators](additional.md) installed from the
[Xtras store](../apps/xtras.md) or as community paks follow their own
emulator's formats.
