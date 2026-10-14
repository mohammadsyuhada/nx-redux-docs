# PlayStation Portable

Play PSP games from `Roms/Sony Playstation Portable (PSP)/`. PSP is built in:
there is nothing to install, and no BIOS or firmware file is needed.

PSP gets the same features as the other systems:

- the [in-game menu](../guide/in-game-options.md) with save states (slots
  with previews), auto-resume and the [Game Switcher](../guide/game-switcher.md)
- fast-forward, screenshots, shaders and screen effects
- playtime tracking and ambient LEDs
- RetroAchievements and cheats through NX Redux

!!! warning "Upgrading from the Xtras PSP emulator"
    Older versions installed a standalone PPSSPP from the [Xtras](../apps/xtras.md)
    store. Updating NX Redux removes it and **moves your in-game saves
    across automatically**, along with texture packs, installed DLC and
    homebrew (`GAME`), plugins and screenshots. Its own settings and cheat
    files are kept in `Saves/PSP/standalone-backup/` rather than deleted.

    **Save states made with the standalone PPSSPP can't be loaded.** Save
    your progress in-game before updating if you rely on a save state.

??? info "More detail"
    PSP games run on **PPSSPP**, bundled as a libretro core and played inside
    NX Redux's own emulator, like most other systems. That's why it gets the
    same features.

## Controls

The face buttons map to the PSP buttons **by position**:

| Device button | PSP button |
| --- | --- |
| Bottom (`B` on the cap) | Cross (✕) |
| Right (`A` on the cap) | Circle (○) |
| Left (`Y` on the cap) | Square (□) |
| Top (`X` on the cap) | Triangle (△) |

| Device control | PSP control |
| --- | --- |
| D-pad | D-pad |
| Left stick | Analog stick |
| `L1` / `R1` | L / R |
| **START** / **SELECT** | START / SELECT |

In PSP system dialogs (saving, loading, entering a name) **✕ confirms**. To
use ○ instead, change **Confirmation Button** in the
[Emulator Options](../guide/emulator-options.md).

The mapping is the same under either
[Button Layout](../guide/button-layout.md). Only the in-game menu's confirm
and back follow that setting.

## Game files

PSP games can be `.iso`, `.cso`, `.chd` or `.pbp` (PSN downloads and
homebrew). `.chd` and `.cso` are compressed and save space.

## Saves

In-game saves are stored in `Saves/PSP/SAVEDATA/`, one folder per game (the
same folders a real PSP keeps in `PSP/SAVEDATA` on its memory stick), so you can
copy saves to and from a PSP or another emulator.

!!! note "Firmware files"
    The first time you play, PPSSPP copies some system files from the game
    disc into `Saves/PSP/NAND/` (about 57 MB). Leave that folder in place.

## Performance

!!! tip "Best on the Smart Pro S"
    The **Smart Pro S** runs every PSP game tested at full speed, including
    Tekken 6 at 2× Rendering Resolution. The **Brick, Brick Hammer, Brick Pro and Smart
    Pro** share a slower chip: most games still run at full speed there, but
    the heaviest 3D games don't.

Measured at the default resolution while playing:

| Game | Brick | Smart Pro S |
| --- | --- | --- |
| Metal Slug XX | Full speed | Full speed |
| Ace Combat X: Skies of Deception | Full speed (first mission) | Full speed |
| Grand Theft Auto: Vice City Stories | About 88% on foot | Full speed |
| Tekken 6 | About 78% in fights; menus at full speed | Full speed, also at 2× |

To get a heavy game to full speed on the Brick, turn on frame skipping for
that game in [Emulator Options](../guide/emulator-options.md):

| Option | Use it for |
| --- | --- |
| **Auto Frameskip** | Games that run at 30 frames per second (Grand Theft Auto: Vice City Stories, Final Fantasy Type-0), especially at 2× Rendering Resolution |
| **Frameskip** `1` | 60 frames per second games such as Tekken 6 (then shown at 30 frames per second, at full speed) |

Leave both off for other games: skipping frames can halve the frame rate even
when a game keeps up, so they are off by default.

**Rendering Resolution** is the PSP's native 480×272 (1×) by default. 2×
(960×544) looks sharper and runs at full speed on the Smart Pro S; on the
Brick family it needs **Auto Frameskip** in heavier games.

??? info "More detail: frame skipping and resolution"
    - **Auto Frameskip** skips frames only when the game falls behind: Vice
      City Stories at 2× went from about 70% to full speed on the Brick and
      still showed about 30 frames per second.
    - **Frameskip** `1`: Tekken 6 measured about 99% at 1× on the Brick.
    - **Resolutions above 2×** aren't offered: they exceed the screen and only
      cost speed and heat.
    - These and the other PPSSPP options are in
      [Emulator Options](../guide/emulator-options.md), for all games or per
      game.

!!! warning "Reset Game"
    **Reset Game** restarts the game, but the restarted game may stop
    responding to the buttons. Quit and launch the game again instead.
