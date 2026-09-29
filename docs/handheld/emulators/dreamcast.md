# Sega Dreamcast

Dreamcast games run on **Flycast** (v2.7), bundled as a libretro core and
played inside NX Redux's own emulator, like most other systems. Put your games
in `Roms/DreamCast (DC)/`.

Flycast also plays the arcade boards built on Dreamcast hardware — **Sega
Naomi** and **Sammy Atomiswave** — from the same folder. See
[Arcade games](#arcade-games-naomi-atomiswave) below: unlike Dreamcast
itself, those need BIOS files.

Because Dreamcast runs in the same emulator as the other systems, it gets
the same features:
- the [in-game menu](../guide/in-game-options.md) with save states (slots
  with previews), auto-resume and the [Game Switcher](../guide/game-switcher.md);
- fast-forward, screenshots, shaders and screen effects;
- playtime tracking and ambient LEDs;
- [RetroAchievements](#retroachievements) through NX Redux.

!!! note "Upgrading from an older NX Redux"
    Older versions ran Dreamcast on a standalone Flycast with its own overlay
    menu. Your memory cards come across automatically (see
    [Memory cards](#memory-cards-vmu)); **save states made with the old
    emulator can't be loaded** by the new one. Save your progress in-game (on
    the memory card) before updating if you rely on a save state.

## Controls

The face buttons map to the Dreamcast pad **by position**, the way the
Dreamcast controller is laid out:

| Device button | Dreamcast button |
| --- | --- |
| Bottom (`B` on the cap) | A |
| Right (`A` on the cap) | B |
| Left (`Y` on the cap) | X |
| Top (`X` on the cap) | Y |

Games that put the camera or movement on the face buttons (Unreal Tournament,
for one) play as designed. The trade-off is that a "Press A" prompt means
the bottom button, not the cap printed `A`. The mapping is the same under
either [Button Layout](../guide/button-layout.md) — only the in-game menu's
confirm and back follow that setting.

The D-pad and left stick drive the Dreamcast D-pad and analog stick, and
`L2`/`R2` are the analog triggers. On Naomi and Atomiswave games the same
four buttons act as the cabinet's buttons, and **SELECT** inserts a coin.
To change the mapping, use **Options → Controls** in the in-game menu, as
for any other system.

## Memory cards (VMU)

Every game gets **its own memory card**, stored next to your other saves:

```
Saves/DC/<rom name>.A1.bin
```

For example `Saves/DC/Soulcalibur (USA).A1.bin`.
- **Multi-disc games share one card:** a `(Disc 1)` / `(Disc 2 of 3)` tag in
  the file name is ignored, so Shenmue's discs all use the same card.
- **The names match [NX Redux Mobile](../../mobile/getting-started.md):**
  copy a card between your phone and handheld and it just works.
- **Card writes are saved immediately,** so a crash or a forced quit can't
  leave a half-written card.
- **Renaming a ROM** leaves its card behind under the old name, as with any
  save. Rename the card to match.

**Coming from an older version?** The standalone emulator kept one shared
card for all games. The first time you launch each game, its new card starts
as a **copy of that shared card**, so every existing save is still there. The
old card itself is never changed or deleted. It stays in
`.userdata/shared/DC-flycast/` as a backup. Your console settings and arcade
high scores are copied over the same way, once.

To give a game a **fresh, empty card**, delete its `.A1.bin` file. The next
launch starts a blank card, and the old shared card is not copied back.

## BIOS

Dreamcast runs **out of the box without a BIOS**, using Flycast's built-in
replacement (HLE). If you prefer to boot through the real BIOS, drop
`dc_boot.bin` into `Bios/DC/`. A RetroArch-style `Bios/DC/dc/` subfolder
also works; if it exists, it's used instead.

Flycast also keeps the console's settings and clock (`dc_nvmem.bin`) and a
couple of shared files in that same folder. Leave them there.

## Settings

Dreamcast's emulator settings live in **Options → Core Options** in the
in-game menu, and in the game list's
[Emulator Options](../guide/emulator-options.md) before launching, per game or
for all games.
- **Internal Resolution:** 640×480 by default on every device (the
  Dreamcast's own resolution). Higher values look sharper but cost speed.
  The Brick has little to spare, while the Smart Pro S can handle 960×720 in
  lighter games. It can be changed mid-game.
- **Widescreen Hack:** on by default on the Smart Pro S (16:9 screen), off on
  the Brick and Brick Pro.
- **Auto Frame Skip** stays on for heavy 3D scenes.
- **Netplay Input Delay:** see [Netplay](#netplay).

Dreamcast uses the **Emulated** [Core Sync](../guide/in-game-options.md#frontend)
by default. It follows the game's own timing, so games that run at 30 fps
(Metal Slug 6, Quake III Arena) play at their real speed. The
**Debug HUD** shows an extra **`EMU nn%`** line with the true emulation speed,
the easiest way to tell whether a heavy scene keeps up.

## Arcade games (Naomi & Atomiswave)

Naomi and Atomiswave games are MAME-style zips. Put them straight into
`Roms/DreamCast (DC)/` next to your Dreamcast games and **don't rename
them** — like [FBNeo arcade zips](arcade.md), the emulator identifies a
game by its short zip name (`mslug6.zip`, not `Metal Slug 6.zip`). The game
list still shows readable names: each zip gets its **full title** from
Flycast's own game list (`ikaruga.zip` shows as *Ikaruga*, `mvsc2.zip` as
*Marvel vs. Capcom 2*), and the in-game menu shows the same title. Dreamcast
disc images keep their filenames. A **Rename Rom** or
[`map.txt`](../guide/main-menu.md#custom-display-names-maptxt) alias always
wins over that title. A BIOS zip placed in the game folder by mistake is
hidden from the list.

Both boards **require their BIOS zip** in `Bios/DC/`:

| Board | BIOS file |
| --- | --- |
| Naomi | `naomi.zip` |
| Atomiswave | `awbios.zip` |

Without it, the game can't start.

!!! note "Atomiswave BIOS: both MAME sets work"
    Either `awbios.zip` variant is accepted — the older MAME set
    (`bios0.ic23`) and the current MAME re-dump (`bios.ic23_l`).

As on the real cabinets, arcade games want coins before START works —
press **SELECT** to insert a coin. High scores and cabinet settings are saved
in `Saves/DC/reicast/`.

## RetroAchievements

Dreamcast, Naomi and Atomiswave games use NX Redux's
[RetroAchievements](../apps/retroachievements.md) support, exactly like the
other systems:
- sign in once in the tool;
- unlocks work offline and sync later;
- they show up in the tool straight away.

!!! tip "\"Unsupported Game Version\""
    If a game shows up as *Unsupported Game Version (title)*, RetroAchievements
    recognises your disc but hasn't tested that particular dump with its
    achievements. Use one of the versions listed on the game's **Supported
    Game Hashes** page on retroachievements.org.

## Netplay

Dreamcast supports **GGPO netplay** for 2 players: rollback netplay, which
keeps controls responsive over Wi-Fi. Start it the same way as on other
systems: press `Y` on a game and host or join (see [Netplay](../netplay.md)).
- **The host brings the save.** The session uses the host's memory card,
  console settings and (for arcade games) high scores. The other player plays
  on a temporary copy, so their own saves are never touched. The host keeps a
  backup of what it brought in `.userdata/shared/DC-flycast/netplay-backup/`.
- **BIOS:** both devices use the real BIOS only when **both have the same
  `dc_boot.bin`**. Otherwise both use the built-in BIOS for that session,
  automatically. Arcade games need their BIOS zip on **both** devices.
- **Settings that change how the game plays are kept the same on both sides**
  for the session, whatever each device has set:
  - region, language and broadcast (these follow the disc and the host's
    console settings);
  - CPU clock, DSP, widescreen cheats and memory-card layout.

  Display settings (resolution, widescreen, frame skip) stay per device.
- **Netplay Input Delay** (Core Options, 0–5, default 1) is each
  player's own. Raise it if a weak connection causes jerky corrections, at
  the cost of a little input lag.
- **Speed:** menus run at full speed, while fights run at around 70% on
  current handhelds, about the same as the old standalone emulator. Expect
  some audio stutter in heavy scenes.

!!! warning "Pausing during a Dreamcast session"
    GGPO can't pause cleanly. Pressing `MENU` shows only **Leave netplay?**,
    and the other player's game waits while it's open. Press `B` to continue
    or `A` to leave. If you don't answer within **20 seconds**, you leave
    automatically. Putting the device to sleep also leaves the session. The
    other player sees **Netplay ended** straight away.

If the two devices' saves don't match (for example a card copied by hand),
the session refuses to start rather than going out of sync, and shows
**Netplay failed**.
