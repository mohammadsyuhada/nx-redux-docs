# Game Context Menu

Press `MENU` on a highlighted game in any game list to open its context menu.

![Game context menu](../../assets/screenshots/context-menu.png)

Depending on the game, the menu offers:

| Option | What it does |
| --- | --- |
| **Pin Item / Unpin** | Pin the game to the main menu for one-press access |
| **Delete Rom** | Remove the game (with a confirmation dialog) |
| **Rename Rom** | Change a game's display name. The [keyboard](keyboard.md#editing-an-existing-name) opens with the current name to edit. The file itself is never touched. |
| **Add to Collection** | Add the game to an existing collection or create a new one on the spot |
| **Remove from Recently Played** | Clear the game from your recent list |
| **Emulator Options** | Edit [per-game emulator options](emulator-options.md), overriding the system-wide defaults |
| **Fetch Box Art** | Download box art for this game in the background (shown when the game has none yet) |
| **Refresh Roms** | Rescan the ROMs list |

!!! tip "Bulk box art"
    To fetch artwork for many games at once, use the
    [Artwork Manager](../apps/artwork-manager.md) instead of fetching one
    game at a time.

??? info "More detail"
    **Rename Rom** stores the new name as a
    [`map.txt` alias](main-menu.md#custom-display-names-maptxt). Box art,
    saves and save states stay matched, and arcade zips keep loading.
