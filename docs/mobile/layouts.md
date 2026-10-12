# Menu Layouts

The Consoles, Collections and Tools tabs, and every game list, can each be
drawn in their own style. Pick them in **Tools → Settings → Layouts**, which
also lets you hide tabs, pick what shows behind consoles and beside games,
and hide the page title, the button hints and the game stats. Home has its own
layout, set here too, and comes in List, Grid or Carousel.

| Style | Tabs | Game lists | In short |
| --- | :---: | :---: | --- |
| [**List**](#list) | ✓ | ✓ | Text rows over the art, the most entries per screen |
| [**Grid**](#grid) | ✓ | ✓ | Two rows of tiles |
| [**Carousel**](#carousel) | ✓ | ✓ | One large item at a time, across or down the screen |
| [**Backdrop**](#backdrop) | | ✓ | Box art over the game's screenshot |

Out of the box, Consoles, Collections and game lists use **Carousel**, and
Home and Tools use **Grid**.

## The Layouts page

![Layouts page](../assets/screenshots/mobile/settings-layouts.webp)

`Right` and `A` step the highlighted row to its next value, and `Left` to
the previous one. Some rows only show when they apply. When a change adds or
removes rows, the highlight stays on the row you changed.

| Row | Values | Default | Shows |
| --- | --- | --- | --- |
| [**Home tab**](#showing-and-hiding-tabs) | Show, Hide | Show | Always |
| **Home layout** | List, Grid, Carousel | Grid | When Home tab is Show |
| [**New shelf**](foldables.md#shelves) | Show, Hide | Show | When Home tab is Show |
| [**Not started shelf**](foldables.md#shelves) | Show, Hide | Show | When Home tab is Show |
| [**Consoles tab**](#showing-and-hiding-tabs) | Show, Hide | Show | Always |
| **Consoles layout** | List, Grid, Carousel | Carousel | When Consoles tab is Show |
| **Consoles orientation** | Horizontal, Vertical | Horizontal | When Consoles tab is Show and Consoles layout is Carousel |
| [**Consoles controller**](#consoles-controller) | Controller, Background, None | Controller | When Consoles tab is Show and Consoles layout is List |
| [**Collections tab**](#showing-and-hiding-tabs) | Show, Hide | Show | Always |
| **Collections layout** | List, Grid, Carousel | Carousel | When Collections tab is Show |
| **Collections orientation** | Horizontal, Vertical | Horizontal | When Collections tab is Show and Collections layout is Carousel |
| [**Tools tab**](#showing-and-hiding-tabs) | Show, Hide | Show | Always |
| **Tools layout** | List, Grid, Carousel | Grid | When Tools tab is Show |
| **Tools orientation** | Horizontal, Vertical | Horizontal | When Tools tab is Show and Tools layout is Carousel |
| **Game lists layout** | List, Grid, Carousel, Backdrop | Carousel | Always |
| **Game lists orientation** | Horizontal, Vertical | Horizontal | When Game lists layout is Carousel or Backdrop |
| [**Game lists alignment**](#game-lists-alignment) | Left, Right | Left | When Game lists orientation is Vertical |
| [**List art**](#list-art) | Screenshot, Mix, 3D box art, 2D box art, Wheel, None | Screenshot | When Game lists layout is List |
| [**Backdrop art**](#backdrop-art) | 3D box art, 2D box art, Wheel | 3D box art | When Game lists layout is Backdrop |
| [**Extra info**](#extra-info) | Show, Hide | Show | Always |
| [**Page title**](#page-title-and-button-hints) | Show, Hide | Show | Always |
| [**Button hints**](#page-title-and-button-hints) | Show, Hide | Show | Always |
| [**Recent hint**](#single-hints) | Show, Hide | Show | When Button hints is Show |
| [**Search hint**](#single-hints) | Show, Hide | Show | When Button hints is Show |
| [**Netplay hint**](#single-hints) | Show, Hide | Show | When Button hints is Show, on a phone with netplay |
| [**Reset to defaults**](#reset-to-defaults) | | | Always |

## Showing and hiding tabs

Set a tab's row to **Hide** to take it out of the tab row. Hide all of them
for a Home-only menu. With only one tab left, the tab row is replaced by an
**NX Redux** title, `L1` / `R1` have nothing to switch to, and `Up` never
moves onto the title.

A hidden tab is never out of reach, so Settings, which lives in Tools, is
always one press away:

- Press `MENU` on any item of the main menu. After the item's own options,
  the menu offers **Consoles**, **Collections** and **Tools** for each tab
  that is hidden and has something in it. A menu that holds only these is
  captioned **NX Redux**.
- Or touch and hold the tab row (or the **NX Redux** title).

Picking one opens that tab over the current one, in its own layout and with
its name as the title. `A` opens items as usual and `MENU` gives their
options. The hint bar shows `B` **Back**, which returns to the tab
underneath, where you left it. `L1` / `R1` and `Left` / `Right` past the ends
do not switch tabs; a Grid wraps around instead, and `Up` never moves onto
the title. A game you start from it brings you back to the main menu's own
tab afterwards.

The tab drops back to the one underneath by itself when you show its tab
again, or when it is emptied.

Home's **+N** square and **Pick a game** open a hidden Tools or Consoles tab
the same way. While that tab is hidden, a long press on **+N** or **Pick a
game** also opens the hidden-tab menu, which is how touch reaches it when the
tab row is hidden.

## List

A plain list. On the Consoles tab the selected console's controller sits
beside the list (see [Consoles controller](#consoles-controller)). In a game
list the selected game's picture fills the background or sits in a box (see
[List art](#list-art)).

*Consoles tab*

![Consoles tab in List style](../assets/screenshots/mobile/consoles-list.webp)

*Game list*

![Game list in List style](../assets/screenshots/mobile/game-list-list.webp)

The line at the bottom shows the selected game's last-played time,
achievements and next achievement in a game list, and the game count on the
Collections tab. On the Consoles tab it holds only the scroll arrows, with no
shade behind them.

`Up` on the first row wraps to the last, and `Down` on the last row wraps to
the first. Only a fresh press wraps: holding the button stops at the end.

## Grid

Two rows of tiles that slide sideways as you move. Consoles show their logo
and game count. Games show their screenshot, and the selected tile adds its
name, last-played time and achievement count.

On a phone held upright the Consoles tab shows two consoles across, each half
the screen wide. Once you move past the second, the selected console stays in
the middle with half of each neighbour showing on either side, as on the
handheld.

*Consoles tab*

![Consoles tab in Grid style](../assets/screenshots/mobile/consoles-grid.webp)

*Game list*

![Game list in Grid style](../assets/screenshots/mobile/game-list-grid.webp)

## Carousel

A single row with the selected item large in the middle and its neighbours
to the sides. Consoles show their logo over their controller, collections
their name, tools their icon. In a game list the caption under the selected
game gives its name, then its play time and achievement count on one line and
the next achievement to earn on the line below.

On the Collections and Tools tabs each item is only as wide as its name or
icon, and the space between neighbours stays the same, so short and long names
sit evenly along the row.

*Consoles tab*

![Consoles tab in Carousel style](../assets/screenshots/mobile/consoles-carousel.webp)

*Game list*

![Game list in Carousel style](../assets/screenshots/mobile/game-list-carousel.webp)

## Backdrop

Game lists only. The selected game's box art stands over its dimmed
screenshot, with its neighbours' boxes to the sides. Its caption is laid out
like the Carousel's: the name, then the play time and achievement count, then
the next achievement on its own line. The Vertical orientation shows the same lines.

![Game list in Backdrop style](../assets/screenshots/mobile/game-list-backdrop.webp)

## Orientation

Carousel and Backdrop can also run **down** the screen instead of across:
set the **orientation** row under the style to **Vertical**. `Up` / `Down`
then move through the items, wrapping as a List does: `Up` on the first item
goes to the last and `Down` on the last to the first, on a fresh press only.
`Left` / `Right` switch tabs on a tab, and do nothing in a game list.

<div class="grid" markdown>

<figure markdown>

![Consoles tab in horizontal Carousel](../assets/screenshots/mobile/consoles-carousel.webp)

<figcaption>Consoles, Horizontal</figcaption>
</figure>

<figure markdown>

![Consoles tab in vertical Carousel](../assets/screenshots/mobile/consoles-carousel-vertical.webp)

<figcaption>Consoles, Vertical</figcaption>
</figure>

</div>

## Game lists alignment

In a vertical game list the stack sits on the left and the details on the
right. Set **Game lists alignment** to **Right** to swap the sides.

<div class="grid" markdown>

<figure markdown>

![Vertical Backdrop aligned left](../assets/screenshots/mobile/game-list-backdrop-vertical-left.webp)

<figcaption>Backdrop, Vertical, Left</figcaption>
</figure>

<figure markdown>

![Vertical Backdrop aligned right](../assets/screenshots/mobile/game-list-backdrop-vertical-right.webp)

<figcaption>Backdrop, Vertical, Right</figcaption>
</figure>

</div>

## In landscape

Turn the phone sideways and the same layouts spread across the wider screen.
These are the Carousel and Backdrop game lists, both Horizontal.

<div class="grid" markdown>

<figure markdown>

![Carousel game list in landscape](../assets/screenshots/mobile/game-list-carousel-landscape.webp)

<figcaption>Carousel, landscape</figcaption>
</figure>

<figure markdown>

![Backdrop game list in landscape](../assets/screenshots/mobile/game-list-backdrop-landscape.webp)

<figcaption>Backdrop, landscape</figcaption>
</figure>

</div>

## List art

The picture a game list shows in the List style:

- **Screenshot** (default): the game's screenshot fills the background.
- **Mix**, **3D box art**, **2D box art** or **Wheel**: that picture, whole,
  in a box on the right. The game names always stop short of the box.
- **None**: no picture and no background on any List-style list below the
  tabs, game lists and collections alike.

A game without the picture you picked shows its screenshot full-screen
instead. Mix, 2D box art and Wheel come from [Artwork](artwork.md).

## Backdrop art

The box in a Backdrop row: **3D box art** (default), **2D box art** or
**Wheel**. A wheel keeps its own shape instead of being cut into a case. A
game without that picture shows its 3D box art, else a placeholder box. The
background stays the screenshot.

## Consoles controller

What shows behind the Consoles tab in the List style. The row shows only
while **Consoles layout** is **List**; the Carousel style always shows each
console's controller.

- **Controller** (default): each console's controller beside the list.
- **Background**: no controller. The selected console's own picture,
  `Roms/<console>/.media/bg.png`, fills the background as a game list's
  screenshot does. A console without one shows plain black.
- **None**: no controller and no background: a plain list on black.

## Page title and button hints

**Page title** set to **Hide** removes the main menu's tab row and a game
list's title. `L1` / `R1` still switch tabs. **Button hints** set to **Hide**
removes the hint bar along the bottom of the main menu and the game lists.
Other screens, such as Settings and the in-game menu, keep both.

- They only take effect while a controller is connected or the portrait pad
  shows. With touch alone in landscape, the hints stay and the main menu
  keeps its tab row (a tap on a tab is the only touch way to switch tabs),
  while a game list's title still hides.
- With the title hidden, its space goes to the page. A List shows more rows.
  Home moves its stats strip to the top of the screen and gains a row of tool
  squares. Grid, Carousel and Backdrop keep their size and centre in the full
  height.
- With the hints hidden, their space stays empty, Home included. In a List
  game list, the selected game's play time and achievements move down into
  that row.

### Single hints

**Recent hint**, **Search hint** and **Netplay hint** each hide one hint,
`SELECT` **Recent**, `START` **Search** or `Y` **Netplay**, and leave the rest
of the bar. The button still works. Its action moves into the `MENU` menu
instead:

- **Netplay** leads a game's menu, in game lists and on Home.
- **Recent** and **Search** join every main menu item's menu, after its own
  items. An item without a menu of its own, such as a console, gets one with
  just these. A long press on the tab row offers them too.

With **Button hints** hidden, all three are in the menu, along with
**Resume** in a game list.

## Extra info

**Extra info** set to **Hide** removes the game stats from the main menu and
the game lists, for a cleaner look:

- **Home** drops its stats strip (**This month**, **Most played**) and the
  play time and achievements on the Continue card, pinned games and the
  [shelves](foldables.md#shelves).
- A **List** game list leaves the selected game's play time, achievements
  and next achievement out of the bottom line, and out of the hint row when
  the hints are hidden.
- The selected **Grid** tile shows only the game's name.
- **Carousel** and **Backdrop** captions show only the name, horizontal and
  vertical alike.

Home gives the strip's space to the top section: the Continue card and the
tool squares grow, and a column of squares gains one more only when a whole
square fits.

Unlike the page title and hints, this works in every mode: touch alone,
with a controller, portrait or landscape. A console's or collection's game
count stays, and the [Game Switcher](game-switcher.md), the
[in-game menu](in-game-menu.md), the [Game Tracker](game-tracker.md) and
[RetroAchievements](retroachievements.md) keep all their info.

## Reset to defaults

**Reset to defaults** puts every row on the Layouts page back to its
default: every tab shown, each tab's layout and orientation, the game
lists' layout, orientation and alignment, **Consoles controller**,
**List art**, **Backdrop art**, **Extra info**, **Page title** and
**Button hints**. It does not ask first.

??? info "Games without artwork"
    A game with no screenshot or box art gets a generated abstract picture,
    the same one every time. To fetch real art, press `MENU` on a game and
    choose **Fetch art**, or use [Artwork](artwork.md) for many games at
    once.
