# Device Sync

**Tools → Device Sync** moves your progress between the phone and an NX Redux
handheld (TrimUI Brick, Brick Pro or Smart Pro S), over a USB-C cable or
Wi-Fi. It works the same way as the handheld's
[Device Sync](../handheld/apps/device-sync.md), and the two talk to each
other.

!!! warning "Update the handheld first"
    Device Sync needs the latest NX Redux on the handheld. An older version
    stops at pairing with **Update the handheld to the latest NX Redux to use
    Device Sync.**, before anything is copied.

## What gets synced

- **Game saves** (`Saves/`)
- **Save states**, with their slot pictures
- **ROMs**, only when you turn them on (see [ROMs](#roms)), with their art and
  RetroAchievements data
- **BIOS** files, **collections** and game hashes

Everything else stays on each device: settings, recently played, play time and
your RetroAchievements login.

## How to sync

1. Connect the devices with a **USB-C cable** (the handheld's **bottom**
   port, the same as for [netplay](netplay.md#usb-cable)), or put both on the
   **same Wi-Fi network**.
2. Close any running game. Device Sync won't start while a game is open,
   and no game starts while a sync runs.
3. Open **Tools → Device Sync** on both devices.
4. Pick **Sync via cable** (the default) or **Sync via Wi-Fi**, the same on
   both devices, and press `A` **Start**. The devices find each other and
   sync.

The page's rows are **Sync ROMs**, where it is offered (see [ROMs](#roms)),
then **Sync via cable** and **Sync via Wi-Fi**. `UP` / `DOWN` move round
them.

While it runs, the page shows the step, such as **2/7 Sending save files**,
the file count and each file as it is copied. A sync has 4 steps (states and
saves), 7 with All files access (BIOS and collections too), and 9 with ROMs.
When it ends, it shows how many files each side got, such as **Sync
complete: 12 files received, 5 sent.**

| Button | What it does |
| --- | --- |
| `A` **Start** | Start the sync |
| `B` **Cancel** | Stop looking for the other device |
| `B` **Stop** | Stop a running sync. It asks **Stop the sync?** first. |
| `A` **Sync again** / **Retry** | Run it again, after it ends or fails |
| `A` on **Sync ROMs** | Switch ROMs **On** or **Off**. `LEFT` / `RIGHT` and `X` work too. |
| `B` **Back** | Go back |

- A stopped sync keeps the files it already copied.
- A sync that is stopped or fails on one device ends on the other at once.
  A phone left waiting says **The other device's sync failed. Check it, then
  sync again.**; a handheld says **The other device's sync failed**.
- If the cable comes out during a sync, the phone stops with **The cable was
  disconnected. Plug it in firmly on both devices, then sync again.**
- If the other device paired but its answer was lost, the phone stops with **The
  other device paired, but its answer never reached this phone. Stop the
  sync on it, then start again on both.**
- You can leave the page or switch apps: the sync goes on, with a
  **Device Sync** notification. The notification's **Cancel** stops
  it. Open Device Sync again to see where it is.
- Sync via Wi-Fi needs the phone on Wi-Fi. If it isn't, the page says
  **Wi-Fi not connected. Turn on Wi-Fi, or sync via cable.**

## ROMs

ROMs are off each time you open the page. **Sync ROMs** is the page's first
row, and the page opens on it: `A` or a tap switches it **On**, and the
headline then names ROMs too. `X` switches it as well, with a notice:
**ROMs will sync too** or **ROMs won't sync**.

- ROM sync needs [**All files access**](library.md#all-files-access). Without
  it, there is no Sync ROMs row.
- ROMs sync when either device turns them on. When the other device asks for
  them and this phone can't, the rest still syncs and the end says **ROMs
  were skipped: turn on All files access to sync them.**

Between two phones, each console folder syncs as it is. With a handheld, the
phone's one folder per console maps onto the handheld's per-emulator folders:

- Games from every handheld folder of a console land in the phone's console
  folder. A game the handheld keeps in two emulator folders of one console
  is pulled once.
- A game pulled from a handheld emulator folder, such as `Game Boy Advance
  (MGBA)` or `Sega Master System (GPGX)`, keeps that emulator on the phone:
  it becomes the game's **Emulator** choice. A game that already has a
  choice keeps it.
- Each phone game goes to one handheld folder: the one whose tag is the
  emulator the phone runs the game with. With several such folders, the one
  named like the console. With none, the console's first emulator folder the
  handheld has. A handheld with only `Sony PlayStation (PSX)` gets the
  phone's PCSX ReARMed games there.
- A console the handheld has no folder for is skipped, and listed when the
  sync is done. Sync never creates a ROM folder on the handheld.
- Box art and screenshots travel with the games, and only fill gaps.

Handheld folders that were renamed still match: by the console's name,
ignoring case, spaces and punctuation (`Gameboy (GB)`, `Mastersystem
(GPGX)`), by a console name inside the folder name (`Sega Mega-CD (GPGX)`), or
by the tag. A folder with a tag that several consoles share, such as `GPGX`,
and a name no console matches is skipped, not guessed.

Saves match by game across the handheld's save formats (MinUI, Generic,
RetroArch, compressed) and go where the game is. BIOS files only fill what the
other side lacks, per console. Collections and game hashes follow the same
mapping.

On Nintendo DS, when a game's only save is the handheld's DraStic `.dsv`, the
phone plays and saves that `.dsv` in place, so progress goes both ways. A game
you started on the phone keeps the phone's save format.

## In first-run setup

When you tell first-run setup you also play on an NX Redux handheld, its
**Sync with your handheld** step is this page, under the setup's step title.
**Skip** sits at the top right, and reads **Continue** once a sync has ended;
`A` **Continue** on the finished sync goes on with setup. See
[Getting Started](getting-started.md).

??? info "More detail"
    - Sync never deletes anything. A file missing on one device is copied
      over; when both devices have the same file, the newer one replaces the
      older one.
    - Both devices send and receive in the same session, so one run brings
      both up to date. A second run right after copies almost nothing.
    - Save states only work with the emulator that made them; states for an
      emulator the other device doesn't have are copied but unused.
    - macOS leftovers (`._*` files, `.DS_Store`) are skipped.
    - Device Sync and [**Import saves**](library.md) don't run at the same
      time. Start during an import says **Wait for the import to finish,
      then sync.**
