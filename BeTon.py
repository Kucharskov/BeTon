#!/usr/bin/python3
import time
import random
import RPi.GPIO as GPIO
from Elements.Wheel import Wheel
from Elements.HCSR04 import HCSR04
from Elements.Light import Light

'''Be "Turbo Oafish Nothing"'''
'''BeTon - Simple Raspberry Pi robot'''
__author__ = "M. Kucharskov"
__version__ = "1.1.0"
__maintainer__ = "M. Kucharskov"
__email__ = "M@Kucharskov.pl"

class BeTon:
	def __init__(self, lfPin, lbPin, rfPin, rbPin, rotatetime = 5):
		self.lWheel = Wheel(lfPin, lbPin)
		self.rWheel = Wheel(rfPin, rbPin)
		self.rotatetime = rotatetime
		self.setupradar = False
		self.lights = []

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

	def turnRight(self, deg = 90):
		self.stop()
		self.rWheel.goForward()
		self.lWheel.goBackward()
		
		sleeptime = (deg * self.rotatetime)/360
		time.sleep(sleeptime)
		
		self.stop()

	def turnLeft(self, deg = 90):
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

	def setupLights(self, *pins):
		for p in pins:
			self.lights.append(Light(p))
			
	def setLights(self, mode):
		for l in self.lights:
			if mode == True:
				l.turnOn()
			else:
				l.turnOff()

	def getDistance(self, acc = 2):
		if self.setupradar:
			if acc == 0:
				return int(self.radar.read())
			else:
				return round(self.radar.read(), acc) 
	
	def automove(self, log = False):
		if self.setupradar:
			if log:
				print(self.getDistance())

			if (self.getDistance() > 35):
				self.goForwardTime(.15)
			else:
				self.goBackwardTime(.15)
				self.turnLeft(45)
				distLeft = self.getDistance()
				self.turnRight(90)
				distRight = self.getDistance()
				if distLeft > distRight:
					self.turnLeft(90)

	def __del__(self):
		self.stop()
		print("Zakonczono prace robota")
		GPIO.cleanup()