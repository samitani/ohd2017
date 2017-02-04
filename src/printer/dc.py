#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

class DCMotor:
    _enable_pins = [4, 17]
    position_pins = []

    IN_1A4A = 2
    IN_2A3A = 3
    
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN_1A4A, GPIO.OUT)
        GPIO.setup(self.IN_2A3A, GPIO.OUT)

        for p in self._enable_pins:
            GPIO.setup(p, GPIO.OUT)
            GPIO.output(p, False)

    def setposition(self, array_pins):
        self.position_pins = array_pins

    def turn_right(self):
        GPIO.output(self.IN_1A4A, False)
        GPIO.output(self.IN_2A3A, True)

        for i, flag in enumerate(self.position_pins):
            if (flag == 1):
                GPIO.output(self._enable_pins[i], True)

    def stop(self):
        GPIO.output(self.IN_1A4A, False)
        GPIO.output(self.IN_2A3A, False)

        for p in self._enable_pins:
            GPIO.output(p, False)

    def turn_left(self):
        GPIO.output(self.IN_1A4A, True)
        GPIO.output(self.IN_2A3A, False)

        for i, flag in enumerate(self.position_pins):
            if (flag == 1):
                GPIO.output(self._enable_pins[i], True)



#m = DCMotor()
#m.setposition([0, 1])
#m.turn_right()
#time.sleep(1)
#m.stop()
#time.sleep(1)
#m.turn_left()
#time.sleep(1)
#m.stop()
