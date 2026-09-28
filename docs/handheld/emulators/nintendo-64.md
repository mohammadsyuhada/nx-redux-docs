# Nintendo 64

Nintendo 64 games run on a bundled standalone **Mupen64Plus** emulator. Put
your ROMs in `Roms/Nintendo 64 (N64)/`.

## Video plugin

Two video plugins are bundled, and each game can use whichever one you pick:

- **GLideN64** — more accurate rendering and the only plugin that loads
  high-resolution texture packs, with the fullest set of Emulator Options
  sections. Heavier on the hardware.
- **Rice** — much lighter to run: on the **Brick** in testing it used roughly
  2.6× less CPU and produced far fewer audio underruns than GLideN64. Rice does
  not load texture packs, and has its own smaller set of Emulator Options
  sections.

!!! note "Option sections follow the selected plugin"
    The Emulator Options sections change with **Video Plugin**: pick a plugin,
    press **B** back to the section list, and that plugin's sections appear.
    GLideN64 has the full set (Rendering, Texture Enhancement, Hi-Res Textures,
    Dithering, Frame Buffer, Performance, Gamma); Rice has **Rendering**,
    **Texture Enhancement**, **Frame Buffer** and **Performance**.
    High-resolution texture packs still load under **GLideN64 only**.

The default plugin depends on the device: the **Brick**, **Brick Pro** and
**Smart Pro** default to **Rice**; the **Smart Pro S** defaults to
**GLideN64**. Existing installs pick up their platform's default automatically
the next time you launch an N64 game or open its options.

**Video Plugin** is the first option section for the N64 emulator (values
`GLideN64` and `Rice`). Set it system-wide from
[Tools → Emulator Settings](../apps/emulator-settings.md) → *Nintendo 64
(Mupen64Plus)*, or for a single game from its
[context menu](../guide/context-menu.md) → *Emulator Options*; a per-game
choice overrides the system-wide default. See
[Emulator Options](../guide/emulator-options.md) for how these fit together.

!!! note "Restart the game to apply"
    A change to the video plugin takes effect the next time the game starts.
    The in-game menu (Continue / Save State / Load State / Quit), quit-autosave
    and Game Switcher resume all behave the same on both plugins.

!!! note "Aspect ratio on 16:9 screens"
    On the 16:9 **Smart Pro** and **Smart Pro S** panels, Rice keeps the 4:3
    N64 picture with black bars down each side by default, the same as GLideN64.
    To change it, open **Emulator Options → Rendering → Aspect Ratio** (4:3 /
    16:9 / Stretch) while Rice is the selected plugin. The 4:3 **Brick** and
    **Brick Pro** panels are unaffected.

!!! warning "Rice has no true widescreen"
    Rice's **16:9** and **Stretch** modes only rescale the 4:3 image, so they
    stretch the picture rather than widening the view. Rice cannot render true
    widescreen. Keep Rice on **4:3** for correct geometry, and switch to
    **GLideN64** if you want a proper widescreen picture, since it adjusts the
    game's field of view.

## High-resolution texture packs

!!! note "Texture packs need GLideN64"
    High-resolution texture packs load only under the **GLideN64**
    [video plugin](#video-plugin) — despite the "Rice-format" name, they do
    **not** work with the Rice plugin. On devices that default to Rice (Brick,
    Brick Pro and Smart Pro), switch a game that uses a texture pack to GLideN64
    first.

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
