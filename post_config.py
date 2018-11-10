from config import *

# WS2813
STRIP_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
STRIP_DMA        = 10       # DMA channel to use for generating signal (try 5)
STRIP_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
STRIP_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
if (STRIP_LIBRARY == STRIP_LIBRARY_WS2813):
	from neopixel import ws
        STRIP_TYPE           = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

