# LED Layout constants
LED_LAYOUT_BOTTOM_RIGHT = 1

# LED Libraries to use
STRIP_LIBRARY_DOTSTAR = 1
STRIP_LIBRARY_WS2813 = 2

# Amount by which colours fade per refresh interval (1 = Slowest, 255 = instant)
FADE_INCREMENT = 255

# Number of seconds to pause between cycles
REFRESH_TIME = 0.1



##############################################
# Defaults that can be overridden in config.py
##############################################
# Initial sleep in seconds
INITIAL_SLEEP = 1

# LED Layout constants
LED_LAYOUT = LED_LAYOUT_BOTTOM_RIGHT
LED_LAYOUT_OFFSET = 0
STRIP_NUMBER_OF_PIXELS = LED_LAYOUT_OFFSET + 14 * 9 - 1

# LED Strip defaults
STRIP_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest

# WS2813 Defaults
STRIP_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
STRIP_DMA        = 5       # DMA channel to use for generating signal (try 5)
STRIP_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
STRIP_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

from neopixel import ws
STRIP_TYPE           = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

