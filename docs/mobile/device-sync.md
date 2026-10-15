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

ROMs don't sync from the phone yet. Everything else stays on each device:
settings, recently played, play time and your RetroAchievements login.

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

While it runs, the page shows the step (**1/4** to **4/4**), the file count
and each file as it is copied. When it ends, it shows how many files each
side got, such as **Sync complete: 12 files received, 5 sent.**

| Button | What it does |
| --- | --- |
| `A` **Start** | Start the sync |
| `B` **Cancel** | Stop looking for the other device |
| `B` **Stop** | Stop a running sync. It asks **Stop the sync?** first. |
| `A` **Sync again** / **Retry** | Run it again, after it ends or fails |
| `B` **Back** | Go back |

- A stopped sync keeps the files it already copied.
- You can leave the page or switch apps: the sync goes on, with a
  **Device Sync** notification. The notification's **Cancel** stops
  it. Open Device Sync again to see where it is.
- Sync via Wi-Fi needs the phone on Wi-Fi. If it isn't, the page says
  **Wi-Fi not connected. Turn on Wi-Fi, or sync via cable.**

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
