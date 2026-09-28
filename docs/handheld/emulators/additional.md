# Additional Emulators

Some emulators are not bundled with NX Redux but can be added.

- **PPSSPP** (PlayStation Portable) — easiest via the
  [Xtras store](../apps/xtras.md#psp-emulator)'s **PSP (PPSSPP)** entry,
  which installs [ben16w/minui-psp](https://github.com/ben16w/minui-psp)
  directly on-device.

For any other system, install a community pak by hand: copy the pak into
the `Emus` folder on your SD card, following the pak's own installation
steps — if they say to place it inside a platform subfolder (e.g.
`Emus/tg5040/PSP.pak`), that layout is supported and, for paks that
reference the platform path internally, required. See
[Installing community paks](../apps/tools.md#installing-community-paks) for
the platform folder name per device.

!!! warning "Community paks target NextUI"
    These paks are built for **NextUI** (which NX Redux is based on), **not**
    for NX Redux. They will generally work, but they are not developed,
    maintained, or supported for NX Redux. Please **do not** report issues you
    hit while using them on NX Redux to their developers — those developers
    build for NextUI and cannot help with NX Redux-specific behavior.

!!! note "Naming"
    Do not give your own pak the same name as one shipped with NX Redux —
    same-named paks in `/Emus` and `/Tools` are treated as NX Redux leftovers
    and are removed on every update.
