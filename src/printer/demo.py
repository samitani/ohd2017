#!/usr/bin/python

import time
import urllib2
import json
import signal

from stepping import SteppingMotor
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


intr_flag = 0

def printout(data):
    signal.signal(signal.SIGINT, exit_handler)
    global intr_flag

    PANEL_VERTICAL_HOLES   = 10
    CYCLES_PER_HOLE = 5

    total_cycles = 0

    stp = SteppingMotor(20, 21, 16)
    dcm = DCMotor()

    for i in range(0, (len(data) / PANEL_VERTICAL_HOLES) - 2):
        if i != 0:
            for j in range(CYCLES_PER_HOLE):
                stp.forward() 
                total_cycles = total_cycles + 1

                if (intr_flag):
                    break

            time.sleep(1)

        if (i == 3 or i == 6 or i == 9 or i == 12):
            stp.forward() 
            total_cycles = total_cycles + 1

        print "INFO: %s %d - %d " % (data[i*PANEL_VERTICAL_HOLES:(i+1)*PANEL_VERTICAL_HOLES], i * PANEL_VERTICAL_HOLES, (i+1) * PANEL_VERTICAL_HOLES)

        dcm.setposition(data[i*PANEL_VERTICAL_HOLES:(i+1)*PANEL_VERTICAL_HOLES])
        dcm.push(2)
        dcm.back(2)
        dcm.stop()

        print "NEXT LINE"

        if (intr_flag):
            break

    for i in range(0, total_cycles):
        stp.backward() 

    stp.turn_off()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def exit_handler(signal, frame):
     global intr_flag
     intr_flag = 1



# Y! mark
printout(list("000000000000000000000000000000011000000001110000000011100000000111000000011111110001111111001110000011110000000110000000000000000000000000000000000000"))

