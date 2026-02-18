# Boardkey

A custom 75% (84+5+1) mechanical keyboard powered by a Raspberry Pi Pico running KMK firmware.

## About

**boardkey** is a compact custom mechanical keyboard with the popular 75% layout extended with extra macro keys and a rotary encoder.

- **Layout**: 75% ANSI  
- **Total keys**: 90 (84 regular + 5 macro + 1 encoder switch)  
- **Microcontroller**: Raspberry Pi Pico  
- **Firmware**: KMK (Python-based, very flexible)

### Key breakdown
- 84 regular ANSI keys  
- 5 programmable macro/layer keys  
- 1 rotary encoder with integrated push switch

<img width="617" height="227" alt="image" src="https://github.com/user-attachments/assets/ebe9ac20-3f3f-4219-9648-1942e0134938" />

## Special Keys & Features

### Media Controls
- **Double tap F1** → Previous track  
- **Double tap F2** → Play / Pause  
- **Double tap F3** → Next track  

### Rotary Encoder
- **Turn left/right** → Volume Down / Volume Up  
- **Press + turn** → Brightness Down / Brightness Up  
- **Double press** → Mute / Unmute  

*(All of these are easily customizable in the `kb.py` / `main.py` KMK keymap file.)*

## Build details (optional sections you can expand)

- Case: 3D Printed, and looks like the following -

<img width="622" height="206" alt="image" src="https://github.com/user-attachments/assets/a8fc2286-d797-4419-92e8-9ef8c927d5d0" />

<img width="619" height="256" alt="image" src="https://github.com/user-attachments/assets/cc15ee15-985f-4309-b04d-d2f34c0025f0" />

- Plate: Looks like this

<img width="619" height="455" alt="image" src="https://github.com/user-attachments/assets/00875b87-6efc-4760-b83e-27613c728036" />

- Switches: Gateron Milky Yellows
- Keycaps: PBT Keycaps
- Stabilizers: 2u and 6.25u Stabilizers
- PCB:

<img width="605" height="245" alt="image" src="https://github.com/user-attachments/assets/4c8a8589-9770-48e2-9aba-3b216bbe7665" />

## Firmware

Firmware is written in CircuitPython using the excellent [KMK](https://github.com/KMKfw/kmk_firmware) framework.

Main features currently implemented:
- Layer switching
- Media keys via tap dance
- Rotary encoder volume & brightness control
- Macro keys (fully programmable)

To flash / edit:
1. Put the Pico into bootloader mode
2. Drag the KMK CircuitPython UF2 onto it
3. Edit `kb.py` and/or `keymaps/default.py`
4. Save → it auto-reloads

## Gallery

For more images, please go to the images folder, and if you want to see the materials, you can go to 

## Thanks / Inspiration

- Huge shoutout to the KMK community
- Linus Tech Tips
- Hack Club Community for the inspiration and help

