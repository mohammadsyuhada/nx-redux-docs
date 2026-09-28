Under the hood each collection is a plain text file at
`Collections/<Name>.txt`, with one path per line, relative to the top of your
library (the SD card on a handheld). You can also build them on a computer:

```
Collections/RPG Nights.txt:

/Roms/Game Boy Advance (GBA)/Golden Sun.gba
/Roms/Sony PlayStation (PS)/Final Fantasy VII/Final Fantasy VII.m3u
```

Entries whose file is missing are silently skipped, and a
`Collections/map.txt` can alias the displayed names, in the same format as a
system folder's `map.txt`.
