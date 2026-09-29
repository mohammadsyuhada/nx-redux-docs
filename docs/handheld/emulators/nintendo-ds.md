# Nintendo DS

Nintendo DS games run on a bundled **Drastic** emulator. Put your ROMs in
`Roms/Nintendo DS (NDS)/`.

## Controls

The face buttons, D-pad, shoulders, `START` and `SELECT` map to the DS as you
would expect. They follow the device-wide
[Button Layout](../guide/button-layout.md) setting. Under the Xbox layout the
bottom button is the DS `A`, in games and in the Drastic menu alike.

On top of that:

| Button | Action |
|--------|--------|
| `MENU` | Open the Drastic menu (save states, options, controls, cheats). |
| `L2` | Turn stylus mode on or off (see below). |
| `R2` | Swap which DS screen is the large one. |
| `SELECT` + `Left` / `Right` | Cycle the screen layout (how the two DS screens are arranged on the device's single screen). |
| `SELECT` + `Y` | Cycle the theme, or the stylus image while stylus mode is on. |

## Stylus mode

Many DS games need the touch screen. Press `L2` to turn stylus mode on. A pen
appears over the touch screen, and the D-pad drives it instead of the game.

<!-- SCREENSHOT: nds-stylus-mode — DS game in stylus mode, pen visible on the touch screen (Brick) -->

| Button | Action |
|--------|--------|
| `D-pad` or left stick | Move the pen. It speeds up the longer you hold a direction. |
| `A` | Tap at the pen's position. Hold `A` while moving to drag. |
| `SELECT` + `Y` | Cycle the pen image. |
| `L2` | Turn stylus mode off again. |

The other buttons keep going to the game, so you can play with the pen out.

!!! note "Turn stylus mode off before opening the Drastic menu"
    While stylus mode is on, `MENU` does nothing. Press `L2` first to leave
    stylus mode, then `MENU` to open the Drastic menu.

!!! tip "Can't see the pen?"
    Nudge the D-pad. The pen hides itself after a moment of stillness.

??? info "More detail"
    The pen is only drawn when it moves. The pen image is the same on every
    device and is remembered across launches.
