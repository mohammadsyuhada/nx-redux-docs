# Release Notes

What changed in each NX Redux release. Download packages for every device
from the [releases page](https://github.com/mohammadsyuhada/nx-redux/releases),
or update on the device from [Settings → About](../settings/about.md).

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
  [Cores & BIOS Files](../emulators/cores.md#systems-and-cores).
- **Dreamcast RetroAchievements.** Flycast now follows the tool's **Enable
  achievements** setting like the built-in cores, with **Hardcore Mode** as
  its one per-game option. The RetroAchievements tool caches Dreamcast, Naomi
  and Atomiswave games (`.chd`, `.gdi`, `.cdi`, `.cue`, `.zip`) and lists
  multi-disc games once. See
  [Dreamcast → RetroAchievements](../emulators/dreamcast.md#retroachievements).
- **Two-phase Sync now.** **Sync now** pushes waiting offline unlocks, then
  pulls your points and unlock state back from the server, so achievements
  earned in Flycast, on another device or on the website show up in the tool.
  Both steps show a progress bar and `B` cancels. See
  [RetroAchievements → Syncing](../apps/retroachievements.md#syncing).
- **Search closes with START.** Tapping `START` again while the search
  keyboard or results list is open returns you to the menu, the same way
  `SELECT` closes the Game Switcher. See
  [Main Menu → Search](../guide/main-menu.md#search).
- **Clearer duplicate names.** When the same game appears in two cores' lists,
  each row shows the emulator tag (`Advance Wars (GBA)` / `(MGBA)`) instead
  of the file extension, dimmed after the name. See
  [Main Menu → Duplicate names](../guide/main-menu.md#duplicate-names).
- **Files.** The left stick moves through folders and panes, holding a
  direction scrolls, the cursor bars are gray, and the face buttons follow the
  device-wide [Button Layout](../guide/button-layout.md). See
  [Files](../apps/files.md).
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
  [Developer → Enable SSH](../settings/developer.md#enable-ssh).

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
  [Xtras Store](../apps/xtras.md#cheat-database), then browse and download
  per-game cheat codes straight from the libretro cheat database — no PC
  needed. Downloaded cheats are picked up automatically the next time you
  open a game's in-game menu. See [Cheats](../apps/cheats.md).
- **Nintendo / Xbox button layout.** A new setting swaps the meaning of the
  face buttons and relabels every hint, so an Xbox-style layout reads
  correctly across the launcher, emulators, PortMaster and the OSD. See
  [Button Layout](../guide/button-layout.md).
- **Netplay save handling.** A lockstep session now plays on the host's save
  and leaves the client's own save completely untouched, so joining a friend
  never overwrites your progress. See [Netplay → Saves](../netplay.md#saves).
- **Join a different version of a game.** If a host is running a sister
  version of the same title — FireRed and LeafGreen, say — the joiner is
  offered a **Join anyway?** prompt instead of being refused. See
  [Netplay → Different versions of one game](../netplay.md#different-versions-of-one-game).
- **Artwork Manager scanning and status.** The Artwork Manager now scans your
  Roms the same way the game list does — every file type, nested folders and
  folder games — lists tags it does not recognise, and shows how complete
  each game's art is. The library drops the sort prefix, shows your
  `map.txt` rename names, and fits one more game per screen. See
  [Artwork Manager](../apps/artwork-manager.md).
- **Pokémon Gen1Recomp++.** The Xtras Pokémon recreation is rebuilt: it
  adopts the upstream launcher's own controls with an on-screen **Select**
  keyboard, scans Gen 2 ROMs, and drops the voxel mod bundle and swapfile for
  a lighter install. See
  [Xtras → Pokémon Gen1Recomp](../apps/xtras.md#pokemon-gen1recomp).
- **Developer debug logging.** A **Debug logging** toggle under
  [Developer settings](../settings/developer.md#debug-logging) turns off all
  `.userdata` log writes when you do not need them, keeping the card clean.

### Fixes

- **Amiga:** Kickstart and other system-scanned option lists now populate in
  [Emulator Settings](../guide/emulator-options.md) instead of showing only a
  placeholder.
- **PSP:** the Brick black screen with minui-psp 6.x is fixed — the PSP pak
  now installs unmodified into its platform folder.
- **Nintendo DS:** the DraStic stylus toggle works on the Brick and Brick
  Pro, and every device now shows the same pen image. See
  [Nintendo DS → Stylus mode](../emulators/nintendo-ds.md#stylus-mode).
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
  [Music Player → Background playback](../apps/music-player.md#background-playback).
- **Music widget in the OSD.** The [On-Screen Display](../guide/osd.md) now
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
  (`Light` / `Normal` / `Strong`) is in [System settings](../settings/system.md),
  and haptic feedback is now on by default.
- **Smart Pro S firmware 1.0.2** is supported alongside 1.0.1 — see
  [Getting Started](../getting-started.md#before-you-install).
- **Game art style and type.** [Appearance](../settings/appearance.md) gains
  **Game art style** (`Thumbnail` or a full-height `Background` that fades
  into the list) and **Game art type** (`Mix`, `Screenshot` or `Box art`).
  The [Artwork Manager](../apps/artwork-manager.md#what-gets-saved) now saves
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
  [Nintendo 64 → Video plugin](../emulators/nintendo-64.md#video-plugin).
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
- **Desktop:** the Linux AppImage no longer bundles the host's graphics
  driver libraries and ships its own libsqlite3.
- **Bluetooth:** the stock-stack backup archive is no longer kept, and
  leftovers are removed on update.

!!! note "Existing game art"
    Releases up to v1.9.0 saved only the Mix image, so the new
    **Screenshot** and **Box art** types fall back to it and the
    **Background** style shows nothing for art fetched back then. To get
    the extra images for an existing library, open **Artwork Manager →
    Settings → Reset artwork**, then queue your systems again. See
    [Appearance → Game art type](../settings/appearance.md#game-art-type).

## Earlier releases

Notes for v1.9.0 and older are on the
[GitHub releases page](https://github.com/mohammadsyuhada/nx-redux/releases).
