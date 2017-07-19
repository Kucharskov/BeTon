#!/usr/bin/python3
import time
from Elements.Wheel import Wheel

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

	def stop(self):
		self.lWheel.stop()
		self.rWheel.stop()

	def goForward(self):
		self.lWheel.goForward()
		self.rWheel.goForward()

	def goBackward(self):
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

	def automove(self, sensor):
		#print(sensor.read())
		if (sensor.read() > 35):
			self.goForward()
		else:
			self.goBackwardTime(.15)
			self.turnLeft(45)
			if (sensor.read() < 35):
				self.turnRight(90)
