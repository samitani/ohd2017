#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

from dc import DCMotor

m = DCMotor()

d = ['1', '0', '0', '0', '0', '0', '0', '0', '0', '0']

m.stop()
m.setposition(d)
m.push(3)
m.back(3)
m.stop()
