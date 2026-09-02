---
hide:
  - navigation
---

# Desktop App

NX Redux also runs as a desktop app on **macOS (Apple Silicon)** and
**Linux (x86_64)** — the same launcher, tools, and bundled libretro cores as
the handheld build, in a window on your computer.

!!! warning "Experimental"
    The desktop build is **experimental**. It is packaged alongside every
    release but gets far less testing than the device builds, and some
    rough edges are expected. Device releases are never affected by desktop
    issues — if something breaks here, your handheld is fine.

## Download & install

Grab the desktop artifact for your OS from the
[releases page](https://github.com/mohammadsyuhada/nx-redux/releases):

| OS | File |
| --- | --- |
| macOS (Apple Silicon) | `NXRedux-<version>-macos-arm64.zip` |
| Linux (x86_64) | `NXRedux-<version>-x86_64.AppImage` |

**macOS** — unzip and move `NXRedux.app` wherever you like. The app is not
code-signed, so macOS blocks the **first** launch:

1. Double-click the app. macOS shows a warning that it could not verify the
   app; close that dialog (do **not** choose *Move to Trash*).
2. Open **System Settings → Privacy & Security** and scroll down to the
   **Security** section. There is a notice that `NXRedux` was blocked; click
   **Open Anyway** and confirm.
3. Launch the app again. From now on it opens normally with a double-click.

**Linux** — make the AppImage executable (`chmod +x NXRedux-*.AppImage`) and
run it. If it refuses to start, your distribution may be missing FUSE 2
(`libfuse2`); either install it or run the AppImage with
`--appimage-extract-and-run`.

On first launch the app creates its data folder at `~/NXRedux` with the same
layout as an SD card — put your games in `Roms/` and BIOS files in `Bios/`
using the usual per-system subfolders (e.g. `Roms/Game Boy Advance (GBA)/`),
then restart the app or refresh the list. Saves, states, and settings all
live under this folder too, so it is the only thing you need to back up.

## Keyboard controls

The default keyboard layout mirrors RetroArch's, so it should feel familiar:

| Key | Button |
| --- | --- |
| ++arrow-up++ ++arrow-down++ ++arrow-left++ ++arrow-right++ | D-pad |
| ++x++ | A |
| ++z++ | B |
| ++s++ | X |
| ++a++ | Y |
| ++q++ | L1 |
| ++w++ | R1 |
| ++e++ | L2 |
| ++r++ | R2 |
| ++enter++ | Start |
| ++"Right Shift"++ | Select |
| ++space++ | Menu (in-game menu / shortcuts) |
| ++backspace++ | Power |

Volume, display brightness, wifi networking and bluetooth are handled by your computer, not by the app —
the device volume/brightness shortcuts do not apply here.

## External controllers

Plug in (or pair) any controller SDL recognizes as a game controller —
Xbox, PlayStation, Switch Pro, and most generic USB/Bluetooth pads work.
Hot-plugging is supported: connect or disconnect at any time, including
mid-game. One controller is active at a time.

The mapping follows button **position**, matching the handheld layout:

| Controller | Button |
| --- | --- |
| D-pad | D-pad |
| Right face button | A |
| Bottom face button | B |
| Top face button | X |
| Left face button | Y |
| Shoulders | L1 / R1 |
| Triggers | L2 / R2 (digital past half-pull) |
| Stick clicks | L3 / R3 |
| Back / Select | Select |
| Start | Start |
| Guide / Home | Menu |
| **Select + Start together** | Menu |

The left stick works as true analog in cores that support it and doubles as
a D-pad in menus; the right stick is passed through to cores as analog only.

!!! tip "macOS reserves the Home button"
    Recent macOS intercepts the controller's Guide/Home button system-wide to
    open the Games app, and offers no way to remap it. Use
    **Select + Start pressed together** instead — it opens the menu without
    involving the Home button, and the game never sees the two buttons held.

## Netplay

Netplay works in the desktop build. When a game supports it, the game list
shows the `Y NETPLAY` hint; press `Y` to **Host** or **Join** a session. The
flow is the same as on the handhelds — see the [Netplay](netplay.md) page.

Two things are specific to desktop:

- **It connects over your existing network only — there is no hotspot
  option.** On the handhelds one device can host a Wi-Fi hotspot for the
  other; on the desktop that is intentionally left out, because managing a
  computer's Wi-Fi hotspot cleanly across both macOS and Linux is more trouble
  than it's worth. Both players simply need to be on the **same network** —
  Wi-Fi or Ethernet, either works.
- **Dreamcast and Nintendo 64 netplay are not available**, because those
  systems run on standalone emulators the desktop build doesn't include yet
  (see [Limitations](#limitations)). Netplay for the bundled libretro cores —
  including Game Boy and Game Boy Advance link — works normally.

## Limitations

- Systems that use standalone emulators on the handhelds — **Dreamcast,
  Nintendo 64, and Nintendo DS** — are not included in the desktop build yet.
  Everything running on a bundled libretro core is. Bringing these standalone
  emulators (and their netplay) to the desktop is something we plan to explore
  in the future.
- Device-specific settings (display hardware, audio routing, Bluetooth,
  LED control, boot logo) are hidden — the host OS owns those.
- Sleep/power management is intentionally disabled; quit from the window
  close button like any desktop app.
