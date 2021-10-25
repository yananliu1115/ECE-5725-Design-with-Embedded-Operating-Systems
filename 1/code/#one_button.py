#FileName:one_button.py
#Lab1,Wednesday,group6
#Name(NetID):Suhui Yu(sy466);Yanan Liu(yl2248)


import RPi.GPIO as GPIO # give a RPI.GPIO a "nick name" GPIO
import time 

GPIO.setmode(GPIO.BCM) 
#set GPIO to refers to the pin by Broadcom numberring 

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#initilize pin 22 as GPIO input,set high as normal and 
#low as button is pressed 
while True:# continuous run the following code
    time.sleep(0.2)
    if (not GPIO.input(22)):# if low is detected on pin 22
        print(" ")
        print "Button Sw1/22 pressed..."
