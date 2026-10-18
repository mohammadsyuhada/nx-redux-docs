# Sega Dreamcast

Play Dreamcast games, plus the **Sega NAOMI** and **Sammy Atomiswave**
arcade games built on the same hardware. They all run on **Flycast**, from one
folder: `Roms/Dreamcast (DC)/`.

<figure class="nx-phone" markdown>
![Crazy Taxi 2 on the Fold's cover screen, with the Dreamcast pad: A, B, X and Y in the Dreamcast's colours](../../assets/screenshots/mobile/pad-dc.webp){ .nx-phone__screen }
![](../../assets/landing/mobile/zfold8.webp){ .nx-phone__frame }
</figure>

Dreamcast has the [in-game menu](../in-game-menu.md) with save states and
auto-resume, the [Game Switcher](../game-switcher.md), play time in the
[Game Tracker](../game-tracker.md), and
[RetroAchievements](#retroachievements) for disc games. It has no cheats.

## BIOS

Put the BIOS files in `Bios/DC/`. Without the right one, the game doesn't
start and the app names the missing file.

| File | For |
| --- | --- |
| `dc_boot.bin` | Dreamcast discs |
| `naomi.zip` | NAOMI games |
| `awbios.zip` | Atomiswave games |

The arcade games don't need `dc_boot.bin`; see
[NAOMI and Atomiswave](#naomi-and-atomiswave).

!!! warning "Coming from the handheld"
    The handheld can run Dreamcast discs without a BIOS. The app can't: add
    `dc_boot.bin` even if your handheld played the games without it.

## Adding games

Put Dreamcast discs in `Roms/Dreamcast (DC)/`. The app plays `.chd`, `.cdi`,
`.gdi`, `.cue` and `.m3u`, and a zip or 7z holding one disc.

A **GDI game** is a `.gdi` file plus its track files. Give each one its own
folder, with the `.gdi` named after the folder. The folder shows as one game:

```
Roms/Dreamcast (DC)/
├── Soulcalibur (USA).chd
└── Shenmue (USA)/
    ├── Shenmue (USA).gdi
    ├── track01.bin
    ├── track02.raw
    └── track03.bin
```

!!! warning "Rename a `disc.gdi`"
    Some sets name every sheet `disc.gdi`. Rename it to match its folder: the
    app doesn't list a folder whose `.gdi` has a different name.

??? info "More detail"
    Saves, states and the memory card are named after the `.gdi` file, so
    every `disc.gdi` game would share them. A zipped disc is unpacked on
    first launch.

A multi-disc game plays as one game from an `.m3u` that lists its discs; see
[Multi-disc games](index.md#multi-disc-games).

## Controls

The face buttons map to the Dreamcast pad **by the printed letter**: `A`
is the Dreamcast's `A`. The Dreamcast pad is lettered like an Xbox pad:

| Position | Dreamcast button |
| --- | --- |
| Bottom | `A` |
| Right | `B` |
| Left | `X` |
| Top | `Y` |

| Control | Dreamcast control |
| --- | --- |
| D-pad | D-pad |
| Left stick | Analog stick |
| `L2` / `R2` | Analog triggers |
| `START` | `START` |
| `SELECT` | Insert a coin (NAOMI and Atomiswave) |
| `L3` (press the left stick) | Test, the operator menu (NAOMI and Atomiswave) |
| `R3` (press the right stick) | Service (NAOMI and Atomiswave) |

- `MENU`, or `SELECT` + `START`, opens the
  [in-game menu](../in-game-menu.md). On NAOMI and Atomiswave the game sees
  the `SELECT` press first, so it may count a coin.
- On a Nintendo-layout pad, set **Controller Layout** to **Xbox** in
  **Options → Console Settings** to play with the Dreamcast's positions (see
  [Controls](../controls.md#controller-buttons)).

??? info "More detail"
    - The on-screen pad draws `A` `B` `X` `Y` in the Dreamcast's colours, in
      the positions above. With it, the in-game menu follows the drawn
      letters: the bottom button (`A`) confirms and the right one (`B`) goes
      back.
    - On a controller, a "Press A" prompt means the button printed `A`. If a
      controller is read wrongly, set **Controller Layout** to match it.
    - `L3` and `R3` are on controllers only: the on-screen pad has no stick
      buttons.
    - On a controller the triggers press as far as you pull them. On the
      on-screen pad, `L2` and `R2` press fully.

## Multiplayer

Up to four players can play, each on their own controller; see
[Local Multiplayer](../multiplayer.md). On Dreamcast discs, games save to
Player 1's memory card.

??? info "More detail"
    - NAOMI and Atomiswave games take up to four players too.
    - On Dreamcast discs, every player's controller has the Vibration Pack,
      and only Player 1's has a memory card.
    - To give Players 2 to 4 a card, set **Device in Expansion Slot B1**,
      **C1** or **D1** to **VMU** in
      [Emulator Settings](../emulator-settings.md) under **Core settings**.

## Memory cards (VMU)

Every game gets **its own memory card**, kept with your other
[saves inside the app](../library.md#saves):

```
Saves/DC/<game>.A1.bin
```

!!! warning "Renaming a ROM file"
    Renaming the game's file leaves its card behind under the old name, as
    with any save. **Rename Rom** in the app only changes the name the list
    shows, so the card stays with the game.

??? info "More detail"
    - For example `Saves/DC/Soulcalibur (USA).A1.bin`. A GDI game's card is
      named after its folder, and an `.m3u` game shares one card across its
      discs.
    - The names match the handheld's NX Redux, so a card carries between
      your phone and your handheld with **Export saves** and **Import
      saves**, or with [Device Sync](../device-sync.md).
    - The arcade games keep their high scores and cabinet settings in
      `Saves/DC/reicast/`, with the other saves.

## Save states

Save states work as on every other system: eight slots, plus the auto-save
when you quit. Each Dreamcast state is **about 36 MB**, so eight full slots
for one game take close to 300 MB.

## Settings

Change Dreamcast's settings in the in-game menu under **Options → Core
Options**, or outside a game in [Emulator Settings](../emulator-settings.md).
The internal resolution starts at 640×480, the Dreamcast's own. Higher values
look sharper but cost speed.

## NAOMI and Atomiswave

NAOMI and Atomiswave games are MAME-style zips (or 7z). To play them:

1. Put the zips straight into `Roms/Dreamcast (DC)/`, next to your Dreamcast
   discs.
2. Put the board's BIOS zip in `Bios/DC/`: `naomi.zip` for NAOMI,
   `awbios.zip` for Atomiswave.
3. Launch the game and press `SELECT` to insert a coin, then `START`.

A few sets need another BIOS zip, such as `naomi2.zip` for NAOMI 2 games.

!!! warning "Don't rename the zips"
    Flycast finds a game by its short zip name (`mslug6.zip`, not
    `Metal Slug 6.zip`). The game list still shows readable names:
    `mslug6.zip` shows as *Metal Slug 6*.

??? info "More detail"
    - **Names.** Each zip gets its full title from Flycast's own game list.
      A **Rename Rom** or `map.txt` alias always wins over that title.
    - **BIOS zips are hidden.** A BIOS zip put in the game folder by mistake
      is not listed as a game. It still has to be in `Bios/DC/`.
    - **Clones.** A clone set loads its parent set from the same folder.
    - **Zipped discs.** A zip that isn't one of Flycast's arcade sets is
      treated as a zipped Dreamcast disc and unpacked.
    - **Atomiswave BIOS.** Both MAME versions of `awbios.zip` work.

### When a set won't start

The app checks before launch and says what is missing: the BIOS zip, a file
inside it, or a file from the game's own zip. Get a complete set that matches
Flycast's version of MAME.

??? info "More detail: the messages"
    - BIOS zip missing: **Metal Slug 6 needs awbios.zip: put it in Bios/DC/**
    - A file missing from the BIOS zip: **‹Game› needs naomi.zip with ‹file›
      in it: put a complete naomi.zip in Bios/DC/**
    - The game's own zip incomplete: **‹Game› needs ‹file›, which ‹set›.zip
      does not have: the set is incomplete or from another MAME version**

## RetroAchievements

Dreamcast discs work with [RetroAchievements](../retroachievements.md) in
`.chd`, `.gdi`, `.cue` and `.m3u`, and zipped discs once unpacked. `.cdi`
games are not recognised, and NAOMI and Atomiswave games are not on
RetroAchievements.
