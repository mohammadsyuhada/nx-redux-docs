# Cheats

NX Redux can load [libretro](https://www.libretro.com/) cheat files for your
games. Setup is a quick two-step, all on-device with no computer:

1. Install the small **Cheat Database** tool from the [Xtras Store](xtras.md).
2. Open it from [Tools](tools.md) and **download** the cheat files.

Once the files are on the card, turn individual cheats on and off from a game's
in-game menu.

## Installing the Cheat Database tool

Open **Tools → Xtras**, switch to the **TOOLS** tab (`Right`), and select
**Cheat Database**:

- This installs a **small tool** (about 1 MB) into your **Tools** menu. It does
  **not** download the cheats yet — that happens on demand from inside the tool.
- When it finishes you'll see *"Installed. Open Cheat Database in Tools to
  download the cheats."*

The entry moves to the *Installed* group in Xtras afterwards, and appears as
**Cheat Database** in your [Tools](tools.md) menu.

## Downloading the cheats

Open **Tools → Cheat Database**. The first time, the menu offers a single
choice — **Download cheat database**:

- It downloads the libretro cheat collection (~37 MB) and unpacks it onto the
  SD card — about **185 MB** once extracted (you'll need ~256 MB free).
- A progress bar advances system by system as it installs.
- When it finishes you'll see *"Done. Open a game and see Options > Cheats."*

!!! note "One download, every system"
    A single download covers every supported system at once — you don't grab
    cheats per game or per console. Come back to the tool later to update them.

## Keeping things up to date

There are **two separate kinds of update**, and they arrive from two places:

- **The cheat files (data)** update **inside the tool**. Open **Tools → Cheat
  Database → Check for updates**. It checks libretro's latest release and, if
  it's newer, re-downloads; otherwise it reports *"Cheat database is up to
  date."*
- **The Cheat Database tool itself (code)** updates through the **[Xtras
  Store](xtras.md)**, like any other tool — Xtras labels the entry when a new
  version is available, and a NX Redux system update refreshes it automatically.

!!! tip "Which update do I want?"
    New or corrected cheats → **Check for updates** inside the tool. Improvements
    to the tool's own menus/behaviour → update **Cheat Database** from **Xtras**.

## Where the files go

Cheats are stored as loose `.cht` text files on the SD card, one folder per
system:

```
/mnt/SDCARD/Cheats/GBA/Advance Wars (USA, Europe) (Code Breaker).cht
/mnt/SDCARD/Cheats/SFC/...
/mnt/SDCARD/Cheats/FC/...
```

Each `Cheats/<system>/` folder uses the same short system tag as your `Roms`
folders (`GBA`, `SFC`, `FC`, `GB`, `GBC`, `MD`, `PS`, and so on), so the right
cheats are matched to the right games automatically.

## Using cheats in a game

1. Launch a game on a **built-in emulator core**.
2. Press `MENU` to open the in-game menu and choose **Options** (see
   [Emulator Options](../guide/emulator-options.md#in-game-the-pause-menu)).
3. Choose **Cheats**.
4. Toggle any cheat `On` or `Off` — changes apply **immediately** while you
   play. Each entry carries a short description you can read from the list.

If no cheats are found for the game, the menu tells you so and points you at
**Tools > Cheat Database** to download them.

!!! tip "Variants are merged automatically"
    Some games ship several cheat sets from different sources (Game Genie,
    GameShark, Code Breaker, Action Replay). NX Redux loads **all** of them
    for the current game and merges them into one list, tagging each cheat with
    its source (for example `[GameShark]`) so you can tell them apart.

### RetroAchievements hardcore mode blocks cheats

If [RetroAchievements](retroachievements.md) **hardcore mode** is active,
cheats cannot be enabled — trying to toggle one shows *"Cheats disabled in
Hardcore mode"* and the switch snaps back off. This keeps hardcore runs
legitimate. Leave hardcore mode to use cheats.

## Standalone emulators (DS, N64, Dreamcast)

The Cheat Database **delivers** files for Nintendo DS, Nintendo 64 and Sega
Dreamcast too — you'll find them under `Cheats/NDS/`, `Cheats/N64/` and
`Cheats/DC/`. However, those systems run on **standalone emulators** (DraStic,
mupen64plus and Flycast), which use their own native cheat formats and **do
not read these libretro `.cht` files yet**.

!!! warning "Libretro cores only, for now"
    Cheats only take effect on the **built-in libretro cores** inside the
    emulator (Game Boy, GBA, NES, SNES, Mega Drive, PlayStation, and the like).
    The DS/N64/Dreamcast files are shipped for future use — wiring the
    standalone emulators to apply them is a separate follow-up.

## Removing cheats and hand-made cheats

You can write your own cheats: drop a `<Game Name>.cht` file into the matching
`Cheats/<system>/` folder and it will be picked up and merged alongside the
downloaded ones just like any other cheat file.

There are two ways to remove the downloaded database, and **both always keep
your hand-made `.cht` files**:

- **From inside the tool** — **Tools → Cheat Database → Remove cheat database**
  deletes only the files it downloaded, but leaves the tool installed so you can
  download again later. You'll see *"Cheat database removed. Hand-made cheats
  kept."*
- **From Xtras** — uninstalling **Cheat Database** removes the tool **and** its
  downloaded cheat files in one step.

Both keep a record of exactly what was downloaded and delete only that, and any
`Cheats/<system>/` folder that still holds one of your own files is kept as
well. So you can safely install, download, remove and reinstall without losing
your own cheats.
