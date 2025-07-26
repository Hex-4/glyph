print("[glyph](left) hardware v1, firmware v1 by hex4")
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

from kmk.modules.split import Split, SplitSide, SplitType
from kmk.extensions.rgb import AnimationModes

keyboard = KMKKeyboard()
rgb = RGB(pixel_pin=board.GP16,
        num_pixels=6,
        animation_speed=3,
        animation_mode=AnimationModes.SWIRL,
        
        )
keyboard.extensions.append(rgb)


encoder_handler = EncoderHandler()


holdtap = HoldTap()



keyboard.modules.append(Layers())

thumbstick = Thumbstick(
        x_pin = (board.GP26),
        y_pin = (board.GP27),
        button_pin = (board.GP22),
        directional_inputs = [KC.MO(1)],
        button_input = KC.SPACE, # Placeholder
        combine_inputs=False,
        )

split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_side=SplitSide.LEFT,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
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



# keyboard.modules.append(split)

keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,)
keyboard.row_pins = (board.GP10, board.GP11, board.GP12,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
encoder_handler.pins = ((board.GP18, board.GP19, board.GP20,),) # D18 and 19 are not connected


keyboard.keymap = [ # Base Layer
    [KC.GRV, KC.Q, KC.W, KC.E, KC.R, KC.T,
     KC.TAB, KC.A, KC.S, KC.D, KC.F, KC.G,
     KC.ESC, KC.Z, KC.X, KC.C, KC.V, KC.B], # Number Layer
    [KC.NO, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5,
     KC.NO, KC.EXCLAIM, KC.AT, KC.HASH, KC.DOLLAR, KC.PERCENT,
     KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO], # Special Layer
    [KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
     KC.NO, KC.LBRC, KC.RBRC, KC.LPRN, KC.RPRN, KC.SLASH,
     KC.NO, KC.LGUI, KC.NO, KC.NO, KC.COLON, KC.SCOLON]
]                  

encoder_handler.map = [ ((KC.NO, KC.NO, KC.HT(KC.SPACE, KC.LSFT),),), # Base
                        ((KC.NO, KC.NO, KC.HT(KC.SPACE, KC.LSFT),),), # Number
                        ((KC.NO, KC.NO, KC.HT(KC.SPACE, KC.LSFT),),), # Special
                        ]

if __name__ == '__main__':
    keyboard.go()
