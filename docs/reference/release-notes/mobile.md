---
title: Mobile Release Notes
---

# Mobile Release Notes

What changed in each release of NX Redux for Android phones, tablets and
Android handhelds. Download the APK from the
[releases page](https://github.com/mohammadsyuhada/nx-mobile/releases).

## v0.2.0

*20 October 2026*

Bring your saves over from another app, a folder or a zip file. The DS and
3DS get a portrait pad you can hide, more screen layouts and on-screen Stylus
and Swap buttons. The Consoles Carousel can show your own console
backgrounds.

### New features

- **Import saves from anywhere.** **Tools → Settings → Emulators → Saves →
  Import saves** copies battery saves and save states **From a folder**,
  **From a zip file** or **From RetroArch**. Saves are matched to your games
  by name, nothing is moved or deleted, and a state never overwrites one you
  already have. First-run setup gets a matching **Bring your saves** step.
  See [Import saves](../../mobile/library.md#import-saves).
- **DS and 3DS: hide the portrait pad.** Long-press the arrow at the bottom
  right of the pad to hide it: the screens take its room and see-through
  buttons sit over the game. Long-press again to bring it back. See
  [Nintendo DS](../../mobile/emulators/nintendo-ds.md#portrait-pad) and
  [Nintendo 3DS](../../mobile/emulators/nintendo-3ds.md#portrait-pad).
- **DS and 3DS: more screen layouts.** Large screen on both, Side by side in
  portrait and Stacked in landscape on the DS, and separate layouts for
  portrait, portrait with a controller and landscape on the 3DS. See the
  [DS](../../mobile/emulators/nintendo-ds.md#screen-layouts) and
  [3DS](../../mobile/emulators/nintendo-3ds.md#screen-layouts) screen layouts.
- **DS and 3DS: Stylus and Swap buttons** on the on-screen pad. **Swap**
  trades the two screens, so you can touch the bottom screen under the
  see-through pad. See
  [Stylus mode](../../mobile/emulators/nintendo-ds.md#stylus-mode).
- **Console backgrounds in the Carousel.** **Consoles controller** is now
  **Consoles background** and works in the Carousel too: **Background** shows
  the console's own `.media/bg.png` behind the row, **None** shows neither,
  and the picture on the Layouts page follows it. See
  [Consoles background](../../mobile/layouts.md#consoles-background).

### Improvements

- **Artwork for badly named zips.** When a zipped game's name isn't found,
  the second lookup now uses the ROM inside the zip, so it gets its art. A
  7z is no longer looked up a second time, which saves ScreenScraper quota.
- **Artwork progress** drops games as they finish, so the one being fetched
  stays in view on a long library.
- **On-screen pad labels** are bigger on the portrait pad, and the Wii
  Classic Controller's lowercase letters sit in the middle of their buttons.
- **Bring your saves** has **Skip** at the top right, as the other setup
  steps do.

### Fixes

- **BIOS files in ROM folders** (such as `scph1001.bin` or `bios7.bin`) are
  no longer listed as games, so artwork fetches stop asking for them.

## v0.1.0

*18 October 2026*

The first public release: an early preview, so our first players can try it
and tell us what works and what doesn't before v1.0. Expect rough edges, and
keep a copy of your saves (**Tools → Settings → Emulators → Saves → Export saves**)
while it settles.

It needs Android 8.0 or later on a 64-bit ARM (arm64) device. Bring your own
games and, for the systems that need them, BIOS files. See
[Getting Started on Mobile](../../mobile/getting-started.md).

### What's in it

- **First-run setup.** Text size, your folders, your handheld, artwork,
  RetroAchievements and the menu's look, page by page.
  [Getting Started](../../mobile/getting-started.md#first-run-setup)
- **The NX Redux menu.** Home, Consoles, Collections and Tools tabs in
  List, Grid, Carousel or Backdrop, search, pinned games and tools, and the
  Game Switcher. [Main Menu & Home](../../mobile/main-menu.md),
  [Menu Layouts](../../mobile/layouts.md)
- **One library with the handheld.** The same `Roms/`, `Bios/` and
  `Collections/` folders, extra ROM folders scanned in place, and saves kept
  inside the app with Export and Import.
  [Library & ROM folders](../../mobile/library.md)
- **30+ systems, built in.** From the Game Boy and NES to the PlayStation,
  PSP, Nintendo 64, Dreamcast, Nintendo DS and 3DS, and Wii & GameCube.
  [Bundled Emulators](../../mobile/emulators/index.md)
- **The in-game menu.** Save states with previews, per-console and per-game
  options, shaders, screen scaling and [cheats](../../mobile/cheats.md).
  [In-Game Menu](../../mobile/in-game-menu.md)
- **Controls your way.** An on-screen pad for each console with themes and an
  editable layout, any Android controller, and rumble.
  [Controls](../../mobile/controls.md)
- **Play together.** [Netplay](../../mobile/netplay.md) with another phone
  or an NX Redux handheld over Wi-Fi or a USB-C cable, Game Boy and GBA link
  trades included, and [local multiplayer](../../mobile/multiplayer.md) for
  up to four controllers.
- **RetroAchievements.** Earn achievements offline and sync them later, with
  an achievements panel on every game list.
  [RetroAchievements](../../mobile/retroachievements.md)
- **Device Sync.** Carry games, saves and save states between the phone and
  an NX Redux handheld. [Device Sync](../../mobile/device-sync.md)
- **And more.** [Artwork](../../mobile/artwork.md) for your games, a
  [Game Tracker](../../mobile/game-tracker.md), the app as your
  [home screen](../../mobile/launcher.md) with your Android games, Flex mode
  on [foldables](../../mobile/foldables.md), and Large or Small
  [text size](../../mobile/appearance.md#text-size).

### Not in this release

Features many retro frontends have that this preview doesn't yet:

- **Fast-forward, slow motion and rewind.**
- **Screenshots** of a game while you play.
- **Turbo (autofire) buttons**, other than the few cores with their own
  turbo option.
- **Full button remapping.** Controller Layout swaps the `A`/`B` and `X`/`Y`
  letters, and Pad layout moves the on-screen buttons, but you can't assign
  any button to any action.
- **Run-ahead** to cut input lag, other than the few cores with their own
  run-ahead option.
- **ROM patches** (IPS, BPS, UPS) applied at launch: a patched game has to be
  patched into its own file.
- **RetroAchievements leaderboards**, and hardcore mode (the same as on the
  handheld).
- **Cloud saves.** Saves stay on the phone; Device Sync carries them to a
  handheld, and Export saves makes a backup.
- **External display:** playing on a TV or monitor over a cable or casting.
- **Home computers** such as the Amiga and C64, which the handheld runs.
- **iOS.**

### Feedback

This preview is for finding what to fix and improve before v1.0. Tell us
what goes wrong, which games don't run well on your phone, and what you'd
like to see. Open an issue on
[GitHub](https://github.com/mohammadsyuhada/nx-mobile/issues), with your phone's
model and Android version (**Tools → Settings → About → Copy device info** copies them
for you).
