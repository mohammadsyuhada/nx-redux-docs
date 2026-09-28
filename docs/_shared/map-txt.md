To rename games without touching the files, drop a `map.txt` inside the
system folder. Each line maps a **filename** to a display name, separated
by a single **tab**:

```
Roms/Game Boy Advance (GBA)/map.txt:

Advance Wars 2 - Black Hole Rising (USA).gba	Advance Wars 2
Legend of Zelda, The - The Minish Cap (USA).gba	Zelda: Minish Cap
```

The list re-sorts by the new display names. Since the files themselves are
untouched, save files, states and box art all stay matched. An alias starting
with a dot (e.g. `Track01.bin	.hidden`) **hides** the entry from the list
entirely.

A `map.txt` at the top level (`Roms/map.txt`) does the same for the
**system folders** — an alternative to renaming the folders themselves.
