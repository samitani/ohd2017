#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

from dc import DCMotor

m = DCMotor()
m.setposition([1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0])
m.push()
time.sleep(3)
m.stop()
