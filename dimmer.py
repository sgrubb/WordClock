# General purpose dimmer

import cronparser
from post_config import *

class Dimmer:
    def __init__(self, cron):
        self.cron = cron

    def get_brightness(self):
        if (cronparser.is_now(self.cron)):
            b = STRIP_BRIGHTNESS_DIM
        else:
            b = STRIP_BRIGHTNESS
        return b

