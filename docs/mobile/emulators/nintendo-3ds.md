# Nintendo 3DS

Nintendo 3DS games run on the bundled **Azahar** core, which draws both
screens.

| | Azahar |
| --- | --- |
| Folder | `Roms/Nintendo 3DS (3DS)/` |
| BIOS | Not needed |
| [File types](index.md) | Decrypted `3ds` `cci` `cxi` `3dsx`, and their compressed versions `zcci` `zcxi` `z3dsx` |

- **Encrypted games don't load.** Decrypt them first.
- `.cia` install files are not supported.
- **Graphics API** can switch a game to Vulkan. See
  [Graphics API](index.md#graphics-api).

## Controls

<div class="nx-phones" markdown>
<div markdown>
<figure class="nx-phone" markdown>
![Mario Kart 7 on the Fold's cover screen, with the 3DS pad: L and R, no ZL, ZR or C-stick, and STYLUS and SWAP beside MENU and STICK](../../assets/screenshots/mobile/pad-3ds-regular.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>
<p class="nx-phones__caption">The 3DS pad</p>
</div>
<div markdown>
<figure class="nx-phone" markdown>
![Mario Kart 7 on the Fold's cover screen, with the 3DS pad and the New 3DS controls: ZL, ZR and the C-stick](../../assets/screenshots/mobile/pad-3ds.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>
<p class="nx-phones__caption">With <a href="#new-3ds-controls">New 3DS controls</a></p>
</div>
</div>

The on-screen pad is laid out like a 3DS. `STICK` / `D-PAD` switches between
the d-pad and the Circle Pad. Games that use the New 3DS buttons also get
`ZL`, `ZR` and the C-stick: see [New 3DS controls](#new-3ds-controls).

The pad also has **STYLUS**, which turns [stylus mode](#stylus-mode) on or
off (pressed in while it's on), and **SWAP**, which swaps the screens. In
portrait they sit either side of `MENU` and `STICK`; over the game
(landscape, or portrait with the [pad hidden](#portrait-pad)) **STYLUS** is
under `MENU` and **SWAP** under `START`.

On a controller the shortcuts are `SELECT` combos, because `L2` and `R2` are
the 3DS's own `ZL` and `ZR`:

| Buttons | What they do |
| --- | --- |
| `SELECT` + `R1`, or **SWAP** | Swap the screens. |
| `SELECT` + `L1`, or **STYLUS** | Turn stylus mode on or off. |
| `SELECT` + `LEFT` / `RIGHT` | Change the layout of the orientation you're in: **Top over bottom**, **Large screen**, **Side by side**, **Single screen**, and round again. |
| `SELECT` + `START`, or `MENU` | Open the [in-game menu](../in-game-menu.md). |

A controller adds:

| Control | Nintendo 3DS |
| --- | --- |
| `L2`, `R2` | `ZL`, `ZR`, also on controllers whose triggers are analog only |
| Left stick | The Circle Pad |
| Right stick | The C-stick, and the touch cursor |
| `R3` (press the right stick) | Tap at the cursor |
| `L3` (press the left stick) | Swap the screens |

A controller's face buttons work as printed: its `A` is the 3DS's `A`. To
use the 3DS's positions on an Xbox pad (`A` on the right), set
**Controller Layout** to **Nintendo** in **Options → Console Settings**; see
[Controls](../controls.md#controller-buttons).

!!! note "`SELECT` waits"
    The game gets `SELECT` when you let go of it, so a combo doesn't pause
    the game.

??? info "More detail: `SELECT`"
    Many 3DS games pause on Select, so the game never sees `SELECT` while you
    hold it:

    - Tap it and the game gets `SELECT` when you let go.
    - Hold it longer than 1 second without a combo and nothing is sent.
    - After a combo (`SELECT` + `R1`, `L1`, `LEFT`, `RIGHT` or `START`) the
      game gets nothing.

### New 3DS controls

**New 3DS Controls** adds `ZL` and `ZR` and the C-stick to the on-screen pad.
Set it for the console in [Emulator Settings](../emulator-settings.md), or
in the in-game menu under **Options → Console Settings**, where
[Save Changes](../in-game-menu.md#save-changes) keeps it for the game or the
console:

| Value | What the pad shows |
| --- | --- |
| **Auto** (default) | The extra controls for games known to use them, such as Majora's Mask 3D (camera). |
| **On** | The extra controls for every game. |
| **Off** | No extra controls. |

A controller's right stick, `L2` and `R2` always reach the game, whatever
the setting. Azahar runs as a New 3DS, so Circle Pad Pro games work without
extra setup.

??? info "More detail"
    - **Auto** covers games that use the C-stick, `ZL` / `ZR` or the Circle
      Pad Pro, such as Majora's Mask 3D, Monster Hunter 4 Ultimate and
      Xenoblade Chronicles 3D.
    - `ZL` and `ZR` sit where `L2` and `R2` are on other consoles. The
      C-stick is centred under `SELECT` and `START` in portrait, and at the
      top left of the face buttons in landscape.
    - A change in the in-game menu updates the pad straight away.

    **Auto** finds the game by the title ID in `.3ds`, `.cci` and `.cxi`
    files. It can't read the compressed `zcci`, `zcxi` and `z3dsx` files or
    `3dsx` files, so for those set **On** yourself.

## Console Settings

The 3DS's own options are in the in-game menu under **Options → Console
Settings**, and for the console in
[Emulator Settings](../emulator-settings.md). `LEFT` / `RIGHT` change a
value; keep it for the game or the console with
[Save Changes](../in-game-menu.md#save-changes).

![Console Settings of a 3DS game in landscape: the three Layout rows, New 3DS Controls, Portrait Pad and Controller Layout](../../assets/screenshots/mobile/3ds-console-settings.webp){ .nx-wide }

| Row | Values | Default | See |
| --- | --- | --- | --- |
| **Layout (portrait)** | Top over bottom, Large screen, Side by side, Single screen | Top over bottom | [Screen layouts](#screen-layouts) |
| **Layout (portrait, controller)** | The same | Top over bottom | [Screen layouts](#screen-layouts) |
| **Layout (landscape)** | The same | Top over bottom | [Screen layouts](#screen-layouts) |
| **New 3DS Controls** | Auto, On, Off | Auto | [New 3DS controls](#new-3ds-controls) |
| **Portrait Pad** | Shown, Hidden | Shown | [Portrait pad](#portrait-pad) |
| **Controller Layout** | Auto-detect, Xbox (A at the bottom), Nintendo (A on the right) | Auto-detect | [Controls](../controls.md#controller-buttons) |

Every row takes effect straight away; none needs the game restarted.
**Graphics API** is read only when a game starts, so it's not here: set it
in [Game Settings](../emulator-settings.md#game-settings) or Emulator
Settings (see [Graphics API](index.md#graphics-api)).

## Screen layouts

<div class="nx-layouts" markdown>

| Layout | Picture |
| --- | --- |
| **Top over bottom** (default)<br>The top screen above the bottom screen. In landscape the top screen takes three quarters of the height and the bottom screen is a third of its size. | [![Mario Kart 7, Top over bottom: the top screen above the bottom screen](../../assets/screenshots/mobile/3ds-portrait-top-over-bottom.webp)](../../assets/screenshots/mobile/3ds-portrait-top-over-bottom.webp) |
| **Large screen**<br>The top screen big, the bottom screen small at its top right. | [![Mario Kart 7, Large screen: the top screen big, the bottom screen small at its top right](../../assets/screenshots/mobile/3ds-portrait-large.webp)](../../assets/screenshots/mobile/3ds-portrait-large.webp) |
| **Side by side**<br>The two screens next to each other. | [![Mario Kart 7, Side by side: the two screens next to each other](../../assets/screenshots/mobile/3ds-portrait-side-by-side.webp)](../../assets/screenshots/mobile/3ds-portrait-side-by-side.webp) |
| **Single screen**<br>Only the top screen. | [![Mario Kart 7, Single screen: only the top screen](../../assets/screenshots/mobile/3ds-portrait-single.webp)](../../assets/screenshots/mobile/3ds-portrait-single.webp) |

</div>

The pictures are in portrait; landscape draws the same layouts across the
wider screen. **SWAP** (or `SELECT` + `R1`) swaps which screen is the big
or upper one, in every layout.

As on the DS, each orientation keeps its own layout: **Layout (portrait)**
and **Layout (landscape)** in [Console Settings](#console-settings), all
**Top over bottom** by default. With a controller connected the on-screen
pad goes away in portrait and **Layout (portrait, controller)** is used.
`SELECT` + `LEFT` / `RIGHT` changes the one you're in and saves it for the
game straight away, without Save Changes.

??? info "More detail"
    - The app sets Azahar's own **Screen Layout** option from the layout rows,
      so in **Core Options** it shows locked.
    - **Screen Swap Mode** in **Core Options** sets whether the swap toggles
      (the default) or lasts only while you hold the buttons.

## Motion

Games that use the 3DS's gyroscope and tilt read your phone's: turn or tip
the phone the way you would turn or tip a 3DS. In Mario Kart 7's first-person
view, for example, you steer by turning the phone.

![Mario Kart 7's first-person view, steered by turning the phone](../../assets/screenshots/mobile/3ds-motion.webp)

Motion is always on, like on a 3DS. Hold the phone the way the game expects,
as you would a 3DS.

??? info "More detail"
    - There's no setting for motion.
    - It works in portrait and in both landscape directions. The game reads
      the phone's tilt as it is.
    - The sensors only run while you play. They stop while the game is
      paused, in the in-game menu, or in the background.
    - On a phone without a gyroscope, tilting still works, but aiming by
      turning the phone does nothing.

## Stylus mode

In stylus mode a dot on the bottom screen is the pen, for touching it without
your finger.

| Control | What it does |
| --- | --- |
| D-pad or left stick | Move the dot. The d-pad speeds up the longer you hold it. |
| `A` | Touch at the dot. |
| **STYLUS**, or `SELECT` + `L1` on a controller | Turn stylus mode on or off. |

Stylus mode is off each time a game starts, and is not saved.

## Touch

Touch the bottom screen wherever it is drawn, as long as the on-screen
buttons aren't over the game: in portrait with the pad band, or with a
controller.

While the on-screen buttons are over the game (landscape without a
controller, or portrait with the [pad hidden](#portrait-pad)), only the main
screen takes touches: the big one, or the first (top or left) when both are
the same size.

**For games that need buttons and touch together**, press **SWAP** to make
the bottom screen the main one. Then touch it anywhere between the buttons
while you play with them. A layout with one big screen gives it the most
room.

??? info "More detail"
    - The see-through buttons still take the touches that land on them. To
      reach something under a button, such as a menu item in a corner of the
      bottom screen, use [stylus mode](#stylus-mode), whose pen reaches the
      bottom screen either way, or turn the phone to portrait.

## Portrait pad

In portrait, long-press the arrow in the pad's bottom-right corner to hide
the pad band. The two screens get its room, and the see-through landscape
buttons sit over the lower half of the game instead. The arrow stays in the
corner: long-press it again to bring the band back. A plain tap does
nothing.

<div class="nx-phones" markdown>
<div markdown>
<figure class="nx-phone" markdown>
![Mario Kart 7 in portrait with the pad band shown, the arrow in its bottom-right corner ringed](../../assets/screenshots/mobile/3ds-portrait-pad-shown-arrow.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>
<p class="nx-phones__caption">Pad shown</p>
</div>
<div markdown>
<figure class="nx-phone" markdown>
![Mario Kart 7 in portrait with the pad hidden: the two screens fill the height, the see-through buttons over the lower half, the arrow ringed](../../assets/screenshots/mobile/3ds-portrait-pad-hidden-arrow.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>
<p class="nx-phones__caption">Pad hidden</p>
</div>
</div>

The choice is **Portrait Pad** (Shown or Hidden) in **Options → Console
Settings**, and the long-press saves it for the console.

??? info "More detail"
    - Touch follows the [touch rule](#touch): swap the bottom screen up with
      **SWAP** to touch it, or use [stylus mode](#stylus-mode).
    - With a controller connected the see-through buttons hide too, as in
      landscape.
    - Landscape is not affected.

## Cheats and achievements

- Cheats: not available. Azahar's libretro core doesn't support them, so the
  in-game menu has no **Cheats** page for 3DS games.
- RetroAchievements: not available for 3DS games in the app.
