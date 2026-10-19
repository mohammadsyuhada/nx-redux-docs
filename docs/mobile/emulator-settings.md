# Emulator Settings

**Tools → Settings → Emulators → Settings** opens **Emulator Settings**. It
sets each emulator's options for a whole console, without starting a game
first.

![Settings, with Emulators open beside the sections: Default emulators, Settings and Saves](../assets/screenshots/mobile/settings-emulators.webp)

For one game, use **Game Settings** in the game's context menu instead. See
[Game Settings](#game-settings).

## The emulator list

The page lists each emulator that runs one of your consoles, with the tags it
covers, such as **Gambatte GB · GBC**. Press `A` on an emulator. When it
covers more than one tag, the app asks for the console first.

![Emulator Settings beside the Settings sections, listing each emulator with its tag, such as Gambatte GB](../assets/screenshots/mobile/emulator-settings.webp)

??? info "More detail"

    Emulators for consoles you have no games for are not listed.

## An emulator's settings

The page is titled with the emulator, the console and the tag, such as
**PicoDrive — Sega Genesis (MD)**. It has two groups:

| Group | What it holds |
| --- | --- |
| **Console settings** | The app's own settings for the console, such as **Controller Layout**. The same rows as the in-game [Console Settings](in-game-menu.md#console-settings) page, plus the ones read only when a game starts, such as **Graphics API**. |
| **Core settings** | The emulator's own options. Rows with `›` open a group of options, such as **Video** or **Audio**. |

![PicoDrive for Sega Genesis (MD): Console settings, then Core settings with its groups](../assets/screenshots/mobile/emulator-settings-core.webp)

- `LEFT` and `RIGHT` change a value. `A` steps it forward too.
- Each change is saved straight away. There is no **Save** row.
- Some options only take effect when a game starts, such as the N64
  resolution. The new value is used the next time you start a game.

What you set here is the console's setting, the same as the in-game menu's
**Save Changes → Save for console**. See the
[in-game menu](in-game-menu.md) for the options themselves.

??? info "More detail"

    - **Console settings** holds **Controller Layout** for every console,
      **Controller Type** for Sega Genesis, Sega CD and Sega 32X, the
      **Layout** and **Big Screen** rows for Nintendo DS, **New 3DS Controls**
      for Nintendo 3DS, **Portrait Pad** for both, and the Wii's rows
      ([Nintendo Wii & GameCube](emulators/wii-gamecube.md#console-settings)).
      The start-only rows are **Graphics API**
      ([Graphics API](emulators/index.md#graphics-api)), and the Wii's **Wii
      Screen** and **Pointer** rows.
    - With no controller and no on-screen pad, a tap on a value with three or
      more choices opens a dropdown of them, with the current one highlighted.
      Tap a choice to pick it, or tap outside to close it. A row with two
      values flips on a tap.
    - The in-game [Core Options](in-game-menu.md#core-options) page leaves out
      the options that only take effect when a game starts.
    - When the app cannot read an emulator's options outside a game, **Core
      settings** shows **This core's options aren't available outside a
      game.** Change them from the in-game menu instead.
    - The console's settings and **Save for console** write the same file.

## Game Settings

Open a game's context menu with `MENU` in a game list, or a long press on
the game, and choose **Game Settings**. The same page opens over the list, for that one game.

![Game Settings for Comix Zone, over the search results](../assets/screenshots/mobile/game-settings.webp)

- The first change gives the game its own settings, starting from the
  console's.
- To go back to the console's settings, press `A` on **Use emulator
  settings** at the top of the page.
- `B` goes back to the game list.

??? info "More detail"

    - The game's settings are the same file **Save Changes → Save for game**
      writes.
    - **Use emulator settings** shows only while the game has its own
      settings. `A` on it deletes them, so the game follows the console's
      again.
    - `B` returns to the game list on the same game.

## Default emulators

Some consoles can run on more than one emulator. **Tools → Settings →
Emulators → Default emulators** picks the emulator for a game with
no emulator of its own.

![Default emulators beside the Settings sections: one row per console, with the consoles that have only one emulator, such as Game Boy, dimmed](../assets/screenshots/mobile/default-emulators.webp)

Each console you have games for has a row, showing its emulator and tag,
such as **gpSP (GBA)**. On a console with more than one emulator, `A`,
`LEFT` or `RIGHT` cycles its emulators.

- Saves and BIOS are shared by the console's emulators, so switching emulator
  copies nothing.
- To switch one game to another emulator, use **Emulator** in its context
  menu. See [Emulators](emulators/index.md).

??? info "More detail"

    - The page explains:

        > For every game of the console, whichever of its folders holds it. A
        > per-game Emulator choice still wins.
        >
        > The tag is where saves and settings are kept.

    - The consoles with more than one emulator (listed in
      [Choosing an emulator](emulators/index.md#choosing-an-emulator)) always
      show. The other rows are dimmed and only show the emulator in use.
