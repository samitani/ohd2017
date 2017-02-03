#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

step_pin1 = 24
step_pin2 = 23

wait_sec  = 0.004

GPIO.setup(step_pin1,GPIO.OUT)
GPIO.setup(step_pin2,GPIO.OUT)

GPIO.setup(16,GPIO.OUT)
GPIO.output(16, True)

for i in range(50*1):
    print "pin20: false, pin21: false"
    GPIO.output(step_pin1, False)
    GPIO.output(step_pin2, False)
    time.sleep(wait_sec)
    print "pin20: true, pin21: false"
    GPIO.output(step_pin1, True)
    GPIO.output(step_pin2, False)
    time.sleep(wait_sec)
    print "pin20: true, pin21: true"
    GPIO.output(step_pin1, True)
    GPIO.output(step_pin2, True)
    time.sleep(wait_sec)
    print "pin20: true, pin21: false"
    GPIO.output(step_pin1, False)
    GPIO.output(step_pin2, True)
    time.sleep(wait_sec)

time.sleep(1)

for i in range(50*10):
    print "pin20: true, pin21: false"
    GPIO.output(step_pin1, False)
    GPIO.output(step_pin2, True)
    time.sleep(wait_sec)
    print "pin20: true, pin21: true"
    GPIO.output(step_pin1, True)
    GPIO.output(step_pin2, True)
    time.sleep(wait_sec)
    print "pin20: true, pin21: false"
    GPIO.output(step_pin1, True)
    GPIO.output(step_pin2, False)
    time.sleep(wait_sec)
    print "pin20: false, pin21: false"
    GPIO.output(step_pin1, False)
    GPIO.output(step_pin2, False)
    time.sleep(wait_sec)



GPIO.output(16, False)


