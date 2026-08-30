# Sega Dreamcast

Dreamcast games run on a bundled standalone **Flycast** emulator. Put your
games in `Roms/DreamCast (DC)/`.

Flycast also plays the arcade boards built on Dreamcast hardware — **Sega
Naomi** and **Sammy Atomiswave** — from the same folder. See
[Arcade games](#arcade-games-naomi-atomiswave) below: unlike Dreamcast
itself, those need BIOS files.

## BIOS

Dreamcast runs **out of the box without a BIOS** (HLE boot). If you prefer to
boot through the real BIOS instead, drop `dc_boot.bin` into `Bios/DC/` on the
SD card.

## Arcade games (Naomi & Atomiswave)

Naomi and Atomiswave games are MAME-style zips. Put them straight into
`Roms/DreamCast (DC)/` next to your Dreamcast games and **don't rename
them** — like [FBNeo arcade zips](arcade.md), the emulator identifies a
game by its short zip name (`mslug6.zip`, not `Metal Slug 6.zip`). Use a
[`map.txt`](../guide/main-menu.md#custom-display-names-maptxt) for readable
names in the game list.

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

## Netplay

Dreamcast supports **GGPO netplay** for up to 2 players — see
[Netplay](../netplay.md) for how sessions work.
