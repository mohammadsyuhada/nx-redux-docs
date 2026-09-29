# Game Switcher

Press `SELECT` on the main menu or in a game list to open the Game Switcher:
a full-screen view of your recent games that resumes any of them where you
left off.

<!-- SCREENSHOT: game-switcher — Game Switcher showing a recent game's resume screenshot -->

Each game fills the screen with the screenshot of its resume point, or its
box art when there is no screenshot, with its name on top.

- `LEFT` / `RIGHT`, or a swipe left or right, move between games.
- `A` **Resume**, or a tap on the picture, continues the game where you left
  off.
- `Y` **Remove** asks to confirm, then takes the game out of your recent
  games. It is also gone from **Recently Played**.
- `B` **Back**, or `SELECT` again, returns to where you were.

## Always resumable

Quitting a game from the [in-game menu](in-game-menu.md) saves a hidden resume
state, and so does leaving the app while a game is open. So with nearly every
core, every game you have played can be resumed. No manual save state is
needed. PICO-8 is the exception for now (see
[Emulators](emulators.md#not-available-yet)).

## Only resumable games are listed

The switcher lists only recent games that can be resumed. With none, it shows
**No Recents** and **Play a game to see it here**. Unlike the handheld, there
is no setting to list every recent game instead.

In a game list, `X` **Resume** does the same for the highlighted game when it
can be resumed.
