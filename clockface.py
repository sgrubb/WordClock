'Represents a clock face, comprising many words'

from word import Word
from dimmer import Dimmer
from colourers import RandomColourer
from colourers import RainbowColourer
from colourers import SpectrumColourer
import wordpositions as wp
import lighter
from post_config import *

class ClockFace:
    'Represents a clock face, comprising many words'

    def __init__(self):
        self.words = [
            # All the timings are set to change 2 minutes before/3 minutes after
            # each 5 minute interval instead of on them
            Word(["*", "*", "*", "*", "3-8,53-58", "*"], wp.MINUTE_FIVE, RandomColourer('FIVE')),
            Word(["*", "*", "*", "*", "8-13,48-53", "*"], wp.MINUTE_TEN, RandomColourer('TEN')),
            Word(["*", "*", "*", "*", "13-18,43-48", "*"], wp.MINUTE_QUARTER, RandomColourer('QUARTER')),
            Word(["*", "*", "*", "*", "18-23,38-43", "*"], wp.MINUTE_TWENTY, RandomColourer('TWENTY')),
            Word(["*", "*", "*", "*", "23-28,33-38", "*"], wp.MINUTE_TWENTY_FIVE, RandomColourer('TWENTYFIVE')),
            Word(["*", "*", "*", "*", "28-33", "*"], wp.MINUTE_HALF, RandomColourer('HALF')),
            Word(["*", "*", "*", "*", "3-33", "*"], wp.PAST, RandomColourer('PAST')),
            Word(["*", "*", "*", "*", "33-58", "*"], wp.TO, RandomColourer('TO')),
            Word(["*", "*", "*", "0,12 & 1,13", "33-60 & 0-33", "*"], wp.HOUR_ONE, RandomColourer('ONE')),
            Word(["*", "*", "*", "1,13 & 2,14", "33-60 & 0-33", "*"], wp.HOUR_TWO, RandomColourer('TWO')),
            Word(["*", "*", "*", "2,14 & 3,15", "33-60 & 0-33", "*"], wp.HOUR_THREE, RandomColourer('THREE')),
            Word(["*", "*", "*", "3,15 & 4,16", "33-60 & 0-33", "*"], wp.HOUR_FOUR, RandomColourer('FOUR')),
            Word(["*", "*", "*", "4,16 & 5,17", "33-60 & 0-33", "*"], wp.HOUR_FIVE, RandomColourer('FIVE')),
            Word(["*", "*", "*", "5,17 & 6,18", "33-60 & 0-33", "*"], wp.HOUR_SIX, RandomColourer('SIX')),
            Word(["*", "*", "*", "6,18 & 7,19", "33-60 & 0-33", "*"], wp.HOUR_SEVEN, RandomColourer('SEVEN')),
            Word(["*", "*", "*", "7,19 & 8,20", "33-60 & 0-33", "*"], wp.HOUR_EIGHT, RandomColourer('EIGHT')),
            Word(["*", "*", "*", "8,20 & 9,21", "33-60 & 0-33", "*"], wp.HOUR_NINE, RandomColourer('NINE')),
            Word(["*", "*", "*", "9,21 & 10,22", "33-60 & 0-33", "*"], wp.HOUR_TEN, RandomColourer('TEN')),
            Word(["*", "*", "*", "10,22 & 11,23", "33-60 & 0-33", "*"], wp.HOUR_ELEVEN, RandomColourer('ELEVEN')),
            Word(["*", "*", "*", "11,23 & 12,0", "33-60 & 0-33", "*"], wp.HOUR_TWELVE, RandomColourer('TWELVE')),
            Word(["*", BDAY_MONTH, BDAY_DAY, BDAY_HOURS, "*", "*"], wp.HAPPY, RainbowColourer('HAPPY', 1)),
            Word(["*", BDAY_MONTH, BDAY_DAY, BDAY_HOURS, "*", "*"], wp.BIRTHDAY, RainbowColourer('BIRTHDAY', 1))
            #Word(["*", BDAY_MONTH, BDAY_DAY, BDAY_HOURS, "*", "*"], wp.BLIB, RainbowColourer('BLIB', 1))
            ]
        self.dimmer = Dimmer(["*", "*", "*", DIM_HOURS, "*", "*"])

    def refresh(self):
        'Updates all the lights on the clock face'
        for word in self.words:
            word.update()
        lighter.set_brightness(self.dimmer.get_brightness())
        lighter.push_changes()
