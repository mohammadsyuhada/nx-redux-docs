# Appearance

Change how the interface looks: menu layouts, colors (with live swatches) and
animations.

Text and menus are sized for each device's screen, so the interface looks the
same size on the Brick, Brick Pro and Smart Pro S. There is no UI scale
setting.

![Appearance settings](../../assets/screenshots/set-appearance.png)

## Main color

The color used to render main UI elements.

## Main color opacity

Opacity of the main color, `10%`–`100%` in 10% steps. Below `100%`, the pills
and selection capsules turn translucent and show the wallpaper through them.
The wallpaper is `bg.png` at the SD card root.

## Primary accent color

The color used to highlight important things in the UI.

## Primary accent opacity

Opacity of the primary accent color, `10%`–`100%`. Below `100%` accented
elements become translucent and show the wallpaper through them.

## Secondary accent color

A secondary highlight color.

## Secondary accent opacity

Opacity of the secondary accent color, `10%`–`100%`. Below `100%` accented
elements become translucent and show the wallpaper through them.

## Hint info color

Color for button hints and info text.

## List text

List text color.

## List text selected

Color of the selected list entry's text.

## Show battery percentage

Show the battery level as a percentage in the status pill.

## Show search hint

Show or hide the `START` search button hint on the main menu tabs. Hiding it
only removes the hint: pressing `START` on a tab still opens search.

## Show recent hint

Show or hide the `SELECT` recent games button hint on the main menu. Hiding it
only removes the hint: pressing `SELECT` still opens the
[Game Switcher](../guide/game-switcher.md).

## Show netplay hint

Show or hide the `Y` netplay button hint in game lists and search results.
Hiding it only removes the hint: pressing `Y` on a game that supports netplay
still opens the netplay menu.

## Show menu animations

Enable or disable menu animations.

## Show menu transitions

Enable or disable the animated slide transitions between screens.

## Bootlogo

Change the device boot logo.

1. Scroll through the images with left/right.
2. Press `A` to apply one. The device reboots to show it.

The NX Redux mark is the default logo. The previous NextUI logo is still in
the list.

## Reset to defaults

Resets all options on this page to their default values. The
[Layouts](layouts.md) page has its own reset.

??? info "Options that moved or were removed"
    The main menu redesign replaced several older options:

    | Old option | Now |
    | --- | --- |
    | **Show Emulators**, **Show Collections**, **Show Tools** | **Consoles tab**, **Collections tab**, **Tools tab** in [Layouts](layouts.md) |
    | **Show Recents** | Removed. Your last game is Home's Continue card, and the [Game Switcher](../guide/game-switcher.md) lists the rest. |
    | **Game art visible / style / type / width / corner radius**, **Use folder background for ROMs** | Removed. Each [layout](../guide/layouts.md) places the art itself. |
    | **Show folder names at root** | Removed. Names always show. |
