# Main Menu & Home

The main menu is split into four tabs: **Home**, **Consoles**,
**Collections** and **Tools**. The app opens on Home, or on the first tab you
have not hidden.

![Home in Grid, with Dragon Ball Z - The Legacy of Goku II on the Continue card under the This month and Most played strip](../assets/screenshots/mobile/home.webp)

Each tab and the game lists can be drawn in different styles (list, grid,
carousel and more). [Menu Layouts](layouts.md) shows them all.

You can drive every screen with the on-screen pad, a controller or touch.
See [Controls](controls.md).

??? info "More detail"
    - Consoles, Collections, Tools and the game lists can each be a list, a
      grid or a carousel, and game lists have a fourth style, Backdrop.
    - With touch only (no controller, and no pad on screen) there is no hint
      bar: tap the items, and use the icons at the top right.

## Tabs

| Tab | What it holds |
| --- | --- |
| **Home** | Your last game, play stats, and the games and tools you pinned |
| **Consoles** | One entry per system that has games in it |
| **Collections** | Your [collections](#collections) |
| **Tools** | The built-in tools, Settings included |

- **Switch tabs** with `L1` / `R1`, or tap a tab. `Left` / `Right` switch
  tabs too.
- An empty tab, such as Collections before you make one, is left out.
- You can hide any tab in [Layouts](layouts.md#showing-and-hiding-tabs).
  `MENU` on any item still opens a hidden tab, so Settings is always
  reachable.

??? info "More detail"
    - The tab order wraps around.
    - `Left` / `Right` switch tabs:
        - in List style and in a Vertical Carousel, always;
        - in Grid and a Horizontal Carousel, when you push past the first or
          last item;
        - on Home, when you push past the left or right edge.
    - Touching and holding the tab row also opens a hidden tab. If a tab you
      are on goes away, the menu moves to the next tab.

### The tab row

Press `Up` from the top of the content to move onto the tab row.

| Button | What it does |
| --- | --- |
| `Left` / `Right`, `L1` / `R1` | Switch tabs |
| `Down`, `A` or `B` | Go back into the content |
| `Up` | Jump to the bottom of the content |
| `SELECT` **Recent** | Open the [Game Switcher](game-switcher.md) |
| `START` **Search** | [Search](#search) your games |

??? info "More detail"
    - `Up` reaches the tab row from the top of Home, the top row of a Grid or
      a Horizontal Carousel. In List style and a Vertical Carousel, `Up` on
      the first item wraps to the last instead.
    - With **Page title** hidden in
      [Layouts](layouts.md#page-title-and-button-hints) there is no tab row,
      and `L1` / `R1` switch tabs.
    - With only one tab left, an **NX Redux** title stands in its place, and
      `Up` does not move onto it. The same goes for a tab opened over another.
    - When the hint bar doesn't show **Recent** or **Search** (touch only,
      Button hints hidden, or their own hint hidden in
      [Layouts](layouts.md#page-title-and-button-hints)), they are icons at
      the right of the tab row instead.

## Home

Home is the starting point: your most recent game, this month's play time,
and everything you pinned. It comes in three layouts, **List**, **Grid** (the
default) and **Carousel**. Pick one in
[Settings → Layouts → Home → Home layout](layouts.md#the-layouts-page).

Every layout starts with a two-line stats strip:

- **This month:** your play time this calendar month, and the
  [RetroAchievements](retroachievements.md) you unlocked (while signed in).
- **Most played:** the month's most played game and its time.

In every layout the buttons are the same:

| Button | What it does |
| --- | --- |
| `A` **Play** / **Resume** / **Open** | Start the game, or open the tool. **Resume** continues from its auto-save |
| `Y` **Netplay** | Play the selected game with another device. Shown for games that have [netplay](netplay.md) |
| `MENU` **Options** | **Pin** / **Unpin**, and **Play from start** when the game has an auto-save |
| `SELECT` **Recent** | Open the [Game Switcher](game-switcher.md) |
| `START` **Search** | [Search](#search) your games |

With touch, tap an item to select it, tap it again to play or open it, and
long-press for the menu.

??? info "More detail"
    - A month without play shows **No play yet** on the first line, and no
      second line.
    - [Home stats](layouts.md#home-stats) in Layouts → Home hides the strip.
      [Extra info](layouts.md#extra-info) hides the play time and
      achievements on the cards. With **Page title** hidden, the strip moves
      up into the tab row's place.
    - `A` shows **Play** when the game has no auto-save.
    - **Play from start** leads the `MENU` list. There is no menu on **Pick a
      game**, unless a tab is hidden and the menu offers it.
    - Games without art get a generated abstract picture, so every card looks
      different.

### List

Everything on Home in one list, with the selected game's picture behind it.

![Home in List: Continue first, then the pinned games as rows over the selected game's picture](../assets/screenshots/mobile/home-layout-list.webp)

- **The list** starts with your most recent game, tagged **Continue** (or
  **Pick a game** on a fresh install). Then come your pinned games, games
  from the [shelves](foldables.md#shelves), and your pinned tools.
- **Game info** (when you last played, play time) shows only while
  [Button hints](layouts.md#page-title-and-button-hints) are hidden.

| Button | What it does |
| --- | --- |
| `Up` / `Down` | Move through the list. It wraps around at either end; a held button stops at the end |
| `Left` / `Right` | Switch tab |

??? info "More detail"
    - The stats sit on two lines under the tabs, left-aligned.
    - The Continue game is selected when Home opens. Pinned games follow in
      the order you pinned them, then the shelf games (**New**, **Not
      started**, **Pick up again**), each with its shelf name as a pill tag,
      then every pinned tool. Each shelf holds at most 3 games. The shelves
      show in List on any screen size.
    - Behind the Continue game you see where you left off. A selected tool
      shows its icon, large and dim, on the right.
    - The scroll arrows sit on the picture just above the button hints, with
      no shade behind them.
    - Game info also needs [Extra info](layouts.md#extra-info) on, and shows
      in the row where the hints were.
    - On a fresh install, with only **Pick a game** in the list, its card
      fills the screen.

### Grid

This is the default layout.

![Home in Grid: the Continue card filling the top, under the stats strip](../assets/screenshots/mobile/home-layout-grid.webp)

![Grid Home scrolled to the pinned games, with Mother 3 selected](../assets/screenshots/mobile/home-pins.webp)

- **Continue card.** Your most recent game, with when you last played it and
  for how long. Press `A` to jump back in. On a fresh install it reads
  **Pick a game** ("Nothing played yet") and opens the Consoles tab.
- **Pinned tools** sit beside it as square icon tiles. If they don't all
  fit, the last square is **+N**, which opens the Tools tab.
- **Pinned games** fill the rows below, each with its name and play time.
- **Shelves** of games to pick from come last: **New**, **Not started** and
  **Pick up again**. See [Shelves](foldables.md#shelves).

| Button | What it does |
| --- | --- |
| D-pad | Move between the cards |
| `MENU` **Options** | **Pin** or **Unpin** the selected game or tool (**Play from start** first on a game with an auto-save) |
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

??? info "More detail"
    - The stats strip sits on two lines under the tabs. The Continue card
      wears a **Continue** badge.
    - While the Consoles tab is hidden, **Pick a game** opens it over Home,
      and a long press opens the hidden-tab menu. **+N** works the same way
      while Tools is hidden.
    - Home scrolls when there are more pinned games than fit.
    - The shelves show on every screen size, portrait and landscape alike,
      at most 3 games each, each under its own label. Their cards are the
      pinned games' size, in the same grid: two to a row in portrait, four
      on a tablet. A **New** or **Not started** game shows its console under
      its name.

### Carousel

The same games in one row of cards, centred on the screen, with your pinned
tools in a row of squares underneath. Swipe the carousel to scroll it.

![Home in Carousel: the Continue card in the middle with its time and achievements, the next items beside it](../assets/screenshots/mobile/home-layout-carousel.webp)

- **The carousel** starts on the **Continue** card (or **Pick a game** on a
  fresh install), then your pinned games, then the shelf games.
- **Game info** (name, last played, play time, achievements) shows inside
  the selected card.

| Button | What it does |
| --- | --- |
| `Left` / `Right` | Move along the carousel or the tools row. Past either end, switch tab |
| `Down` | From the carousel, go to the tools row (the square you last used) |
| `Up` | From the tools row, back to the carousel. From the carousel, the tab row |

??? info "More detail"
    - The stats sit on two centred lines under the tabs.
    - The Continue card has a **Continue** badge and is selected when Home
      opens. Shelf games follow in the order **New**, **Not started**,
      **Pick up again**, each badged with its shelf name. Each shelf holds at
      most 3 games. The shelves show in Carousel on any screen size.
    - Game info sits at the bottom of the selected card over a dark fade,
      like the Grid's Continue card. The cards beside it show their picture
      only.
    - The tool squares are the size of the Grid's portrait tool squares, in
      landscape too. The strip, the carousel and the tools row sit centred
      on the screen as one group. When the tools don't all fit, the last
      square is **+N**, which opens the Tools tab.

## Pinning games and tools

- **Pin a game:** press `MENU` on it in a game list and choose **Pin Item**.
  **Unpin Item** removes it again. On Home, `MENU` on the Continue card or a
  shelf game offers **Pin**, and on a pinned game **Unpin**.
- **Pin a tool:** press `MENU` on it in the Tools tab and choose **Pin**.
  **Unpin** removes it.
- You can pin up to **12** games. At the limit the app says
  "Pins are full (12). Unpin one first."

## Consoles, Collections and Tools

These three tabs list their entries in the style chosen in
[Layouts](layouts.md). By default Consoles and Collections are a carousel,
and Tools is a grid.

![Consoles tab in Carousel, with Dreamcast (8 games) in the middle](../assets/screenshots/mobile/tab-consoles.webp)

- **Consoles** show their logo and how many games they hold.
- **Collections** show their name and game count.

![Collections tab in Carousel, with Pokemon World (9 games) in the middle](../assets/screenshots/mobile/tab-collections.webp)

- **Tools** show an icon for each tool: **RetroAchievements**,
  **Game Tracker**, **Artwork**, **Cheat Database**, **Device Sync** and
  **Settings**, plus any Android apps you choose to show there (see
  [Launcher Mode & Android Games](launcher.md)).

![Tools tab in Grid: RetroAchievements, Game Tracker, Artwork, Cheat Database, Device Sync and Settings](../assets/screenshots/mobile/tab-tools.webp)

| Button | What it does |
| --- | --- |
| `MENU` **Options** | **Rename** / **Delete** on a collection, **Pin** / **Unpin** on a tool |
| `SELECT` **Recent** | Open the [Game Switcher](game-switcher.md) |
| `START` **Search** | [Search](#search) your games |
| `A` **Open** | Open the console, collection or tool |

![The RetroAchievements tool's menu with Unpin, over the Tools tab](../assets/screenshots/mobile/tool-menu.webp)

The tools have their own pages: [RetroAchievements](retroachievements.md),
[Game Tracker](game-tracker.md), [Artwork](artwork.md),
[Cheat Database](cheats.md), [Device Sync](device-sync.md) and
[Settings](settings.md).

??? info "More detail"
    In the Carousel style the selected console's controller shows too. In the
    List style it does as well, unless you set **Consoles controller** to
    **Background** or **None** in [Layouts](layouts.md#consoles-controller).

## Game lists

Opening a console or a collection shows its games. The page title names the
console or collection, e.g. **Sega Genesis**.

![The Game Boy Advance list in the default Carousel style, with Advance Wars 2 - Black Hole Rising selected: 0 of 72, Next: Lucky Star](../assets/screenshots/mobile/game-list.webp)

The selected game shows when you last played it and your total play time
("Today - 11m 0s"), plus your achievement progress where it has any. Game
names leave out the region and version text in brackets.

| Button | What it does |
| --- | --- |
| `MENU` **Options** | Open the game's context menu |
| `SELECT` | Open the [Game Switcher](game-switcher.md) |
| `START` | [Search](#searching-a-game-list) this list |
| `X` **Achievements** | Open the [achievements panel](#achievements-panel) |
| `Y` **Netplay** | Play the game with another device. Shown for games that have [netplay](netplay.md) |
| `B` **Back** | Return to the tab |
| `A` **Resume** / **Open** | Launch the game. **Resume** continues from its auto-save; **Open** shows when it has none |

A long press on a game opens the context menu too. To start a game with an
auto-save from the beginning, choose **Play from start** in its menu.

??? info "More detail"
    - For games with achievements, the info line adds your progress and the
      next achievement to go for.
    - In Carousel the line sits inside the selected card, with the name below
      it. In List it shows in the hint bar's row, so only while
      [Button hints](layouts.md#page-title-and-button-hints) are hidden or
      with touch only.

### Title icons

On a phone or tablet, icons sit at the right of a game list's title:

| Icon | What it does |
| --- | --- |
| **Recent** | Open the [Game Switcher](game-switcher.md) |
| **Search** | [Search](#searching-a-game-list) this list |
| **Layout** | Pick the game list layout. It applies to every game list. See [Menu Layouts](layouts.md) |
| Trophy | Open or close the [achievements panel](#achievements-panel) |

![The Layout dropdown open from the title icons over the Game Boy Advance list, with Carousel ticked](../assets/screenshots/mobile/game-list-layout-menu.webp)

??? info "More detail"
    - The **Layout** dropdown offers **List**, **Grid**, **Carousel**,
      **Carousel, vertical left** / **right**, **Backdrop** and **Backdrop,
      vertical left** / **right**.
    - **Layout options** and **Achievements panel** in Layouts → Game lists
      hide the Layout and trophy icons. See
      [Layouts](layouts.md#layout-options-and-achievements-panel).

### Searching a game list

`START`, or the **Search** icon, searches only the games of the list you are
in. The prompt is titled after the list, such as **Search Sega Genesis**.
`B` returns to the list, on the game you had selected in the results.
Matching works as in [Search](#how-matching-works).

??? info "More detail"
    The results are titled with the list and your words, such as **Sega
    Genesis: sonic**.

### Achievements panel

While you are signed in to [RetroAchievements](retroachievements.md), `X` or
the trophy icon opens a panel from the right with the selected game's
achievements. See [RetroAchievements on game lists](retroachievements.md#on-game-lists)
for its buttons.

![The achievements panel over the Game Boy Advance list: Advance Wars (0 of 92) and its achievements, Class Dismissed! selected](../assets/screenshots/mobile/achievements-panel.webp)

??? info "More detail"
    - Tapping the selected game's name or info line opens the panel too.
    - With **Achievements panel** hidden, `X` still opens it, and the game's
      menu ends with **Achievements**.

## Context menus

Press `MENU` on a game to see what you can do with it. The menu depends on
where the game is listed.

![Advance Wars 2 - Black Hole Rising's context menu in the Game Boy Advance list, with Netplay first](../assets/screenshots/mobile/context-menu.webp)

| Item | What it does |
| --- | --- |
| **Play from start** | Start the game from the beginning instead of its auto-save. Shown first when the game has one |
| **Pin Item** / **Unpin Item** | Pin the game to Home, or take it off |
| **Hide Game** | Hide the game from its list |
| **Rename Rom** | Change the name the list shows |
| **Add to Collection** | Add the game to a collection, or start a new one |
| **Game Settings** | This game's own emulator settings. See [Emulator Settings](emulator-settings.md) |
| **Netplay** | Play the game with another device. See [Netplay](netplay.md) |
| **Fetch art** | Download art for this game. See [Artwork](artwork.md) |
| **Emulator** | Pick which emulator runs this game. See [Emulators](emulators/index.md) |
| **Remove from Collection** | Take the game out of the collection you are in |
| **Achievements** | Open the [achievements panel](#achievements-panel). Shown last, only while its icon is hidden |

- **Hidden games** are listed in **Tools → Settings → Library → Hidden
  games**. Press `A` **Unhide** there to bring one back.
- **Unassigned games** are files in an extra ROM folder that the app could
  not match to a system. Open them from **Tools → Settings → Library →
  Unassigned games**, and use **Console** to say which system a game belongs
  to. See [Library & ROM folders](library.md).

??? info "More detail: which items show where"
    | List | Items |
    | --- | --- |
    | A console | **Play from start** when the game has an auto-save, then **Pin Item**, **Hide Game**, **Rename Rom**, **Add to Collection**, **Game Settings**, **Netplay**, **Fetch art**, and **Emulator** on systems with more than one emulator |
    | A collection | The same, with **Remove from Collection** at the end |
    | [Search](#search) results | The same as a console, without **Emulator** |
    | Unassigned games | **Hide Game**, **Rename Rom**, **Console** |
    | The Android console | **Pin Item** / **Unpin Item** only |

    - **Fetch art** shows only for systems the art sources know, and only
      when the game's art is incomplete, or when **Artwork → Replace existing
      art** is on.
    - **Netplay** shows only for systems that have [netplay](netplay.md).
      When the `Y` **Netplay** hint is not on screen (touch only, Button
      hints hidden, or **Netplay hint** hidden in
      [Layouts](layouts.md#page-title-and-button-hints)), **Netplay** moves
      up, right after **Play from start**. On Home too.
    - A menu with 9 to 16 items shows as two columns when the screen is wide
      enough. `Left` / `Right` move between the columns. `Up` / `Down` loop
      round the items.
    - The Android console holds the Android games you added. See
      [Launcher Mode & Android Games](launcher.md).

### Hidden tabs

When you hide a tab in [Layouts](layouts.md#showing-and-hiding-tabs), `MENU`
on any item of the main menu ends with an entry for each hidden tab
(**Consoles**, **Collections** or **Tools**). Pick one to open that tab over
the current one; `B` returns.

![Home with the Tools tab hidden: Dragon Ball Z - The Legacy of Goku II's menu, with Netplay, Pin and Tools, Tools selected](../assets/screenshots/mobile/hidden-tabs-menu.webp)

??? info "More detail"
    Only a hidden tab that has something in it is offered. Items that have no
    menu of their own, such as a console, get a menu with just these,
    captioned **NX Redux**.

## Search

Press `START` on the main menu, or tap the **Search** icon, to search all
your games. It works from any tab. In a game list, `START` searches only that
list: see [Searching a game list](#searching-a-game-list).

1. The **Search** prompt opens, with your last search filled in.
2. Type part of a name and press `A` or the keyboard's **Done**.
3. The matches open as a game list titled **Search:** and your words, such
   as **Search: mario kart**.

![The Search prompt over the Home tab, with “castlevania” typed](../assets/screenshots/mobile/search-prompt.webp)

`B` or `START` closes the prompt without searching.

The results list games from every console, each with its console's tag, such
as `GBA`. It reads **No results** when nothing matches.

![Search results for castlevania in Carousel, with Castlevania - Aria of Sorrow selected: 0 of 66, Next: Old Bones](../assets/screenshots/mobile/search-results.webp)

| Button | What it does |
| --- | --- |
| `MENU` **Options** | The game's context menu |
| `X` **Achievements** | Open the [achievements panel](#achievements-panel) |
| `Y` **Netplay** | Play the game with another device, for games that have [netplay](netplay.md) |
| `B` **Back** | Return to the tab and the item you searched from |
| `A` **Resume** / **Open** | Launch the game, from its auto-save when it has one |

??? info "More detail"
    - Search also works from the tab row. The hint reads **Search** once you
      have games.
    - The results use your game list style.

### How matching works

The search looks in each game's name, its file name and its console tag.

- **Case, accents and punctuation don't matter.** `pokemon` finds
  *Pokémon*, and `pac man` finds *Pac-Man*.
- **Words can come in any order**, and each can be part of a word.
  `kart mario` finds *Mario Kart: Super Circuit*.
- **No typos.** Each word you type has to be there.

??? info "More detail"
    - **Roman numerals and digits match.** `final fantasy 6` finds *Final
      Fantasy VI*, and `vi` still finds *Virtua Fighter*.
    - **Words can be glued together.** `pacman` finds *Pac-Man*.
    - Names that start with your search come first, then names where every
      word starts a word, then the rest. Each group is A to Z.
    - Unassigned games, games without an emulator and Android games are not
      searched.

## Collections

Build your own game collections from a game list:

1. Press `MENU` on a game.
2. Choose **Add to Collection**.
3. Pick an existing collection, or **New Collection…** to make one and name
   it.

Your collections live on the **Collections** tab, each with its game count.
The tab appears once you have a collection.

Press `MENU` on a collection, or long-press it, to **Rename** or **Delete**
it. Delete asks first, and removes only the list: the games stay in your
library.

??? info "More detail"
    Collections are saved in the `Collections/` folder in your home folder.
