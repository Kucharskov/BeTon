#!/usr/bin/python3
import time
from BeTon import BeTon

if __name__ == "__main__":
	bot = BeTon(37, 35, 38, 40, 6.3)
	bot.goForwardTime(4)
	bot.goBackwardTime(0.5)
	bot.turnRight(180)
	bot.goForwardTime(4)
	bot.stop()
