'Contains lots of different colourers'

import logging
logger = logging.getLogger('clock')

import datetime
from random import randint

class SpectrumColourer:
    'Produces colours that iterate through the spectrum across an hour'

    def __init__(self, name):
        self.update_frequency = 1
        self.next_update = datetime.datetime.now()
        self.name = name

    def set_colours(self, state):
        'Sets the colours on the state object passed in'

        now = datetime.datetime.now()
        if now > self.next_update:
            logger.debug('Spectrum Updating %s, due at : %s, Now : %s', self.name, self.next_update, now)

            self.set_state_colours(state, now)
            while self.next_update < now:
                self.next_update = self.next_update + datetime.timedelta(0, self.update_frequency)

    def set_state_colours(self, state, now):
        'Sets a new colour property for each pixel of a given word-state object'
        for key in sorted(state):
            state[key] = self.get_colour_for_now(now)

    def get_colour_for_now(self, now):
        print now.minute
        print now.second
        hue = (now.minute * 60.0 + now.second) / 3600.0
        print hue
        r = self.hue_to_rgb(hue + 0.333) * 255
        print r
        print int(round(r))
        g = self.hue_to_rgb(hue) * 255
        print g
        print int(round(g))
        b = self.hue_to_rgb(hue - 0.333) * 255
        print b
        print int(round(b))
        print '################################'
        return [int(round(r)), int(round(g)), int(round(b))]

    def hue_to_rgb(self, hue):
        if hue < 0:
            hue += 1.0
        if hue > 1.0:
            hue -= 1.0
        if hue < 0.167:
            return 6.0 * hue
        if hue < 0.5:
            return 1.0
        if hue < 0.667:
            return (0.667 - hue) * 6.0
        return 0


class RandomColourer:
    'Produces random colours which change every 2 seconds'

    def rand_colour_value(self):
        return min(max((randint(0,2) * 128 -1),0),255)

    def rand_colour(self):
	while True:
            r = self.rand_colour_value()
            g = self.rand_colour_value()
            b = self.rand_colour_value()
            if (r>0) or (g>0) or (b>0):
                break;
        return [r,g,b]

    def __init__(self,name):
        self.update_frequency = 300
        self.next_update = datetime.datetime.now()
        self.next_colour = self.rand_colour()
        self.name = name

    def set_colours(self, state):
        'Returns a new random colour at a set frequency'
        now = datetime.datetime.now()
        if now > self.next_update:
	    logger.debug('Random Updating %s, due at : %s, Now : %s',self.name,self.next_update,now)
            self.set_state_colours(state)

            # setting next_update to (current time + delta) causes drift so apply delta to next_update
            # however, if word has been "off" for a while then next_update may be a long way behind so keep adding
            # until up to date
            while self.next_update < now:
                self.next_update = self.next_update + datetime.timedelta(0, self.update_frequency)
            self.next_colour = self.rand_colour()

    def set_state_colours(self, state):
        'Sets a new colour property for each pixel of a given word-state object'
        for key in sorted(state):
            state[key] = self.next_colour


class RainbowColourer:
    'Produces rainbow colours which change every x seconds (x provided as parmameter to constructor)'
    POSSIBLE_COLOURS = (
        [255, 0, 0],
        [255, 127, 0],
        [0, 255, 0],
        [0, 0, 255],
        [148, 0, 211],
    )
    current_index = 0

    def __init__(self,name,freq):
        self.update_frequency = freq
        self.next_update = datetime.datetime.now()
        self.colour = RainbowColourer.POSSIBLE_COLOURS[RainbowColourer.current_index]
	self.name= name

    def set_colours(self, state):
        'Sets the colours on the state object passed in.'
        now = datetime.datetime.now()
        if now > self.next_update:
	    logger.debug('Rainbow Updating %s, due at : %s, Now : %s',self.name,self.next_update,now)
            while self.next_update < now:
                self.next_update = self.next_update + datetime.timedelta(0, self.update_frequency)
            self.set_state_colours(state)

    def set_state_colours(self, state):
        'Sets a new colour property for each pixel of a given word-state object'
        for key in sorted(state):
            state[key] = self.get_next_colour()

    @classmethod
    def get_next_colour(cls):
        'Increments the colour index and returns the next colour'
        number_of_colours = len(cls.POSSIBLE_COLOURS)
        cls.current_index = (cls.current_index + 1) % number_of_colours
        return cls.POSSIBLE_COLOURS[cls.current_index]
