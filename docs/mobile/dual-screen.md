# Dual Screens & External Displays

On a handheld with a second screen, NX Redux uses both. Nintendo DS and 3DS
games get one screen each, like the real console. Other games show the game
on one screen and a [game panel](#the-game-panel) on the other, with your play
time, achievements and a few shortcuts.

<!-- screenshot: a dual-screen handheld running a DS game, the DS top screen on the upper screen and the bottom screen on the lower one, with the SWAP and Panel pills -->

Two kinds of second screen count:

- **A built-in second screen**, as on dual-screen Android handhelds.
- **A wired display on USB-C**, such as a clip-on screen add-on, a monitor
  or a TV.

Casting and wireless displays, and a foldable's cover screen, are never used.
On a phone with one screen, nothing on this page applies, and the game panel
shows in the [in-game menu](in-game-menu.md#the-game-panel) instead.

??? info "More detail"
    - Plug a display in or unplug it during a game and the game carries on: the
      layout switches straight away.
    - The app's own pages, such as Home, Settings and the in-game menu, stay on
      the phone's main screen. The second screen only ever shows part of a
      running game.
    - Android doesn't tell an add-on screen from a monitor or a TV, so a
      wired monitor counts as a second screen too.

## Which screen is which

One screen is the **picture screen** and the other the **touch screen**:

- The **picture screen** shows the game, or the DS or 3DS top screen.
- The **touch screen** shows the DS or 3DS bottom screen, or the game panel.

By default the wider screen is the picture screen. When both have the same
shape, the second screen gets the picture. To choose yourself, set
[**Bottom screen**](#settings) to the screen you want to touch.

While the second screen is in use, the game stays in landscape, either way
up. Unplug the display, or turn the second screen off, and the game gets its
usual orientation back.

??? info "More detail"
    - Games drawn on their side, such as vertical arcade games, always keep
      the picture on the main screen, whatever **Bottom screen** says.
    - While the main screen shows the game panel, the on-screen pad is hidden:
      it would cover the panel. Dual-screen handhelds have their own buttons.

## First-run setup

On a handheld with a built-in second screen, setup asks **Which is the bottom
screen?** right after the text size. Both screens show a **This is the bottom
screen** button: tap the one on the screen below. **Skip** leaves it on
**Auto**.

A wired display never gets this question. Change the answer any time in
[Settings](#settings).

<!-- screenshot: setup's "Which is the bottom screen?" page on the main screen, with the second screen's big "This is the bottom screen" button -->

## Settings

**Tools → Settings → Emulators → Second screen** has the system-wide
settings. The **Second screen** row shows only while a second screen is
connected.

| Row | Values | Default | What it does |
| --- | --- | --- | --- |
| **Enable** | On, Off | On | **Off** leaves the second screen alone, free for another app. |
| **Bottom screen** | Auto, Main screen, Second screen | Auto | Which screen is the touch screen. **Auto** picks by shape. |

With **Enable** off, DS and 3DS games use their usual
[single-screen layouts](emulators/nintendo-ds.md#screen-layouts) and other
games show no panel. The game panel's **Second screen** shortcut changes the
same setting without leaving the game.

### For one console

Each console has its own **Bottom screen** row in its Console Settings:
**System default**, **Main screen** or **Second screen**. **System default**
follows the setting above. Set it in [Emulator Settings](emulator-settings.md),
or during a game in **Options → Console Settings**, where it applies straight
away.

??? info "More detail"
    - The console's **Bottom screen** row shows only while a second screen is
      connected, like the system-wide rows. Values you set are kept while it's
      hidden.
    - Keep an in-game change with
      [Save Changes](in-game-menu.md#save-changes), for the game or the
      console.

## Nintendo DS and 3DS

With a second screen, a DS or 3DS game starts split across both screens: the
top screen on the picture screen and the bottom screen on the touch screen.

- **Touch** goes to the bottom screen, on whichever screen it shows.
  Touching the top screen does nothing.
- **SWAP**, `R2` on the DS or `SELECT` + `R1` on the 3DS swaps the two
  screens over.
- In [stylus mode](emulators/nintendo-ds.md#stylus-mode) the DS stylus dot
  follows the bottom screen to whichever screen shows it.

### The Panel and Game pills

A **Panel** pill sits at the bottom right of the touch screen. Tap it and the
touch screen shows the [game panel](#the-game-panel), while both DS or 3DS
screens move side by side onto the picture screen. Touch reaches the bottom
screen there.

On the panel, the **Game** pill, in the same corner, brings the bottom screen
back to the touch screen.

<!-- screenshot: a DS game with the panel up: both DS screens side by side on the picture screen, the game panel with the Game pill on the touch screen -->

??? info "More detail"
    - On the DS, **SWAP** while split changes the **Big Screen** setting, the
      same as on one screen, so it carries over when you play without the
      second screen. On the 3DS the swap lasts for this session.
    - The screen layout settings, such as **Layout (landscape)**, aren't used
      while the game is split or the panel is up.

## Other games

Every other game shows its picture on the picture screen and the game panel
on the touch screen while you play. The panel works by touch only: your
buttons keep playing the game.

Opening the [in-game menu](in-game-menu.md) pauses the game and adds the menu
list to the left of the panel. Closing it takes the list away again.

<!-- screenshot: a regular game on a dual-screen handheld: the game on the picture screen, the game panel's Shortcuts tab on the touch screen -->

## The game panel

The same panel shows on the touch screen and, on a phone with one screen,
on the right of the [in-game menu](in-game-menu.md#the-game-panel).

<!-- screenshot: the game panel on its own: header with box art, title, Total play time, Achievements count, clock and battery; the Shortcuts tab -->

Across the top, the game's header shows:

- its box art, or the console's logo when it has none;
- its name;
- its total play time, such as **Total 4h 12m**;
- with a [RetroAchievements](retroachievements.md) set, your count, such as
  **Achievements 3 / 40**;
- the time and the battery level, since the game hides Android's status bar.

Below it are up to three tabs. A tab shows only when it applies.

| Tab | Shows when | What it holds |
| --- | --- | --- |
| **Shortcuts** | Always | One-tap buttons. See [below](#shortcuts). |
| **Achievements** | The game has a RetroAchievements set | The game's achievements, in your **Achievement sort order**. |
| **Players** | The game has more than one player | Which controller is which player. See [Local Multiplayer](multiplayer.md#the-players-page). |

??? info "More detail"
    - The play time is the total before this launch. It doesn't count up while
      you play.
    - The clock follows the phone's 12 or 24-hour setting.

### Shortcuts

| Shortcut | Shows when | What it does |
| --- | --- | --- |
| **Swap disc** | A game with more than one disc | Puts the next disc in, such as **Disc 2 of 3**. The button shows the disc in use, such as `1/2`. |
| **Second screen** | A second screen is connected | Turns the second screen on or off. Filled while on. |
| **Fast forward**, **Rewind**, **Screenshot**, **Reset** | Always | Shown dimmed: not available yet. |

??? info "More detail"
    - **Swap disc** works as the in-game menu's **Disc** row does, while the
      game keeps running.
    - **Second screen** changes **Settings → Emulators → Second screen →
      Enable**.
    - In a [netplay](netplay.md) match, **Swap disc** is hidden.

### Achievements

Each row shows the achievement's badge, its name with its points in a small
pill, and its description. The badge says where you are: in colour once
unlocked, greyed while locked. Rows open nothing.

<!-- screenshot: the game panel's Achievements tab: coloured and greyed badges, names with points pills, descriptions -->

### Players

The **Player 1** to **Player 4** rows show each player's controller, **Empty**
or the name with **(disconnected)**. Tap a row to step it to the next
controller, or **Empty**. It works as the
[Players page](multiplayer.md#the-players-page).

## Limits

- The panel can't be driven with buttons on the touch screen. In the in-game
  menu on one screen it can: see [The game panel](in-game-menu.md#the-game-panel).
- Achievements in the panel have no details page for now.
