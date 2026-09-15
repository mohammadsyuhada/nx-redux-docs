---
hide:
  - navigation
---

# Netplay

NX Redux includes [Netplay](https://github.com/mohammadsyuhada/nextui-netplay)
for **local wireless multiplayer**. When a game supports it, the hint bar in
the game list shows `Y NETPLAY`:

![Y NETPLAY hint in the game list](assets/screenshots/game-list.png)

Press `Y` on a supported game to host or join over Wi-Fi or a device-hosted
hotspot — no manual IP entry, no persistent toggle to remember to turn back
off, and save data is synced automatically before the match starts.

![Netplay host/join](assets/screenshots/netplay.png)

## Starting a session

1. Both players pick the same game in their game list and press `Y`.
2. One player chooses **Host Game**, the other **Join Game**.
3. Devices discover each other automatically over the local network (or a
   hotspot hosted by one device); save data syncs before the match starts.

## Supported systems

Netplay is only available on the cores listed below — the `Y NETPLAY` hint
appears only for games in these `Roms` folders. Systems not in the table
(Nintendo DS, Virtual Boy, Neo Geo Pocket, the Atari and Commodore machines,
and so on) have no netplay.

| System | `Roms` folder | Core | Netplay type |
| --- | --- | --- | --- |
| Game Boy | `Game Boy (GB)` | gambatte | **GB Link** — link cable games (Pokémon trades and battles, etc.) |
| Game Boy Color | `Game Boy Color (GBC)` | gambatte | **GB Link** — link cable games |
| Game Boy Advance | `Game Boy Advance (GBA)` | gpSP | **GBA Link** — wireless adapter and link cable games |
| Nintendo ES | `Nintendo ES (FC)` | FCEUmm | Lockstep |
| Famicom Disk System | `Famicom Disk System (FDS)` | FCEUmm | Lockstep |
| Super Nintendo ES | `Super Nintendo ES (SFC)` | Snes9x | Lockstep |
| Super Nintendo ES | `Super Nintendo ES (SUPA)` | Mednafen Supafaust | Lockstep |
| Sega SG-1000 | `Sega SG-1000 (SG1000)` | PicoDrive | Lockstep |
| Sega Master System | `Sega Master System (SMS)` | PicoDrive | Lockstep |
| Sega Game Gear | `Sega Game Gear (GG)` | PicoDrive | Lockstep |
| Sega Genesis | `Sega Genesis (MD)` | PicoDrive | Lockstep |
| Sega CD | `Sega CD (SEGACD)` | PicoDrive | Lockstep |
| Sega 32X | `Sega 32X (32X)` | PicoDrive | Lockstep |
| Sony PlayStation | `Sony PlayStation (PS)` | PCSX-ReARMed | Lockstep |
| Arcade | `Arcade (FBN)` | FBNeo | Lockstep |
| Nintendo 64 | `Nintendo 64 (N64)` | Mupen64Plus (standalone) | Up to 4 players, device-dependent ([details](emulators/nintendo-64.md#netplay)) |
| Sega Dreamcast | `DreamCast (DC)` | Flycast (standalone) | GGPO, up to 2 players ([details](emulators/dreamcast.md#netplay)) |

**Lockstep** is classic frame-synchronised netplay: both devices run the same
game and exchange controller input every frame, so it suits games with a
built-in multiplayer mode. **GB Link** and **GBA Link** instead emulate the
link cable (and, for GBA, the wireless adapter), so single-player-cartridge
features like trading and versus battles work between two devices.

!!! warning "Game Boy Advance: use the `GBA` folder, not `MGBA`"
    NX Redux ships two Game Boy Advance cores in two `Roms` folders:
    **gpSP** in `Game Boy Advance (GBA)` and **mGBA** in
    `Game Boy Advance (MGBA)`. Only **gpSP** supports netplay. A GBA game
    placed in the `MGBA` folder shows no `Y NETPLAY` hint and cannot host or
    join — move it to `Game Boy Advance (GBA)` to play over link.
    The same applies to `Super Game Boy (SGB)`, which also runs on mGBA:
    put Game Boy games in `Game Boy (GB)` / `Game Boy Color (GBC)` for link
    play.

Both players must use the same system folder (and therefore the same core)
for the same game.

## During a session

Save states, fast-forward and rewind are automatically disabled during a
session to protect the connection.
