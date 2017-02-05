#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

class DCMotor:
    #_enable_pins = [4, 27, 10, 11, 6, 17, 22, 9, 5, 13]
    _enable_pins = [4, 17, 27, 22, 10, 9, 11, 5, 6, 13]
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
        if len(array_pins) != len(self._enable_pins):
            raise Exception("invalid args")

        self.position_pins = array_pins

    def push(self, t):
        print "### PUSH"
        GPIO.output(self.IN_1A4A, False)
        GPIO.output(self.IN_2A3A, True)

        for i in range(len(self.position_pins)):
            if (i < 3 and self.position_pins[i] == 1):
                GPIO.output(self._enable_pins[i], True)
            else:
                GPIO.output(self._enable_pins[i], False)

        time.sleep(t)

        for i in range(len(self.position_pins)):
            if (i >= 3 and i < 6 and self.position_pins[i] == 1):
                print self._enable_pins[i]
                GPIO.output(self._enable_pins[i], True)
            else:
                GPIO.output(self._enable_pins[i], False)

        time.sleep(t)

        for i in range(len(self.position_pins)):
            if (i >= 6 and i < 9 and self.position_pins[i] == 1):
                GPIO.output(self._enable_pins[i], True)
            else:
                GPIO.output(self._enable_pins[i], False)

        time.sleep(t)

        for i in range(len(self.position_pins)):
            if (i == 9 and self.position_pins[i] == 1):
                GPIO.output(self._enable_pins[i], True)
            else:
                GPIO.output(self._enable_pins[i], False)

        time.sleep(t)




    def stop(self):
        GPIO.output(self.IN_1A4A, False)
        GPIO.output(self.IN_2A3A, False)

        for p in self._enable_pins:
            GPIO.output(p, False)

    def back(self, t):
        print "### BACK"
        GPIO.output(self.IN_1A4A, True)
        GPIO.output(self.IN_2A3A, False)

        for i in range(len(self.position_pins)):
            if (i < 3 and self.position_pins[i] == 1):
                GPIO.output(self._enable_pins[i], True)
            else:
                GPIO.output(self._enable_pins[i], False)

        time.sleep(t)

        for i in range(len(self.position_pins)):
            if (i >= 3 and i < 6 and self.position_pins[i] == 1):
                GPIO.output(self._enable_pins[i], True)
            else:
                GPIO.output(self._enable_pins[i], False)

        time.sleep(t)

        for i in range(len(self.position_pins)):
            if (i >= 6 and i < 9 and self.position_pins[i] == 1):
                GPIO.output(self._enable_pins[i], True)
            else:
                GPIO.output(self._enable_pins[i], False)

        time.sleep(t)

        for i in range(len(self.position_pins)):
            if (i == 9 and self.position_pins[i] == 1):
                GPIO.output(self._enable_pins[i], True)
            else:
                GPIO.output(self._enable_pins[i], False)

        time.sleep(t)



