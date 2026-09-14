# Bluetooth

Bluetooth pairing. A connected audio device takes over sound output
automatically — see [Audio](audio.md). The [OSD](../guide/osd.md) has a
quick Bluetooth toggle too.

![Bluetooth settings](../assets/screenshots/set-bluetooth.png)

## Bluetooth

Enable or disable Bluetooth.

## Bluetooth diagnostics

Extra Bluetooth logging for troubleshooting.

## Device list

With Bluetooth on, discovered devices appear below — select one to pair
and connect.

## Under the hood

The stock TrimUI firmware ships an old Bluetooth stack. When NX Redux is
installed from a full release zip, the first boot replaces it with newer
builds on the device's system partition (see
[Getting Started](../getting-started.md#installing)):

| Component | Version |
| --- | --- |
| BlueZ (`bluetoothd`, `bluetoothctl`, `btmon`, …) | 5.78 |
| bluez-alsa (`bluealsa`, ALSA plugins) | 4.1.0 |
| SBC codec (`libsbc`) | 2.1 |

This is what makes the audio routing and pairing described above reliable.
The upgrade applies once per device and survives later updates, whether
over the air or by copying `MinUI.zip`. To check it is present, look for
`/usr/lib/libsbc.so.1.3.1` on the device (for example with the
[Files](../apps/files.md) app) — the installer uses that file as its
"already upgraded" marker.
