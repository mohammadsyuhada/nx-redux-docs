# About

**Tools → Settings → About** shows the app's version and your device's
details. The rows are read-only.

![Settings, with About open beside the sections](../assets/screenshots/mobile/settings-about.webp){ .nx-wide }

| Row | What it shows |
| --- | --- |
| **NX Redux** | The app's version, with its build number in brackets |
| **Build** | The commit the app was built from |
| **Released** | The date of that commit |
| **Platform** | The Android version and its API level |
| **Device** | The phone's maker and model |
| **Chip** | The phone's processor |
| **GPU** | The graphics chip |
| **Page size** | The memory page size, e.g. 4 KB |
| **Font** | The font the app uses, MiSans by Xiaomi. See [Licenses](../reference/licenses.md#fonts) |

??? info "More detail"
    - **GPU** reads **…** for a moment while the app asks for it.
    - **Font** credits MiSans as its license asks.
    - A row the app can't read shows **Unknown**.

## Copy device info

Select **Copy device info** and press `A` **Copy**, then paste the text into
a bug report so the details are exact.

??? info "More detail"
    It copies every row but **Font**, as text. The app shows "Device info
    copied".
