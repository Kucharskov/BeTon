#!/usr/bin/python3
import time
import RPi.GPIO as GPIO

'''BeTon light module'''
__author__ = "M. Kucharskov"
__version__ = "1.1.0"

class Light:
	def __init__(self, pin):
		self.pin = pin
	
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

	def turnOn(self):
		GPIO.output(self.pin, GPIO.HIGH)

	def turnOff(self):
		GPIO.output(self.pin, GPIO.LOW)
		
	def blink(self, times = 1):
		for i in range(times):
			self.turnOn()
			time.sleep(.15)
			self.turnOff()
			time.sleep(.15)