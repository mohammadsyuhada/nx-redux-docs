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

To get readable names in the game list, use a
[`map.txt`](../guide/main-menu.md#custom-display-names-maptxt) instead —
this is the intended way for arcade folders:

```
Roms/Arcade (FBN)/map.txt:

dino.zip	Cadillacs and Dinosaurs
mslug.zip	Metal Slug
sf2.zip	Street Fighter II
```

(Filename, then a single **tab**, then the display name.)

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
too. You can hide it from the game list with a dot alias in `map.txt`:

```
neogeo.zip	.hidden
```

## Sound samples

A few classics (mostly pre-1990) play some or all of their audio from
**sample packs**. FBNeo looks for them under the system's BIOS folder:

```
Bios/FBN/fbneo/samples/<game>.zip
```

Games run without samples — those sounds are just missing or replaced by
approximations.
