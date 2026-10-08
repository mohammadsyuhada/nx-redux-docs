# Arcade (FBNeo)

Arcade games run on the bundled **FinalBurn Neo** core.

| | FinalBurn Neo |
| --- | --- |
| Folder | `Roms/Arcade (FBN)/` |
| BIOS | BIOS sets, such as `neogeo.zip`, next to the games or in `Bios/FBN/` |
| [File types](index.md) | `zip` `7z` (MAME-style sets) |

## Adding games

- An arcade set's zip or 7z *is* the game and is never unpacked.
- Parent and BIOS sets are read from the same folder or from `Bios/FBN/`.
  BIOS sets are not listed as games.
- A missing BIOS set stops the launch with a message. A missing parent set
  does not: the game is tried without it.
- Games show their arcade titles, with bracketed text dropped as on the
  handheld.

!!! warning "Don't rename the zips"
    FBNeo finds a game by its short zip name (`sf2.zip`). The game list shows
    the readable title anyway. To pick your own name, use **Rename Rom** or a
    `map.txt` alias.

## Controls

| Control | What it does |
| --- | --- |
| `SELECT` | Insert a coin |
| `START` | Start |
| D-pad, left stick | The joystick |
| Face buttons and shoulders | The game's buttons |

- Some games put extra buttons, such as Service, on `L3` and `R3` (pressing
  the sticks). Those are on controllers only: the on-screen pad has no stick
  buttons.
- `MENU`, or `SELECT` + `START`, opens the [in-game menu](../in-game-menu.md).
  The game sees the `SELECT` press first, so it may count a coin.
- Up to four players can play, each on their own controller, as many as the
  game has. See [Local Multiplayer](../multiplayer.md).

## Limits

- Arcade has no cheats.

NAOMI and Atomiswave games run on Flycast instead, from the Dreamcast folder.
See [Sega Dreamcast](dreamcast.md#naomi-and-atomiswave).
