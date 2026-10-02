# PlayStation

NX Redux plays PlayStation games with the built-in **PCSX-ReARMed** core.

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
