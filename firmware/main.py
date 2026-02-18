import board
# import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.mouse_keys import MouseKeys
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
mouse = MouseKeys()
encoder_handler = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 250
keyboard.modules.append(MouseKeys())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())
keyboard.modules.append(tapdance)

# R0 - R5
keyboard.row_pins = (board.GP22, board.GP19, board.GP18, board.GP17, board.GP16, board.GP11)
# C0 - C16
keyboard.col_pins = (board.GP12, board.GP13, board.GP14, board.GP15, board.GP20, board.GP21, board.GP2, board.GP1, board.GP0, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

_______ = KC.TRNS
xxxxxxx = KC.NO
xxxx = KC.NO
Fn = KC.MO(1)

RSW = KC.TD(Fn, KC.MUTE)
LOCKTD = KC.TD(KC.NO, KC.MACRO(Press(KC.LGUI), Delay(100), Tap(KC.L), Release(KC.LGUI)))
text = KC.TD(KC.NO, KC.MACRO(custom, Tap(KC.ENTER)))
RMB = KC.TD(KC.MACRO(Release(KC.MB_RMB)), KC.MACRO(Press(KC.MB_RMB)),)

F1 = KC.TD(KC.F1, KC.MPRV)
F2 = KC.TD(KC.F2, KC.MPLY)
F3 = KC.TD(KC.F3, KC.MNXT)

WAVE = KC.MACRO(Tap(KC.DOT), Delay(100), Tap(KC.N1))
GD = KC.MACRO(Tap(KC.E), Tap(KC.T), Tap(KC.Q), Tap(KC.Y), Tap(KC.R))
WAVEGD = KC.TD(WAVE, GD)

FPS = KC.MACRO(Press(KC.LSFT), Delay(100), Tap(KC.F5), Release(KC.LSFT))
PING = KC.MACRO(Press(KC.LCTRL), Press(KC.LSFT), Press(KC.F7), Release(KC.LCTRL), Release(KC.LSFT), Release(KC.F7))
FPSPING = KC.TD(FPS, PING)

keyboard.keymap = [
    # Base (Layer 0)
    [
        KC.ESC,   F1,      F2,    F3,      KC.F4, KC.F5, KC.F6,    KC.F7, KC.F8, KC.F9,    KC.F10,  KC.F11,    KC.F12,   KC.PSCR,  KC.PAUS, KC.DEL,   RSW,
        KC.GRAVE, KC.N1,   KC.N2, KC.N3,   KC.N4, KC.N5, KC.N6,    KC.N7, KC.N8, KC.N9,    KC.N0,   KC.MINUS,  KC.EQUAL, xxxxxxx,  KC.BSPC, KC.HOME,  KC.MUTE,
        KC.TAB,   xxxxxxx, KC.Q,  KC.W,    KC.E,  KC.R,  KC.T,     KC.Y,  KC.U,  KC.I,     KC.O,    KC.P,      KC.LBRC,  KC.RBRC,  KC.BSLS, KC.PGUP,  LOCKTD,
        KC.CAPS,  xxxxxxx, KC.A,  KC.S,    KC.D,  KC.F,  KC.G,     KC.H,  KC.J,  KC.K,     KC.L,    KC.SCOLON, KC.QUOTE, KC.ENTER, KC.NO,   KC.PGDN,  WAVEGD,
        xxxxxxx,  KC.LSFT, KC.Z,  KC.X,    KC.C,  KC.V,  KC.B,     KC.N,  KC.M,  KC.COMMA, KC.DOT,  KC.SLASH,  xxxxxxx,  KC.RSFT,  KC.UP,   KC.END,   FPSPING,
        KC.LCTRL, KC.LGUI, xxxx,  KC.LALT, xxxx,  xxxx,  KC.SPACE, xxxx,  xxxx,  xxxxxxx,  KC.RALT, Fn,        KC.RCTRL, KC.LEFT,  KC.DOWN, KC.RIGHT, xxxxxxx,
    ],
    # Fn (Layer 1)
    [
        xxxxxxx, xxxxxxx, xxxxxxx,  xxxxxxx,  xxxxxxx,  xxxxxxx,   xxxxxxx,  xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,  xxxxxxx, xxxxxxx, KC.NLCK, KC.SLCK, KC.INS,  _______,
        _______, _______, _______,  _______,  _______,  _______,   _______,  _______, _______, _______, _______,  _______, _______, _______, _______, _______, _______,
        _______, _______, _______,  KC.MS_UP, _______,  KC.MB_LMB, KC.MW_UP, _______, _______, _______, _______,  _______, _______, _______, _______, _______, _______,
        _______, _______, KC.MS_LT, KC.MS_DN, KC.MS_RT, KC.MB_RMB, KC.MW_DN, _______, _______, _______, _______,  _______, _______, _______, _______, _______, text,
        _______, _______, _______,  _______,  _______,  _______,   _______,  _______, _______, _______, _______,  _______, _______, _______, _______, _______, _______,
        _______, _______, _______,  _______,  _______,  _______,   _______,  _______, _______, _______, _______,  _______, _______, _______, _______, _______, RMB,
    ]
]

# volume knob
encoder_handler.pins = ((board.GP26, board.GP27),)
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),), # Volume
    ((KC.BRID, KC.BRIU),), # Brightness (Fn)
    ]

# RPi Pico GP25 LED
'''
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT
led.value = True
'''

if __name__ == '__main__':
    keyboard.go()
