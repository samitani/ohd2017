#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

enable_pin = 11
in1A = 7
in2A = 8

GPIO.setup(enable_pin,GPIO.OUT)
GPIO.setup(in1A,GPIO.OUT)
GPIO.setup(in2A,GPIO.OUT)


GPIO.output(enable_pin, False)

GPIO.output(in1A, True)
GPIO.output(in2A, False)
GPIO.output(enable_pin, True)
time.sleep(1)
GPIO.output(enable_pin, False)
time.sleep(1)
GPIO.output(in1A, False)
GPIO.output(in2A, True)
GPIO.output(enable_pin, True)
time.sleep(1)
GPIO.output(enable_pin, False)
