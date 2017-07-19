#!/usr/bin/python3
import time
import RPi.GPIO as GPIO

'''BeTon HC-SR04 sensor module'''
__author__ = "M. Kucharskov"
__version__ = "1.0.0"

class HCSR04:
	def __init__(self, trigPin, echoPin):
		self.trigPin = trigPin
		self.echoPin = echoPin

		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.trigPin, GPIO.OUT, initial=GPIO.LOW)
		GPIO.setup(self.echoPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

		time.sleep(.001)

	def read(self):
		GPIO.output(self.trigPin, 1)
		time.sleep(.001)
		GPIO.output(self.trigPin, 0)

		start = 0
		while GPIO.input(self.echoPin) == 0:
			start = time.time()

		stop = 0
		while GPIO.input(self.echoPin) == 1:
			stop = time.time()

		return (stop - start) * 17150
