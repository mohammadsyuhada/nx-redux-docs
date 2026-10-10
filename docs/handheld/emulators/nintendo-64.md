# Nintendo 64

Nintendo 64 games run on the **Mupen64Plus-Next** core, the same way as the
other built-in systems: the in-game menu, save states with screenshots,
[RetroAchievements](../apps/retroachievements.md), [cheats](../apps/cheats.md),
the Game Switcher and quit-autosave all work as they do everywhere else, and
ROMs can be zipped. Put your ROMs in
`Roms/Nintendo 64 (N64)/`.

!!! info "Coming from an older NX Redux"
    N64 used to run on a separate, standalone emulator. Your game saves come
    along on their own: the **first time** you start a game after updating, its
    in-game saves and Controller Pak data are copied over (the old files are
    left untouched). **Save states don't carry over**, so make an in-game save
    before you update. Texture packs stay where they were.

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
You can remap everything in the in-game menu under **Controls**.

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

Two video plugins are built in, and each game can use whichever one you pick:

| Plugin | Best for | Texture packs |
| --- | --- | --- |
| **GLideN64** | More accurate rendering. Heavier on the hardware. | Yes, the only plugin that loads them |
| **Rice** | Much lighter to run | No |

The default plugin depends on your device:

| Device | Default plugin |
| --- | --- |
| Brick | Rice |
| Brick Pro | Rice |
| Smart Pro | Rice |
| Smart Pro S | GLideN64 |

To change it:

1. Open the N64 emulator's options:
    - For all games: [Tools → Emulator Settings](../apps/emulator-settings.md)
      → *Nintendo 64 (mupen64plus-next)*.
    - For one game: its [context menu](../guide/context-menu.md) →
      *Emulator Options*. A per-game choice overrides the system-wide
      default.
2. Set **RDP Plugin** to `GLideN64` or `Rice`.
3. Restart the game. The change takes effect the next time the game starts.

See [Emulator Options](../guide/emulator-options.md) for how these fit
together.

!!! warning "Doom 64 needs GLideN64"
    With Rice, **Doom 64** shows a black screen. On the Brick, Brick Pro and
    Smart Pro, switch Doom 64 to **GLideN64** in its Emulator Options. It runs
    below full speed on the Brick, since GLideN64 is heavy on its GPU.

??? info "More detail"
    **Why Rice on the Brick-class devices.** In testing on the **Brick**, Mario
    Kart 64 ran at full speed with Rice, while GLideN64 kept the GPU close to
    its limit and fell behind in heavier games (Doom 64 at about two thirds of
    full speed).

    **Same behaviour on both plugins.** The in-game menu, save states,
    quit-autosave and Game Switcher resume behave the same on both plugins.

## High-resolution texture packs

