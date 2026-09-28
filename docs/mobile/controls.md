# Controls

## On-screen pad and controllers

Without a controller the app shows an on-screen pad. Connect any Android
controller to play with real buttons instead.

- **Portrait:** the pad sits in a band below the game. On Nintendo DS, the
  band goes away while a controller is connected, so both screens get the full
  height (see [Nintendo DS](emulators.md#nintendo-ds)).
- **Landscape:** the buttons sit in two clusters over the game. **Pad Opacity
  (landscape)** sets how opaque they are: 100, 60, 40 or 25 % (40 % by
  default). It is in the in-game menu under **Options →
  [Frontend](in-game-menu.md#frontend)**, not in Settings, and it is saved per
  game or console with Save Changes.

### Pad themes

**Pad theme** in **Tools → Settings → [Appearance](appearance.md)** colors
the portrait pad:

| Theme | Look |
| --- | --- |
| **Charcoal** (default) | The dark pad |
| **Retro** | A light grey body with magenta face buttons |

The landscape clusters always stay Charcoal.

<!-- SCREENSHOT: pad-themes — portrait pad in Charcoal and Retro side by side -->

### Controller buttons

A controller's buttons map to the NX Redux buttons by their Android names:

| Controller | NX Redux |
| --- | --- |
| `A`, `B`, `X`, `Y` | `A`, `B`, `X`, `Y` |
| `L1`, `R1`, `L2`, `R2` | `L1`, `R1`, `L2`, `R2` |
| `START`, `SELECT` | `START`, `SELECT` |
| Mode button (Android's `BUTTON_MODE`) | `MENU` |
| D-pad | `UP`, `DOWN`, `LEFT`, `RIGHT` |
| Left and right sticks | The core's analog sticks |

The mapping is fixed: there is no button remapping in the app. On a
controller without a mode button, hold `SELECT` and `START` together to open
the in-game menu.

Menus show key hints you can tap when a controller or the on-screen pad is
present, and real buttons in landscape without one.

## In the menus

| Button | What it does |
| --- | --- |
| `A` | Open or start the highlighted item |
| `B` | Back. Android's Back gesture does the same. |
| `X` | In a game list, resume the highlighted game when it can be resumed |
| `SELECT` | Open the [Game Switcher](game-switcher.md) |
| `MENU`, or a long press | Open the game-list context menu |

## Game-list context menu

Press `MENU`, or long-press a game, for the same context menu as on the
handheld:

- **Pin Item / Unpin Item**
- **Hide Game**
- **Rename Rom** (writes a `map.txt` alias; the file is never renamed)
- **Add to / Remove from Collection**
- **Remove from Recently Played**
- **Emulator** to run a game on a console's other emulator, or **Console** to
  give an Unassigned game its console (see
  [Library & ROM folders](library.md#unassigned-games))

## In-game menu

Press `MENU`, hold `SELECT` + `START`, or use Android's Back gesture during a
game. The menu has save states, Frontend, Shaders, Core Options, Cheats,
Achievements and Save Changes. See [In-game Menu](in-game-menu.md).
