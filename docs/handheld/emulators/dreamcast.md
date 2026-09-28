# Sega Dreamcast

Dreamcast games run on a bundled standalone **Flycast** emulator. Put your
games in `Roms/DreamCast (DC)/`.

Flycast also plays the arcade boards built on Dreamcast hardware — **Sega
Naomi** and **Sammy Atomiswave** — from the same folder. See
[Arcade games](#arcade-games-naomi-atomiswave) below: unlike Dreamcast
itself, those need BIOS files.

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

## BIOS

Dreamcast runs **out of the box without a BIOS** (HLE boot). If you prefer to
boot through the real BIOS instead, drop `dc_boot.bin` into `Bios/DC/` on the
SD card.

## Arcade games (Naomi & Atomiswave)

Naomi and Atomiswave games are MAME-style zips. Put them straight into
`Roms/DreamCast (DC)/` next to your Dreamcast games and **don't rename
them** — like [FBNeo arcade zips](arcade.md), the emulator identifies a
game by its short zip name (`mslug6.zip`, not `Metal Slug 6.zip`). The game
list still shows readable names: each zip gets its **full title** from
Flycast's own game list (`ikaruga.zip` shows as *Ikaruga*, `mvsc2.zip` as
*Marvel vs. Capcom 2 New Age of Heroes*), while Dreamcast disc images keep
their filenames. A **Rename Rom** or
[`map.txt`](../guide/main-menu.md#custom-display-names-maptxt) alias always
wins over that title. A BIOS zip placed in the game folder by mistake is
hidden from the list.

Both boards **require their BIOS zip** in `Bios/DC/`:

| Board | BIOS file |
| --- | --- |
| Naomi | `naomi.zip` |
| Atomiswave | `awbios.zip` |

Without it, the game exits immediately (the log shows
`cannot load BIOS awbios` / `naomi`).

!!! note "Atomiswave BIOS: both MAME sets work"
    Either `awbios.zip` variant is accepted — the older MAME set
    (`bios0.ic23`) and the current MAME re-dump (`bios.ic23_l`).

As on the real cabinets, arcade games want coins before START works —
press **SELECT** to insert a coin.

## RetroAchievements

Flycast has its own RetroAchievements support. Sign in once in the
[RetroAchievements](../apps/retroachievements.md) tool and every Dreamcast,
Naomi and Atomiswave launch logs in with your account (it needs a network
connection at launch). Unlocks are submitted straight to the server by
Flycast, so to see them in the tool run **Download all game data** once (so
your Dreamcast games are cached) and then **Sync now**, which pulls your
points and unlock state back from the server.

Whether Flycast tracks achievements follows the tool's **Enable
achievements** setting, exactly like the built-in cores — there is no
separate per-game switch. **Hardcore Mode** is the one Flycast-specific
option: it lives in the game's [Emulator Options](../guide/emulator-options.md)
(and the in-game overlay's **RetroAchievements** section), is off by default,
and disables save states while playing.

## Netplay

Dreamcast supports **GGPO netplay** for up to 2 players — see
[Netplay](../netplay.md) for how sessions work.
