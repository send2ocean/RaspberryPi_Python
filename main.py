#import  Infrared.RemoteControl as Remote
import RPi.GPIO as GPIO
import time

from Infrared.RemoteControl import RemoteControl
# RemoteControl().getKey()
from AlphaBot import AlphaBot

Ab = AlphaBot()

def remoteControl():

    try:
        r = RemoteControl()
        while True:
            key =r.getKey()
            if(key != None):
                print(key)
                if key == 0x18:
        #            Ab.forward()
        #                print("forward")
                    DR_status = r.getDR()
                    DL_status = r.getDL()
                    print DR_status
                    print DL_status

                    if((DL_status == 1) and (DR_status == 1)):
                        Ab.forward()
                        print("forward")
                    elif((DL_status == 1) and (DR_status == 0)):
                        Ab.left()
                        print("left")
                    elif((DL_status == 0) and (DR_status == 1)):
                        Ab.right()
                        print("right")
                    else:
                        Ab.backward()
                        time.sleep(0.2)
                        Ab.left()
                        time.sleep(0.2)
                        Ab.stop()
                        print("backward")
            #1 12
            #2 24
            #3 94
            #4 8
            #5 28
            #6 90
            #7 66
            #8 82
            #9 74
            #0 22
    except KeyboardInterrupt:
        GPIO.cleanup();
Ab.stop()
remoteControl()
