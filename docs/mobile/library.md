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

## Rescanning

The scanned library is kept in an index, so the app starts without walking
your folders. After adding or removing games outside the app, use
**Rescan library** in **Tools → Settings → Library**.

A folder on an SD card that is taken out keeps its place: its games are left
out until the card is back, and **Settings → Library** marks it
**Not available**. A folder that was deleted, or whose access was revoked, is
removed with a notice.

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
