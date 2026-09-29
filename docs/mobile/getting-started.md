---
title: Getting Started with NX Redux Mobile
---

# Getting Started with NX Redux Mobile

!!! info "Coming soon"
    NX Redux Mobile is not released yet. These pages grow as its features
    ship.

NX Redux Mobile brings the NX Redux look, folder layout and in-game features
to Android phones, tablets and Android handhelds. It runs retro systems
through bundled libretro cores, with no downloads needed.

An iOS version is planned after Android. New to NX Redux? See
[About NX Redux](../about.md) first.

## What's different from the handheld

- **Emulators:** Nintendo DS runs melonDS DS (DraStic is not available), and
  Sega Dreamcast is not included in the first release. See
  [Emulators](emulators.md).
- **Library:** besides the home folder, the app can scan extra folders in
  place. See [Library & ROM folders](library.md).
- **Controls:** an on-screen pad, or any Android controller. See
  [Controls](controls.md).
- **Artwork:** the app shows art you already have, but does not download it
  yet. See [Artwork](artwork.md).
- **RetroAchievements:** softcore only for now. See
  [RetroAchievements](retroachievements.md).
- **Coming later:** Netplay and Device Sync are planned for a later release.
- **Left to Android:** Wi-Fi and Bluetooth management, the on-screen display,
  the music player, PortMaster and firmware updates are not part of the app.

## Install

NX Redux Mobile is not released yet. This section will list where to get it
once it is out.

## Choose a home folder

On first start the app asks for a **home folder** through Android's folder
picker. It creates the NX Redux layout inside it:

| Folder | What goes there |
| --- | --- |
| `Roms/<Display Name (TAG)>/` | Games, one folder per system |
| `Bios/<TAG>/` | BIOS files for systems that need them |
| `Saves/<TAG>/` | Battery saves, mirrored from the app |
| `Collections/` | Your game collections |

The folders are visible to file managers, so you can copy games in from a
computer. The home folder can sit on an SD card.

If your games already follow the NX Redux layout from a handheld, the same
folder names and `Bios/<TAG>/` files work unchanged.

!!! note "Pick a folder, not a root"
    The picker can't use the storage root, the SD card root or the Download
    folder. Pick or create a folder inside one of them, such as `NXRedux`.

## Add a ROMs folder

Right after you pick the home folder, the app asks **Add a ROMs folder?**

<!-- SCREENSHOT: mobile-add-roms-folder — "Add a ROMs folder?" prompt (Fold) -->

- If you already keep games somewhere else on the phone, press `A` **Add
  folder** and pick that folder. It is scanned in place and nothing is moved.
- Press `B` **Skip** to go straight to your library.

You can add more folders later as **extra folders** in **Tools → Settings →
Library**. See [Library & ROM folders](library.md).

## Next steps

- [Controls](controls.md): the on-screen pad, controllers and the buttons in
  the menus.
- [In-game Menu](in-game-menu.md): save states, options and Save Changes.
- [Game Switcher](game-switcher.md): resume recent games.
