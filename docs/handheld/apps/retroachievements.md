# RetroAchievements

NX Redux supports [RetroAchievements](https://retroachievements.org/) with
**full offline support**. The **RetroAchievements** tool in Tools is the single
home for the feature: sign in, browse your achievements and manage every
setting here.

![RetroAchievements tool](../../assets/screenshots/retroachievements.png)

The home screen shows your account at a glance: points, unlocks waiting to
be synced, and when the last sync happened. Below that are four entries:
**Achievements**, **Sync now**, **Library** and **Settings**.

??? info "More detail"
    The integration is powered by
    [rcheevos](https://github.com/RetroAchievements/rcheevos).

## Setting up

You need a free [retroachievements.org](https://retroachievements.org/)
account. Then, in **Settings**:

![RetroAchievements settings](../../assets/screenshots/ra-settings.png)

1. Set **Enable achievements** to `On`.
2. Enter your **Username** and **Password** with the on-screen keyboard.
3. Choose **Authenticate**. It tests the credentials and retrieves your API
   token. **Status** shows `Authenticated` when it works.

Below the account block, Settings also holds:

| Setting | What it does |
| --- | --- |
| **Download all game data** | Pre-cache your whole library (see [Offline support](#offline-support)) |
| **Show notifications** and **Notification duration** | In-game unlock popups and how long they stay |
| **Progress duration** | How long progress updates (top-left) stay on screen; `Off` disables them |
| **Achievement sort order** | How achievements are sorted, both here and in the in-game menu |
| **Reset account data** | Clear login and progress, keeping cached game data (for switching accounts) |
| **Erase all achievement data** | Remove everything, including cached game data. Badges kept in your ROM folders stay |
| **Reset settings to defaults** | Put every setting back to its default |

## Earning achievements

Achievements work in the **built-in emulator cores**. Launch a recognized
game and unlocks are tracked automatically as you play. That includes the
Sega systems under `GPGX`, Dreamcast (with Naomi and Atomiswave), Nintendo
64, PSP and WonderSwan.

- An **unlock notification** pops up when you earn an achievement.
- **Progress updates** (e.g. collectible counters) appear in the top-left.
- The in-game [pause menu](../guide/playing-games.md#the-in-game-menu)'s
  **Options** gains an **Achievements** entry. Browse the game's achievements
  without leaving the game:
    - Press `Y` to filter to locked ones.
    - Press `X` to **mute** a specific achievement's notifications (handy for
      spammy progress trackers).

![In-game Achievements list for Mario Kart - Super Circuit, 0/94 unlocked](../../assets/screenshots/ra-ingame-achievements.png)

??? info "More detail: system notes"
    - **Genesis Plus GX covers every Sega system.** The alternate Sega core
      [Genesis Plus GX](../emulators/other-systems.md#sega-genesis-sega-cd-32x-master-system-game-gear-and-sg-1000)
      plays Genesis/Mega Drive, Master System, Game Gear, SG-1000 and Sega CD
      under a single `GPGX` tag. It still identifies each game with the
      correct console, by picking the system from the ROM's file extension.
    - **Dreamcast.** [Dreamcast](../emulators/dreamcast.md), Naomi and
      Atomiswave games run on a built-in core, so their achievements work
      like every other system, offline journal included.
    - **WonderSwan.** Games in the `Wonderswan Color (WSC)` folder earn
      achievements on the built-in core. If you installed the WonderSwan pak
      from the Pak Store before, it keeps priority over the built-in one;
      delete it from `Emus/` to switch. Your saves stay where they are.
    - **Nintendo DS** runs on the standalone DraStic emulator, which has no
      achievements support.

!!! info "Softcore only, by design"
    NX Redux is not an RA-approved hardcore emulator, so hardcore mode is
    intentionally omitted to keep your account safe. Unlocks are submitted
    as softcore.

## Offline support

Everything is built to work without a connection:

| Feature | What it does |
| --- | --- |
| **Earn offline** | Unlocks are journaled to the SD card and submitted automatically once you're back online (the home screen counts "unlocks waiting") |
| **Connection drops** | An unlock earned while the connection is down, for example right after waking from sleep, is journaled too, so it isn't lost if you quit before WiFi comes back. The popup reads *RetroAchievements: offline, unlocks will sync later* |
| **Slow WiFi at launch** | If WiFi isn't ready when a game starts (such as a game resumed after the device powered off in sleep), the login keeps retrying for a few seconds, then the game continues offline from the cache |
| **Cached game data** | Achievement definitions, unlock state and badges are cached as you play, so a game you've launched once keeps working offline |
| **Pre-download** | **Download all game data** caches achievement data for every game in your library, with a live progress bar. Even games you have *never* launched online then work offline. **Library** does the same one console at a time (see below). Zipped (`.zip`/`.7z`) ROMs are unpacked for a moment to identify the game inside |

??? info "More detail: where the cache lives"
    - Each console folder keeps a `.retroachievements` folder: `hashes.json`
      remembers each ROM's fingerprint, so a game isn't re-identified on every
      launch, and `badges/<game id>/` holds that game's badge pictures.
    - Achievement definitions and your account data stay in
      `.userdata/shared/.ra/`.
    - [Device Sync](device-sync.md) with ROMs on carries the
      `.retroachievements` folders along.

??? info "More detail: Dreamcast and multi-disc games"
    - Pre-download includes Dreamcast folders. Disc images (`.chd`, `.gdi`,
      `.cdi`, `.cue`) and Naomi/Atomiswave sets (`.zip`) are identified the
      same way the Dreamcast core does it.
    - Multi-disc games (PlayStation, Dreamcast) are covered too. Every disc is
      cached so any disc is recognised offline, and the game shows up once in
      the browser.

## Library

**Library** lists every console you have games for that RetroAchievements
supports, for example *Game Boy (GB)*. The count next to each one shows how
many of its games are done: their achievement data is cached, or they turned
out not to be in RetroAchievements.

- `A` downloads the achievement data for the selected console only. This is
  the quick way through a large library.
- `Y` downloads it for every console, the same as **Download all game data**.

Each download shows a progress bar and can be cancelled with `B`. Games
already cached are skipped, so running it again only fetches what's missing.

## Browsing your achievements

**Achievements** lists every cached game with box art and unlock progress,
fully offline:

![RetroAchievements Games list with 1942, Alleyway, Astro Boy and Batman Returns](../../assets/screenshots/ra-games.png)

Open a game to see its achievements, each with its badge, status and
points. Unlocked, pending-sync and locked achievements are all here, in your
chosen sort order:

![1942's achievements, each locked at 5 points](../../assets/screenshots/ra-game-detail.png)

Press `A` for the full details of an achievement: badge, description,
points, global unlock rate, and type tags like `[Missable]`,
`[Progression]` or `[Win Condition]`:

![Details for the 1942 achievement Midway](../../assets/screenshots/ra-achievement-details.png)

## Syncing

Offline unlocks sync automatically, in the background, when WiFi is
connected:

- when a game logs in online,
- when you open the in-game menu during an offline session,
- when you quit a game.

Nothing checks the connection while you play. A *N offline achievements
synced* popup confirms it. If none of these get through, the unlocks wait
for the next launch or for **Sync now**. An unlock for an achievement that
has since been removed from RetroAchievements is dropped instead of retried
forever.

**Sync now** on the home screen does two things in one go:

1. **Push**: submits any offline unlocks still waiting.
2. **Pull**: refreshes your cloud status, meaning the points total and the
   unlock state of every cached game. Achievements earned on another device or
   on the website show up here too. Games whose progress changed on the server
   are re-fetched.

Both steps show the same progress bar as **Download all game data**. Press
`B` to cancel. Unsent unlocks stay queued for the next sync, and games
already refreshed are kept.

The home screen's points, "unlocks waiting" and "Last sync" tell you where
you stand.
