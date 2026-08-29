# Nintendo 64

Nintendo 64 games run on a bundled standalone **Mupen64Plus** emulator. Put
your ROMs in `Roms/Nintendo 64 (N64)/`.

## High-resolution texture packs

Rice-format texture packs are supported (with limitations due to 1 GB RAM):

1. Place the pack in `Roms/Nintendo 64 (N64)/.hires_texture/<ROM NAME>/`,
   where `<ROM NAME>` is the ROM's **internal header name** (e.g.
   `MARIOKART64`), not its filename. To find it, run the game once and look
   for the `Core: Name:` line in `.userdata/<platform>/logs/N64.txt`.
2. On the game's first launch the pack is converted into a cache in
   `Roms/Nintendo 64 (N64)/.cache/` with an on-screen progress display — large
   packs take several minutes and need extra free space on the SD card (e.g. a
   2.6 GB pack produces a ~450 MB cache).
3. Later launches load straight from the cache and start fast.

## Netplay

Nintendo 64 [Netplay](../netplay.md) supports up to 4 players.

!!! warning "Player count depends on the device's GPU"
    N64 renders a separate split-screen viewport per player, so 3–4 players
    need a **Smart Pro S** on *every* seat. On the **Smart Pro / Brick /
    Brick Pro** the GPU can't hold full speed past a 2-way split, so N64
    netplay there is limited to **2 players** (as host or joiner).
