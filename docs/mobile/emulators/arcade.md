# Arcade (FBNeo)

Arcade games run on the bundled **FinalBurn Neo** core.

| | FinalBurn Neo |
| --- | --- |
| Folder | `Roms/Arcade (FBN)/` |
| Saves | `Saves/FBN/` |
| BIOS | BIOS sets, such as `neogeo.zip`, next to the games or in `Bios/FBN/` |
| [File types](index.md) | `zip` `7z` (MAME-style sets) |

- NAOMI and Atomiswave games run on Flycast instead, from the Dreamcast
  folder. See [Sega Dreamcast](dreamcast.md#naomi-and-atomiswave).

## Controls

| Control | What it does |
| --- | --- |
| `SELECT` | Insert a coin |
| `START` | Start |
| D-pad, left stick | The joystick |
| Face buttons and shoulders | The game's buttons |

- `MENU`, or `SELECT` + `START`, opens the [in-game menu](../in-game-menu.md).
  The game sees the `SELECT` press first, so it may count a coin.
- Some games put extra buttons, such as Service, on `L3` and `R3` (pressing
  the sticks), on controllers only.

## Adding games

- Put the zips (or 7z) in the folder as they are. Each one *is* the game.
- Put BIOS sets, such as `neogeo.zip`, next to the games or in `Bios/FBN/`.
- A missing BIOS set stops the launch with a message.

??? info "More detail"
    - Arcade sets are never unpacked.
    - Parent sets are read from the same folder or from `Bios/FBN/`. A
      missing parent set doesn't stop the launch: the game is tried without
      it.
    - BIOS sets are not listed as games.
    - Games show their arcade titles, with bracketed text dropped as on the
      handheld.

!!! warning "Don't rename the zips"
    FBNeo finds a game by its short zip name (`sf2.zip`). The game list shows
    the readable title anyway. To pick your own name, use **Rename Rom** or a
    `map.txt` alias.

## Multiplayer

- Up to four players can play, each on their own controller, as many as the
  game has. See [Local Multiplayer](../multiplayer.md).
- Arcade games also play over [Netplay](../netplay.md).

## Cheats and achievements

- Cheats: not available for arcade games. The in-game menu has no **Cheats**
  page for them.
- [RetroAchievements](../retroachievements.md) works for arcade games it
  recognises.
