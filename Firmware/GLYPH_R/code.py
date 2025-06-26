print("[glyph](right) hardware v1, firmware v1 by hex4")
print("---")
print("[ OPEN SOURCE      ]")
print("{ is.gd/glyphkb    }")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.holdtap import HoldTap
from kmk.extensions.RGB import RGB
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler # why an encoder? my thumb switch is acting as an encoder but without the spinny part, just the button
from kmk.modules.thumbstick import Thumbstick
from kb import data_pin
from kmk.modules.split import Split, SplitSide

encoder_handler = EncoderHandler()

keyboard = KMKKeyboard()
holdtap = HoldTap()
rgb = RGB(pixel_pin=board.D16, num_pixels=6)
rgb.animation_mode = "rainbow"

thumbstick = Thumbstick(
        x_pin = (board.GP26),
        y_pin = (board.GP27),
        button_pin = (board.GP22),
        directional_inputs = [KC.UP, KC.RIGHT, KC.DOWN, KC.LEFT],
        button_input = KC.SPACE, # Placeholder
        combine_inputs=False,
        )

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_side=SplitSide.RIGHT,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP8,  # The primary data pin to talk to the secondary device with
    data_pin2=board.GP9,  # Second uart pin to allow 2 way communication
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)


keyboard.modules.append(holdtap)
keyboard.modules.append(encoder_handler)
keyboard.modules.append(thumbstick)
keyboard.modules.append(Layers())
keyboard.modules.append(split)

keyboard.col_pins = (board.D0,board.D1,board.D2,board.D3,board.D4,board.D5,)
keyboard.row_pins = (board.D10,board.D11,board.D12,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.D18, board.D19, board.D20,),) # D18 and 19 are not connected


keyboard.keymap = [ # Base Layer
    [KC.Y, KC.U, KC.I, KC.O, KC.P, KC.MINUS,
     KC.H, KC.J, KC.K, KC.L, KC.QUOTE, KC.ENTER,
     KC.N, KC.M, KC.COMMA, KC.DOT, KC.QUESTION, KC.EQUAL], # Number Layer
    [KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.TRNS,
     KC.CIRC, KC.AMPR, KC.ASTERISK, KC.BSLASH, KC.PIPE, KC.TRNS,
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO] # Special Layer
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.UNDERSCORE,
     KC.DQUO, KC.LABK, KC.RABK, KC.LCBR, KC.RCBR, KC.TRNS,
     KC.NO, KC.TRNS, KC.NO, KC.NO, KC.TRNS, KC.PLUS]
]

encoder_handler.map = [ ((KC.NO, KC.NO, KC.MO(2),),), # Base
                        ((KC.NO, KC.NO, KC.MO(2),),), # Number
                        ((KC.NO, KC.NO, KC.MO(2),),), # Special
                        ]

if __name__ == '__main__':
    keyboard.go()