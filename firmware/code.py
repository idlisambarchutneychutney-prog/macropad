import board
import busio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.pegasus_oled_display import Oled, OledDisplayMode, OledData
from kmk.modules.macros import Macros, Delay

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4, board.D5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.D6, board.D7, None),) 
keyboard.modules.append(encoder_handler)

i2c = busio.I2C(board.SCL, board.SDA)
oled_ext = Oled(
    OledData(
        corner_one="ehehehe!!", 
        corner_two="",
        corner_three="",
        corner_four="",
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False
)
keyboard.extensions.append(oled_ext)


COPY = KC.LCTRL(KC.C)
PASTE = KC.LCTRL(KC.V)
UNDO = KC.LCTRL(KC.Z)

GITHUB = KC.MACRO(KC.LGUI(KC.R), Delay(500), "https://github.com")
VSCODE = KC.MACRO(KC.LGUI(KC.R), Delay(500), "code")
CHROME = KC.MACRO(KC.LGUI(KC.R), Delay(500), "chrome")

SHUTDOWN = KC.MACRO(KC.LGUI(KC.R), Delay(500), "shutdown /s /t 0\n")
RESTART = KC.MACRO(KC.LGUI(KC.R), Delay(500), "shutdown /r /t 0\n")
LOCK = KC.LGUI(KC.L)

keyboard.keymap = [
    [
        COPY,     PASTE,   UNDO,
        GITHUB,   VSCODE,  CHROME,
        SHUTDOWN, RESTART, LOCK,
    ]
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),)
]

if __name__ == '__main__':
    keyboard.go()