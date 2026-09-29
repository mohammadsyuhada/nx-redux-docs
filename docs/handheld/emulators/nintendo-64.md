# Nintendo 64

Nintendo 64 games run on a bundled standalone **Mupen64Plus** emulator. Put
your ROMs in `Roms/Nintendo 64 (N64)/`.

## Controls

| Device button | N64 button (Nintendo layout) | N64 button (Xbox layout) |
| --- | --- | --- |
| Right (`A` on the cap) | A | B |
| Bottom (`B` on the cap) | B | A |
| Top (`X` on the cap) | C-Left | C-Down |
| Left (`Y` on the cap) | C-Down | C-Left |
| Right stick | C-Up / C-Down / C-Left / C-Right | same |
| Left stick | Analog stick | same |
| D-pad | D-pad | same |
| `L1` / `R1` | L / R | same |
| `L2` | Z | same |
| `START` | Start | same |

Unlike Dreamcast, the N64 face buttons follow the
[Button Layout](../guide/button-layout.md) setting. N64 A and B stay on
whichever buttons act as `A` and `B`. The two C buttons on the face follow
`X` and `Y`.

All four C buttons are on the right stick. C-Left and C-Down are also on the
face, so you can press the two C buttons most games use for items or actions
without letting go of the stick. C-Up and C-Right exist only on the right stick.

!!! note "Brick: no analog sticks"
    The **Brick** has no sticks, so most games (Mario Kart 64, Super Mario 64)
    won't move. Set the
    [FN switch's Dpad mode](../settings/fn-switch.md#dpad-mode-when-fn-is-on)
    to `Joystick` or `Both`, and flip the switch on to steer with the D-pad.

??? info "More detail"
    - A stick push counts as a C-button press once it is most of the way
      over.
    - On the Brick, the D-pad normally drives the N64 D-pad, not the analog
      stick. That's why games won't move until you change the FN switch.
    - C-Up and C-Right have no button on the Brick.

## Video plugin

Two video plugins are bundled, and each game can use whichever one you pick:

| Plugin | Best for | Texture packs |
| --- | --- | --- |
| **GLideN64** | More accurate rendering, and the fullest set of Emulator Options sections. Heavier on the hardware. | Yes, the only plugin that loads them |
| **Rice** | Much lighter to run | No |

The default plugin depends on your device.

To change it:

1. Open the N64 emulator's options:
    - For all games: [Tools → Emulator Settings](../apps/emulator-settings.md)
      → *Nintendo 64 (Mupen64Plus)*.
    - For one game: its [context menu](../guide/context-menu.md) →
      *Emulator Options*. A per-game choice overrides the system-wide
      default.
2. In **Video Plugin**, the first option section, choose `GLideN64` or
   `Rice`.
3. Restart the game. The change takes effect the next time the game starts.

See [Emulator Options](../guide/emulator-options.md) for how these fit
together.

!!! warning "Rice has no true widescreen"
    Rice's **16:9** and **Stretch** modes only stretch the 4:3 picture rather
    than widening the view. Keep Rice on **4:3** for correct geometry. Switch
    to **GLideN64** for a proper widescreen picture, since it adjusts the
    game's field of view.

??? info "More detail"
    **Default plugin per device.** Existing installs pick up their
    platform's default automatically the next time you launch an N64 game or
    open its options.

    | Device | Default plugin |
    | --- | --- |
    | Brick | Rice |
    | Brick Pro | Rice |
    | Smart Pro | Rice |
    | Smart Pro S | GLideN64 |

    **Rice performance.** On the **Brick** in testing, Rice used roughly 2.6×
    less CPU and produced far fewer audio underruns than GLideN64.

    **Option sections follow the selected plugin.** The Emulator Options
    sections change with **Video Plugin**: pick a plugin, press **B** back to
    the section list, and that plugin's sections appear.

    - GLideN64 has the full set: Rendering, Texture Enhancement, Hi-Res
      Textures, Dithering, Frame Buffer, Performance, Gamma.
    - Rice has its own smaller set: **Rendering**, **Texture Enhancement**,
      **Frame Buffer** and **Performance**.
    - High-resolution texture packs still load under **GLideN64 only**.

    **Same behaviour on both plugins.** The in-game menu (Continue / Save
    State / Load State / Quit), quit-autosave and Game Switcher resume all
    behave the same on both plugins.

    **Aspect ratio on 16:9 screens.** On the 16:9 **Smart Pro** and
    **Smart Pro S** panels, Rice keeps the 4:3 N64 picture with black bars
    down each side by default, the same as GLideN64. To change it, open
    **Emulator Options → Rendering → Aspect Ratio** (4:3 / 16:9 / Stretch)
    while Rice is the selected plugin. The 4:3 **Brick** and **Brick Pro**
    panels are unaffected. Rice cannot render true widescreen.

## High-resolution texture packs

Rice-format texture packs are supported (with limitations due to 1 GB RAM).

!!! note "Texture packs need GLideN64"
    Despite the "Rice-format" name, packs load only under the **GLideN64**
    [video plugin](#video-plugin), **not** Rice. On devices that default to
    Rice (Brick, Brick Pro and Smart Pro), switch the game to GLideN64 first.

1. Place the pack in `Roms/Nintendo 64 (N64)/.hires_texture/<ROM NAME>/`.
   `<ROM NAME>` is the ROM's **internal header name** (e.g. `MARIOKART64`),
   not its filename.
2. Launch the game. The first launch converts the pack, with an on-screen
   progress display. Large packs take several minutes.
3. Later launches start fast.

??? info "More detail"
    - **Finding the header name:** run the game once and look for the
      `Core: Name:` line in `.userdata/<platform>/logs/N64.txt`.
    - **The cache:** the pack is converted into a cache in
      `Roms/Nintendo 64 (N64)/.cache/`. It needs extra free space on the SD
      card (e.g. a 2.6 GB pack produces a ~450 MB cache). Later launches load
      straight from the cache.

## Netplay

Nintendo 64 [Netplay](../netplay.md) supports up to 4 players.

!!! warning "Player count depends on the device"
    3–4 players need a **Smart Pro S** on *every* seat. On the **Smart Pro /
    Brick / Brick Pro**, N64 netplay is limited to **2 players** (as host or
    joiner).

??? info "More detail"
    N64 renders a separate split-screen viewport per player. On the Smart
    Pro, Brick and Brick Pro, the GPU can't hold full speed past a 2-way
    split.
