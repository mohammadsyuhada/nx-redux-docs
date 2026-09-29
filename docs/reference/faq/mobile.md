---
title: Mobile FAQ
---

# Mobile FAQ

Common questions about NX Redux Mobile, the Android app. It is not released
yet, so these answers describe the app as it is being built. Using a TrimUI
handheld? See the [Handheld FAQ](handheld.md).

## Can I use the same games folder as my handheld?

Yes. The app uses the NX Redux layout: `Roms/<Name (TAG)>/`, `Bios/<TAG>/`,
`Saves/<TAG>/`, `Collections/` and `map.txt`. A copy of your handheld's
folders works as the app's home folder. A handheld's BIOS layout (such as
`Bios/PS/psxonpsp660.bin`) works unchanged. See
[Library & ROM folders](../../mobile/library.md).

## Do my handheld saves carry over?

Battery saves carry over for systems that run the same core on both. Where
the app uses the same core as the handheld, save states carry over too. Sega
Genesis, Master System, Game Gear, SG-1000 and Sega CD are the exception:
cartridge saves usually carry over, but save states do not.

## Do I need to download emulators or cores?

No. Every core is bundled in the app. See
[Emulators](../../mobile/emulators.md) for the full list.

## Why is there no DraStic or Dreamcast?

DraStic is closed-source and no longer available, so Nintendo DS runs on
**melonDS DS** instead. Sega Dreamcast is not included in the first release.

## Can I play netplay or use Device Sync with the app?

Not yet. Both are planned for a later release.

## Can I remap controller buttons?

No. Controller buttons map to the NX Redux buttons by their Android names,
and the app has no remapping. On a controller without a mode button, hold
`SELECT` + `START` to open the in-game menu. See
[Controls](../../mobile/controls.md#controller-buttons).

## Is there a RetroAchievements hardcore mode?

Not for now. RetroAchievements on mobile is softcore only for now, so cheats
and save states are not blocked. See
[RetroAchievements](../../mobile/retroachievements.md).

## Where does the game artwork come from?

For now, bring your own. The app shows box art, screenshots and mix images
from each game folder's `.media` folder — the same layout the handheld's
Artwork Manager uses. Downloading art automatically while you browse, and an
art downloader for your whole library, are planned. See
[Artwork](../../mobile/artwork.md).

## I removed my SD card and some games disappeared

Games from a folder on a card that is not mounted are left out until the card
is back. **Tools → Settings → Library** marks the folder
**Not available**. Nothing is lost. See
[Rescanning](../../mobile/library.md#rescanning).

## Is there an iOS version?

An iOS version is planned after Android.
