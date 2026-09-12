# Appearance

UI customization — colors (with live swatches), animations, and which
entries the main menu shows.

![Appearance settings](../assets/screenshots/set-appearance.png)

## Main color

The color used to render main UI elements.

## Main color opacity

Opacity of the main color, `10%`–`100%` in 10% steps. Below `100%` the pills
and selection capsules become translucent and show the wallpaper (`bg.png` at
the SD card root, or the per-folder art) through them.

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

Show or hide the START search button hint on the main menu. Hiding it only removes the hint; pressing START at the top level still opens search.

## Show menu animations

Enable or disable menu animations.

## Show menu transitions

Enable or disable the animated slide transitions between screens.

## Game art corner radius

Radius of the rounded corners on game art.

## Game art width

Percentage of the screen width used for game art: the size of the image on
the right, and the width left over for game titles. This applies to the
**Thumbnail** style only. The **Background** style has fixed geometry and
caps titles at 85% of the screen width.

## Game art style

How game art is shown in the game list.

- **Thumbnail** (default) — the art sits on the right side of the screen at
  the size set by *Game art width*, with rounded corners.
- **Background** — the image is scaled so its height matches the screen, with
  nothing cropped, and fades diagonally into the list background. The fade
  runs from 40% in from the right edge at the top of the screen to 60% in at
  the bottom, and from 20% to 40% on the 16:9 Smart Pro S, whose wider screen
  would otherwise carry the fade much further across. It reaches full strength
  only at the right edge and stays near invisible for a long stretch at the
  dark end, so a bright screenshot blends into the background rather than
  starting at a visible line. The image is also pushed 30% of its width off
  the right edge, so more of its middle is in view. A screenshot that is
  taller than it is wide is a stacked two-screen shot (a Nintendo DS one is
  both screens, one above the other): it is sized to the width of the art
  area and the top part that fills the screen height is used, rather than
  squeezing both screens into a narrow strip. Game titles may use 85% of the
  screen width and glide over the image, so long names stop short of its
  brightest part. *Game art corner radius* and *Game art width* do not apply
  in this style.

*Thumbnail*

![Thumbnail style](../assets/screenshots/game-art-thumbnail.png)

*Background*

![Background style](../assets/screenshots/game-art-background.png)

In the Background style the screenshot is always used, regardless of *Game
art type* (see below), and a game with no screenshot shows an empty
background rather than a different image.

## Game art type

Which of the fetched images the game list shows: **Mix** (default, the
screenshot with box art and logo floating over it), **Screenshot** or
**Box art**. The [Artwork Manager](../apps/artwork-manager.md) stores all
three per game; when the chosen one is missing for a game, the Mix image is
shown instead.

*Mix*

![Mix](../assets/screenshots/game-art-thumbnail.png)

*Screenshot*

![Screenshot](../assets/screenshots/game-art-type-screenshot.png)

*Box art*

![Box art](../assets/screenshots/game-art-type-boxart.png)

This setting applies to the **Thumbnail** style, where a missing variant
falls back to the Mix image. The **Background** style always uses the
screenshot, because a mix composite's floating box art and logo read as
clutter once the image spans the whole screen; a game whose screenshot has
not been fetched shows an empty background instead of falling back.

!!! note "Upgrading from v1.9.0 or older"
    Releases up to v1.9.0 saved only the Mix image. **Screenshot** and
    **Box art** therefore fall back to it, and the **Background** style,
    which never falls back, shows nothing at all for art fetched back then.
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

Show the emulator (system) folders in the main menu — turn this off for a
minimal menu of just your pinned games and shortcuts.

## Game art visible

Show game artwork in the main menu.

## Use folder background for ROMs

Use the emulator's background image behind its game list.

## Bootlogo

Change the device boot logo.

## Reset to defaults

Resets all options on this page to their default values.
