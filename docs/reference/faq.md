# FAQ

## Can I move my SD card between devices?

No. SD cards are built per device model — resolution, OSD assets and other
layout differ between models. Use the
[Device Sync](../apps/device-sync.md) tool to carry saves, save states,
settings and (optionally) ROMs across devices.

## Something doesn't work after installing

Check your stock firmware version first. NX Redux relies on system libraries
the stock firmware ships — install the
[official TrimUI firmware](https://github.com/trimui) listed in
[Getting Started](../getting-started.md) for your device, then reinstall.

## I forgot my Simple Mode PIN

Delete `.userdata/shared/enable-simple-mode` from the SD card (from a
computer) to turn Simple Mode off.

## Where are my screenshots and recordings saved?

Screenshots go to `Images/Screenshots`, screen recordings to
`Videos/Recordings` on the SD card. See
[On-Screen Display](../guide/osd.md).

## Where are my saves?

Battery saves live in the `Saves` folder on the SD card; save states are kept
per platform under `.userdata`. **Device Sync** moves all of it between
devices for you.

## Why is there no RetroAchievements hardcore mode?

By design. NX Redux is not an RA-approved hardcore emulator, so hardcore mode
is intentionally omitted to keep your account safe — softcore unlocks work
fully, including offline. See
[RetroAchievements](../apps/retroachievements.md).

## A community pak (e.g. PPSSPP) misbehaves — where do I report it?

Not to the pak's developer — community paks are built for NextUI, not NX
Redux, and their developers cannot help with NX Redux-specific behavior. See
[Additional Emulators](../emulators/additional.md).

## How do I update NX Redux?

Use the OTA updater in [Settings → About](../settings/about.md) (needs
Wi-Fi), or copy the new release's `MinUI.zip` (without unzipping) to the
root of your SD card and boot. Bundled emulator and tool paks update
automatically either way. See
[Getting Started](../getting-started.md#updating).

## Where do I report bugs or ask questions?

On the [NX Redux GitHub repository](https://github.com/mohammadsyuhada/nx-redux)
via Issues.
