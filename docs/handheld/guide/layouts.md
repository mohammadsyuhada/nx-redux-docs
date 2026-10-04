# Menu Layouts

The Consoles, Collections and Tools tabs, and every game list, can each be
drawn in their own style. Pick them in
[Settings → Appearance → Layouts](../settings/layouts.md). The menu picks up
the change as soon as you leave Settings, with no restart.

| Style | Tabs | Game lists | In short |
| --- | :---: | :---: | --- |
| [**List**](#list) | ✓ | ✓ | Text rows over the art, the most entries per screen |
| [**Grid**](#grid) | ✓ | ✓ | Two rows of tiles |
| [**Carousel**](#carousel) | ✓ | ✓ | One large item at a time, across or down the screen |
| [**Backdrop**](#backdrop) | | ✓ | Box art over the game's screenshot |

Out of the box, Consoles, Collections and game lists use **Carousel**, and
Tools uses **Grid**.

## List

A plain list. On the Consoles tab the selected console's controller sits
behind the list. In a game list the selected game's screenshot fills the
background.

*Consoles tab*

![Consoles tab in List style](../../assets/screenshots/consoles-list.png)

*Game list*

![Game list in List style](../../assets/screenshots/game-list-list.png)

- The line at the bottom shows the game count on a tab, and the selected
  game's last-played time, achievements and next achievement in a game list.
- In game lists `Left` / `Right` page up and down.

## Grid

Two rows of tiles that slide sideways as you move. Consoles show their logo
and game count. Games show their screenshot, and the selected tile adds its
name, last-played time and achievement count.

*Consoles tab*

![Consoles tab in Grid style](../../assets/screenshots/consoles-grid.png)

*Game list*

![Game list in Grid style](../../assets/screenshots/game-list-grid.png)

*Tools tab (the default for Tools)*

![Tools tab in Grid style](../../assets/screenshots/tools-grid.png)

## Carousel

A single row with the selected item large in the middle and its neighbours
fading out to the sides. Consoles show their logo over their controller,
collections their name, tools their icon. In a game list the caption under
the selected game gives its name, play time and achievements.

*Consoles tab*

![Consoles tab in Carousel style](../../assets/screenshots/consoles-carousel.png)

*Game list*

![Game list in Carousel style](../../assets/screenshots/game-list-carousel.png)

## Backdrop

Game lists only. The selected game's box art stands over its dimmed
screenshot, with its neighbours' boxes to the sides. A game with no box art
gets a placeholder box.

![Game list in Backdrop style](../../assets/screenshots/game-list-backdrop.png)

## Vertical orientation

Carousel and Backdrop can also run **down** the screen instead of across:
set the **orientation** row under the style to **Vertical**. `Up` / `Down`
then move through the items, and `Left` / `Right` switch tabs (on a tab) or
do nothing (in a game list).

*Consoles tab, vertical Carousel*

![Consoles tab in vertical Carousel](../../assets/screenshots/consoles-carousel-v.png)

*Game list, vertical Carousel*

![Game list in vertical Carousel](../../assets/screenshots/game-list-carousel-v.png)

*Game list, vertical Backdrop*

![Game list in vertical Backdrop](../../assets/screenshots/game-list-backdrop-v.png)

In a vertical game list the stack sits on the left and the details on the
right. Set **Vertical alignment** to **Right** to swap the sides.

??? info "More detail"
    - **Controller art.** The Consoles tab shows each console's controller
      behind it in the List and Carousel styles. Turn **Controller** off in
      Layouts for plain logos.
    - **Logos.** Systems without a logo of their own show their name under a
      cartridge emblem. Tools without an icon get a generic one.
    - **Games without artwork.** A game with no screenshot or box art gets a
      generated abstract picture, the same one every time. These pictures are
      stored in `.userdata/shared/.minui/placeholders/`, never next to your
      ROMs, and are safe to delete. To fetch real art for one game, press
      `MENU` on it and choose **Fetch Artwork**; for many games, use the
      [Artwork Manager](../apps/artwork-manager.md).
