#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

from dc import DCMotor

m = DCMotor()
m.setposition([1, 1, 1, 1, 1, 1, 1, 1 ,1 , 1])
m.back()
time.sleep(1)
m.push()
time.sleep(5)
m.back()
time.sleep(5)
m.stop()
