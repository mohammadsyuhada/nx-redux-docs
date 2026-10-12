# Game Switcher

Tap `SELECT` anywhere in the menus to open the Game Switcher — your recent
games, ready to resume any of them instantly. It has two layouts, picked in
[**Settings → Layouts → Game Switcher layout**](../settings/layouts.md#game-switcher-layout):
`Full screen` (the default) and `List`.

## Full screen

![Game Switcher, Full screen](../../assets/screenshots/game-switcher.png)

One game at a time, its resume frame filling the screen. The top shows the
game's name and, under it, its system and its place in the list
("Game Boy Advance 1 / 12"). The line at the bottom shows when you last played
it, your total play time and your achievement progress. With nothing played
yet, the switcher says **Nothing played yet**.

| Button | What it does |
| --- | --- |
| `Left` / `Right` | Flip through games |
| `A` **Resume** | Continue exactly where you left off |
| `Y` **Remove** | Take the game out of the switcher |
| `B` **Back** | Return to the menu |

## List

![Game Switcher, List](../../assets/screenshots/game-switcher-list.png)

Your recent games as a list titled **Recent**, drawn like a game list in the
List style: the selected game's resume frame sits behind the rows, faded in
from the right. Two games with the same name from different systems show the
system's tag after the name, dimmed ("Tetris (GB)").

| Button | What it does |
| --- | --- |
| `Up` / `Down` | Move through games |
| `A` **Resume** | Continue exactly where you left off |
| `Y` **Remove** | Take the game out of the switcher |
| `B` **Back** | Return to the menu |

## Play time and achievements

Both layouts follow [**Extra info**](../settings/layouts.md#extra-info) and
[**Button hints**](../settings/layouts.md#button-hints) in
**Settings → Layouts**:

- Extra info hidden: no play time or achievement line.
- Button hints hidden: the hint bar's row stays, without hints, and the play
  time and achievement line moves into it. In the List layout the line shows
  only then, as in a List game list.

## Always resumable

Quitting a game auto-saves to a hidden save slot. The Game Switcher always
resumes exactly where you left off, with no manual save states needed. This
works on the built-in cores, Dreamcast and Nintendo 64 included.

Games without a save state show their box art instead, so the switcher stays
visual even for freshly added titles.

## Resumable-only by default

By default the switcher lists **only resumable games**. To see all recent
games, set [**Game Switcher games**](../settings/layouts.md#game-switcher-games)
in **Settings → Layouts** to `All recent games`.
