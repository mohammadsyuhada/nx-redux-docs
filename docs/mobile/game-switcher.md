# Game Switcher

Press `SELECT` on the main menu or in a game list to open the Game Switcher:
your recent games, ready to resume any of them where you left off. On the
main menu the `SELECT` hint reads **Recent**.

It has two layouts, picked in
[**Tools → Settings → Layouts → Game Switcher layout**](layouts.md#game-switcher-layout):
**Full screen** (the default) and **List**.

## Full screen

![The Game Switcher showing Streets of Rage 2, 1 of 23](../assets/screenshots/mobile/game-switcher.webp)

Each game fills the screen with its picture. On top are its name, its console
and its place in the list, such as **1 / 23**. Above the hints is the game's
info line: when you last played it and for how long, its achievements and the
next one to unlock.

- `LEFT` / `RIGHT`, or a swipe left or right, move between games.
- `A` **Resume**, or a tap on the picture, continues the game where you left
  off.
- `Y` **Remove** asks **Remove "‹name›" from recents?** Choose **Remove** to
  take the game out of your recent games.
- `B` **Back**, or `SELECT` again, returns to where you were.

`LEFT` and `RIGHT` stop at the first and last game; they do not wrap.

## List

Your recent games as a list titled **Recent**, drawn like a game list in the
[List](layouts.md#list) style. The selected game's picture fills the
background behind the rows, and the line at the bottom gives its info, as in a
List game list.

- `UP` / `DOWN` move through the games. `UP` on the first wraps to the last
  and `DOWN` on the last to the first, on a fresh press only: holding the
  button stops at the end.
- A tap on a row highlights it, and a second tap resumes it.
- `A` **Resume**, `Y` **Remove** and `B` **Back** work as in Full screen.
  `LEFT` and `RIGHT` do nothing.

Two games with the same name from different consoles show the console's
tag, such as **Tetris (GB)**, or their whole file names when those differ only
by extension, such as **Tetris.nes (FC)**. A copy of a game kept in an extra
folder shows that folder's name after the title, dimmed.

The background is the first of these that loads:

1. the screenshot of the game's resume point, with any black bars trimmed off,
2. its screenshot,
3. its hero image, then its grid image,
4. its generated abstract picture.

With no recent games, the List shows the same **No Recents** screen as Full
screen.

## The picture

In Full screen the switcher shows the first of these it has for the game:

1. the screenshot of its resume point,
2. its 3D box art,
3. its 2D cover, or else its SteamGridDB grid image, shown in a case,
4. **No Preview**.

See [Artwork](artwork.md) for where box art comes from.

## Play time and achievements

Both layouts follow [**Extra info**](layouts.md#extra-info) and
[**Button hints**](layouts.md#page-title-and-button-hints) in
**Tools → Settings → Layouts**:

- With **Extra info** hidden, the info line is left out.
- With **Button hints** hidden, the hint bar's row stays, without hints, and
  the info line moves into it. In Full screen the row keeps its dark shade so
  the line reads over a light picture.

## Always resumable

Quitting a game from the [in-game menu](in-game-menu.md) saves a hidden resume
state, and so does leaving the app while a game is open. So with nearly every
core, every game you have played can be resumed. No manual save state is
needed. PICO-8 is the exception for now (see
[Emulators](emulators/index.md#limits)).

## Only resumable games are listed

The switcher lists only recent games that can be resumed. With none, it shows
**No Recents** and **Play a game to see it here**. Unlike the handheld, there
is no setting to list every recent game instead. Android games are never
listed.

In a game list, `X` **Resume** does the same for the highlighted game when it
can be resumed.
