#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

from dc import DCMotor

m = DCMotor()

d = ['1', '1', '1', '0', '0', '0', '0', '0', '0', '0']

m.setposition(['0', '1', '0', '0', '0', '0', '0', '0', '0', '0'])
m.back(3)
m.stop()
time.sleep(1)

m.setposition(['0', '0', '0', '1', '1', '1', '0', '0', '0', '0'])
m.back(3)
m.stop()
time.sleep(1)

m.setposition(['0', '0', '0', '0', '0', '0', '1', '1', '1', '0'])
m.back(3)
m.stop()
time.sleep(1)

m.setposition(['0', '0', '0', '0', '0', '0', '0', '0', '0', '1'])
m.back(3)
m.stop()
time.sleep(1)
