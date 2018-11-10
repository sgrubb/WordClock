'Module to handle low-level lighting of the adafruit strip'

from post_config import *

if (STRIP_LIBRARY == STRIP_LIBRARY_DOTSTAR):
	from dotstar import Adafruit_DotStar
elif (STRIP_LIBRARY == STRIP_LIBRARY_WS2813):
	from neopixel import Adafruit_NeoPixel
	from neopixel import ws

# Setup
if (STRIP_LIBRARY == STRIP_LIBRARY_DOTSTAR):
    STRIP = Adafruit_DotStar(STRIP_NUMBER_OF_PIXELS, STRIP_DATA_PIN, STRIP_CLOCK_PIN)
elif (STRIP_LIBRARY == STRIP_LIBRARY_WS2813):
    STRIP = Adafruit_NeoPixel(STRIP_NUMBER_OF_PIXELS, STRIP_DATA_PIN, STRIP_FREQ_HZ, STRIP_DMA, STRIP_INVERT, STRIP_BRIGHTNESS, STRIP_CHANNEL, STRIP_TYPE)
else:
    sys.exit ("Unknown Strip Type in config.py")

STRIP.begin()
STRIP.setBrightness(STRIP_BRIGHTNESS)

def set_brightness(b):
    STRIP.setBrightness(b)


def _set_pixel_color (strip,p,r,g,b):
    rgb = r*256*256 + g*256 + b

    if (STRIP_LIBRARY == STRIP_LIBRARY_DOTSTAR):
        strip.setPixelColor(p,r,g,b)
    elif (STRIP_LIBRARY == STRIP_LIBRARY_WS2813):
        strip.setPixelColor(p,rgb)

def fade(current_state, target_state):
    'Sets the colours of the lights to be closer to the target colour'
    updated_state = {}
    for pixel_coordinate, pixel_colour in current_state.items():
        target_colour = target_state[pixel_coordinate]
        new_colour = _get_fade_colour(pixel_colour, target_colour)
        _set_grid_pixel_colour(pixel_coordinate, new_colour)
        updated_state[pixel_coordinate] = new_colour
    return updated_state

def light(word_state):
    'Sets the colours of many pixels using the state of a word object'
    for pixel_coordinate, pixel_colour in word_state.items():
        _set_grid_pixel_colour(pixel_coordinate, pixel_colour)

def push_changes():
    STRIP.show()

def _get_fade_colour(old_colour, new_colour):
    return_colour = []
    for old, new in zip(old_colour, new_colour):
        if old < new:
            return_colour.append(old + min(FADE_INCREMENT,new-old))
        elif old > new:
            return_colour.append(old - min(FADE_INCREMENT,old-new))
        else:
            return_colour.append(old)
    return return_colour

def _set_linear_pixel_colour(pixel_number, rgb_colour_array):
    'Sets a the colour of a pixel using its linear address'
    _set_pixel_color(STRIP,pixel_number, rgb_colour_array[1], rgb_colour_array[0], rgb_colour_array[2])

def _get_pixel_number(coorinate):
    if (LED_LAYOUT == LED_LAYOUT_BOTTOM_RIGHT):
        # 0,0 is assumed to be top-left, x=11, y=8 is bottom right
        # Code assumes:
        # - first pixel is bottom right
        # - 12 pixels in a row
        # - 9 rows
        # - 2 pixels between rows
        # Total number of pixels = 14 * 9 - 2 = 124 ( 0 -> 123 )
        x_coordinate = 11 - coorinate[0]
        y_coordinate = 8 - coorinate[1]
        y_coordinate_is_even = y_coordinate % 2 == 0
        if y_coordinate_is_even:
            pixnum = y_coordinate * 14 + x_coordinate 
        else:
            pixnum = (y_coordinate + 1) * 14 - x_coordinate - 3
    
        pixnum = pixnum + LED_LAYOUT_OFFSET
    else:
        sys.exit("Invalid LED_LAYOUT value in config.py")

    return pixnum


def _set_grid_pixel_colour(coordinate, colour_array):
    'Sets the colour of a pixel using its coordinate address'
    linear_address = _get_pixel_number(coordinate)
    _set_linear_pixel_colour(linear_address, colour_array)
