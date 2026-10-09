# PlayStation

NX Redux plays PlayStation games with the built-in **PCSX-ReARMed** core, and
ships **[SwanStation](#swanstation)** as a second, more accurate core.

| | PCSX-ReARMed |
| --- | --- |
| Folder | `Roms/Sony PlayStation (PS)/` |
| BIOS | Recommended: `psxonpsp660.bin` or `scph1001.bin` in `Bios/PS/` |
| [Netplay](../netplay.md) | Yes |
| [File types](rom-formats.md) | `chd` `cue` `bin` `img` `iso` `pbp` `toc` `mdf` `cbn` `m3u` `exe` |

Every device runs PlayStation games at full speed at the native resolution.

!!! warning "Use a real BIOS"
    The core has a built-in fallback BIOS, but some games only work with a
    real one. See [Cores & BIOS Files](cores.md).

## Enhanced Resolution

**Enhanced Resolution** renders 3D games at twice the native resolution, for
sharper models and textures. Turn it on in the game's
[emulator options](../guide/emulator-options.md).

!!! tip "Turn on Threaded Rendering with it"
    On its own, Enhanced Resolution slows heavy 3D games to about 40 fps.
    Turn on **Threaded Rendering** in the same options as well, and the game
    runs at a steady 60 fps again.

    Leave Threaded Rendering off when you play at the native resolution. It
    doesn't help there, and on the Smart Pro S it costs a few fps.

Both options are off by default. Measured in a Wipeout 3 race:

| Setup | Brick | Smart Pro S |
| --- | --- | --- |
| Native resolution (default) | Full speed | Full speed |
| Enhanced Resolution | About 40 fps | About 40 fps |
| Enhanced Resolution + Threaded Rendering | Full speed | Full speed |

??? info "More detail"
    Enhanced Resolution only applies to games that run in the standard
    resolution modes. Games that already use a high-resolution mode, and
    full-motion video, are shown as they are. Threaded Rendering moves the
    drawing work onto its own CPU core, so it no longer slows the emulation
    down.

## SwanStation

**SwanStation** is a second PlayStation system built on a more accurate
emulator. It draws 3D games with the device's GPU at twice the native
resolution, for sharper models and textures with no extra setup.

To use it, copy or move a game into `Roms/Sony PlayStation (PSX)/`. Both
folders show up together under **Sony PlayStation** in the main menu; the
folder a game is in decides which core plays it.

| | SwanStation |
| --- | --- |
| Folder | `Roms/Sony PlayStation (PSX)/` |
| BIOS | Recommended: `scph5500.bin` (Japan), `scph5501.bin` (USA), `scph5502.bin` (Europe) in `Bios/PSX/` |
| [Netplay](../netplay.md) | Yes, with another player on SwanStation |
| [File types](rom-formats.md) | `chd` `cue` `bin` `img` `iso` `pbp` `ecm` `mds` `m3u` `exe` `psexe` `psf` |

- **It has its own BIOS folder.** Without a BIOS file the core uses a
  built-in OpenBIOS, which runs most games; copy your real BIOS into
  `Bios/PSX/` for full compatibility.
- **Saves are separate.** SwanStation keeps its own memory cards
  (`Saves/PSX/`), save states and settings. Progress made in the
  PCSX-ReARMed version of a game does not carry over.

Use PCSX-ReARMed by default, and SwanStation for games that glitch on it or
when you want the sharper picture. SwanStation runs at full speed on every
device but works the CPU harder, so the odd frame takes longer: measured
2026-10-09, about 3 hitches a minute against none on PCSX-ReARMed.

| Measured (60 s) | Brick | Smart Pro S |
| --- | --- | --- |
| PCSX-ReARMed, native resolution | Full speed, 58% CPU | Full speed, 40% CPU |
| SwanStation, 2× resolution (default) | Full speed, 77% CPU | Full speed, 74% CPU |

??? info "More detail"
    The resolution, the renderer (hardware or software) and PGXP geometry
    correction, which removes the wobble of PlayStation 3D, are in the
    game's [emulator options](../guide/emulator-options.md). Native
    resolution saves a little CPU on the Brick; the software renderer looks
    like real hardware.
