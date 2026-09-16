# Xtras Store

**Tools → Xtras** is an on-device add-on store for optional games and tools
that are not part of the core install. Browse the **GAMES** and **TOOLS** tabs
(`Left` / `Right` to switch), press `A` for details, and install or update
right from the device.

![Xtras store](../assets/screenshots/xtras.png)

The **TOOLS** tab holds installable tools and emulators — already-installed
entries are grouped under an *Installed* header:

![Xtras TOOLS tab](../assets/screenshots/xtras-tools.png)

Installed entries show up in your regular menus — a game appears in **Xtra
Games**, a tool appears in [Tools](tools.md). When an update is available, the
store labels the entry accordingly.

!!! note "The catalog grows"
    More standalone games and tools will be added to Xtras over time — check
    back after updating NX Redux.

## PSP emulator

**PSP (PPSSPP)** installs
[ben16w's community PSP.pak](https://github.com/ben16w/minui-psp) directly
on-device (~31 MB download) — no computer needed. It lands unmodified in
the pak's own `Emus/<platform>/PSP.pak` location, exactly as a manual
install would. Put your games in `Roms/Sony Playstation Portable (PSP)`
afterwards. Community-pak [support notes](../emulators/additional.md)
apply.

## Pokémon Gen1Recomp

**Pokemon Gen1Recomp++** in the **GAMES** tab installs
[bryanthaboi/gen1recomp](https://github.com/bryanthaboi/gen1recomp), a
native LÖVE2D recreation of Pokémon Red, Blue, Yellow, Gold, Silver and
Crystal, together with three bundled mods: Stadium battle effects, Running
Shoes and Wilds of Kanto. The 3D voxel overworld mods offered in its mod
browser need far more memory than these 1 GB devices have, so they are
not bundled and not recommended. You supply your own US
cartridge ROMs in `Roms/Game Boy` or `Roms/Game Boy Color`; the installer
copies recognised dumps into the game for you (Crystal 1.0 must be copied
by hand, only the 1.1 dump is recognised).

The game opens on its own launcher (ROM import, mods, saves). It is built
for a mouse pointer, so on a handheld it works like this:

| Button | Action |
|---|---|
| D-pad, A | Move between controls and select |
| L1 / R1 | Previous / next tab |
| L2 / R2 | Scroll lists up / down |
| Y | Switch between menu navigation and a free pointer cursor |
| Select | Open the on-screen keyboard (search, names, URLs) |
| Start | Play the selected version |

## PortMaster

[PortMaster](https://portmaster.games/) — the community launcher for game
ports — is the flagship entry in the **TOOLS** tab. Once installed it
appears in the Tools menu; see the dedicated
[PortMaster page](portmaster.md) for how it works.
