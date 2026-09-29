# Audio

Sound output and sample rates. NX Redux negotiates the sample rate with whatever
output is active: 48 kHz on the speaker, the negotiated Bluetooth rate, or a
USB DAC's supported rates.

- It uses high-quality in-app resampling instead of silent low-quality system
  resampling.
- Hot-plugging a USB-C DAC or connecting Bluetooth mid-playback reroutes audio
  automatically.
- A headphone icon appears in the status bar while an external output is
  active.

![Audio settings](../../assets/screenshots/settings-audio.png)

## Output

The current audio sink and its sample rate, live. For example
`Speaker – 48000 Hz`, or your DAC/Bluetooth device when connected.

## Volume

Master volume.

## Rate negotiation

`Auto` negotiates the best rate with the active output; forcing 48 kHz is
the escape hatch if a device misbehaves.

## Bluetooth max sampling rate

Caps the sample rate used for Bluetooth audio.
