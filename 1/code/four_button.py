#FileName:four_button.py
#Lab1,Wednesday,group6
#Name(NetID):Suhui Yu(sy466);Yanan Liu(yl2248)

import RPi.GPIO as GPIO # give a RPI.GPIO a "nick name"GPIO
import time 

GPIO.setmode(GPIO.BCM) 
#set GPIO to refers to the pin by Broadcom numberring

#initilize four pins, set high as normal and low as button is pressed 
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:# continuous run the following code
    if (not GPIO.input(22)):# if low is detected on pin 22
        print(" ")
        print "Button 22 pressed.."
    elif (not GPIO.input(17)):# if low is detected on pin 17
        print(" ")
        print "Button 17 pressed.."
    elif (not GPIO.input(27)):# if low is detected on pin 27
        print(" ")
        print "Button 27 pressed.."
        break  #break the while loop and terminate the program
    elif (not GPIO.input(23)):# if low is detected on pin 23
        print(" ")
        print "Button 23 pressed.."
