---
hide:
  - navigation
---

# Getting Started

## Before you install

!!! warning "Update the stock firmware first"
    NX Redux relies on system libraries the stock firmware ships, so older
    firmware breaks some features. Install the
    [official TrimUI firmware](https://github.com/trimui) version listed below
    for your device **before** installing NX Redux.

| Device | Required stock firmware |
| --- | --- |
| TrimUI Brick / Brick Hammer / Brick Pro | `1.1.1` |
| TrimUI Smart Pro S | `1.0.1` |
| TrimUI Smart Pro | `1.1.1` |

You will also need:

- A reputable-brand microSD card, freshly formatted as **exFAT** (preferred).
- The release zip for **your exact device model** from the
  [releases page](https://github.com/mohammadsyuhada/nx-redux/releases) —
  releases are packaged per device (`brick`, `brickpro`, `smartpro`,
  `smartpros`) and are not interchangeable.

## Installing

A release has two essential parts: an installer/updater archive named
`MinUI.zip` and a bootstrap folder named `trimui`, alongside the SD card
folder skeleton (`Bios`, `Roms`, `Saves`, and so on).

1. Format the SD card as exFAT.
2. Extract the release zip and copy **everything** to the root of the SD card —
   all the folders, the `trimui` folder, and `MinUI.zip` (do **not** unzip
   `MinUI.zip`).
3. Preload at minimum your `Bios` and `Roms` folders. Each system has its own
   subfolder under `Roms` (e.g. `Roms/Game Boy Advance (GBA)/`) and `Bios`
   (e.g. `Bios/GBA/`).
4. Insert the card and power the device on. The installer runs automatically on
   first boot.

## Updating

Two ways to update, pick either:

- **OTA updater (on-device)** — go to
  [Settings → About](settings/about.md): it checks for a new release when
  you open the page, and downloads and installs the update right there
  (needs Wi-Fi).
- **Manually** — copy the new release's `MinUI.zip` (without unzipping) to
  the root of the SD card containing your ROMs, then boot the device.

Emulator and Tool paks are part of NX Redux itself: they live in `/.system/paks/`
and update automatically with every update. There is nothing to copy by hand.

!!! note "Your own paks"
    The `/Emus` and `/Tools` folders on the SD card are for your **own**
    community paks (e.g. a PSP.pak). Do not place a pak there with the same
    name as a shipped one — same-named paks are treated as NX Redux leftovers
    and are removed on every update.

## First boot

After installation you land on the main menu: your systems are listed with
**Recently Played** at the top and **Tools** at the bottom. From here:

- Press `A` to open a system or game.
- Press `START` to search your whole library.
- Tap `SELECT` to open the [Game Switcher](guide/game-switcher.md).
- Press `MENU` on a game for its [context menu](guide/context-menu.md).

Continue with the [User Guide](guide/main-menu.md).
