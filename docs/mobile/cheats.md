# Cheats

NX Redux uses [libretro](https://www.libretro.com/)'s cheat
collection. Download it once from **Tools → Cheat Database**, then turn
cheats on and off from a game's [in-game menu](in-game-menu.md#cheats).

Unlike the handheld, there is no separate tool to install first: Cheat
Database is part of the app.

## Downloading the cheats

Open **Tools → Cheat Database** and choose **Download (about 37 MB)**.

![Tools → Cheat Database, not installed: about 37 MB download, cheats for 25 systems, and Download (about 37 MB)](../assets/screenshots/mobile/cheat-database.webp)

- You need about 400 MB of free space. With less, it stops with **Not enough
  space (needs about 400 MB free)**.
- A progress bar follows the download and install. `B` cancels.
- When it is done, the page shows **Installed**.

One download covers every supported system. Wii and GameCube games use
Dolphin's own codes instead. See
[Nintendo Wii & GameCube](emulators/wii-gamecube.md#cheats-and-achievements).

??? info "More detail"

    - Before the first download the page shows **Not installed**, the download
      size and how many systems it covers.
    - The install goes system by system (**Installing** followed by the
      system's tag and count).
    - Once installed, the page shows the number of systems and files, and the
      date of the last update.
    - The download has no Wii or GameCube cheats.

## Keeping it up to date

With the cheats installed, the page offers **Check for updates** and
**Remove**.

- **Check for updates** downloads libretro's latest copy only when it has
  changed.
- **Remove** deletes the downloaded files, after asking. Your own cheat files
  stay.

??? info "More detail"

    - When nothing changed, **Check for updates** reports **Cheat database is
      up to date**. With no connection it reports **Could not check for
      updates (Wi-Fi?)**.
    - **Remove** asks **Remove cheat database?**

## Where the files go

The cheats live inside the app's own storage. Unlike the handheld, they are
not on your card or in your home folder.

Some systems have no cheats, because their emulators don't take them, such as
Arcade (`FBN`), Dreamcast and Nintendo 3DS.

??? info "More detail"

    - The systems with no cheats: Arcade (`FBN`), ColecoVision, Dreamcast
      (with NAOMI and Atomiswave), Neo Geo Pocket, Virtual Boy, Atari Lynx,
      Atari 2600, 5200 and 7800, Pokémon mini, PICO-8 and Nintendo 3DS.
    - The cheats are libretro `.cht` files, kept in one `Cheats/<TAG>/` folder
      per system inside the app's own storage. The app reads cheats only from
      there.
    - The download installs folders only for systems whose core takes cheats.
    - A game reads its own system's folder, even when it sits in another
      system's `Roms` folder: a Sega CD disc in `Sega Genesis (MD)` reads
      `Cheats/SEGACD/`, a `.fds` disk in `Nintendo ES (FC)` reads
      `Cheats/FDS/`, and a PC Engine CD game reads the PC Engine CD cheats.
      Game Boy and Game Boy Color look in each other's folder when their
      own has nothing.

## Using cheats in a game

1. Open the [in-game menu](in-game-menu.md) and choose **Options**.
2. Choose **Cheats**.
3. Turn a cheat **On** or **Off** with `LEFT` or `RIGHT`. It applies straight
   away. `A` shows its full description.
4. To keep your cheats for next time, use **Save Changes → Save for game**.

![The in-game Cheats page on Mega Man X4, with Infinite Lives turned On](../assets/screenshots/mobile/in-game-cheats.webp)

If no cheat file matches the game, the page says **No cheats for this game.**

!!! tip "Variants are merged"
    Some games have cheats from several sources, such as GameShark or Action
    Replay. They all show in one list, and a highlighted cheat's description
    starts with its source, such as `(GameShark)`.

![A merged cheat highlighted: the line under the list reads (GameShark) Joker Command](../assets/screenshots/mobile/in-game-cheats-merged.webp)

??? info "More detail: how a game's cheats are found"

    - The app finds the game's cheat file by the ROM's file name first, then
      by the game's name, then by the first file whose name starts with the
      game's name.
    - PSP games are matched by their game ID, such as `ULUS10041`, from the
      disc itself.
    - With no match, the page also names the file it looked for, such as
      `Looked for Cheats/GBA/...`.
    - For merged cheats, the app loads every cheat file for the game's name
      and region into one list.

## Cheats and RetroAchievements

[RetroAchievements](retroachievements.md) on mobile is **softcore only**,
so there is no hardcore mode to block cheats. You can turn cheats on
with achievements enabled.
