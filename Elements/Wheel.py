#!/usr/bin/python3
import time
import RPi.GPIO as GPIO

'''BeTon wheel module'''
__author__ = "M. Kucharskov"
__version__ = "1.0.0"

class Wheel:
	def __init__(self, fPin, bPin):
		self.fPin = fPin
		self.bPin = bPin
	
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.fPin, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.bPin, GPIO.OUT, initial=GPIO.LOW)

	def stop(self):
		GPIO.output(self.fPin, GPIO.LOW)
		GPIO.output(self.bPin, GPIO.LOW)

	def goForward(self):
		GPIO.output(self.fPin, GPIO.HIGH)

	def goBackward(self):
		GPIO.output(self.bPin, GPIO.HIGH)

	def goForwardTime(self, t):
		self.goForward()
		time.sleep(t)
		self.stop()

	def goBackwardTime(self, t):
		self.goBackward()
		time.sleep(t)
		self.stop()