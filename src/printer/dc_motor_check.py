#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

from dc import DCMotor

m = DCMotor()

d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

m.stop()
for i in range(10):
    print i
    d[i] = '1'
    print d
    m.setposition(d)
    m.push(3)
    m.back(3)
    d[i] = '0'

m.stop()
