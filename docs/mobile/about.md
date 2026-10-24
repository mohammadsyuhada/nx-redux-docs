# System

**Tools → Settings → System** is the last Settings section. It holds the
app-wide switches, the app's version and your device's details, and the
licenses, in five groups:

| Group | Rows |
| --- | --- |
| [**General**](#pause-when-unfocused) | **Pause when unfocused** |
| [**Launcher**](#use-as-home-screen) | **Use as home screen** |
| [**Developer**](#debug-log) | **Debug log** |
| [**About**](#about) | The version and device rows, **Copy device info**, and **Check for updates** in the build from GitHub |
| [**Licenses**](#licenses) | What the app is made of and its licenses, and **Full list of licenses** |

![Settings, with System open beside the sections: General, Launcher, Developer and About](../assets/screenshots/mobile/settings-about.webp){ .nx-wide }

## Pause when unfocused

**Pause when unfocused** (On by default) pauses a game when another app
takes over while the game is still on screen: in split screen, in a desktop
window such as Samsung DeX, or with an app open on a second screen. Go back
to the game, by tapping or clicking it, and it plays on by itself.

Turn it off to keep a game running while you use another app beside it.

??? info "More detail"
    - The game's sound and rumble stop with it.
    - If you open the in-game menu before going back, the game stays paused
      until you choose **Continue**.
    - Your own screens don't count: the game panel, the DS or 3DS bottom
      screen and the in-game menu never pause it.
    - In a [netplay](netplay.md) match, the other player sees you paused, as
      when you leave the app.
    - Leaving the app, such as to Home, always pauses the game, whatever this
      setting says.

## Use as home screen

**Use as home screen** makes the app your Android home screen. See
[Launcher Mode & Android Games](launcher.md#use-as-home-screen).

## Debug log

**Debug log** (Off by default) writes the app's and the emulators' detailed
logs to Android's system log, for a bug report. With it off, only errors are
logged. It takes effect at once.

## About

The **About** rows show the app's version and your device's details. They
are read-only.

| Row | What it shows |
| --- | --- |
| **NX Redux** | The app's version, with its build number in brackets |
| **Build** | The commit the app was built from |
| **Released** | The date of that commit |
| **Platform** | The Android version and its API level |
| **Device** | The phone's maker and model |
| **Chip** | The phone's processor |
| **GPU** | The graphics chip |
| **Page size** | The memory page size, e.g. 4 KB |

??? info "More detail"
    - **GPU** reads **…** for a moment while the app asks for it.
    - A row the app can't read shows **Unknown**.

### Copy device info

Select **Copy device info** and press `A` **Copy**, then paste the text into
a bug report so the details are exact.

??? info "More detail"
    It copies every About row as text. The app shows "Device info copied".

### Check for updates

In the build from GitHub, the last About row is **Check for updates**.
`A` **Check** looks for a newer version. When there is one, the row reads
**Update to** and the version: `A` **Update** downloads and installs it.

??? info "More detail"
    - While it works, the row shows what it is doing, such as **Checking for
      updates…** or **Downloading** with a percentage.
    - With nothing newer, it reads **Up to date** with your version.

## Licenses

A few short paragraphs say what NX Redux is made of and under which
licenses: the app itself (GPL-3.0), the MiSans font by Xiaomi, the libretro
emulator cores, the game runner and its libraries, and the Kotlin and
Android libraries.

**Full list of licenses** opens the [Licenses](../reference/licenses.md)
page of this site in your browser.

??? info "More detail"
    - The paragraphs credit MiSans as its license asks.
    - The **?** icon on **Full list of licenses** shows the address it opens.
