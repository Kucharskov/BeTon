#!/usr/bin/python3
import time
import random
from Elements.Wheel import Wheel
from Elements.HCSR04 import HCSR04

'''Be "Turbo Oafish Nothing"'''
'''BeTon - Simple Raspberry Pi robot'''
__author__ = "M. Kucharskov"
__version__ = "1.0.0"
__maintainer__ = "M. Kucharskov"
__email__ = "M@Kucharskov.pl"

class BeTon:
	def __init__(self, lfPin, lbPin, rfPin, rbPin, rotatetime = 5):
		self.lWheel = Wheel(lfPin, lbPin)
		self.rWheel = Wheel(rfPin, rbPin)
		self.rotatetime = rotatetime
		self.setupradar = False

	def stop(self):
		self.lWheel.stop()
		self.rWheel.stop()

	def goForward(self):
		self.stop()
		self.lWheel.goForward()
		self.rWheel.goForward()

	def goBackward(self):
		self.stop()
		self.lWheel.goBackward()
		self.rWheel.goBackward()

	def turnLeft(self, deg = 90):
		self.stop()
		self.rWheel.goForward()
		self.lWheel.goBackward()
		
		sleeptime = (deg * self.rotatetime)/360
		time.sleep(sleeptime)
		
		self.stop()

	def turnRight(self, deg = 90):
		self.stop()
		self.lWheel.goForward()
		self.rWheel.goBackward()
		
		sleeptime = (deg * self.rotatetime)/360
		time.sleep(sleeptime)
		
		self.stop()

	def goForwardTime(self, t):
		self.goForward()
		time.sleep(t)
		self.stop()

	def goBackwardTime(self, t):
		self.goBackward()
		time.sleep(t)
		self.stop()

	def setupRadar(self, trigPin, echoPin):
		self.radar = HCSR04(trigPin, echoPin)
		self.setupradar = True

	def automove(self, log = False):
		if self.setupradar:
			if log:
				print(self.radar.read())

			if (self.radar.read() > 35):
				self.goForwardTime(.15)
			else:
				self.goBackwardTime(.15)
				if random.randint(0, 100) % 2 == 0:
					self.turnRight(45)
					self.turnLeft(45)