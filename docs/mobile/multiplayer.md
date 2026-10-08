# Local Multiplayer

Two to four people can play one game on one phone or tablet, each on their
own controller. Any Android controller works, over Bluetooth or USB. There
is nothing to set up first:

- **Everyone on a controller:** stand the phone up or connect it to a TV,
  and give each player a pad.
- **A handheld plus a pad:** on an Android handheld, such as a Retroid, play
  on its built-in controls while a friend uses a Bluetooth pad.

The on-screen pad is never a player of its own: it always controls
Player 1. Each extra player needs a controller.

## Which systems

Each system has as many players as the console had controller ports. The
TurboGrafx-16 is the exception: its multitap is always plugged in, so it
has four. Other multitap adapters aren't supported.

| Players | Systems |
| --- | --- |
| Up to 4 | Nintendo 64, Sega Dreamcast, Arcade (FBNeo), TurboGrafx-16 |
| 2 | NES and Famicom Disk System, Super Nintendo, Sega Genesis, Master System, SG-1000, Sega CD, 32X, PlayStation, Atari 2600, Atari 7800, Atari 5200, ColecoVision |
| 1 | Every other system, such as Game Gear, the Game Boys, Nintendo DS, Nintendo 3DS, PSP and PICO-8 |

On Arcade, each game uses as many players as the cabinet had.

## Joining a game

1. Start the game.
2. Press any button on a controller. It takes the next free player:
   Player 1 first, then Player 2, and so on.
3. A notice names the player and the controller, such as
   **Player 2: Xbox Wireless Controller**.

Moving the left stick or the d-pad joins too. Moving only the right stick
doesn't. A press while the [in-game menu](in-game-menu.md) is open never
joins: close the menu first.

Who is which player lasts until you quit the game. Each launch starts with
every player free again. Save states don't store who is which player.

## The in-game menu

- Only Player 1 opens the in-game menu with `SELECT` + `START`. For Players
  2 to 4, `SELECT` and `START` go to the game.
- The Home or Guide button (`MENU`) opens the menu from any controller.
- Any controller can move around the open menu.

## The Players page

In a game with more than one player, the in-game menu has a **Players** row
under **Load**. Its page lists:

| Row | Value | `LEFT` / `RIGHT` |
| --- | --- | --- |
| **Player 1** to **Player 4** | The controller's name, **Empty**, or the name with **(disconnected)** | Steps through the connected controllers that are playing, and **Empty**. Picking a controller another player has swaps the two players. |
| One row per connected controller | **Playing** or **Not playing** | Switches between them. |

The footer reads **Close the menu, then press a button on a new controller to
join.** Two controllers with the same name are numbered, such as
**Xbox Wireless Controller (2)**.

### Not playing

A controller set to **Not playing** is ignored in multiplayer games until
you set it back to **Playing**. It is remembered for that controller, across
games, and it doesn't affect one-player games.

!!! tip "Bench a handheld's built-in controls"
    Playing on an Android handheld with an external pad? Set the handheld's
    built-in controls to **Not playing**, and your pad stays Player 1.

## When a controller disconnects

If a controller drops out, such as a flat battery or a lost Bluetooth
connection, its player stays reserved. Its row reads, for example,
**Xbox Wireless Controller (disconnected)**.

- Reconnect the same controller and it gets the same player back.
- The other players carry on as before.
- Any buttons the dropped player was holding are let go.

## Rumble

Each player's rumble goes to their own controller.

- **Player 1** falls back to the phone's vibration motor when their
  controller has no motor Android can use, or when they play on the
  on-screen pad.
- **Players 2 to 4** never vibrate the phone.
- **Game rumble** in [**Tools → Settings → Controls**](controls-settings.md)
  sets the strength for everyone.

Some controllers' motors aren't available to Android over Bluetooth. An
8BitDo Ultimate 2 over Bluetooth on a Galaxy Fold is one we tried. That
player then gets no rumble.

Which games rumble: see [Controls → Game rumble](controls.md#game-rumble).

## System notes

| System | Note |
| --- | --- |
| [Sega Dreamcast](emulators/dreamcast.md#multiplayer) | Players 2 to 4 have the Vibration Pack but no memory card. Games save to Player 1's card. |
| [PlayStation](emulators/playstation.md#controls) | Player 2 gets the same DualShock pad as Player 1. |
| [Sega Genesis, Sega CD, 32X](emulators/other-systems.md#controller-type) | **Controller Type** applies to Player 2 too. |
| [Nintendo 64](emulators/nintendo-64.md#rumble) | Each player's Rumble Pak is set in Core Options, from **Player 1 Pak** to **Player 4 Pak**. |

## Limits

- A controller that Android sees as two devices, such as a pair of
  Joy-Cons, becomes two players.
- No multitap adapters yet, such as the NES Four Score, the Super Nintendo
  or PlayStation multitap, or the Sega Team Player.
- No link-cable play for handheld systems.
