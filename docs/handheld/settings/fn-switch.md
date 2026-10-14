# FN Switch

Choose what flipping the **FN switch** does. Treat it as a night-mode
profile: a quiet, dim setup for late-night play, or just LEDs off. Flipping
the switch on applies everything you pick here at once; flipping it back
reverts it. Any row left at `Unchanged` is not touched.

For turbo fire or a joystick-style D-pad, use
[Emulator Shortcuts](emulator-shortcuts.md).

![FN switch settings](../../assets/screenshots/set-fn.png)

| Setting | While the switch is on | Values |
| --- | --- | --- |
| **Volume when FN is on** | Speaker volume. Default `Muted`. | `Unchanged`, `Muted`, `5%`–`100%` |
| **FN switch disables LED** | Also turn the LEDs off. | `Off`, `On` |
| **Brightness when FN is on** | Display brightness. | `Unchanged`, `0`–`10` |
| **Color temperature when FN is on** | Color temperature. *(Hardware-dependent.)* | `Unchanged`, `0`–`40` |
| **Contrast when FN is on** | Contrast enhancement. *(Hardware-dependent.)* | `Unchanged`, `-4`–`5` |
| **Saturation when FN is on** | Saturation enhancement. *(Hardware-dependent.)* | `Unchanged`, `-5`–`5` |
| **Exposure when FN is on** | Exposure enhancement. *(Hardware-dependent.)* | `Unchanged`, `-4`–`5` |
| **Reset to defaults** | Resets all options on this page to their default values. | |

??? info "More detail: FN switch and the OSD Mute toggle"
    The FN switch and the [OSD](../guide/osd.md) **Mute** toggle are
    separate things.

    - **OSD Mute** is a speaker mute only. It silences the audio output,
      changes nothing else, and doesn't depend on the FN switch. Press
      either volume key to unmute; that press also steps the volume.
    - **Volume when FN is on** is part of the FN profile, not the OSD mute.
