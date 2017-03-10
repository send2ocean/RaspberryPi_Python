#!/usr/bin/python
# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

class RemoteControl(object):
    """docstring for RemoteControl."""
    DR = 16
    DL = 19

    IR = 18
    PWM = 50
    n=0

    def __init__(self):
        super(RemoteControl,self).__init__()
        #self.arg = arg
        print("init remote controller")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.IR,GPIO.IN,GPIO.PUD_UP)

        GPIO.setup(self.DR,GPIO.IN,GPIO.PUD_UP)
        GPIO.setup(self.DL,GPIO.IN,GPIO.PUD_UP)

    def getKey(self):

        if GPIO.input(self.IR) == 0:
            count = 0
            while GPIO.input(self.IR) == 0 and count < 200:  #9ms
                count += 1
                time.sleep(0.00006)

            count = 0
            while GPIO.input(self.IR) == 1 and count < 80:  #4.5ms
                count += 1
                time.sleep(0.00006)

            idx = 0
            cnt = 0
            data = [0,0,0,0]
            for i in range(0,32):
                count = 0
                while GPIO.input(self.IR) == 0 and count < 15:    #0.56ms
                    count += 1
                    time.sleep(0.00006)

                count = 0
                while GPIO.input(self.IR) == 1 and count < 40:   #0: 0.56mx
                    count += 1                               #1: 1.69ms
                    time.sleep(0.00006)

                if count > 8:
                    data[idx] |= 1<<cnt
                if cnt == 7:
                    cnt = 0
                    idx += 1
                else:
                    cnt += 1
            print data
            if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:  #check
                return data[2]

            if data[0] == 255 and data[1] == 255 and data[2] == 15 and data[3] == 255:
                return "repeat"

    def getDR(self):
        print "test"
        data = GPIO.input(self.DR)
        print data
        return data

    def getDL(self):
        return GPIO.input(self.DL)
