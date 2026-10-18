# Nintendo 64

Nintendo 64 games run on the bundled **Mupen64Plus-Next** core.

| | Mupen64Plus-Next |
| --- | --- |
| Folder | `Roms/Nintendo 64 (N64)/` |
| BIOS | Not needed |
| [File types](index.md) | `n64` `z64` `v64` (also inside a zip or 7z) |

## Controls

<figure class="nx-phone" markdown>
![Super Mario 64 on the Fold's cover screen, with the Nintendo 64 pad: A, B, the yellow C buttons and Z](../../assets/screenshots/mobile/pad-n64.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>

The Nintendo 64 maps a controller **by the printed letter**, like every
Nintendo console: the button printed `A` is the N64's `A`.

| Controller | Nintendo 64 |
| --- | --- |
| `A`, `B` | `A`, `B` |
| `X` | C-Left |
| `Y` | C-Down |
| `L1`, `R1` | `L`, `R` |
| `L2` | `Z` |
| `START` | `START` |
| Left stick | Analog stick |
| Right stick | The C buttons |
| `R2`, `SELECT` | Nothing |

- The on-screen pad draws `A`, `B` and a yellow C-button diamond, with `Z` on
  `L2`. It has no `SELECT`.
- `MENU`, or `SELECT` + `START`, still opens the
  [in-game menu](../in-game-menu.md).

??? info "More detail"
    **Controller Layout** in **Options → Console Settings** names your
    controller's letters if it is read wrongly. Set it to the layout that
    isn't your controller's to swap `A`/`B` and `X`/`Y`; see
    [Controls](../controls.md#controller-buttons).

## Rumble

Rumble is off out of the box: the controller holds the Controller Pak (for
saves) instead. To turn it on:

1. Open [Emulator Settings](../emulator-settings.md) for the console, or
   **Game Settings** for one game.
2. Under **Core settings → Pak/Controller Options**, set **Player 1 Pak** to
   **rumble**.
3. Start the game again.

Only games that support the Rumble Pak rumble, such as Super Smash Bros.
Mario Kart 64 doesn't. See [Vibration](../controls.md#game-rumble).

Up to four players can play, each on their own controller; see
[Local Multiplayer](../multiplayer.md).

??? info "More detail"
    - The Rumble Pak takes the Controller Pak's place.
    - Each player has their own setting, from **Player 1 Pak** to **Player 4
      Pak**.

## Settings

- Video uses the **GLideN64** plugin. With **Graphics API** set to
  **Vulkan**, it switches to the paraLLEl plugins: more accurate, and
  heavier. See [Graphics API](index.md#graphics-api).
- Many video options, such as the resolution, only take effect when a game
  starts. They are in [Emulator Settings](../emulator-settings.md), not in
  the in-game **Core Options**.
