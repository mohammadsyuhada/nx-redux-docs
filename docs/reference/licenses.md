# Licenses

The license NX Redux is distributed under, and the licenses of the emulators,
libraries, fonts and art it includes, on the handheld and on mobile.

<!-- Publish with the mobile release that ships the licences branch (licence
     texts in the APK, MiSans fetched at build time, the About Font row), and
     once nx-redux ships each core's licence text in its pak. Until then the
     "Where to find the full texts" section is ahead of both platforms. -->

## NX Redux

NX Redux is free software under the **GNU General Public License v3.0**, on
the handheld and on mobile. You can use, study, change and share it, and any
copy you share, changed or not, must stay under the same license with its
source available.

- Handheld: [source and LICENSE](https://github.com/mohammadsyuhada/nx-redux)
- Mobile: [source and LICENSE](https://github.com/mohammadsyuhada/nx-mobile)

On mobile, NX Redux's emulator runner is a fork of
[LibretroDroid](https://github.com/Swordfish90/LibretroDroid) by Filippo
Scognamiglio, also GPL-3.0.

## Emulators

Each emulator keeps its own license. Most are GPL or another open-source
license. Four are **non-commercial**: they may not be sold or used in a
commercial product.

| Emulator | Systems | License | In |
| --- | --- | --- | --- |
| a5200 | Atari 5200 | GPL-2.0 | Both |
| blueMSX | MSX | zlib-style, with GPL parts | Handheld |
| Caprice32 (cap32) | Amstrad CPC | GPL-2.0 | Handheld |
| DraStic | Nintendo DS | Closed-source freeware | Handheld |
| FAKE-08 | PICO-8 | MIT | Both |
| FB Neo | Arcade | **Non-commercial** (FB Neo license) | Both |
| FCEUmm | NES, Famicom Disk System | GPL-2.0 | Both |
| Flycast | Dreamcast, NAOMI, Atomiswave | GPL-2.0 or later | Both |
| Gambatte | Game Boy, Game Boy Color | GPL-2.0 | Both |
| Gearcoleco | ColecoVision | GPL-3.0 | Both |
| Genesis Plus GX | Mega Drive / Genesis, Master System, Game Gear, SG-1000, Sega CD (mobile); the GPGX folder (handheld) | **Non-commercial** (Genesis Plus GX license) | Both |
| gpSP | Game Boy Advance | GPL-2.0 | Both |
| Handy | Atari Lynx | zlib | Both |
| Beetle PCE Fast | PC Engine | GPL-2.0 | Both |
| Beetle Supafaust | Super Nintendo (SUPA) | GPL-2.0 | Both |
| Beetle VB | Virtual Boy | GPL-2.0 | Both |
| Beetle WonderSwan | WonderSwan Color | GPL-2.0 | Both |
| melonDS DS | Nintendo DS | GPL-3.0 | Mobile |
| mGBA | Game Boy Advance, Super Game Boy | MPL-2.0 | Both |
| Mupen64Plus | Nintendo 64 | GPL-2.0 | Both |
| PCSX ReARMed | PlayStation | GPL-2.0 | Both |
| PicoDrive | 32X; on the handheld also Mega Drive / Genesis, Master System, Game Gear, SG-1000, Sega CD | **Non-commercial** (PicoDrive license) | Both |
| PokeMini | Pokémon mini | GPL-3.0 | Both |
| PPSSPP | PSP | GPL-2.0 or later | Both |
| PrBoom | Doom | GPL-2.0 | Both |
| ProSystem | Atari 7800 | GPL-2.0 | Both |
| PUAE | Amiga | GPL-2.0 | Handheld |
| RACE | Neo Geo Pocket, Neo Geo Pocket Color | GPL-2.0 | Both |
| Snes9x | Super Nintendo | **Non-commercial** (Snes9x license) | Both |
| Stella 2014 | Atari 2600 | GPL-2.0 | Both |
| VICE | Commodore 64, 128, VIC-20, PET, Plus/4 | GPL-2.0 | Handheld |

Where the projects change an emulator's source, the changes are published in
their repositories as patch files under that emulator's license.

### No donations

FB Neo's license forbids asking for donations to support work on any project
that uses FB Neo's source code. NX Redux ships FB Neo, so **NX Redux does
not ask for donations** anywhere: no sponsor buttons, no donation links, no
in-app requests. It is free and stays free.

## Libraries

On mobile, NX Redux is built on open-source libraries, including:

- **AndroidX, Jetpack Compose, Compose Multiplatform, Kotlin and kotlinx,
  SQLDelight, Coil, Okio, Guava and Accompanist**: Apache-2.0
- **Apache Commons Compress, IO, Lang and Codec**: Apache-2.0
- **XZ for Java**: 0BSD
- **oboe**: Apache-2.0
- **rcheevos** (RetroAchievements) and **libretro-common**: MIT
- **libchdr**: BSD-3-Clause, with miniz (MIT), zstd (BSD-3-Clause) and the
  LZMA SDK (public domain)

On the handheld, NX Redux inherits its libraries from NextUI and MinUI; see
[Credits](credits.md).

## Fonts

- **MiSans** (handheld and mobile), © Xiaomi, used under
  [Xiaomi's MiSans terms](https://hyperos.mi.com/font/en/download/). Software
  may embed the font as long as it notes that MiSans is used
  ([MiSans FAQ](https://hyperos.mi.com/font/en/faq/)), which NX Redux does in
  **Settings → About**. The font files may not be distributed on their own, so
  the mobile build downloads MiSans from Xiaomi rather than keeping it in the
  repository.
- **Rounded Mplus 1c** and **BPreplay** (handheld): SIL Open Font License 1.1.

## Art

- **Console overlays** (handheld and mobile): by
  [KrutzOtrem](https://github.com/KrutzOtrem/Trimui-Brick-Overlays), MIT.
- **Console logos** (mobile main menu): converted from Dan Patrick's
  [redrawn console logo set](https://archive.org/details/console-logos-professionally-redrawn-plus-official-versions). His terms: never to be sold; credit appreciated. They are
  not under the GPL.
- **Controller art** (mobile main menu): from ScreenScraper and manufacturers'
  product images.
- **Input prompts** (mobile): Kenney's
  [Input Prompts](https://kenney.nl/assets/input-prompts), CC0.
- **Shaders**: from libretro's
  [glsl-shaders](https://github.com/libretro/glsl-shaders) and sinedied's
  [perfect-retroshaders](https://github.com/sinedied/perfect-retroshaders);
  each file keeps its own license header.

Console names, logos and hardware designs are trademarks of their owners.

## Where to find the full texts

- **Mobile**: every license text ships inside the app, under
  `assets/licenses/` in the APK. The
  [repository](https://github.com/mohammadsyuhada/nx-mobile) has them in
  `LICENSES/`, with the art notes in `THIRD_PARTY_ART.md`; each emulator's
  license is copied from its source at build time.
- **Handheld**: each emulator's license text ships next to it in its `.pak`
  folder, copied from the emulator's source at build time.
