# Buttons & Shortcuts

A quick reference for the hardware shortcuts built into NX Redux: the combos
that work from anywhere, plus the buttons worth knowing in the menus and
in-game.

## Anywhere — menus or in-game

These work on any screen, including mid-game:

| Shortcut | Action |
| --- | --- |
| `VOL +` / `VOL −` | Adjust volume (hold to repeat). |
| `SELECT` + `VOL +` / `VOL −` | Adjust screen brightness. |
| `START` + `VOL +` / `VOL −` | Adjust color temperature — *Brick, Brick Pro and Smart Pro*. |
| `HOME` (Smart Pro S) · hold `MENU` ~1 s (other devices) | Open the [On-Screen Display](osd.md). |
| `L2` + `R2` | Take a screenshot — once the capture daemon is [armed via the OSD](osd.md#screenshots). |
| `POWER` (tap) | Sleep. |
| `POWER` (hold ~1 s) | Shut down. |

Volume and brightness show an on-screen indicator as you adjust.

!!! note
    The color-temperature combo isn't available on the Smart Pro S. Set
    color temperature in [Settings → Display](../settings/display.md)
    instead.

The **FN switch** is a shortcut of its own. One flick applies the set of
changes you configured for it (volume, screen, LEDs, turbo fire, D-pad mode;
see [FN switch settings](../settings/fn-switch.md)). Flipping it back restores
everything. Muting the speaker from the OSD is separate and does not depend on
the switch.

??? info "More detail"
    The combos above are handled by a background service, which is why they
    work on any screen.

## In the menus

`A` confirms and `B` goes back. Prefer confirm at the bottom? See
[Button Layout](button-layout.md).

| Button | Action |
| --- | --- |
| `SELECT` | Open the [Game Switcher](game-switcher.md) |
| `START` | At the top level of the main menu, open **Search** |
| `X` | Resume the highlighted game from where you last left off |
| `Y` | Launch a netplay-capable game straight into [Netplay](../netplay.md) |
| `MENU` | Open the [context menu](context-menu.md) for the highlighted game or tool |
| `F1` / `F2` | Launch your assigned tools (Brick and Brick Pro; see [Settings → F1 / F2 Keys](../settings/fn-keys.md)) |

## In-game

| Button | Action |
| --- | --- |
| `MENU` | Pause the game and open the [in-game menu](playing-games.md#the-in-game-menu) |
| `MENU` + `SELECT` | Save, grab a fresh screenshot, and quit straight back to the [Game Switcher](game-switcher.md). The fastest way to hop between games. |

Fast-forward, rewind and turbo get their own configurable shortcuts
(optionally `MENU`-modified). Set them under the in-game menu's
[Options → Shortcuts](in-game-options.md#shortcuts), per emulator or per game.
