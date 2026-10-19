# PlayStation

PlayStation games run on the bundled **PCSX-ReARMed** core. Games in a
`PSX` folder run on **SwanStation**, as on the handheld.

| | PCSX-ReARMed | SwanStation |
| --- | --- | --- |
| Folder | `Roms/Sony PlayStation (PS)/` | `Roms/Sony PlayStation (PSX)/` |
| Saves | `Saves/PS/` | `Saves/PSX/` |
| BIOS | Optional: a BIOS is built in. A real one in `Bios/PS/` is used when present. | Needed: `scph5500.bin` (Japan), `scph5501.bin` (USA) or `scph5502.bin` (Europe) in `Bios/PSX/` |
| [File types](index.md) | `chd` `cue` `bin` `img` `iso` `pbp` `toc` `mdf` `cbn` `m3u` | `chd` `cue` `bin` `img` `iso` `pbp` `ecm` `mds` `m3u` |

!!! tip "Use a real BIOS"
    The built-in BIOS plays most games, but some only work with a real one.
    For PCSX-ReARMed, put one of `psxonpsp660.bin`, `scph101.bin`,
    `scph5501.bin`, `scph7001.bin` or `scph1001.bin` in `Bios/PS/`.

- To pick the emulator for a folder without a tag, or for one game, see
  [Choosing an emulator](index.md#choosing-an-emulator).
- **Graphics API** can switch a SwanStation (`PSX`) game to Vulkan. See
  [Graphics API](index.md#graphics-api).

## Controls

<figure class="nx-phone" markdown>
![Mega Man X4 on the Fold's cover screen, with the PlayStation pad: × ○ △ □](../../assets/screenshots/mobile/pad-ps.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>

The face buttons map to the PlayStation buttons **by position**:

| Position | PlayStation button |
| --- | --- |
| Bottom | Cross (×) |
| Right | Circle (○) |
| Top | Triangle (△) |
| Left | Square (□) |

| Control | PlayStation control |
| --- | --- |
| D-pad | D-pad |
| Left and right sticks | The DualShock's analog sticks |
| `L1`, `R1`, `L2`, `R2` | `L1`, `R1`, `L2`, `R2` |
| `START`, `SELECT` | `START`, `SELECT` |

- In the app's menus, `×` confirms and `○` goes back.
- `MENU`, or `SELECT` + `START`, opens the [in-game menu](../in-game-menu.md).
- Games with [DualShock rumble](../controls.md#game-rumble) rumble.

## Multi-disc games

Put a multi-disc game in an `.m3u` that lists its discs, or use a multi-disc
`.pbp`. The in-game menu then has a **Disc** row to change disc; see
[Multi-disc games](index.md#multi-disc-games).

## Multiplayer

- Two players can play, each on their own controller; see
  [Local Multiplayer](../multiplayer.md). The game sees a DualShock pad for
  both.
- PlayStation games also play over [Netplay](../netplay.md), on both cores.

## Cheats and achievements

- [Cheats](../cheats.md): the cheat download has codes for PlayStation games,
  on both cores, or add your own `.cht` files.
- [RetroAchievements](../retroachievements.md) works for PlayStation games.

## Limits

- PlayStation `.exe` homebrew doesn't load.
