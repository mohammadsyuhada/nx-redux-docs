# Library & ROM folders

## Home folder and extra folders

The library comes from two kinds of folder:

- **The home folder**, laid out as `Roms/<Name (TAG)>/`. The app created it
  and writes only inside it.
- **Extra folders**, any number of them, scanned in place and never written
  to.

Files in an extra folder are matched to a console:

1. by a `(TAG)` or an alias in the folder name (a short alias such as `GBA`
   may be followed only by roms, games or isos, singular or plural),
2. then by an extension only one console uses (a zip by its first entry, a 7z
   only by its folder).

Anything left over lands in **Unassigned** until you pick its console. The
choice is saved in a `systems.txt` (`<file><TAB><TAG>`). For extra folders
this file lives in the home folder under `Roms/.sources/`, so the extra folder
itself is never changed.

## Unassigned games

**Unassigned** shows on the main menu like a console. Its games can't start
until they have a console. To give one a console:

1. Highlight the game and press `MENU`, or long-press it.
2. Choose **Console**. It lists every console whose emulator can run the
   file's type. A zip or 7z file is unpacked at launch, so every console is
   offered for it.
3. Pick the console. The game moves to that console's list, using the
   console's [default emulator](#default-emulator-per-console).

The context menu for an Unassigned game offers only **Hide Game**, **Rename
Rom** and **Console**.

## Settings → Library

**Tools → Settings → Library** has these rows:

| Row | What it does |
| --- | --- |
| **Home folder** | Shows the home folder. `A` picks a different one. |
| **Add ROM folder** | Pick another extra folder. |
| One row per extra folder | Shows **ROM folder**, or **Not available** while its storage is missing. `A` offers to remove it. |
| **Rescan library** | Scan every folder again. Shows how many games the library has. |
| **Hidden games** | Only when some games are hidden. `A` on a game shows it again. |
| **Game Boy Advance emulator**, **Super Nintendo ES emulator**, **Sega Genesis emulator** | The [default emulator](#default-emulator-per-console) for each console that has more than one. |

Removing an extra folder asks **Stop scanning this folder? Its ROMs stay where
they are.** Choose **Remove** to stop scanning it; nothing in the folder is
deleted.

## Default emulator per console

Three consoles have two emulators, each with its own tag:

| Console | Tags | Default |
| --- | --- | --- |
| Game Boy Advance | `GBA` (gpSP), `MGBA` (mGBA) | `GBA` |
| Super Nintendo | `SFC` (Snes9x), `SUPA` (Supafaust) | `SFC` |
| Sega Genesis | `GPGX`, `MD` (both Genesis Plus GX) | `GPGX` |

The console's row in **Tools → Settings → Library** sets which tag games get
when the app matches them to that console: games in extra folders, and
Unassigned games you give a console. `A` switches to the next tag, and the
library is scanned again with the new choice when you leave the page. Games in
the home folder follow the tag of their `Roms/<Name (TAG)>/` folder.

To run one game on the other emulator, use **Emulator** in its context menu.
For consoles whose saves work on both emulators, the app then offers to copy
the newer save across, keeping a timestamped `.bak` of the save it replaces.

## Rescanning

The scanned library is kept in an index, so the app starts without walking
your folders. After adding or removing games outside the app, use
**Rescan library** in **Tools → Settings → Library**.

An extra folder that was deleted, or whose access was revoked, is dropped
with a notice. A home folder that is lost returns you to the folder picker.

For an SD card taken out: an extra folder's games are left out until the
card is back. A home on that card keeps the last index on screen, and
**Settings → Library** shows **"<name> · not available"**.

## Game names

Bracketed region and version text is dropped from names, as on the handheld:
"Tetris (World) (Rev 1)" shows as "Tetris". If two games would end up with the
same name, both show their file names.

## Custom display names (map.txt)

--8<-- "map-txt.md"

**Rename Rom** in the game-list context menu writes these aliases for you. For
games in an extra folder the alias goes into a `map.txt` under
`Roms/.sources/` in the home folder, and it overrides the extra folder's own
`map.txt`.

## Collections

Use **Add to Collection** in the game-list context menu.

--8<-- "collections.md"

## Saves

Cores play from a private working copy of each battery save, mirrored to
`Saves/<TAG>/` in the home folder. The mirror is updated after each save
write and when you quit. Replace files in `Saves/<TAG>/` only while that game
is not running, because the working copy wins on the next write.

BIOS files are read from `Bios/<TAG>/` before each launch.

Pinned and hidden games are stored inside the app. Hidden games can be shown
again from **Tools → Settings → Library**. Nothing in the app deletes a ROM.

## Unpacked games cache

Zip and 7z games are unpacked into the app's cache on their first launch, and
some cores get a copy of the game file there too. The app trims this cache
when it starts and after **Download all game data** in
[RetroAchievements](retroachievements.md): anything not played for 30 days
goes first, then the least recently used, until the cache holds at most
256 MiB. The game that is running is never removed. Clearing the app's cache
in Android's settings is safe too: games are unpacked again when needed.
