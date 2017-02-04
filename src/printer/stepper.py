#!/usr/bin/python

import sys
import time
import signal
import RPi.GPIO as GPIO

from dc import DCMotor

#################################
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
# 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 #
#################################

PANEL_HORIZONTAL_HOLES = 15
PANEL_VERTICAL_HOLES   = 10

MM_PER_CYCLE = 3
MM_HOLE2HOLE = 10

step_pin1 = 20
step_pin2 = 21
stb_pin   = 16
WAIT_SEC  = 0.004

total_cycles = 0
intr_flag   = 0

if len(sys.argv) != 2:
   print "ERROR: no input strings"
   sys.exit(1)

data = sys.argv[1]

def exit_handler(signal, frame):
        global intr_flag
        intr_flag = 1

signal.signal(signal.SIGINT, exit_handler)

dcm = DCMotor()

GPIO.setmode(GPIO.BCM)

GPIO.setup(step_pin1,GPIO.OUT)
GPIO.setup(step_pin2,GPIO.OUT)

GPIO.setup(stb_pin,GPIO.OUT)
GPIO.output(stb_pin, True)

try:
    for i in range(0,PANEL_HORIZONTAL_HOLES):
        for j in range(50):
            print "pin1: false, pin2: false"
            GPIO.output(step_pin1, False)
            GPIO.output(step_pin2, False)
            time.sleep(WAIT_SEC)
            print "pin1: true, pin2: false"
            GPIO.output(step_pin1, True)
            GPIO.output(step_pin2, False)
            time.sleep(WAIT_SEC)
            print "pin1: true, pin2: true"
            GPIO.output(step_pin1, True)
            GPIO.output(step_pin2, True)
            time.sleep(WAIT_SEC)
            print "pin1: false, pin2: true"
            GPIO.output(step_pin1, False)
            GPIO.output(step_pin2, True)
            time.sleep(WAIT_SEC)

        print data[i*PANEL_VERTICAL_HOLES:(i+1)*PANEL_VERTICAL_HOLES]
        time.sleep(2)

        total_cycles = total_cycles + 1

        dcm.setposition(data[i:(i+1)*PANEL_VERTICAL_HOLES])

        # push bars
        dcm.push()
        time.sleep(3)
        dcm.stop()

        print "NEXT LINE"

        if (intr_flag):
            raise Exception

except Exception:
    pass

print "TOTAL CYCLES: %d" % total_cycles

for i in range(0,total_cycles):
    for j in range(50):
        print "pin1: true, pin2: false"
        GPIO.output(step_pin1, False)
        GPIO.output(step_pin2, True)
        time.sleep(WAIT_SEC)
        print "pin1: true, pin2: true"
        GPIO.output(step_pin1, True)
        GPIO.output(step_pin2, True)
        time.sleep(WAIT_SEC)
        print "pin1: true, pin2: false"
        GPIO.output(step_pin1, True)
        GPIO.output(step_pin2, False)
        time.sleep(WAIT_SEC)
        print "pin1: false, pin2: false"
        GPIO.output(step_pin1, False)
        GPIO.output(step_pin2, False)
        time.sleep(WAIT_SEC)

    time.sleep(1)


GPIO.output(stb_pin, False)
GPIO.cleanup()