Texture packs replace the N64's blurry textures with high-resolution ones.
They're **off by default** (they need a lot of memory on these 1 GB devices),
and they load only under the **GLideN64** [video plugin](#video-plugin).

<figure class="compare">
<img-comparison-slider>
  <img slot="first" width="100%" src="../../../assets/screenshots/n64-hires-textures-off.png" alt="Mario Kart 64 Game Select screen with the original, blurry textures">
  <img slot="second" width="100%" src="../../../assets/screenshots/n64-hires-textures-on.png" alt="The same screen with the Mario Kart 64 Reloaded texture pack: sharp lettering and character faces">
</img-comparison-slider>
<figcaption>Drag the slider: original textures (left), Mario Kart 64 Reloaded pack (right). Smart Pro S.</figcaption>
</figure>

### Where to get them

[evilgames.eu](https://evilgames.eu/texture-packs.htm) hosts a collection of
packs, among them *Mario Kart 64 Reloaded*, *Super Mario 64 Reloaded* and
*The Legend of Zelda: Ocarina of Time Reloaded*. Each pack's page offers
several downloads; pick the ones marked **GLideN64**:

| Download | What it is | Use it? |
| --- | --- | --- |
| **GLideN64 Cache** (`…-gliden64-hts-….7z`) | The ready-made cache: one `.hts` file inside a `.7z` archive | **Yes, recommended.** Nothing to convert, the game starts right away |
| **GLideN64 / rt64 Source** (`.zip`) | The pack as PNG images | Works too, but the first launch converts it into a cache (several minutes) |
| Dolphin, rt64, SpaghettiKart… | Packs for other emulators and PC ports | No |

Where a pack comes in **HD** and **4k**, take **HD**: it is much smaller and
loads faster. The 4k textures are far bigger than these screens can show.

### Installing a pack

1. Put the pack where the game looks for it:
    - **A ready-made cache** (a single `<NAME>_HIRESTEXTURES.hts` file) goes in
      `Roms/Nintendo 64 (N64)/.cache/`. This is the fastest way: the game
      starts right away. Extract the `.hts` file from the downloaded `.7z`
      first (on your computer, with e.g. 7-Zip); keep its file name as it is.
    - **A folder of PNG files** goes in
      `Roms/Nintendo 64 (N64)/.hires_texture/<ROM NAME>/`. `<ROM NAME>` is the
      ROM's **internal header name** (e.g. `MARIOKART64`), not its filename.
2. Open the game's *Emulator Options* (its context menu), set **RDP Plugin**
   to `GLideN64` if your device defaults to Rice, and turn on
   **Use High-Res textures**.
3. Launch the game. A PNG pack is converted into a cache on the first launch,
   with a *Processing hi-res textures (first time only)...* screen. Large packs
   take several minutes. Later launches start fast.

!!! tip "Pack instructions written for Mupen64Plus or RetroArch"
    Many packs (e.g. Mario Kart 64 Reloaded) list settings like
    `txHiresEnable`, `txHiresTextureFileStorage` and
    `CorrectTexrectCoords = Auto`. Only the first one is up to you (**Use
    High-Res textures**). The others are already the N64 defaults here, and the
    resolution is set to 2× native. Ignore the cache folder paths those
    instructions give for PC (`%appdata%`, `~/.cache`…): on NX Redux the
    `.hts` file goes in `Roms/Nintendo 64 (N64)/.cache/`.

??? info "More detail"
    - **Short stutters are normal.** Textures are read from the SD card the
      first time a scene uses them.
    - **Memory.** At most 200 MB of high-resolution textures stay loaded. While
      an N64 game runs with packs on the card, a 512 MB swap file on the
      internal storage backs this up (created on the first such launch).
      Tested with a 3.6 GB Mario Kart 64 cache on the Smart Pro S.
    - **Finding the header name:** run the game once and look for the
      `mupen64plus: Name:` line in `.userdata/<platform>/logs/N64.txt`.
    - **The cache** needs extra free space on the SD card (a 2.6 GB PNG pack
      produces a cache of roughly 450 MB).
    - **Use enhanced Texture Storage** only matters if you turn on one of the
      texture enhancement filters; it keeps the enhanced textures in a file
      instead of memory.

## Netplay

Nintendo 64 [Netplay](../netplay.md) supports up to 4 players.

!!! warning "Player count depends on the device"
    For 3–4 players, use a **Smart Pro S** on *every* seat. On the **Smart Pro /
    Brick / Brick Pro**, stick to **2 players** (as host or joiner).

??? info "More detail"
    - N64 renders a separate split-screen viewport per player. With
      GLideN64, the Smart Pro, Brick and Brick Pro GPUs can't hold full speed
      past a 2-way split (3–4 players haven't been tested with Rice).
    - Devices on different video plugins can play together (for example a
      Brick on Rice with a Smart Pro S on GLideN64): only the controller inputs
      travel between them. If a game ever drifts out of sync, set the same RDP
      Plugin for that game on every device.
    - Every device in a session must run the same NX Redux version.
