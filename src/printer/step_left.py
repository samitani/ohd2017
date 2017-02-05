#!/usr/bin/python

import time
import urllib2
import json
import signal

from stepping import SteppingMotor

intr_flag = 0

def printout(data):
    signal.signal(signal.SIGINT, exit_handler)
    global intr_flag

    PANEL_HORIZONTAL_HOLES = 15
    PANEL_VERTICAL_HOLES   = 10

    total_cycles = 0

    stp = SteppingMotor(20, 21, 16)

    for i in range(0,10):
        stp.backward() 
        total_cycles = total_cycles + 1
   
        if (intr_flag):
            break

        #time.sleep(0.1)

        print "INFO: %s" % data[i*PANEL_VERTICAL_HOLES:(i+1)*PANEL_VERTICAL_HOLES]

        print "NEXT LINE"

    stp.turn_off()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def exit_handler(signal, frame):
     global intr_flag
     intr_flag = 1


printout([0])
