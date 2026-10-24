---
title: Handheld Release Notes
---

# Handheld Release Notes

What changed in each NX Redux release for TrimUI handhelds. Download packages
for every device from the
[releases page](https://github.com/nx-redux/nx-handheld/releases), or
update on the device from [Settings → About](../../handheld/settings/about.md).

## v2.4.0

*24 October 2026*

Games start and quit faster, and resuming goes straight from the menu to your
game without a black screen. RetroAchievements can download achievement data
one console at a time, and about a thousand more cheats work, including MSX.
Home, the Grid and Settings get a round of layout fixes, and Save & Quit from
the in-game menu no longer crashes.

### New features

- **Faster launch and quit.** On the Brick a Game Boy game resumes in about
  0.9 s instead of 1.4 s, and **Save & Quit** gets you back to the menu in
  0.8 s instead of 2 s. Resuming shows the save state's picture until the
  game's first frame, and quitting keeps the last frame on screen until the
  menu appears, so neither passes through black.
- **RetroAchievements Library.** The RetroAchievements tool's new
  [Library](../../handheld/apps/retroachievements.md#library) lists each
  console with how many of its games have their achievement data downloaded.
  `A` downloads one console, `Y` all of them. Zipped (`.zip`/`.7z`) games
  are now identified (they came back as "not in RetroAchievements" before),
  and libraries over 4,096 games are no longer cut short.
- **RAM cheats.** About a thousand cheat files in the database hold
  [RAM cheats](../../handheld/apps/cheats.md#two-kinds-of-cheats), which
  showed in **Options → Cheats** but did nothing. They now apply: arcade,
  Dreamcast, ColecoVision, Atari, Lynx and MSX, plus some SNES and PC Engine
  games. MSX cheats were never downloaded; download the cheat database again
  to get them.

### Changes

- **Grid (Brick and Brick Pro):** game lists, Consoles and Collections show
  two tiles across, all at one size, and the selected column stays in the
  middle as you scroll. Tools tiles are a little wider on every device, and
  game list tiles are 50% wider on the Smart Pro S.
- **Home, pinned games:** two rows of pinned games fill the screen when you
  scroll down to them, centred between the top and bottom bars. On the Smart
  Pro S the first two pinned games stand beside the Continue card, the rest
  follow below in rows of three, and the pinned tools always stand in columns
  of five.
- **Settings and options pages** (Settings, in-game Options, Launch Options,
  the Music Player's settings and Artwork Manager) start at the top of the
  screen instead of being centred.
- **Button hints hidden:** with **Extra info** hidden too, the Game Switcher
  and List game lists no longer keep an empty black bar at the bottom. With
  the page title hidden, Home no longer fades its top edge while scrolled.
- **Game Switcher:** the console name and position under the game's name are
  larger.
- **Simple Mode:** a game's `MENU` no longer offers Delete, Rename, Pin,
  Add to Collection, Emulator Options, Launch Options or Fetch Artwork. See
  [Simple Mode](../../handheld/guide/simple-mode.md).
- **Artwork Manager:** finished downloads clear themselves, and the
  **Clear Done** button is gone.

### Fixes

- **Save & Quit:** quitting from the in-game menu crashed on the way out
  every time. The save and its picture were already written, but the
  in-game clock, RetroAchievements and the emulator itself (on PSP, its
  shader cache) weren't shut down properly.
- **Brick Pro:** it could reboot by itself a few seconds after waking from
  sleep, when Bluetooth came back on.
- **Updates:** **Check for updates** failed after the project moved to the
  [nx-redux](https://github.com/nx-redux/nx-handheld) organisation. It now
  checks the new address and follows a moved project's redirect.
- **PSP cheats:** cheats from the cheat database load and apply, and a game
  with a cheat already turned on no longer crashes at launch.
- **Cheats:**
    - Long cheat codes load. They had shown with no code, and some crashed
      the SNES, Mega Drive, N64, PC Engine and Supafaust emulators.
    - **Options → Cheats** no longer crashes on a cheat without a name. Names
      show `&` and accented letters instead of codes such as `&amp;`.
    - A game without a region in its name gets the full cheat set, and names
      spelled differently in the database (*Soulcalibur*, *Marvel vs Capcom
      2*) are found.
- **Saves and settings** are written safely, so a crash or power loss while
  saving no longer leaves a broken file.
- **Screenshots and save-state pictures** no longer include a message that
  was on screen, such as "State Saved".
- **Game names with a dot** (*Super Mario Bros. 3*, *Ys Vol. 2*) show in
  full.
- **Large zipped games:** a game too big to unzip into memory shows "Game
  too big to unzip" instead of filling it.
- **Streams:** radio, podcast and lyrics connections now check the server's
  certificate. A device whose clock is badly wrong can't open them until the
  clock is set.

## v2.3.0

*21 October 2026*

A new Minimal layout shows your games as big names only, and search results
open as a regular game list. The in-game Shortcuts menu is back for setting a
console's or a game's own shortcuts. Fast-forward up to 4x is smooth again,
and over-the-air updates no longer fail as "corrupt" on the Smart Pro S.

### New features

- **Minimal layout.** **Settings → Layouts** offers **Minimal** for Home,
  the Consoles, Collections and Tools tabs and the game lists: big names
  only, no art, with the selected name in your accent color. Long names wrap,
  Home shows each game's tag (Continue, New…) next to the selected name, and
  opening a console whose list is also Minimal carries its name up into the
  title. See [Minimal](../../handheld/guide/layouts.md#minimal) and
  [Minimal Home](../../handheld/guide/main-menu.md#minimal).
- **Search results as a game list.** [Search](../../handheld/guide/main-menu.md#search)
  results now open as a game list in your **Layouts → Game list layout**
  (List, Grid, Carousel, Backdrop or Minimal), with the same menu and launch
  options as any other list.
- **Shortcuts for one console or game.** The in-game **Options → Shortcuts**
  page is back. A shortcut you set there replaces the
  [Settings → Emulator Shortcuts](../../handheld/settings/emulator-shortcuts.md)
  one for that console or game (keep it with **Save Changes**); the others
  keep following Settings. Shortcuts you saved for a console or game before
  v2.2.0 work again, unless you have saved its options since. See
  [In-game Options](../../handheld/guide/in-game-options.md#shortcuts).

### Fixes

- **Fast-forward:** at a Max FF Speed of 2x to 4x, fast-forward shows a new
  frame on every screen refresh again (about 60 fps instead of an uneven 20
  to 30). Since v2.1.2 it looked jumpy, most of all on PlayStation at 2x.
  None and 5x to 8x keep the faster mode.
- **Updates (Smart Pro S):** an over-the-air update could fail with
  "MinUI.zip is corrupt or the card is full", then retry and fail on every
  boot. Files the card's driver had left hidden from earlier boots blocked
  the update; they are now cleared before it runs.

## v2.2.1

*19 October 2026*

A fix for PortMaster.

### Fixes

- **PortMaster:** after PortMaster updated itself to 2026.10.18, every port
  install failed and was rolled back. Ports install again; ports you
  installed earlier were not affected.
- **Moonlight New:** pairing failed with a missing `libavcodec.so.58`; it
  now finds the library PortMaster ships.

## v2.2.0

*18 October 2026*

Device Sync now works over a USB cable, syncs with NX Redux for Android, and
also carries your BIOS files and collections. Emulator shortcuts move to
Settings and apply to every game. Consoles can use your own logos, and
fast-forward runs faster on SNES, arcade and Mega Drive.

!!! warning "Before you update"
    - **Set your emulator shortcuts again.** Shortcuts are now set once for
      every game in **Settings → Emulator Shortcuts**. Shortcuts you set
      earlier in a game's **Options → Shortcuts** menu (for a console or a
      game) don't carry over. The FN switch no longer turns on turbo fire or
      D-pad joystick mode; bind the **Toggle Turbo** and **Toggle D-pad
      Joystick** shortcuts instead. See
      [Emulator Shortcuts](../../handheld/settings/emulator-shortcuts.md).
    - **Achievement badges download again.** Badges are now kept per game in
      each console's ROM folder, and the old badge folder is removed on
      update. Each game's badges come back the next time you launch it
      online, or all at once with **RetroAchievements → Download all game
      data**. Your achievements and offline unlocks are kept.
    - **Update both devices before using Device Sync.** A device on v2.1 or
      older still sends its settings and recently played list, can't sync
      over the cable, and skips BIOS files and collections.
    - **Old Dreamcast memory cards are no longer copied in on every launch.**
      If your cards are still in the old standalone emulator's folder, copy
      them across once by hand. See
      [Bringing in an existing card](../../handheld/emulators/dreamcast.md#bringing-in-an-existing-card).

### New features

- **Device Sync over a USB cable.** **Tools → Device Sync** gets **Sync via
  cable** (the default) next to **Sync via Wi-Fi**, using the same cable as
  netplay. See [Device Sync](../../handheld/apps/device-sync.md).
- **Device Sync carries only your progress.** Saves, save states and, if you
  turn them on, ROMs. Settings, recently played, pinned games and your
  RetroAchievements login stay on each device. It also adds your BIOS files
  (never replacing one the other device already has) and merges your
  collections on both sides. It can sync with a phone running NX Redux for
  Android.
- **Emulator shortcuts in Settings.** **Settings → Emulator Shortcuts** sets
  save, load, reset, fast-forward, Game Switcher and the other shortcuts for
  every game in one place, plus a new **Toggle D-pad Joystick** shortcut that
  makes the D-pad move the left stick. The **FN switch** now turns night mode
  on and off only.
- **Your own console logos.** Put a `logo.png` in a console's
  `Roms/<Folder>/.media/` folder to give a custom console a logo or replace
  a built-in one. See
  [Your own console logos](../../handheld/guide/layouts.md#your-own-console-logos).
- **Console backgrounds in the Carousel.** The Consoles Carousel shows a
  console's `.media/bg.png` behind it when **Consoles background** (renamed
  from **Consoles controller**) is set to **Background**. See
  [Your own console backgrounds](../../handheld/guide/layouts.md#your-own-console-backgrounds).
- **Quit without saving.** On **Quit** in the in-game menu, `X` quits without
  the resume save, so **Resume** goes back to where you were before. `A`
  still saves and quits.
- **Rotate pictures.** In the **Image Viewer**, `Y` turns the picture 90°
  clockwise and saves it to the file. See
  [Image Viewer](../../handheld/apps/image-viewer.md).
- **Controller art.** Ports show a modern gamepad, and Pico-8, Doom and the
  home computers show a keyboard, instead of a blank space.

### Improvements

- **Faster fast-forward.** SNES (snes9x and Supafaust), FBNeo arcade and
  Genesis Plus GX no longer draw the frames fast-forward skips, so they get
  much closer to your Max FF Speed (SNES at 8x on the Brick went from about
  2.75x to 5.5x).
- **Faster RetroAchievements launches.** Each console folder remembers its
  games' fingerprints, so a game isn't checked again on every launch, and
  **Download** in the RetroAchievements app skips games it has already
  checked.

### Fixes

- **Device Sync:** a sync could hang when the devices paired but one missed
  the other's reply, and a failed or cancelled sync on one device left the
  other waiting. A sync cut short (`B`, cable pulled, Wi-Fi lost) no longer
  leaves a half-copied file behind. ROM sync no longer copies a game into a
  second emulator folder of the same console, and never replaces existing
  game art.
- **Dreamcast:** save states made mid-game (on the handheld or a phone) load
  on the first try. The shared memory cards now live in `Saves/DC`, so Device
  Sync carries them with your other saves; existing cards move there on
  their own.
- **Nintendo 64:** save, load and Game Switcher shortcuts no longer freeze
  the game.
- **Nintendo DS (Brick, Brick Pro):** holding `A` drags the stylus again.
- **Game Boy Advance:** Classic NES Series carts (such as *Pac-Man* or
  *Super Mario Bros.*) now run; they start on mGBA automatically, keeping
  their saves in `Saves/GBA`.

## v2.1.2

*13 October 2026*

A patch release. The Game Switcher gets a List layout, fast-forward and
PlayStation run faster, and a launch could load the wrong game from a zip.
RetroAchievements, PSP and mGBA each get fixes too.

### New features

- **Game Switcher List layout.** **Settings → Layouts → Game Switcher
  layout** switches between **Full screen** (the default) and **List**, which
  shows your recent games as a list with the selected game's last frame
  behind it. Full screen gets a larger title and an info line that runs the
  full width and follows **Extra info**. See
  [Game Switcher](../../handheld/guide/game-switcher.md).
- **Resume and Netplay in the context menu.** With **Layouts → Button
  hints** set to `Hide`, a game's `MENU` context menu now lists **Resume (X)** and
  **Netplay (Y)** so those actions stay easy to find.
- **Settings moved.** The boot view and Game Switcher rows are now under
  **Layouts**, and the clock rows under **Appearance**.

### Fixes

- **Zipped games:** launching a game could load another game whose name
  starts the same way (for example *Double Dragon* opening *Double Dragon
  II*), with saves going to the wrong game. Every zip or 7z now unpacks into
  its own folder.
- **RetroAchievements:** an achievement earned offline no longer shows as
  locked when you open the game again online before the sync finishes, and
  the **offline (softcore)** notice shows again when a game starts without
  Wi-Fi.
- **PSP:** choosing **Vulkan** or **None** as the Backend made games very
  slow (the core fell back to software rendering). Backend now offers
  **Automatic** and **OpenGL** only; a saved Vulkan setting switches back
  automatically.
- **Fast-forward:** NES and Famicom Disk System now reach the Max FF Speed
  you set (they stopped at 2x on the Brick).
- **Smart Pro S:** the lighter consoles (NES, SNES, Mega Drive, Game Boy and
  others) no longer stutter or crackle on CPU **Auto**, and shaders get the
  full GPU speed.
- **PlayStation (Brick, Brick Pro):** threaded rendering is on by default,
  so demanding games drop far fewer frames.
- **Dreamcast, Nintendo 64, PSP:** the left stick no longer also presses the
  D-pad.
- **mGBA:** **More Sun** and **Less Sun** now brighten and darken the solar
  sensor as named (they were swapped), for the Boktai games.
- **Music Player:** some MP3s with a cover embedded in the file showed a
  wrong cover fetched online instead; the embedded cover now shows.

## v2.1.1

*12 October 2026*

A patch release. PortMaster ports get per-game CPU and GPU settings, Game Boy
Advance no longer lags on the Smart Pro S, and RetroAchievements, the Music
Player and Weston-based ports each get fixes.

### New features

- **Launch Options for ports.** Choose **Launch Options** in a port's context
  menu to set its CPU speed and, on the Smart Pro S, how many CPU cores and
  how much GPU speed it gets. Lower settings save battery on light games;
  higher ones help heavy ports. Each port remembers its choice, and
  **Tools → Emulator Settings → Ports (Launch Options)** sets the default for
  all of them. See [Launch Options](../../handheld/guide/launch-options.md).
- **JPG game art.** Box art and screenshots saved as `.jpg` or `.jpeg` in a
  `.media` folder now show when there is no `.png` with the same name.

### Fixes

- **Game Boy Advance (Smart Pro S):** gpSP and mGBA no longer lag, including
  with a shader on.
- **RetroAchievements:** achievements made offline now sync even when your
  username in Settings is capitalised differently from your account.
  **Sync** no longer downloads games it already has, and the achievement list
  follows the set's own order, so **Next** shows the right achievement.
- **PortMaster:** ports that use the Weston runtime no
  longer unmount the SD card and leave a black screen.
- **Music Player:** song tags and radio song titles in non-English text
  (accents, Japanese, Cyrillic and so on) show correctly instead of `???` or
  nothing.

## v2.1.0

*11 October 2026*

Netplay grows up in NX Redux 2.1: play over a USB cable between two devices,
link Game Boy Advance games with a real link cable, and start netplay straight
from Home. Nintendo 64 now runs inside NX Redux's own emulator, PlayStation
gains a second, sharper system (SwanStation) and Dreamcast a lighter one for
the slower devices, and the menus run at a smooth 60 fps with more art choices
for your game lists.

!!! warning "Before you update"
    - **Netplay needs v2.1 on both devices.** v2.1 can't play with v2.0 or
      older.
    - **Nintendo 64 save states** made with the old standalone emulator can't
      be loaded. Make an in-game save first if you rely on one; in-game saves
      and Controller Pak data come across on a game's first launch.
    - **Coming from v1.x?** Back up your SD card first. A clean install is
      recommended: delete the hidden `.system` and `.tmp_update` folders
      (keep `Roms`, `Saves`, `Bios` and `.userdata`), then extract the
      release.
    - **Your own paks are no longer removed on update.** A pak in `/Emus` or
      `/Tools` with the same name as a shipped one is now ignored instead, so
      give yours its own name. See
      [Additional Emulators](../../handheld/emulators/additional.md).
    - **The first start after updating rescans your games once** (the list
      cache changed), so it takes a little longer than usual.

### New features

- **Netplay over a USB cable.** Connect two devices with a USB-C cable and
  pick **USB Cable** in the netplay wizard: no Wi-Fi, and lower lag. See
  [Netplay → USB Cable](../../handheld/netplay.md#usb-cable).
- **A real Game Boy Advance link cable.** Over the USB cable, GBA games link
  like the original cable: trade Pokémon, play Four Swords or Mario Kart
  multiplayer, on both gpSP and mGBA. See
  [Game Boy Advance link cable over USB](../../handheld/netplay.md#game-boy-advance-link-cable-over-usb)
  and [mGBA link cable over USB](../../handheld/netplay.md#mgba-link-cable-over-usb).
- **Netplay from Home.** `Y` starts the Continue game or a pinned game with
  netplay, as it does in the game lists. See
  [Home](../../handheld/guide/main-menu.md#home).
- **Better netplay.** Analog sticks stay in sync (PlayStation), the
  third and fourth players' input reaches the game, Genesis Plus GX games
  support netplay, and the wizard says on both screens when the two devices
  picked the game from different folders (different emulators). A
  **Show netplay hint** setting hides the `Y NETPLAY` hint. See
  [Netplay](../../handheld/netplay.md) and
  [Show netplay hint](../../handheld/settings/appearance.md#show-netplay-hint).
- **Nintendo 64 on NX Redux's emulator.** N64 runs on Mupen64Plus-Next with
  the in-game menu, save states with screenshots, RetroAchievements, cheats
  and the Game Switcher. The Brick uses the lighter Rice video plugin, high
  resolution texture packs still work, and N64 netplay supports up to four
  players (3–4 players need a Smart Pro S on every seat). See
  [Nintendo 64](../../handheld/emulators/nintendo-64.md).
- **SwanStation for PlayStation.** A second PlayStation system with a more
  accurate emulator that draws on the GPU and can render 3D games at a higher
  resolution. Put games in `Roms/Sony PlayStation (PSX)/`. See
  [SwanStation](../../handheld/emulators/playstation.md#swanstation).
- **Dreamcast Lite.** A second Dreamcast system on a lighter Flycast that keeps
  heavy 3D games such as Crazy Taxi 2 at full speed on the Brick, Brick Pro and
  Smart Pro. See
  [Dreamcast Lite](../../handheld/emulators/dreamcast.md#dreamcast-lite).
- **Home in List and Carousel layouts.** Home now comes as a **List**,
  **Grid** or **Carousel**, and **Extra info** hides the stats. See
  [Home](../../handheld/guide/main-menu.md#home) and
  [Home layout](../../handheld/settings/layouts.md#home-layout).
- **Smooth menus.** Every layout, Home and the game lists scroll at 60 fps,
  and **Settings → Layouts** gathers all the layout choices in one place. See
  [Layouts](../../handheld/settings/layouts.md).
- **More art in game lists.** The List can show a game's **Mix**, **3D box
  art**, **2D box art** or **Wheel** in a box beside the list, Backdrop can use
  them as the picture, and **None** hides list art or the Consoles controller.
  The Artwork Manager can download 2D box art and wheels and build a Mix. See
  [List art](../../handheld/settings/layouts.md#list-art),
  [Backdrop art](../../handheld/settings/layouts.md#backdrop-art) and
  [Artwork Manager](../../handheld/apps/artwork-manager.md).
- **Optimize images.** The Artwork Manager can shrink your existing art so
  menus load faster. See
  [Optimize images](../../handheld/apps/artwork-manager.md#optimize-images).
- **Your own console backgrounds.** With **Consoles controller** set to
  **Background**, a `bg.png` in a console's `.media` folder shows behind it
  in the List layout. See
  [Your own console backgrounds](../../handheld/guide/layouts.md#your-own-console-backgrounds).
- **Text sized for each device.** Menus use a size tuned for each screen, so
  they look the same on the Brick, Brick Pro and Smart Pro S; the UI scale
  setting is gone.
- **RetroAchievements.** Games are recognized from their emulator, file type
  and folder, so more of your games earn achievements, and a game now tells
  you when it has no achievements or isn't recognized. See
  [RetroAchievements](../../handheld/apps/retroachievements.md).
- **Music Player.** Lyrics show more lines on the Brick Pro and Smart Pro S,
  album art is looked up in your country's iTunes store, then the US store,
  then Deezer, and the spectrum visualizer moves smoothly. Tap `START` on the
  music, radio or podcast player to leave the app and keep listening. See
  [Background playback](../../handheld/apps/music-player.md#background-playback).
- **Newer emulators.** Snes9x, FCEUmm, Gambatte and mGBA are updated to their
  latest versions.
- **Faster emulators.** DraStic (Nintendo DS) runs at the CPU's full speed,
  **Auto** CPU speed uses the whole clock range, and the Smart Pro S keeps its
  fast cores on for the lighter systems.

### Fixes

- **Brick Pro:** no more random reboots after joining Wi-Fi.
- **PSP:** games save again on FAT32-formatted cards.
- **Game Boy Advance:** gpSP no longer crashes when a netplay session starts.
- **Netplay:** a session stays in step when one player's menu closes while the
  other's is still open, a host only accepts the device it paired with, and
  Genesis games always use a 3-button pad in a session so both devices match.
- **Fast-forward:** **Max FF Speed** now really caps the speed.
- **Saving:** **Save** in the in-game menu is instant again with shaders on.
- **Home:** multi-disc games kept in a folder show their screenshot and box
  art.
- **Collections:** games show the name you gave them (including multi-disc
  games kept in a folder), **New Collection** checks the name the way
  **Rename** does, and the Collections tab appears as soon as you make your
  first collection. Renaming a game no longer writes a stray entry into
  `Collections/map.txt`.
- **Delete Rom** also removes the game's artwork. Saves and save states are
  kept.
- **Consoles:** a folder without a `(TAG)`, such as `Roms/GB`, no longer pulls
  in another console's games (`GBA`), and a tab inside a `map.txt` no longer
  makes every start rescan your games.
- **Backdrop:** the picture no longer goes black after a menu closes or in a
  short list such as a collection.
- **Artwork:** fetched art shows right away, and **Refresh Roms** picks up art
  you copied onto the card.
- **Last played:** a game started from Search or the Game Switcher while inside
  a collection reopens in its own place.
- **PortMaster:** ports from the NextOS Ports catalog no longer show a black
  screen on the Brick, Brick Pro and Smart Pro, Streets of Rage 4 from NextOS
  Ports installs on the Brick, and a failed PortMaster install or upgrade keeps
  its `config`, `libs` and `themes`.
- **RetroAchievements:** keep working after the device sleeps, and unlocks
  made offline sync reliably.
- **Music Player:** with the screen off, `A` still plays and pauses and the
  power button still works.
- **Battery:** the percentage shows while charging.
- **Volume:** with an FN mode set and the volume on **Unchanged**, launching
  an app no longer jumps to full volume.
- **Background music (Brick, Brick Pro):** no more pop when an app or game
  starts.
- **Brightness and color temperature:** holding `SELECT` with the volume keys
  works after the device has been idle, and volume-only presses no longer show
  the brightness hint.
- **OSD:** changing a setting from the OSD no longer pops the speaker or
  flashes the screen.
- **LED Control:** only lists the effects the LED actually supports.
- **SSH:** turning SSH off also closes open sessions, so it stays off.
- **Updates:** a failed in-app update download no longer leaves a broken zip
  that makes Windows ask for "the last disk of a multi-volume set".
- **Updates keep your files:** an update no longer overwrites your edited
  shader presets, overlays or sample art, no longer resets the DraStic layout
  and theme, and keeps PSP standalone save states when an earlier backup
  exists. A damaged `MinUI.zip` no longer leaves the device unable to start:
  the update is skipped and the current system boots. The Bluetooth upgrade no
  longer leaves a 26 MB `.update_bluez` folder behind.
- **Third-party paks:** paks built on the old mute settings, such as
  minui-presenter, start again.
- **Folders:** every system now has its `Bios`, `Cheats`, `Overlays` and
  `Saves` folders on a fresh install.

## v2.0.0

*4 October 2026*

A redesigned main menu leads NX Redux 2.0: a Home dashboard, tabs, and four
layouts for consoles and game lists. Dreamcast and PSP now run inside NX
Redux's own emulator with the in-game menu, save states and
RetroAchievements, WonderSwan is built in, and the Music Player reads the
tags, cover art and lyrics inside your files.

!!! warning "Before you update"
    - **Dreamcast and PSP save states** made with the old standalone
      emulators can't be loaded. Save in-game first if you rely on one.
      In-game saves and memory cards come across automatically.
    - The PSP emulator from Xtras is removed on update; PSP is now built in.

### New features

- **New main menu.** The menu opens on **Home** with **Consoles**,
  **Collections** and **Tools** tabs beside it. Switch tabs with `L1`/`R1`,
  or press `Up` from the top of a tab to reach the tab row. See
  [Main Menu & Home](../../handheld/guide/main-menu.md).
- **Home.** A **Continue** card for your last game (with its save-state
  picture), this month's play time, achievements and most played game, and
  your pinned games and tools. On a fresh install a **Pick a game** card
  opens the Consoles tab. Launching from Home brings you back to Continue.
  See [Home](../../handheld/guide/main-menu.md#home).
- **Pinning.** Pin games with **Pin Item** and tools with **Pin Tool** from
  `MENU`. Up to 12 pins, of which up to 9 can be tools, and Home always shows
  every one. See
  [Pinning games and tools](../../handheld/guide/main-menu.md#pinning-games-and-tools).
- **Four layouts.** Each tab and the game lists can be drawn as a **List**,
  **Grid**, **Carousel** or **Backdrop** (box art over the game's
  screenshot), across or down the screen. Choose them in
  **Settings → Appearance → Layouts**. See
  [Menu Layouts](../../handheld/guide/layouts.md).
- **Collections.** Rename or delete a collection from `MENU`, and console
  and collection entries show how many games they hold. See
  [Collections](../../handheld/guide/main-menu.md#collections).
- **A refreshed look across the apps.** Page titles show where you are
  (*Settings | Appearance*), lists and option pages share a cleaner layout,
  and the Game Switcher and progress screens match the new menu.
- **Dreamcast on NX Redux's emulator.** Dreamcast, Naomi and Atomiswave run
  on Flycast 2.7 inside NX Redux's own emulator: the in-game menu, save-state
  slots with previews, auto-resume, the Game Switcher, fast-forward, shaders
  and RetroAchievements. Each game gets its own memory card (your old card is
  copied in on first launch), 30 fps games run at their real speed, and
  Dreamcast netplay uses the same wizard as the other systems. See
  [Sega Dreamcast](../../handheld/emulators/dreamcast.md).
- **PSP built in.** PSP runs on PPSSPP inside NX Redux's emulator, with the
  in-game menu, save states, auto-resume, shaders, RetroAchievements and
  cheats. There is nothing to install from Xtras, and updating moves your PSP
  saves, DLC, texture packs and plugins across. See
  [PlayStation Portable](../../handheld/emulators/psp.md).
- **WonderSwan built in.** WonderSwan and WonderSwan Color games play from
  the `Wonderswan Color (WSC)` folder with no pak to install, and earn
  RetroAchievements. See
  [Other Systems](../../handheld/emulators/other-systems.md#wonderswan-and-wonderswan-color).
- **Music Player tags, cover art and lyrics.** Titles, artists, albums and
  cover art are read from MP3, M4A, FLAC, Ogg and Opus files, and lyrics
  embedded in a file are shown before any online lookup. See
  [Music Player → Now playing](../../handheld/apps/music-player.md#now-playing).
- **Rename Rom keeps the name.** **Rename Rom** opens with the game's current
  name typed in, and the keyboard has a movable text cursor (`L1`/`R1`, or
  `Up` to the text line). See
  [On-Screen Keyboard](../../handheld/guide/keyboard.md#editing-an-existing-name).
- **Arcade versions told apart.** Arcade games that share a title are
  labelled by region or version (*Alien vs. Predator (Europe)* /
  *(Japan)*) instead of the zip name, in the game list and in Search. See
  [Keeping several versions of a game](../../handheld/emulators/arcade.md#keeping-several-versions-of-a-game).
- **PortMaster community catalogs.** **NextOS Ports** and **RHH Ports** are
  one-tap installs in Xtras; PortMaster then lists their ports alongside the
  official ones. See
  [PortMaster → Community catalogs](../../handheld/apps/portmaster.md#community-catalogs).
- **Leaving netplay.** During any netplay session, `MENU` now opens a single
  **Leave netplay?** prompt.

### Fixes

- **PortMaster:** ports such as Perfect Dark and Celeste find their data
  again, ports that need the Weston display (The Binding of Isaac: Rebirth)
  start instead of showing a black screen, the PortMaster app follows your
  [Button Layout](../../handheld/guide/button-layout.md) and is larger and
  easier to read on the Brick, and the Brick Pro's two analog sticks are
  reported to ports again. Ports that change their home folder keep
  Bluetooth and USB audio routing.
- **RetroAchievements:** games with large achievement sets (Pokémon
  FireRed, for one) no longer freeze for several seconds at launch.
- **Music Player:** a USB DAC or headset plugged in or removed while nothing
  is playing is used straight away, and playback no longer drops short
  moments of silence under load.
- **Volume:** the lowest volume steps are quieter on the speaker and
  headphones.
- **Secure downloads:** updates, Xtras installs, the Cheat Database and the
  Music and Media Players now check server certificates properly.

## v1.13.0

*28 September 2026*

A selectable UI scale, a new NX Redux look, and readable arcade game names
lead this release, alongside fixes for Dreamcast controls, long IPTV channel
lists, search and netplay over a hotspot.

### New features

- **UI scale.** **Settings → Appearance → UI scale** sets the size of text
  and menus across the whole UI: **Default**, **1x** (smaller, more rows) or
  **2x** (larger, fewer rows). Default follows the device, 2x on the Brick and
  1x on the Brick Pro and Smart Pro S. The Dreamcast and Nintendo 64 in-game
  menus follow it too. See [Appearance → UI scale](../../handheld/settings/appearance.md#ui-scale).
- **New NX Redux look.** The new NX Redux mark is the install splash, the
  default boot logo and the default background. The previous NextUI boot logo is still in the boot logo list. See
  [Why "NX Redux"?](../../about.md#why-nx-redux).
- **Arcade game titles.** FBNeo, Naomi and Atomiswave zips show their full
  game title instead of the short zip name (`mslug.zip` shows as
  *Metal Slug - Super Vehicle-001*), and BIOS zips such as `neogeo.zip` are
  hidden from the game list automatically. **Rename Rom** and `map.txt`
  names still win. See [Arcade (FBNeo)](../../handheld/emulators/arcade.md) and
  [Dreamcast → Arcade games](../../handheld/emulators/dreamcast.md#arcade-games-naomi-atomiswave).
- **Scraping Sega and arcade games.** The Artwork Manager recognises the
  `(GPGX)` tag and matches each Sega game by its file extension (Master
  System, Game Gear, SG-1000, Sega CD or Genesis), so all your Sega games can
  live under `(GPGX)` folders and still get the right art. Naomi and
  Atomiswave zips in the `DC` folder are scraped as arcade sets. See
  [Artwork Manager](../../handheld/apps/artwork-manager.md).
- **SFTP file access.** The Developer toggles are now **Enable SSH / SFTP**
  and **Start SSH / SFTP on boot**, making clear that the same switch lets
  you browse and copy files on the SD card over Wi-Fi with an SFTP client
  such as FileZilla. A new guide page walks through it. See
  [Accessing Your Files](../../handheld/guide/file-access.md).

### Fixes

- **Dreamcast:** the face buttons map to the Dreamcast pad by position
  (bottom is Dreamcast `A`, right is `B`), so games that use the face buttons
  for the camera, like Unreal Tournament, play as designed. This holds under
  either button layout. See [Dreamcast → Controls](../../handheld/emulators/dreamcast.md#controls).
- **Media Player:** Online TV no longer cuts long country lists short. The
  whole list is shown (the United States alone has over 1,400 channels), and
  the channel list gains `L1`/`R1` to jump between letters and `LEFT`/`RIGHT`
  to jump a page.
- **Search:** results use your `map.txt` names, show the dimmed emulator tag
  for duplicates like the game lists do, and include games from every console
  folder.
- **In-game menu:** the "X / Y unlocked" count now shows on the Achievements
  entry.
- **Netplay:** a host running its own hotspot is now found by the joining
  device, and the joiner's prompt for a different game title appears.
- **Launching games:** ROMs whose path contains two spaces in a row launch
  correctly.
- **Game Tracker:** play time for games with an apostrophe in the title is
  recorded under the right game.

## v1.12.0

*22 September 2026*

Genesis Plus GX joins as a second Sega core, Dreamcast gets full
RetroAchievements support, and a save-truncation bug from v1.10.0 is fixed.
Menus and emulators also run cooler with new per-device CPU policies.

### New features

- **Genesis Plus GX.** A more accurate alternative to PicoDrive that plays
  Genesis/Mega Drive, Master System, Game Gear, SG-1000 and Sega CD from a
  single `(GPGX)` tag, picking the system from each ROM's extension so
  RetroAchievements identifies every game with the right console. Name a
  `Roms` folder `Sega Genesis (GPGX)`, say, to use it. See
  [Other Systems](../../handheld/emulators/other-systems.md#sega-genesis-sega-cd-32x-master-system-game-gear-and-sg-1000).
- **Dreamcast RetroAchievements.** Flycast now follows the tool's **Enable
  achievements** setting like the built-in cores, with **Hardcore Mode** as
  its one per-game option. The RetroAchievements tool caches Dreamcast, Naomi
  and Atomiswave games (`.chd`, `.gdi`, `.cdi`, `.cue`, `.zip`) and lists
  multi-disc games once. See
  [Dreamcast → RetroAchievements](../../handheld/emulators/dreamcast.md#retroachievements).
- **Two-phase Sync now.** **Sync now** pushes waiting offline unlocks, then
  pulls your points and unlock state back from the server, so achievements
  earned in Flycast, on another device or on the website show up in the tool.
  Both steps show a progress bar and `B` cancels. See
  [RetroAchievements → Syncing](../../handheld/apps/retroachievements.md#syncing).
- **Search closes with START.** Tapping `START` again while the search
  keyboard or results list is open returns you to the menu, the same way
  `SELECT` closes the Game Switcher. See
  [Main Menu → Search](../../handheld/guide/main-menu.md#search).
- **Clearer duplicate names.** When the same game appears in two cores' lists,
  each row shows the emulator tag (`Advance Wars (GBA)` / `(MGBA)`) instead
  of the file extension, dimmed after the name. See
  [Main Menu → Duplicate names](../../handheld/guide/main-menu.md#duplicate-names).
- **Files.** The left stick moves through folders and panes, holding a
  direction scrolls, the cursor bars are gray, and the face buttons follow the
  device-wide [Button Layout](../../handheld/guide/button-layout.md). See
  [Files](../../handheld/apps/files.md).
- **Verified HTTPS.** The launcher and tools now check server certificates
  against a bundled CA store when downloading updates, Xtras and cheats,
  instead of skipping verification.

### Performance

- **Launcher CPU policy.** The launcher runs at full speed while booting,
  then caps the CPU while you browse and drops further after three seconds
  without input. On the Smart Pro S the big core is switched off entirely
  for the launcher and the tools, so menus run cooler on less battery.
- **Per-core CPU profiles.** Each emulator ships a measured CPU range that
  the **Auto** CPU speed applies, instead of every core running the whole
  frequency range. On the Smart Pro S, PlayStation runs on both big cores
  with the render and audio helpers moved to the little cores, and the
  **Auto** ceiling no longer clamps the big core to the little cluster's top
  speed.
- **Rumble.** The vibration thread sleeps between rumble events instead of
  polling settings every 17 ms.

### Fixes

- **Saves:** quitting a game no longer writes a 0 KB save over your existing
  one. A regression since v1.10.0, most reported on Game Boy Advance and
  Game Boy Color on the Brick.
- **Cheats:** on PCSX-ReARMed, enabling a cheat other than the first one now
  activates it even when the cheats before it are off.
- **Dreamcast:** RetroAchievements login from Flycast no longer fails with
  "No response"; Flycast now finds the certificate bundle it needs for HTTPS.
- **Music Player:** opening the app while its background service is still
  starting shows a loading screen instead of failing to launch.
- **Search:** the hint bar repaints cleanly when the shift indicator clears.

## v1.11.1

*19 September 2026*

A small patch release. The Smart Pro S no longer pops from the speaker at
boot or when a game starts, its Bluetooth comes back after sleep, the
On-Screen Display gets three fixes and a lighter idle poll, and the
Developer SSH toggle now shows the full login line with the device's IP.

### New features

- **SSH login hint.** While SSH is running, the hint under
  **Settings → Developer → Enable SSH** shows the exact login line with the
  device's current IP address and password, and the connected network in
  **Settings → Network** shows the same IP. See
  [Developer → Enable SSH](../../handheld/settings/developer.md#enable-ssh-sftp).

### Fixes

- **Smart Pro S:** the speaker pop at boot and at the start of a game,
  most noticeable with the N64, Nintendo DS and Dreamcast emulators, is
  gone. The codec powers its output stage up for every new audio stream
  and that transient reached the speaker amp; the amp is now kept muted
  until the stream is running and is unmuted with the volume held at zero.
- **Smart Pro S:** Bluetooth re-attaches after the device wakes from sleep,
  and stays off when you have disabled it.
- **OSD:** on the Brick Pro the **Home** press that opens the panel no longer
  closes it again, the slider widget is centred, and the active widget's
  focus ring stays white instead of taking the theme accent.
- **OSD:** the hidden daemon polls input every 20 ms instead of every
  millisecond, so it uses less CPU while the panel is closed.

## v1.11.0

*17 September 2026*

This release adds a built-in cheat downloader, a Nintendo / Xbox button
layout setting, and safer Netplay saves that never touch the client's own.
The Artwork Manager scans Roms like the game list, Pokémon Gen1Recomp++
replaces the old Xtras recreation, and a batch of fixes covers Amiga, PSP,
DraStic, offline RetroAchievements and the Brick updater.

### New features

- **Built-in cheat downloader.** Install the **Cheat Database** tool from the
  [Xtras Store](../../handheld/apps/xtras.md#cheat-database), then browse and download
  per-game cheat codes straight from the libretro cheat database — no PC
  needed. Downloaded cheats are picked up automatically the next time you
  open a game's in-game menu. See [Cheats](../../handheld/apps/cheats.md).
- **Nintendo / Xbox button layout.** A new setting swaps the meaning of the
  face buttons and relabels every hint, so an Xbox-style layout reads
  correctly across the launcher, emulators, PortMaster and the OSD. See
  [Button Layout](../../handheld/guide/button-layout.md).
- **Netplay save handling.** A lockstep session now plays on the host's save
  and leaves the client's own save completely untouched, so joining a friend
  never overwrites your progress. See [Netplay → Saves](../../handheld/netplay.md#saves).
- **Join a different version of a game.** If a host is running a sister
  version of the same title — FireRed and LeafGreen, say — the joiner is
  offered a **Join anyway?** prompt instead of being refused. See
  [Netplay → Different versions of one game](../../handheld/netplay.md#different-versions-of-one-game).
- **Artwork Manager scanning and status.** The Artwork Manager now scans your
  Roms the same way the game list does — every file type, nested folders and
  folder games — lists tags it does not recognise, and shows how complete
  each game's art is. The library drops the sort prefix, shows your
  `map.txt` rename names, and fits one more game per screen. See
  [Artwork Manager](../../handheld/apps/artwork-manager.md).
- **Pokémon Gen1Recomp++.** The Xtras Pokémon recreation is rebuilt: it
  adopts the upstream launcher's own controls with an on-screen **Select**
  keyboard, scans Gen 2 ROMs, and drops the voxel mod bundle and swapfile for
  a lighter install. See
  [Xtras → Pokémon Gen1Recomp](../../handheld/apps/xtras.md#pokemon-gen1recomp).
- **Developer debug logging.** A **Debug logging** toggle under
  [Developer settings](../../handheld/settings/developer.md#debug-logging) turns off all
  `.userdata` log writes when you do not need them, keeping the card clean.

### Fixes

- **Amiga:** Kickstart and other system-scanned option lists now populate in
  [Emulator Settings](../../handheld/guide/emulator-options.md) instead of showing only a
  placeholder.
- **PSP:** the Brick black screen with minui-psp 6.x is fixed — the PSP pak
  now installs unmodified into its platform folder.
- **Nintendo DS:** the DraStic stylus toggle works on the Brick and Brick
  Pro, and every device now shows the same pen image. See
  [Nintendo DS → Stylus mode](../../handheld/emulators/nintendo-ds.md#stylus-mode).
- **RetroAchievements:** logging in from the pak now writes the offline login
  cache and prefetches, so previously earned achievements show up offline.
- **Brick Pro:** the rumble voltage cap is lowered to 1.7 V so **Normal**
  vibration feels subtler, and the **Home** button closes the OSD.
- **Updater:** installing an update with long release notes no longer crashes
  the Brick's Settings.
- **Settings:** tag-named release builds show the commit date as their
  **Release date**, and settings-row labels now fit beside their value.
- **PortMaster:** it is now a shell launcher and installed paks are migrated
  automatically, so a system update keeps PortMaster installed.

## v1.10.0

*14 September 2026*

This release lets the Music Player keep playing in the background — music,
online radio and podcasts carry on through the menus and inside games, with a
redesigned OSD that puts a Music widget with transport controls and a
Game / Music balance slider at its centre, next to a new Motor toggle that
acts as the master vibration switch. Game lists gain a full-height Background
art style and a choice of Mix, Screenshot or Box art thumbnails, with the
Artwork Manager now saving all three from a single fetch, and theme colours
accept an opacity so pills and accents can show the wallpaper through them.
Nintendo 64 gets a selectable Rice video plugin that is far lighter than
GLideN64 and is now the default on the Brick family, the Smart Pro S is
supported on firmware 1.0.2, app transitions are noticeably quicker, and a
batch of fixes covers Brick Pro deep sleep, turbo fire, the save-slot picker,
Wi-Fi connection errors and Device Sync on FAT32 cards.

### New features

- **Background music playback.** Music, online radio and podcasts keep
  playing when you leave the Music Player — in the menus and inside games.
  Playback is owned by a small background service, so the app is just a
  remote control for it. See
  [Music Player → Background playback](../../handheld/apps/music-player.md#background-playback).
- **Music widget in the OSD.** The [On-Screen Display](../../handheld/guide/osd.md) now
  centres on a Music widget showing the current track or station with
  play/pause, previous and next, plus a **Game / Music balance** slider that
  sets how loud games are relative to the music. The same **Balance** setting
  lives in the Music Player's Settings. With nothing playing the widget
  offers to open the Music Player.
- **OSD redesign.** Widgets are laid out around the Music tile, the volume
  slider is gone (the volume keys already cover it), the focus ring follows
  the theme's accent colour, and the default accent is brighter.
- **Motor toggle and vibration strength.** The OSD's new **Motor** toggle is
  the master vibration switch for the whole device — game rumble, the sleep
  and wake pulses and the new shutdown-complete tap. **Vibration strength**
  (`Light` / `Normal` / `Strong`) is in [System settings](../../handheld/settings/system.md),
  and haptic feedback is now on by default.
- **Smart Pro S firmware 1.0.2** is supported alongside 1.0.1 — see
  [Getting Started](../../handheld/getting-started.md#before-you-install).
- **Game art style and type.** [Appearance](../../handheld/settings/appearance.md) gains
  **Game art style** (`Thumbnail` or a full-height `Background` that fades
  into the list) and **Game art type** (`Mix`, `Screenshot` or `Box art`).
  The [Artwork Manager](../../handheld/apps/artwork-manager.md#what-gets-saved) now saves
  all three images per game from a single ScreenScraper fetch.
- **Theme colour opacity.** **Main color**, **Primary accent** and
  **Secondary accent** each have an opacity setting from `10%` to `100%`;
  below `100%` the pills and accents turn translucent and show the wallpaper
  through them.
- **Show search hint** setting to hide the START search hint on the main
  menu, and **Show game art** is renamed **Game art visible** and now leads
  the game art group.
- **Nintendo 64 video plugin.** Pick **Rice** or **GLideN64** system-wide or
  per game. Rice is much lighter to run and is now the default on the Brick,
  Brick Pro and Smart Pro; the Smart Pro S keeps GLideN64. Each plugin shows
  only its own option sections. See
  [Nintendo 64 → Video plugin](../../handheld/emulators/nintendo-64.md#video-plugin).
- **Faster app transitions and startup.** A short CPU boost around app
  hand-off, quicker screen clears and mixer setup make moving between the
  launcher, Tools and games noticeably snappier.

### Fixes

- **Music:** the background service was hardened after review. Powering on
  restores the last track paused instead of auto-playing, the app stays
  usable if the service is unreachable, launching a standalone emulator no
  longer interrupts playback, shutting down with a stalled radio stream
  completes promptly, and the OSD widget idles at near-zero CPU.
- **Sleep:** Brick Pro deep sleep now pauses stick polling and wakes again
  reliably.
- **Emulation:** turbo fire works, and FBNeo's error screen no longer wedges
  the emulator.
- **In-game menu:** the save/load slot picker is vertically centred and its
  arrows render properly instead of as boxes.
- **Wi-Fi:** a failed connection shows a retry dialog, and rejected passwords
  are no longer saved.
- **Device Sync:** FAT32 timestamp rounding no longer causes unchanged files
  to be copied again.
- **OSD:** the Smart Pro S OSD works from a FAT32 card, its rumble pulses use
  the motor's PWM level, and the Brick Pro grid is centred.
- **UI:** search results and folder art fixes, and the selection pill glide
  honours **Show menu animations**.
- **Video:** an SDL initialisation failure is logged and falls back to
  software rendering instead of crashing.
- **Bluetooth:** the stock-stack backup archive is no longer kept, and
  leftovers are removed on update.

!!! note "Existing game art"
    Releases up to v1.9.0 saved only the Mix image, so the new
    **Screenshot** and **Box art** types fall back to it and the
    **Background** style shows nothing for art fetched back then. To get
    the extra images for an existing library, open **Artwork Manager →
    Settings → Reset artwork**, then queue your systems again. See
    [Artwork Manager → What gets saved](../../handheld/apps/artwork-manager.md#what-gets-saved).

## Earlier releases

Notes for v1.9.0 and older are on the
[GitHub releases page](https://github.com/nx-redux/nx-handheld/releases).
