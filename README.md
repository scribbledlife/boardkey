# Boardkey

A custom 75% (84+5+1) ANSI mechanical keyboard powered by a Raspberry Pi Pico running KMK firmware.

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

- Case: 
- Plate: 
- Switches: 
- Keycaps: 
- Stabilizers: 
- PCB: handwired 

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


## Thanks / Inspiration

- Huge shoutout to the KMK community
- Linus Tech Tips
- Hack Club Community for the inspiration and help

