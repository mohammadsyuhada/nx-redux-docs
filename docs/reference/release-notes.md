# Release Notes

What changed in each NX Redux release. Download packages for every device
from the [releases page](https://github.com/mohammadsyuhada/nx-redux/releases),
or update on the device from [Settings → About](../settings/about.md).

## v1.10.0

*14 September 2026*

This release lets the Music Player keep playing in the background — music,
online radio and podcasts carry on through the menus and inside games, with a
redesigned OSD that puts a Music widget with transport controls and a
Game / Music balance slider at its centre, next to a new Motor toggle that
acts as the master vibration switch. Game lists gain a full-height Background
art style and a choice of Mix, Screenshot or Box art thumbnails, with the
Artwork Manager now saving all three from a single fetch, and theme colours
accept an opacity so pills and accents can show the wallpaper through them.
Nintendo 64 gets a selectable Rice video plugin that is far lighter than
GLideN64 and is now the default on the Brick family, the Smart Pro S is
supported on firmware 1.0.2, app transitions are noticeably quicker, and a
batch of fixes covers Brick Pro deep sleep, turbo fire, the save-slot picker,
Wi-Fi connection errors and Device Sync on FAT32 cards.

### New features

- **Background music playback.** Music, online radio and podcasts keep
  playing when you leave the Music Player — in the menus and inside games.
  Playback is owned by a small background service, so the app is just a
  remote control for it. See
  [Music Player → Background playback](../apps/music-player.md#background-playback).
- **Music widget in the OSD.** The [On-Screen Display](../guide/osd.md) now
  centres on a Music widget showing the current track or station with
  play/pause, previous and next, plus a **Game / Music balance** slider that
  sets how loud games are relative to the music. The same **Balance** setting
  lives in the Music Player's Settings. With nothing playing the widget
  offers to open the Music Player.
- **OSD redesign.** Widgets are laid out around the Music tile, the volume
  slider is gone (the volume keys already cover it), the focus ring follows
  the theme's accent colour, and the default accent is brighter.
- **Motor toggle and vibration strength.** The OSD's new **Motor** toggle is
  the master vibration switch for the whole device — game rumble, the sleep
  and wake pulses and the new shutdown-complete tap. **Vibration strength**
  (`Light` / `Normal` / `Strong`) is in [System settings](../settings/system.md),
  and haptic feedback is now on by default.
- **Smart Pro S firmware 1.0.2** is supported alongside 1.0.1 — see
  [Getting Started](../getting-started.md#before-you-install).
- **Game art style and type.** [Appearance](../settings/appearance.md) gains
  **Game art style** (`Thumbnail` or a full-height `Background` that fades
  into the list) and **Game art type** (`Mix`, `Screenshot` or `Box art`).
  The [Artwork Manager](../apps/artwork-manager.md#what-gets-saved) now saves
  all three images per game from a single ScreenScraper fetch.
- **Theme colour opacity.** **Main color**, **Primary accent** and
  **Secondary accent** each have an opacity setting from `10%` to `100%`;
  below `100%` the pills and accents turn translucent and show the wallpaper
  through them.
- **Show search hint** setting to hide the START search hint on the main
  menu, and **Show game art** is renamed **Game art visible** and now leads
  the game art group.
- **Nintendo 64 video plugin.** Pick **Rice** or **GLideN64** system-wide or
  per game. Rice is much lighter to run and is now the default on the Brick,
  Brick Pro and Smart Pro; the Smart Pro S keeps GLideN64. Each plugin shows
  only its own option sections. See
  [Nintendo 64 → Video plugin](../emulators/nintendo-64.md#video-plugin).
- **Faster app transitions and startup.** A short CPU boost around app
  hand-off, quicker screen clears and mixer setup make moving between the
  launcher, Tools and games noticeably snappier.

### Fixes

- **Music:** the background service was hardened after review. Powering on
  restores the last track paused instead of auto-playing, the app stays
  usable if the service is unreachable, launching a standalone emulator no
  longer interrupts playback, shutting down with a stalled radio stream
  completes promptly, and the OSD widget idles at near-zero CPU.
- **Sleep:** Brick Pro deep sleep now pauses stick polling and wakes again
  reliably.
- **Emulation:** turbo fire works, and FBNeo's error screen no longer wedges
  the emulator.
- **In-game menu:** the save/load slot picker is vertically centred and its
  arrows render properly instead of as boxes.
- **Wi-Fi:** a failed connection shows a retry dialog, and rejected passwords
  are no longer saved.
- **Device Sync:** FAT32 timestamp rounding no longer causes unchanged files
  to be copied again.
- **OSD:** the Smart Pro S OSD works from a FAT32 card, its rumble pulses use
  the motor's PWM level, and the Brick Pro grid is centred.
- **UI:** search results and folder art fixes, and the selection pill glide
  honours **Show menu animations**.
- **Video:** an SDL initialisation failure is logged and falls back to
  software rendering instead of crashing.
- **Desktop:** the Linux AppImage no longer bundles the host's graphics
  driver libraries and ships its own libsqlite3.
- **Bluetooth:** the stock-stack backup archive is no longer kept, and
  leftovers are removed on update.

!!! note "Existing game art"
    Releases up to v1.9.0 saved only the Mix image, so the new
    **Screenshot** and **Box art** types fall back to it and the
    **Background** style shows nothing for art fetched back then. To get
    the extra images for an existing library, open **Artwork Manager →
    Settings → Reset artwork**, then queue your systems again. See
    [Appearance → Game art type](../settings/appearance.md#game-art-type).

## Earlier releases

Notes for v1.9.0 and older are on the
[GitHub releases page](https://github.com/mohammadsyuhada/nx-redux/releases).
