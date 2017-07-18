#!/usr/bin/python3
import time
from BeTon import BeTon
from Elements.HCSR04 import HCSR04

if __name__ == "__main__":
	try:
		bot = BeTon(37, 35, 38, 40, 6.3)
		s = HCSR04(33, 36)
		
		while True:
			bot.automove(s)
	except KeyboardInterrupt:
		bot.stop()
