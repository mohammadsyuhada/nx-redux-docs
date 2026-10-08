# Nintendo 64

Nintendo 64 games run on the bundled **Mupen64Plus-Next** core.

| | Mupen64Plus-Next |
| --- | --- |
| Folder | `Roms/Nintendo 64 (N64)/` |
| BIOS | Not needed |
| [File types](index.md) | `n64` `z64` `v64` (also inside a zip or 7z) |

## Controls

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
- **Controller Layout** in **Options → Console Settings** names your
  controller's letters if it is read wrongly. Set it to the layout that
  isn't your controller's to swap `A`/`B` and `X`/`Y`; see
  [Controls](../controls.md#controller-buttons).

## Rumble

The controller holds the Controller Pak (for saves) out of the box. To feel a
game's rumble, set **Player 1 Pak** to **rumble** under **Core settings →
Pak/Controller Options**, in [Emulator Settings](../emulator-settings.md) for
the console or **Game Settings** for one game. The Rumble Pak takes the
Controller Pak's place. Start the game again for the change to take effect.
See [Vibration](../controls.md#game-rumble).

Up to four players can play, each on their own controller; see
[Local Multiplayer](../multiplayer.md). Each player has their own setting,
from **Player 1 Pak** to **Player 4 Pak**. Only games that support the
Rumble Pak rumble, such as Super Smash Bros. Mario Kart 64 doesn't.

## Settings

- Video uses the **GLideN64** plugin. The paraLLEl plugins are not offered:
  they need Vulkan, which the app doesn't use.
- Many video options, such as the resolution, only take effect when a game
  starts. They are in [Emulator Settings](../emulator-settings.md), not in
  the in-game **Core Options**.
