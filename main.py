#!/usr/bin/python

from post_config import *
from clockface import ClockFace
import time

if (STRIP_LIBRARY == STRIP_LIBRARY_DOTSTAR):
	from dotstar import Adafruit_DotStar
elif (STRIP_LIBRARY == STRIP_LIBRARY_WS2813):
	from neopixel import Adafruit_NeoPixel
	from neopixel import ws

from logging.handlers import RotatingFileHandler
import logging
logpath = '/var/log/clock.log'
logformat='%(asctime)s %(message)s'

# Logger init
logger = logging.getLogger('clock')
logger.setLevel(logging.DEBUG)

# Handler
handler = RotatingFileHandler(logpath, maxBytes=1000000, backupCount=5)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

#First log
logger.debug('This message should go to the log file')

logger.info("Initial Sleep Start")
time.sleep(INITIAL_SLEEP)
logger.info("Initial Sleep End")

# Testing
CLOCK_FACE = ClockFace()
while True:
	CLOCK_FACE.refresh()
	time.sleep(REFRESH_TIME)
