# Getting Started with NX Redux Mobile

!!! info "Coming soon"
    NX Redux Mobile is not released yet. These pages grow as its features
    ship.

NX Redux Mobile brings the NX Redux look, folder layout and in-game features
to Android phones, tablets and Android handhelds. It runs retro systems
through bundled libretro cores, with no downloads needed. An iOS version is
planned after Android. New to NX Redux? See [About NX Redux](../about.md)
first.

## What's different from the handheld

- **Emulators:** Nintendo DS runs melonDS DS (DraStic is not available), and
  Sega Dreamcast is not included in the first release. See
  [Emulators](emulators.md).
- **Library:** besides the home folder, the app can scan extra folders in
  place. See [Library & ROM folders](library.md).
- **Controls:** an on-screen pad, or any Android controller. See
  [Controls](controls.md).
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

## Add more folders

Games elsewhere on the phone can stay where they are: add their folders as
**extra folders** in **Tools → Settings → Library**. See
[Library & ROM folders](library.md).
