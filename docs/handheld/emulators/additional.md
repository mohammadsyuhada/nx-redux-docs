# Additional Emulators

Some emulators are not bundled with NX Redux but can be added as community
paks. Install one by hand:

- Copy the pak into the `Emus` folder on your SD card, following the pak's
  own installation steps. If they say to place it inside a platform subfolder
  (e.g. `Emus/tg5040/MyEmu.pak`), do that.

See [Installing community paks](../apps/tools.md#installing-community-paks)
for the platform folder name per device.

??? info "More detail"
    The platform-subfolder layout is supported. For paks that reference the
    platform path internally, it's required.

!!! warning "Community paks target NextUI"
    These paks are built for **NextUI** (which NX Redux is based on), **not**
    for NX Redux. They will generally work, but they are not developed,
    maintained, or supported for NX Redux. Please **do not** report issues you
    hit on NX Redux to their developers: they build for NextUI and cannot help
    with NX Redux-specific behavior.

!!! note "Naming"
    Give your pak its own name. NX Redux always uses the emulators and tools it
    ships, so a pak in `/Emus` or `/Tools` with the same name as a shipped one
    is ignored.
