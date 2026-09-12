# Artwork Manager

**Tools → Artwork Manager** fetches box art, screenshots and a mix composite
for your ROMs in bulk.

![Artwork Manager](../assets/screenshots/artwork-manager.png)

## Library

The Library lists every system with its artwork coverage (games with art /
total games).

![Artwork Manager Library](../assets/screenshots/artwork-library.png)

- `A` **Open** — drill into a system to queue individual games.
- `Y` **Queue All** — queue every missing artwork in the selected system.
- `B` **Back**.

## Progress

Queued downloads run in the background; the **Progress** page shows what's
being fetched. Downloaded art is placed alongside the ROMs, so it shows up in
the game lists immediately.

!!! tip "Single game instead?"
    For one game, use **Fetch Box Art** in the game's
    [context menu](../guide/context-menu.md) — no need to open the Artwork
    Manager at all.

## What gets saved

Every fetch stores up to three images per game inside the system's `.media`
folder, from a single set of ScreenScraper downloads:

| File | Content |
|---|---|
| `.media/<game>.png` | **Mix** — screenshot with the box art and logo floating over it |
| `.media/screenshot/<game>.png` | the in-game screenshot on its own |
| `.media/boxart/<game>.png` | the box art on its own |

A variant is skipped when ScreenScraper has no such image for a game. Which
one the game list shows is a launcher setting: **Settings → Appearance →
[Game art type](../settings/appearance.md)** (Mix / Screenshot / Box art),
next to **Game art style** (thumbnail or full-height background). If the
chosen variant is missing for a game, the list falls back to the Mix image.
The **Background** style always uses the screenshot, whatever the type is set
to, and shows an empty background for a game whose screenshot has not been
fetched.

!!! note "Upgrading from v1.9.0 or older"
    Releases up to v1.9.0 saved only the Mix image. **Screenshot** and
    **Box art** therefore fall back to it, and the **Background** art style,
    which never falls back, shows nothing at all for art fetched back then.
    To get the extra images for an existing library, open **Artwork Manager
    → Settings → Reset artwork**, then queue your systems again from the
    Library page.

## Settings — reset

![Artwork Manager Settings](../assets/screenshots/artwork-settings.png)

- **Reset artwork** — after a confirmation, deletes every fetched image
  (Mix, screenshot and box art) inside the `.media` folder of every system
  folder under `Roms`, including systems the scraper does not recognise,
  folder games and leftovers from renamed ROMs. The folder backgrounds
  `bg.png` and `bglist.png` are kept. Refused while a queue is still running.

## Settings — your ScreenScraper account

Artwork comes from [ScreenScraper](https://www.screenscraper.fr/). Fetching
works **without any account**, but anonymous access shares a limited request
budget — fine for a game here and there, slow going for a whole library.

Enter your own (free) ScreenScraper **username** and **password** here and
every fetch runs on your account's allowance instead:

- **Higher rate limits** — your account's own daily request quota, which for
  registered users is well above the shared anonymous budget.
- **Live quota display** — once logged in, the page shows **Requests Today**
  and **Max Requests** (your account's daily limit), fetched straight from
  your ScreenScraper account.
- **Logout** — a logged-in page also gains a Logout entry that clears the
  saved credentials from the device.

Both fields are typed with the on-screen keyboard; the password is stored on
the SD card and always displayed masked.
