# Game Boy Advance

NX Redux ships two Game Boy Advance cores, **gpSP** and **mGBA**. You choose
one per game by which `Roms` folder the game is in:

| | gpSP | mGBA |
| --- | --- | --- |
| Folder | `Roms/Game Boy Advance (GBA)/` | `Roms/Game Boy Advance (MGBA)/` |
| Strength | Faster | More accurate, better for ROM hacks |
| [Netplay](../netplay.md) (GBA Link) | Yes, for link and wireless adapter games | Link cable games, [USB Cable](../netplay.md#mgba-link-cable-over-usb) only |
| BIOS | Recommended: `Bios/GBA/gba_bios.bin` | Optional: `Bios/MGBA/gba_bios.bin` |
| [File types](rom-formats.md) | `gba` `bin` `agb` `gbz` | `gba` |

## Which one to use

Start with **gpSP** in the `GBA` folder. It is the faster core, and the right
choice for most games.

Use **mGBA** in the `MGBA` folder for **ROM hacks**, and for any game that
glitches, crashes or runs incorrectly on gpSP. mGBA trades some speed for
accuracy, so it handles games that gpSP gets wrong.

!!! warning "Netplay needs a game that supports link play"
    Netplay only works with games that support the GBA **link cable or
    wireless adapter**, such as trading and versus modes. **gpSP** plays over
    USB Cable, Hotspot and WiFi, wireless adapter included. **mGBA** plays
    link cable games over the
    [USB Cable](../netplay.md#mgba-link-cable-over-usb) only, so for Wi-Fi
    or the Union Room move the game to the `GBA` folder.

??? info "More detail: netplay"
    Netplay connects the GBA **link cable** (and, on gpSP, the **wireless
    adapter**), so games without link play have nothing to connect. Both
    players must use the same folder: an mGBA device can't link with a gpSP
    device.

!!! note "gpSP and the BIOS"
    gpSP has a built-in replacement BIOS, so games start without one. The
    real `gba_bios.bin` in `Bios/GBA/` improves compatibility. See
    [Cores & BIOS Files](cores.md).

## Using both

You can keep the same game in both folders. The game list then shows it
twice with the emulator tag, `Advance Wars (GBA)` and
`Advance Wars (MGBA)`. Pick the core each time you play (see
[duplicate names](../guide/main-menu.md#duplicate-names)).

![Game Boy Advance game list showing Advance Wars twice, tagged (MGBA) and (GBA)](../../assets/screenshots/game-list-duplicates.png)

Saves are kept per folder, in `Saves/GBA/` and `Saves/MGBA/`. To carry your
progress across, copy the game's save file from one folder to the other.
Save states cannot move between the two cores.

??? info "More detail"
    Battery saves are written in the RetroArch-compatible `.srm` format by
    default, which is why the save file can be copied between the folders.

## Super Game Boy

The `Super Game Boy (SGB)` folder runs Game Boy games on **mGBA** as a Super
Game Boy. `sgb_bios.bin` in `Bios/SGB/` is optional and gives full Super Game
Boy accuracy.

It has no netplay. Use the `Game Boy (GB)` folder for
Game Boy link cable games.
