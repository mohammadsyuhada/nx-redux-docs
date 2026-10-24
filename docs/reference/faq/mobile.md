---
title: Mobile FAQ
---

# Mobile FAQ

Common questions about NX Redux for Android. Using a TrimUI
handheld? See the [Handheld FAQ](handheld.md).

## Can I use the same games folder as my handheld?

Yes. A copy of your handheld's folders, BIOS files included, works as the
app's home folder. See [Library & ROM folders](../../mobile/library.md).

??? info "More detail"
    The app uses the NX Redux layout: `Roms/<Name (TAG)>/`, `Bios/<TAG>/`,
    `Saves/<TAG>/`, `Collections/` and `map.txt`. A handheld's BIOS layout
    (such as `Bios/PS/psxonpsp660.bin`) works unchanged.

## Do my handheld saves carry over?

Battery saves carry over for systems that run the same core on both. Where
the app uses the same core as the handheld, save states carry over too.

The Sega systems run PicoDrive on both, so their saves and states carry over
too. For games from a legacy handheld `(GPGX)` folder, see below.

Dreamcast memory cards carry over: both name them
`Saves/DC/<game>.A1.bin`. See [Sega Dreamcast](../../mobile/emulators/dreamcast.md#memory-cards-vmu).

## Do my handheld's Sega save states work on the phone?

Yes. The phone runs the Sega consoles on PicoDrive, as the handheld does, so
a state made in a handheld folder such as `Sega Genesis (MD)` resumes on the
phone.

- **Games from a handheld `(GPGX)` folder** ran on Genesis Plus GX there.
  [Device Sync](../../mobile/device-sync.md) sets such a game's
  **Emulator** to Genesis Plus GX when it brings the game over, so its
  states resume too. For a game you copied yourself, pick Genesis Plus GX in
  its **Emulator** menu.
- **Battery saves** work in either emulator: PicoDrive and Genesis Plus GX
  share them.

See [Emulators](../../mobile/emulators/sega.md).

## Do I need to download emulators or cores?

No. Every core is bundled in the app. See
[Emulators](../../mobile/emulators/index.md) for the full list.

## Is there DraStic or Dreamcast?

There is no DraStic. It is closed-source and no longer available, so
Nintendo DS runs on **melonDS DS** instead. DraStic battery saves carry over.

Dreamcast is included, with the NAOMI and Atomiswave arcade games. See
[Sega Dreamcast](../../mobile/emulators/dreamcast.md).

## Can I play netplay with the app?

Yes. Two players can play over Wi-Fi or a USB-C cable, phone to phone or
phone to an NX Redux handheld (TrimUI Brick, Brick Pro or Smart Pro S).
Press `Y` **Netplay** on a game. Game Boy and Game Boy Advance games link
for trades and battles. See [Netplay](../../mobile/netplay.md).

## Can I sync saves with my handheld?

Yes. **Tools → Device Sync** carries saves and save states between the phone
and an NX Redux handheld, over Wi-Fi or a USB-C cable. Update the handheld to
the latest NX Redux first. ROMs sync too when you turn them on, with
**All files access** allowed. See [Device Sync](../../mobile/device-sync.md).

## Can two people play on one phone?

Yes. Two to four people can play one game, each on their own controller.
Start the game and press a button on each controller to join. Nintendo 64,
Sega Dreamcast, Arcade and TurboGrafx-16 take up to four players, and most
other home consoles two. See [Local Multiplayer](../../mobile/multiplayer.md).

## Can a second player use the touch controls?

No. The on-screen pad always controls Player 1, so every other player needs
a controller.

## Why did my Joy-Cons become two players?

Android sees a pair of Joy-Cons as two controllers, so each one joins as its
own player. Multitap adapters, such as the NES Four Score, aren't supported
yet either. See [Local Multiplayer](../../mobile/multiplayer.md#limits).

## Can I remap controller buttons?

Not freely. Each console has a fixed mapping, and face buttons work **as
printed**: your controller's `A` is the console's `A`. To swap the layout,
use **Controller Layout** in the in-game menu's **Options → Console
Settings**.

On a controller without a mode button, hold `SELECT` + `START` to open the
in-game menu. See [Controls](../../mobile/controls.md).

??? info "More detail"
    - PlayStation, PSP, Sega, arcade and a few others go by position instead
      of by letter.
    - **Controller Layout** names your controller's letters: **Auto-detect**,
      **Xbox (A at the bottom)** or **Nintendo (A on the right)**. Pick the
      one that isn't your controller's for the console's original button
      positions, such as the right button as `A` on Super Nintendo with an
      Xbox pad.

## Is there a RetroAchievements hardcore mode?

No, the same as on the handheld. RetroAchievements in the app is softcore
only, so cheats and save states are not blocked. See
[RetroAchievements](../../mobile/retroachievements.md).

## How do I find a game in a big library?

Press `START` on the main menu, or tap the **Search** icon, and type part of
its name. Case, accents, punctuation and word order don't matter, and
`fantasy 6` finds *Final Fantasy VI*. In a game list, `START` searches just
that list. See [Search](../../mobile/main-menu.md#search).

## Can I make the text smaller?

Yes. **Tools → Settings → Appearance → Text size** has **Large** (the
default) and **Small**. It sets the text of the lists, page titles and
button hints across the app. First-run setup asks it first. See
[Text size](../../mobile/appearance.md#text-size).

## Where does the game artwork come from?

The app fetches it. Open **Tools → Artwork** and pick **Fetch missing art**,
or **Fetch by console**. To fetch one game, press `MENU` on it and pick
**Fetch art**. See [Artwork](../../mobile/artwork.md).

??? info "More detail"
    The art comes from ScreenScraper, libretro-thumbnails, TheGamesDB and
    SteamGridDB, and is saved in each game folder's `.media` folder. Art you
    put there yourself is used too.

## Why does artwork need a ScreenScraper account or API keys?

It doesn't have to. libretro-thumbnails needs nothing, and ScreenScraper
works without an account at a small daily quota.

- **Signing in to ScreenScraper** raises that quota, so a large library
  fetches faster.
- **TheGamesDB** and **SteamGridDB** are only used with your own free API
  key.

Set them in **Tools → Artwork → Settings**. See
[Artwork](../../mobile/artwork.md).

## Can I use the app as my home screen?

Yes. Turn on **Use as home screen** in **Tools → Settings → System**. The
phone's Home key then brings you back to the app's **Home** tab. You can also
open any Android app from **Tools → Apps**, and add apps to **Tools**. See
[Launcher Mode & Android Games](../../mobile/launcher.md).

## Why do Android games have no play time?

The app only starts an Android game. The game runs in its own app, so NX
Redux can't tell how long you play. Android games have no play time, and
they don't show in recents or on the Continue card. See
[Launcher Mode & Android Games](../../mobile/launcher.md).

## Does the app work on foldables?

Yes. On a half-folded phone with a horizontal hinge, the game moves above the
fold and the controls go below it. This is automatic. On a wide screen, such
as an unfolded Fold held sideways, some pages split into two panes. See
[Foldables & Large Screens](../../mobile/foldables.md).

??? info "More detail"
    - Nintendo DS games keep their usual layout when folded.
    - The pages that split into two panes are Settings, the in-game menu,
      RetroAchievements and Artwork.

## I removed my SD card and some games disappeared

Games from a folder on a card that is not mounted are left out until the card
is back. **Tools → Settings → Library** marks the folder **Not available**. Nothing is lost. See
[Library & ROM folders](../../mobile/library.md).

## Is there an iOS version?

Not yet. NX Redux runs on Android only for now. An iOS version follows
the Android one.
