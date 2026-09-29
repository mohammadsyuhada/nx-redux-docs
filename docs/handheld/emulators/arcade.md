# Arcade (FBNeo)

Arcade games run on the bundled **FBNeo** core and need more care than
console ROMs: the files are zips with cryptic databases names, they must
not be renamed, and some games need extra support files.

## Where games go

Put your game zips straight into:

```
Roms/Arcade (FBN)/
├── dino.zip
├── mslug.zip
├── neogeo.zip      ← BIOS set, next to the games
└── sf2.zip
```

## Never rename the zips

FBNeo identifies a game by its **zip filename** (the MAME-style short name,
e.g. `sf2` = Street Fighter II) and by the ROM files inside it. Renaming
`sf2.zip` to `Street Fighter II.zip` breaks the game entirely.

You don't need to rename them for readable names either: the game list shows
each zip's **full title** from FBNeo's own game database, without the
revision or region details (`mslug.zip` shows as *Metal Slug - Super
Vehicle-001*, `sf2ce.zip` as *Street Fighter II': Champion Edition*). Zips
the database doesn't know keep their filename.

To pick your own name, use **Rename Rom** in the
[context menu](../guide/context-menu.md) or a
[`map.txt`](../guide/main-menu.md#custom-display-names-maptxt); your name
always wins over the database title:

```
Roms/Arcade (FBN)/map.txt:

mslug.zip	Metal Slug
sf2.zip	Street Fighter II
```

(Filename, then a single **tab**, then the display name.)

### Keeping several versions of a game

Versions of the same game share one plain title: `avsp.zip` (Europe) and
`avspj.zip` (Japan) are both *Alien vs. Predator*. You can keep both in the
folder, for example the English set for RetroAchievements and the Japanese
one for gameplay. The game list tells them apart with the detail the
title leaves out, shown dimmed after it:

- **Region** when each version is from a different one: *Alien vs.
  Predator (Europe)* and *Alien vs. Predator (Japan)*.
- The **full version detail** from FBNeo's database when regions repeat or
  are missing: *Street Fighter II': Champion Edition (Japan 920322)* and
  *(Japan 920513)*, *1942 (Revision B)* and *(Revision A)*.
- A version with no detail at all (usually the parent set) keeps the plain
  title, and the others get theirs.
- If nothing else tells them apart, the **zip name** goes in brackets:
  *Virtua Tennis 2 (vtennis2)* and *Virtua Tennis 2 (vtenis2c)*.

Versions with different titles, like *Cadillacs and Dinosaurs* (`dino`) and
*Cadillacs: Kyouryuu Shin Seiki* (`dinoj`), simply show those titles. A
**Rename Rom** or `map.txt` name still wins over all of this.

![Arcade game list with two versions of Alien vs. Predator and of 1942](../../assets/screenshots/arcade-clone-names.png)

## Romset version matters

FBNeo only loads zips that match its own ROM database — sets built for
MAME or for a different FBNeo version often fail with missing/bad ROM
errors. Use a **FBNeo romset**, and prefer **non-merged** sets (each zip
self-contained); with split/merged sets, a clone needs its **parent** zip
in the same folder.

## BIOS sets (neogeo.zip and friends)

Games on BIOS-based boards need the board's BIOS zip **in the same folder
as the game** — most commonly `neogeo.zip` for Neo Geo titles (Metal Slug,
KOF, …). The BIOS zip is part of the romset, and its version must match
too. BIOS zips (`neogeo.zip`, `pgm.zip`, …) are **hidden from the game
list automatically**, so they don't show up as unplayable entries. To show
one anyway, give it an alias in `map.txt`.

## Sound samples

A few classics (mostly pre-1990) play some or all of their audio from
**sample packs**. FBNeo looks for them under the system's BIOS folder:

```
Bios/FBN/fbneo/samples/<game>.zip
```

Games run without samples — those sounds are just missing or replaced by
approximations.
