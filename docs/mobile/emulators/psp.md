# PlayStation Portable

PSP games run on the bundled **PPSSPP** core.

| | PPSSPP |
| --- | --- |
| Folder | `Roms/Sony Playstation Portable (PSP)/` |
| BIOS | Not needed: PPSSPP's own files are bundled |
| [File types](index.md) | `iso` `cso` `chd` `pbp` `elf` `prx` |

## Controls

<figure class="nx-phone" markdown>
![Tekken 6 on the Fold's cover screen, with the PSP pad: × ○ △ □](../../assets/screenshots/mobile/pad-psp.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>

The face buttons map to the PSP buttons **by position**:

| Position | PSP button |
| --- | --- |
| Bottom | Cross (×) |
| Right | Circle (○) |
| Top | Triangle (△) |
| Left | Square (□) |

| Control | PSP control |
| --- | --- |
| D-pad | D-pad |
| Left stick | Analog stick |
| `L1` / `R1` | `L` / `R` |
| `START`, `SELECT` | `START`, `SELECT` |

- In the app's menus, `×` confirms and `○` goes back.
- `MENU`, or `SELECT` + `START`, opens the [in-game menu](../in-game-menu.md).

## Settings

- PSP renders with OpenGL ES, or with Vulkan; see
  [Graphics API](index.md#graphics-api).
- Some options, such as the CPU core and the PSP model, only take effect when
  a game starts. They are in [Emulator Settings](../emulator-settings.md),
  not in the in-game **Core Options**.
- In-game saves go in `Saves/PSP/`, with your other
  [saves inside the app](../library.md#saves).

??? info "More detail"
    - The software renderer is not offered.
    - In-game saves are in the PSP's own `SAVEDATA` folder, under
      `Saves/PSP/`.
