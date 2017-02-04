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


class PPAPAPIWatcher:
    API_HOST = 'yhack-ppap17.mybluemix.net'
    API_ENTRY_POINT = '/api/ppapcode'
    callback = ''

    def __init__(self, cb):
        self.callback = cb

    def run(self):
        while True:
            time.sleep(1)
            print "INFO: HTTP get..."
            response = urllib2.urlopen('http://' + self.API_HOST + self.API_ENTRY_POINT)
            body = response.read()

            print body
            jsondata = json.loads(body)

            if 'ppapcode' in jsondata and jsondata['ppapcode']:
                self.callback(list(jsondata['ppapcode']))


intr_flag = 0

def printout(data):
    signal.signal(signal.SIGINT, exit_handler)
    global intr_flag

    PANEL_HORIZONTAL_HOLES = 15
    PANEL_VERTICAL_HOLES   = 10

    total_cycles = 0

    stp = SteppingMotor(20, 21, 16)
    dcm = DCMotor()

    for i in range(0,PANEL_HORIZONTAL_HOLES):
        stp.forward() 
        total_cycles = total_cycles + 1
   
        if (intr_flag):
            break

        time.sleep(1)

        print "INFO: %s" % data[i*PANEL_VERTICAL_HOLES:(i+1)*PANEL_VERTICAL_HOLES]

        dcm.setposition(data[i*PANEL_VERTICAL_HOLES:(i+1)*PANEL_VERTICAL_HOLES])
        dcm.push(5)
        dcm.back(5)

        print "NEXT LINE"

    for i in range(0, total_cycles):
        stp.backward() 

    stp.turn_off()
    signal.signal(signal.SIGINT, signal.SIG_DFL)

def exit_handler(signal, frame):
     global intr_flag
     intr_flag = 1


watcher = PPAPAPIWatcher(printout)
watcher.run()

