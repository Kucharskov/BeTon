#!/usr/bin/python3
import time
from BeTon import BeTon

if __name__ == "__main__":
	try:
		bot = BeTon(37, 35, 38, 40, 6.3)
		bot.setupRadar(33, 36)

		print("Komendy BeTon:")
		print("f/b - krok w przod/tyl")
		print("l/r - obrot lewo/prawo")
		print("s - odczyt odleglosci z radaru")
		print("e - zakonczenie pracy robota")

		cmd = ""
		while cmd != "e":
			cmd_str = input("Polecenie: ")
			
			for cmd in cmd_str:
				if cmd == "f":
					bot.goForwardTime(0.7)
				elif cmd == "b":
					bot.goBackwardTime(0.7)
				elif cmd == "r":
					bot.turnRight()
				elif cmd == "l":
					bot.turnLeft()
				elif cmd == "s":
					print("Odleglosc " + str(round(bot.radar.read(), 2)))
			
		bot.stop()
	except KeyboardInterrupt:
		bot.stop()
