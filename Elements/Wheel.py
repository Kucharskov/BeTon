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
		
class WheelPWM(Wheel):
	#ToDo: Ogarnąć działanie za pomocą start(dc) i stop(dc)
	#Link: https://sourceforge.net/p/raspberry-gpio-python/wiki/PWM/
	def __init__(self, fPin, bPin, power = 100):
		self.power = power
		GPIO.setmode(GPIO.BOARD)
		self.f = GPIO.PWM(fPin, 100)
		self.b = GPIO.PWM(bPin, 100)

	def stop(self):
		self.f.stop()
		self.b.stop()

	def goForward(self):
		self.b.stop()
		self.f.start(self.power)

	def goBackward(self):
		self.f.stop()
		self.b.start(self.power)
		
	def changePower(self, power):
		self.f.ChangeDutyCycle(power)
		self.b.ChangeDutyCycle(power)