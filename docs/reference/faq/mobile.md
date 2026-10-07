---
title: Mobile FAQ
---

# Mobile FAQ

Common questions about NX Redux for Android. Using a TrimUI
handheld? See the [Handheld FAQ](handheld.md).

## Can I use the same games folder as my handheld?

Yes. The app uses the NX Redux layout: `Roms/<Name (TAG)>/`, `Bios/<TAG>/`,
`Saves/<TAG>/`, `Collections/` and `map.txt`. A copy of your handheld's
folders works as the app's home folder. A handheld's BIOS layout (such as
`Bios/PS/psxonpsp660.bin`) works unchanged. See
[Library & ROM folders](../../mobile/library.md).

## Do my handheld saves carry over?

Battery saves carry over for systems that run the same core on both. Where
the app uses the same core as the handheld, save states carry over too.

The Sega systems are the exception. The handheld runs PicoDrive for Sega
Genesis, Master System, Game Gear, SG-1000 and Sega CD, and the app runs
Genesis Plus GX. Cartridge saves usually carry over, but save states don't.
Games you ran from a legacy `Sega Genesis (GPGX)` folder on the handheld
already used Genesis Plus GX: kept in that folder, their saves and states
carry over (see below).

Dreamcast memory cards carry over: both name them
`Saves/DC/<game>.A1.bin`. See [Sega Dreamcast](../../mobile/dreamcast.md#memory-cards-vmu).

## My Sega Genesis save states are gone

Sega Genesis now uses the `MD` tag only. The app creates
`Roms/Sega Genesis (MD)/`, and folders without a tag use `MD` too.

Save states are kept per tag. States made under the legacy GPGX tag don't
show in the in-game menu of a game that now runs as `MD`, and they don't
carry over.

- **A legacy GPGX folder** (`Sega Genesis (GPGX)`, from the handheld) still
  plays. Move its games to `Roms/Sega Genesis (MD)/` when you're ready to
  leave its states behind.
- **Battery saves** don't move by themselves. This applies to games you
  move into the `MD` folder, and to games in a folder without a tag. Copy
  each game's `.srm` from the legacy `Saves/GPGX/` folder to `Saves/MD/`.
  The original stays in the legacy `Saves/GPGX/` folder.

!!! warning "Copy the save before you play"
    The app takes a save from `Saves/MD/` when the game starts, and only if
    the file is newer than its own copy. When you quit, its own copy
    replaces the file in `Saves/MD/`. So:

    - Copy the `.srm` with the game closed. A game waiting in the Game
      Switcher counts as open.
    - Copy it before you first play the game as `MD`. If you already have,
      the copied file must be newer than the game's last `MD` save. A copy
      that keeps its old date loses.

See [Emulators](../../mobile/emulators.md#sega-genesis).

## Do I need to download emulators or cores?

No. Every core is bundled in the app. See
[Emulators](../../mobile/emulators.md) for the full list.

## Is there DraStic or Dreamcast?

There is no DraStic. It is closed-source and no longer available, so
Nintendo DS runs on **melonDS DS** instead. DraStic battery saves carry over.

Dreamcast is included, with the NAOMI and Atomiswave arcade games. See
[Sega Dreamcast](../../mobile/dreamcast.md).

## Can I play netplay or use Device Sync with the app?

Not yet. Netplay and Device Sync come in a later release.

## Can two people play on one phone?

Not yet. Local multiplayer, for 2 to 4 players each on their own controller,
comes in a later release.

## Can I remap controller buttons?

Not freely. Each console has a fixed mapping:

- Face buttons work **by position**, like the console's own pad: the bottom
  button does the same thing on every controller, whatever letter it shows.
- If your controller is read wrongly, set **Controller Layout** in the
  in-game menu's **Options → Console Settings**: **Auto-detect**,
  **Xbox (A at the bottom)** or **Nintendo (B at the bottom)**.
- The Nintendo 64 goes by the printed name instead, and has no Controller
  Layout.

On a controller without a mode button, hold `SELECT` + `START` to open the
in-game menu. See [Controls](../../mobile/controls.md).

## Is there a RetroAchievements hardcore mode?

No, the same as on the handheld. RetroAchievements in the app is softcore
only, so cheats and save states are not blocked. See
[RetroAchievements](../../mobile/retroachievements.md).

## Where does the game artwork come from?

The app fetches it. Open **Tools → Artwork** and pick **Fetch missing art**,
or **Fetch by console**. To fetch one game, press `MENU` on it and pick
**Fetch art**.

The art comes from ScreenScraper, libretro-thumbnails, TheGamesDB and
SteamGridDB, and is saved in each game folder's `.media` folder. Art you put
there yourself is used too. See [Artwork](../../mobile/artwork.md).

## Why does artwork need a ScreenScraper account or API keys?

It doesn't have to. libretro-thumbnails needs nothing, and ScreenScraper
works without an account at a small daily quota.

- **Signing in to ScreenScraper** raises that quota, so a large library
  fetches faster.
- **TheGamesDB** works with the key built into the app. Your own free key
  is optional and gives you your own monthly allowance.
- **SteamGridDB** is only used with your own free API key.

Set them in **Tools → Artwork → Account**. See
[Artwork](../../mobile/artwork.md).

## Can I use the app as my home screen?

Yes. Turn on **Use as home screen** in **Tools → Settings → Launcher**. The
phone's Home key then brings you back to the app's **Home** tab. You can also
show Android apps in **Tools**. See
[Launcher Mode & Android Games](../../mobile/launcher.md).

## Why do Android games have no play time?

The app only starts an Android game. The game runs in its own app, so NX
Redux can't tell how long you play. Android games have no play time, and
they don't show in recents or on the Continue card. See
[Launcher Mode & Android Games](../../mobile/launcher.md).

## Does the app work on foldables?

Yes. On a half-folded phone with a horizontal hinge, the game moves above the
fold and the controls go below it. This is automatic, except that Nintendo DS
games keep their usual layout. In landscape on a wide screen, such as an
unfolded Fold held sideways, Settings, the in-game menu and RetroAchievements
split into two panes. See [Foldables & Large Screens](../../mobile/foldables.md).

## I removed my SD card and some games disappeared

Games from a folder on a card that is not mounted are left out until the card
is back. **Tools → Settings → Library → ROM folders** marks the folder
**Not available**. Nothing is lost. See
[Library & ROM folders](../../mobile/library.md).

## Is there an iOS version?

Not yet. NX Redux runs on Android only for now. An iOS version follows
the Android one.
