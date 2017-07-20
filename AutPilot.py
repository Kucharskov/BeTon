#!/usr/bin/python3
import time
from BeTon import BeTon

if __name__ == "__main__":
	try:
		bot = BeTon(37, 35, 38, 40, 6.3)
		bot.setupRadar(33, 36)
				
		while True:
			bot.automove()
	except KeyboardInterrupt:
		bot.stop()
