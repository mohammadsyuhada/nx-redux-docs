# Appearance

Change how the interface looks: UI scale, colors (with live swatches),
animations, and which entries the main menu shows.

![Appearance settings](../../assets/screenshots/set-appearance.png)

## UI scale

Size of text and menus across the whole UI.

| Choice | What it does |
| --- | --- |
| **Default** | Follows the device and shows which scale that is: **Default (2x)** on the Brick, **Default (1x)** on the Brick Pro and Smart Pro S. |
| **1x** | Smaller, shows more rows. |
| **2x** | Larger, shows fewer rows. |

- Settings redraws at the new scale straight away.
- The main menu, the other tools and the in-game menus pick it up the next
  time they start. For the main menu, that is as soon as you leave Settings.
- The Nintendo 64 in-game menu uses the same scale.

*Default (2x) on the Brick*

![Tools list at Default (2x)](../../assets/screenshots/ui-scale-default.png)

*1x on the Brick*

![Tools list at 1x](../../assets/screenshots/ui-scale-1x.png)

## Main color

The color used to render main UI elements.

## Main color opacity

Opacity of the main color, `10%`–`100%` in 10% steps. Below `100%`, the pills
and selection capsules turn translucent and show the wallpaper through them.
The wallpaper is `bg.png` at the SD card root, or the per-folder art.

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

Show or hide the `START` search button hint on the main menu. Hiding it only
removes the hint: pressing `START` at the top level still opens search.

## Show menu animations

Enable or disable menu animations.

## Show menu transitions

Enable or disable the animated slide transitions between screens.

## Game art visible

Show game artwork in the main menu.

## Game art corner radius

Radius of the rounded corners on game art.

## Game art width

Percentage of the screen width used for game art. It sets the size of the
image on the right, and so the width left over for game titles.

This applies to the **Thumbnail** style only. The **Background** style has
fixed geometry and caps titles at 85% of the screen width.

## Game art style

How game art is shown in the game list.

- **Thumbnail** (default): the art sits on the right of the screen, with
  rounded corners, at the size set by *Game art width*.

    *Thumbnail*

    ![Thumbnail style](../../assets/screenshots/game-art-thumbnail.png)

- **Background**: the art fills the screen height and fades diagonally into
  the list, with the titles over it.
    - It always uses the screenshot, whatever *Game art type* is set to.
    - A game whose screenshot has not been fetched gets an empty background.
    - *Game art corner radius* and *Game art width* have no effect here.

    *Background*

    ![Background style](../../assets/screenshots/game-art-background.png)

## Game art type

Which of the fetched images the game list shows in the **Thumbnail** style.
The [Artwork Manager](../apps/artwork-manager.md) stores all three per game.
When the chosen one is missing for a game, the Mix image is shown instead.

- **Mix** (default): the screenshot with the box art and logo over it.

    *Mix*

    ![Mix](../../assets/screenshots/game-art-thumbnail.png)

- **Screenshot**: the in-game screenshot on its own.

    *Screenshot*

    ![Screenshot](../../assets/screenshots/game-art-type-screenshot.png)

- **Box art**: the box art on its own.

    *Box art*

    ![Box art](../../assets/screenshots/game-art-type-boxart.png)

!!! note "Upgrading from v1.9.0 or older"
    Releases up to v1.9.0 saved only the Mix image. **Screenshot** and
    **Box art** fall back to it. The **Background** style never falls back,
    so it shows nothing at all for art fetched back then.

    To get the extra images for an existing library, open **Artwork Manager
    → Settings → Reset artwork**, then queue your systems again from the
    Library page.

## Show folder names at root

Show folder names in the root directory.

## Show Recents

Show the "Recently Played" entry in the main menu.

## Show Tools

Show the "Tools" entry in the main menu.

## Show Collections

Show the "Collections" entry in the main menu.

## Show Emulators

Show the emulator (system) folders in the main menu. Turn this off for a
minimal menu of just your pinned games and shortcuts.

## Use folder background for ROMs

Use the emulator's background image behind its game list.

## Bootlogo

Change the device boot logo.

1. Scroll through the images with left/right.
2. Press `A` to apply one. The device reboots to show it.

The NX Redux mark is the default logo. The previous NextUI logo is still in
the list.

## Reset to defaults

Resets all options on this page to their default values.
