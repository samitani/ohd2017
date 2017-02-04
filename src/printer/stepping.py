import sys
import time
import signal
import RPi.GPIO as GPIO

class SteppingMotor:
    PIN1 = 0
    PIN2 = 0
    PINSTB  = 0
    WAIT_SEC = 0.004

    def __init__(self, pin1, pin2, stb):
        self.PIN1 = pin1
        self.PIN2 = pin2
        self.PINSTB  = stb

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN1,GPIO.OUT)
        GPIO.setup(self.PIN2,GPIO.OUT)

        GPIO.setup(self.PINSTB,GPIO.OUT)
        GPIO.output(self.PINSTB, True)



    def forward(self):
        for j in range(50):
            print "pin1: false, pin2: false"
            GPIO.output(self.PIN1, False)
            GPIO.output(self.PIN2, False)
            time.sleep(self.WAIT_SEC)
            print "pin1: true, pin2: false"
            GPIO.output(self.PIN1, True)
            GPIO.output(self.PIN2, False)
            time.sleep(self.WAIT_SEC)
            print "pin1: true, pin2: true"
            GPIO.output(self.PIN1, True)
            GPIO.output(self.PIN2, True)
            time.sleep(self.WAIT_SEC)
            print "pin1: false, pin2: true"
            GPIO.output(self.PIN1, False)
            GPIO.output(self.PIN2, True)
            time.sleep(self.WAIT_SEC)

    def turn_off(self):
        GPIO.output(self.PINSTB, False)
        GPIO.cleanup()

    def backward(self):
        for j in range(50):
            print "pin1: true, pin2: false"
            GPIO.output(self.PIN1, False)
            GPIO.output(self.PIN2, True)
            time.sleep(self.WAIT_SEC)
            print "pin1: true, pin2: true"
            GPIO.output(self.PIN1, True)
            GPIO.output(self.PIN2, True)
            time.sleep(self.WAIT_SEC)
            print "pin1: true, pin2: false"
            GPIO.output(self.PIN1, True)
            GPIO.output(self.PIN2, False)
            time.sleep(self.WAIT_SEC)
            print "pin1: false, pin2: false"
            GPIO.output(self.PIN1, False)
            GPIO.output(self.PIN2, False)
            time.sleep(self.WAIT_SEC)

    

#stp = SteppingMotor(20, 21, 16)
#
#total_cycles = 0
#intr_flag = 0
#
#def exit_handler(signal, frame):
#     global intr_flag
#     intr_flag = 1
#
#signal.signal(signal.SIGINT, exit_handler)
#
#for i in range(3):
#    stp.forward() 
#    total_cycles = total_cycles + 1
#
#    if (intr_flag):
#        break
#
#print "#### %d" % total_cycles
#
#time.sleep(1)
#
#for x in range(total_cycles):
#    stp.backward()
#
#print total_cycles
#
#stp.turn_off()
#GPIO.cleanup()
