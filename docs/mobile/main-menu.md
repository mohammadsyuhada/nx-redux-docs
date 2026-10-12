# Main Menu & Home

The main menu is split into four tabs: **Home**, **Consoles**,
**Collections** and **Tools**. The app opens on Home, or on the first tab you
have not hidden.

![Home tab](../assets/screenshots/mobile/home.webp)

Consoles, Collections, Tools and the game lists can each be drawn as a list,
a grid or a carousel, and game lists have a fourth style, Backdrop.
[Menu Layouts](layouts.md) shows them all.

You can drive every screen with the on-screen pad, a controller or touch.
See [Controls](controls.md).

## Tabs

| Tab | What it holds |
| --- | --- |
| **Home** | Your last game, play stats, and the games and tools you pinned |
| **Consoles** | One entry per system that has games in it |
| **Collections** | Your [collections](#collections) |
| **Tools** | The built-in tools, Settings included |

- **Switch tabs** with `L1` / `R1`, or tap a tab. The tab order wraps around.
- `Left` / `Right` also switch tabs:
    - in List style and in a Vertical Carousel, always;
    - in Grid and a Horizontal Carousel, when you push past the first or last
      item;
    - on Home, when you push past the left or right edge.
- A Consoles or Collections tab with nothing in it, such as Collections before
  you make one, is left out.
- You can hide any tab in [Layouts](layouts.md#showing-and-hiding-tabs).
  `MENU` on any item, or touching and holding the tab row, still opens a
  hidden tab, so Settings is always reachable. If a tab you are on goes away,
  the menu moves to the next tab.

### The tab row

Press `Up` from the top of Home, from the top row of a Grid or from a
Horizontal Carousel to move the highlight onto the tab row. In List style and
a Vertical Carousel, `Up` on the first item wraps to the last instead. With
**Page title** hidden in [Layouts](layouts.md#page-title-and-button-hints)
there is no tab row, and `L1` / `R1` switch tabs. With only one tab left, an
**NX Redux** title stands in its place, and `Up` does not move onto it. The
same goes for a tab opened over another.

| Button | What it does |
| --- | --- |
| `Left` / `Right`, `L1` / `R1` | Switch tabs |
| `Down`, `A` or `B` | Go back into the content |
| `Up` | Jump to the bottom of the content |
| `SELECT` **Recent** | Open the [Game Switcher](game-switcher.md) |
| `START` **Search** | [Search](#search) your games |

## Home

Home is the starting point: your most recent game, this month's play time,
and everything you pinned. It comes in three layouts, **List**, **Grid** (the
default) and **Carousel**. Pick one in
[Settings → Layouts → Home layout](layouts.md#the-layouts-page). With
[Extra info](layouts.md#extra-info) hidden, every layout leaves out the stats.

In every layout the buttons are the same:

| Button | What it does |
| --- | --- |
| `A` **Play** / **Resume** / **Open** | Start the game (**Resume** continues from its auto-save, **Play** shows when it has none), or open the tool |
| `Y` **Netplay** | Play the selected game with another device. Shown for games that have [netplay](netplay.md) |
| `MENU` **Options** | The context menu for the selected game or tool. There is none on **Pick a game**, unless a tab is hidden and the menu offers it |
| `SELECT` **Recent** | Open the [Game Switcher](game-switcher.md) |
| `START` **Search** | [Search](#search) your games |

Touch works the same everywhere: tap an item to select it, tap the selected
item to play or open it, and long-press for the menu.

Games without art get a generated abstract picture, so every card looks
different.

### List

Everything on Home in one list.

- **Stats** sit on two lines under the tabs, left-aligned: **This month** and
  the achievements you unlocked, then **Most played**. A month without play
  shows **Nothing played yet. Let's go!** instead.
- **The list** starts with your most recent game, marked with a **Continue**
  tag and selected when Home opens. On a fresh install it is **Pick a game**
  instead. Your pinned games follow in the order you pinned them, then the
  games from the shelves (**New**, **Not started**, **Pick up again**), each
  wearing its shelf name as a pill tag, like the Continue game's tag, and
  last every pinned tool. Each shelf holds at most 3 games. The shelves show
  in List on any screen size.
- **Behind the list** you see the selected game's picture (for the Continue
  game, where you left off). A selected tool shows its icon, large and dim, on
  the right.
- **The scroll arrows** sit on the picture just above the button hints, with no
  shade behind them.
- **Game info** (when you last played, play time) shows only while
  [Button hints](layouts.md#page-title-and-button-hints) are hidden and
  [Extra info](layouts.md#extra-info) is on, in the row where the hints were.
- **On a fresh install**, with only **Pick a game** in the list, its card
  fills the screen.

| Button | What it does |
| --- | --- |
| `Up` / `Down` | Move through the list. It wraps around at either end; a held button stops at the end |
| `Left` / `Right` | Switch tab |

### Grid

This is the default layout.

![Home with a pinned game selected](../assets/screenshots/mobile/home-pins.webp)

- **Stats strip.** The top line shows **This month**'s total play time and
  the RetroAchievements you unlocked this month. It reads **Sign in** while
  you are signed out of [RetroAchievements](retroachievements.md). The second
  line shows the month's **Most played** game and its time. A month without
  play shows **No play yet**. "This month" is the calendar month.
  [Extra info](layouts.md#extra-info) can hide it.
- **Continue card.** Your most recent game, wearing a **Continue** badge, with
  when you last played it and for how long. Press `A` to jump back in.
- **Pick a game.** On a fresh install the Continue card is replaced by
  **Pick a game** ("Nothing played yet"), which opens the Consoles tab. While
  the Consoles tab is hidden, it opens it over Home, and a long press opens
  the hidden-tab menu.
- **Pinned tools** sit beside the Continue card as square icon tiles. When
  more tools are pinned than fit, the last square becomes **+N**, which opens
  the Tools tab. While Tools is hidden, it opens over Home, and a long press
  opens the hidden-tab menu.
- **Pinned games** fill the rows below. Home scrolls when there are more. The
  selected pin shows its name and play time.
- Games without art get a generated abstract picture, so every card looks
  different.

| Button | What it does |
| --- | --- |
| D-pad | Move between the cards |
| `MENU` **Options** | **Pin** or **Unpin** the selected game or tool |
| `SELECT` **Recent** | Open the [Game Switcher](game-switcher.md) |
| `START` **Search** | [Search](#search) your games |
| `Y` **Netplay** | Play the selected game with another device. Shown for games that have [netplay](netplay.md) |
| `A` **Resume** / **Play** | Start the selected game. **Resume** continues from its auto-save; **Play** shows when it has none |
| `A` on a pinned tool | Open the tool. The hint names the tool, e.g. **Game Tracker** |
| `A` **More tools** | On **+N**: open the Tools tab |

??? info "Touch on Home"
    - Tap a card to select it, then tap it again to play or open it. This
      goes for the Continue card, pinned games and pinned tools.
    - A long press opens the same menu as `MENU`.
    - Drag up and down to scroll without selecting anything. Let go mid-drag
      and the page glides on.

Under the pinned games, Home shows shelves of games to pick from, on every
screen size, portrait and landscape alike: **New**, **Not started** and
**Pick up again**, at most 3 games each, under a label like the **Pinned**
one. Their cards are the pinned games' size, in the same grid: two to a row
in portrait, four on a tablet. See [Shelves](foldables.md#shelves).

### Carousel

The same games in one row of cards, centred on the screen.

- **Stats** sit on two centred lines under the tabs: **This month** above,
  **Most played** below. A month without play shows **Nothing played yet.
  Let's go!** instead.
- **The carousel** starts on the **Continue** card (with a **Continue** badge),
  selected when Home opens, or **Pick a game** on a fresh install. Your pinned
  games follow, then the games from the shelves in the order **New**, **Not
  started**, **Pick up again**, each badged with its shelf name. Each shelf holds at most 3 games. The
  shelves show in Carousel on any screen size.
- **Game info** shows inside the selected card, at the bottom over a dark
  fade like the Grid's Continue card: its name, when you last played it, play
  time and achievements. The cards beside it show their picture only.
- **Pinned tools** sit in a row of squares under the carousel, the same size
  as the Grid's tool squares on that screen. When they don't all fit, the last
  square is **+N**, which opens the Tools tab.
- **Swipe** the carousel to scroll it.

| Button | What it does |
| --- | --- |
| `Left` / `Right` | Move along the carousel or the tools row. Past either end, switch tab |
| `Down` | From the carousel, go to the tools row (the square you last used) |
| `Up` | From the tools row, back to the carousel. From the carousel, the tab row |

## Pinning games and tools

- **Pin a game:** press `MENU` on it in a game list and choose **Pin Item**.
  **Unpin Item** removes it again. On Home, `MENU` on the Continue card offers
  **Pin**, and on a pinned game **Unpin**.
- **Pin a tool:** press `MENU` on it in the Tools tab and choose **Pin**.
  **Unpin** removes it.
- You can pin up to **12** games. At the limit the app says
  "Pins are full (12). Unpin one first."

## Consoles, Collections and Tools

These three tabs list their entries in the style chosen in
[Layouts](layouts.md). By default Consoles and Collections are a carousel,
and Tools is a grid.

![Consoles tab](../assets/screenshots/mobile/tab-consoles.webp)

- **Consoles** show their logo and how many games they hold. In the Carousel
  style the selected console's controller shows too. In the List style it
  does as well, unless you set **Consoles controller** to **Background** or
  **None** in [Layouts](layouts.md#consoles-controller).
- **Collections** show their name and game count.

![Collections tab](../assets/screenshots/mobile/tab-collections.webp)

- **Tools** show an icon for each tool: **RetroAchievements**,
  **Game Tracker**, **Artwork**, **Cheat Database** and **Settings**, plus any
  Android apps you choose to show there (see
  [Launcher Mode & Android Games](launcher.md)).

![Tools tab](../assets/screenshots/mobile/tab-tools.webp)

| Button | What it does |
| --- | --- |
| `MENU` **Options** | **Rename** / **Delete** on a collection, **Pin** / **Unpin** on a tool |
| `SELECT` **Recent** | Open the [Game Switcher](game-switcher.md) |
| `START` **Search** | [Search](#search) your games |
| `A` **Open** | Open the console, collection or tool |

![Tool menu with Unpin](../assets/screenshots/mobile/tool-menu.webp)

The tools have their own pages: [RetroAchievements](retroachievements.md),
[Game Tracker](game-tracker.md), [Artwork](artwork.md),
[Cheat Database](cheats.md) and [Settings](settings.md).

## Game lists

Opening a console or a collection shows its games. The page title names the
console or collection, e.g. **Sega Genesis**.

![Game list in the default Carousel style](../assets/screenshots/mobile/game-list.webp)

Under the selected game you see when you last played it and your total play
time ("Today - 11m 0s"). For games with achievements, the line adds your
progress and the next achievement to go for. Game names leave out the region
and version text in brackets.

| Button | What it does |
| --- | --- |
| `MENU` **Options** | Open the game's context menu |
| `SELECT` | Open the [Game Switcher](game-switcher.md) |
| `Y` **Netplay** | Play the game with another device. Shown for games that have [netplay](netplay.md) |
| `X` **Resume** | Jump straight back into your auto-saved session (shown when the game has one) |
| `B` **Back** | Return to the tab |
| `A` **Open** | Launch the game |

A long press on a game opens the context menu too.

## Context menus

Press `MENU` on a game to see what you can do with it. The menu depends on
where the game is listed.

![Game context menu](../assets/screenshots/mobile/context-menu.webp)

| Item | What it does |
| --- | --- |
| **Pin Item** / **Unpin Item** | Pin the game to Home, or take it off |
| **Hide Game** | Hide the game from its list |
| **Rename Rom** | Change the name the list shows |
| **Add to Collection** | Add the game to a collection, or start a new one |
| **Game Settings** | This game's own emulator settings. See [Emulator Settings](emulator-settings.md) |
| **Resume** | Jump back into the game's auto-save. Shown only while Button hints are hidden |
| **Netplay** | Play the game with another device. See [Netplay](netplay.md) |
| **Fetch art** | Download art for this game. See [Artwork](artwork.md) |
| **Emulator** | Pick which emulator runs this game. See [Emulators](emulators/index.md) |
| **Remove from Collection** | Take the game out of the collection you are in |

Not every item shows everywhere:

| List | Items |
| --- | --- |
| A console | **Pin Item**, **Hide Game**, **Rename Rom**, **Add to Collection**, **Game Settings**, **Netplay**, **Fetch art**, and **Emulator** on systems with more than one emulator |
| A collection | The same, with **Remove from Collection** at the end |
| [Search](#search) results | The same as a console, without **Emulator** |
| Unassigned games | **Hide Game**, **Rename Rom**, **Console** |
| The Android console | **Pin Item** / **Unpin Item** only |

- **Fetch art** shows only for systems the art sources know, and only when
  the game's art is incomplete, or when **Artwork → Replace existing art** is
  on.
- While [Button hints](layouts.md#page-title-and-button-hints) are hidden
  (with a controller connected or the portrait pad shown), the `X` Resume and
  `Y` Netplay hints are not on screen, so a game's menu starts with
  **Resume** (when the game has a save) and **Netplay** (when available).
  On Home it starts with **Netplay** only.
- A menu with 9 to 16 items shows as two columns when the screen is wide
  enough. `Left` / `Right` move between the columns.
- **Netplay** shows only for systems that have [netplay](netplay.md).
- **Unassigned games** are files in an extra ROM folder that the app could
  not match to a system. Open
  them from **Tools → Settings → Library → Unassigned games**, and use
  **Console** to say which system a game belongs to. See
  [Library & ROM folders](library.md).
- **Hidden games** are listed in **Tools → Settings → Library → Hidden games**.
  Press `A` **Unhide** there to bring one back.
- The Android console holds the Android games you added. See
  [Launcher Mode & Android Games](launcher.md).

### Hidden tabs

When you hide a tab in [Layouts](layouts.md#showing-and-hiding-tabs), `MENU`
on any item of the main menu ends with **Consoles**, **Collections** and
**Tools** for each hidden tab that has something in it. Items that have no
menu of their own, such as a console, get a menu with just these, captioned
**NX Redux**. Pick one to open that tab over the current one; `B` returns.

## Search

Press `START` on the main menu to search your games. It works from any tab,
and from the tab row. The hint reads **Search** once you have games.

1. The **Search** prompt opens, with your last search filled in.
2. Type part of a name and press `A` or the keyboard's **Done**.
3. The matches open as a game list titled **Search:** and your words, such
   as **Search: mario kart**.

![The Search prompt over the Consoles tab, with “super mario” typed and the keyboard up](../assets/screenshots/mobile/search-prompt.webp)

`B` or `START` closes the prompt without searching.

The results list games from every console, in your game list style, each
with its console's tag, such as `GBA`. It reads **No results** when nothing
matches.

![Search: super mario, showing Super Mario 64 with its play time and achievements, and the X Resume hint](../assets/screenshots/mobile/search-results.webp)

| Button | What it does |
| --- | --- |
| `MENU` **Options** | The game's context menu |
| `Y` **Netplay** | Play the game with another device, for games that have [netplay](netplay.md) |
| `X` **Resume** | Jump back into the game's auto-saved session (shown when it has one) |
| `B` **Back** | Return to the tab and the item you searched from |
| `A` **Open** | Launch the game |

### How matching works

The search looks in each game's name, its file name and its console tag.

- **Case, accents and punctuation don't matter.** `pokemon` finds
  *Pokémon*, and `pac man` finds *Pac-Man*.
- **Words can come in any order**, and each can be part of a word.
  `kart mario` finds *Mario Kart: Super Circuit*.
- **Roman numerals and digits match.** `final fantasy 6` finds *Final
  Fantasy VI*, and `vi` still finds *Virtua Fighter*.
- **Words can be glued together.** `pacman` finds *Pac-Man*.
- **No typos.** Each word you type has to be there.

Names that start with your search come first, then names where every word
starts a word, then the rest. Each group is A to Z.

Unassigned games, games without an emulator and Android games are not
searched.

## Collections

Build your own game collections from a game list:

1. Press `MENU` on a game.
2. Choose **Add to Collection**.
3. Pick an existing collection, or **New Collection…** to make one and name
   it.

Your collections live on the **Collections** tab, each with its game count.
The tab appears once you have a collection. Collections are saved in the
`Collections/` folder in your home folder.

Press `MENU` on a collection, or long-press it, to **Rename** or **Delete**
it. Delete asks first, and removes only the list: the games stay in your
library.
