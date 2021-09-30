import time
import board
import busio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_mpr121

kbd = Keyboard(usb_hid.devices)

key_send = True

KEY_MAPPING = {
    0: Keycode.UP_ARROW ,
    1: Keycode.DOWN_ARROW ,
    2: Keycode.LEFT_ARROW ,
    3: Keycode.RIGHT_ARROW,
    4: Keycode.SPACE ,
    5: Keycode.ENTER ,
    6: Keycode.KEYPAD_PLUS ,
    7: Keycode.KEYPAD_MINUS ,
    8: Keycode.W ,
    9: Keycode.S ,
    10: Keycode.A,
    11: Keycode.D
    }

# Sleep this long between polling for events:
EVENT_WAIT_SLEEP_SECONDS = 0.01

# Create I2C bus.
i2c = busio.I2C(board.GP1, board.GP0)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)

while True:
    # Loop through all defined inputs:
    for pin, key in KEY_MAPPING.items():
        if mpr121[pin].value:
            if key_send:
                kbd.send(key)
            else:
                kbd.press(key)
        elif not key_send:
            kbd.release(key)
    time.sleep(
        EVENT_WAIT_SLEEP_SECONDS
    )  # Small delay to keep from spamming output messages.
