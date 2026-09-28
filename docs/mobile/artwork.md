# Artwork

## What the app does today

NX Redux Mobile shows game art that is already in your folders. It uses the
same `.media` layout as the handheld's
[Artwork Manager](../handheld/apps/artwork-manager.md), so art fetched on a
handheld shows up when you copy its folders over. The app does not download
art yet.

Each game can have up to three images, as PNG files named after the game's
file without its extension:

| File | Image |
| --- | --- |
| `.media/<game>.png` | **Mix**: the screenshot with the box art and logo over it |
| `.media/screenshot/<game>.png` | The in-game screenshot on its own |
| `.media/boxart/<game>.png` | The box art on its own |

## Where to put it

Put the `.media` folder in the folder that holds the games:

```
Roms/Game Boy Advance (GBA)/Golden Sun.gba
Roms/Game Boy Advance (GBA)/.media/Golden Sun.png
Roms/Game Boy Advance (GBA)/.media/screenshot/Golden Sun.png
Roms/Game Boy Advance (GBA)/.media/boxart/Golden Sun.png
```

This works in extra folders too: the `.media` folder goes next to the games
in that folder. For a multi-disc game kept in its own folder, the art goes in
the `.media` of the folder above it, named after the game's folder.

A `.media/bg.png` in a system folder of your home folder is that console's
background on the main menu.

After adding or changing art, use **Rescan library** in **Tools → Settings →
Library** so the app picks it up.

## Where each image shows

- **Game lists** show the screenshot, or the mix when there is no screenshot.
  **Game art style** and **Game art width** in
  [Appearance](appearance.md) set how it is framed.
- The **[Game Switcher](game-switcher.md)** shows the resume screenshot, or the
  box art when there is none.
- The RetroAchievements **Achievements** browser shows the mix, or the box
  art.

<!-- SCREENSHOT: artwork-game-list — game list with art, Background style -->

## Planned

!!! info "Not in the app yet"
    These are planned and not available today:

    - Art will download automatically while you browse your games.
    - An art downloader will fetch the art for all your games at once, as the
      handheld's Artwork Manager does.

Until then, bring your own art in the `.media` layout above.
