#FileName:video_control.py
#Lab1,Wednesday,group6
#Name(NetID):Suhui Yu(sy466);Yanan Liu(yl2248)

import RPi.GPIO as GPIO # give a RPI.GPIO a "nick name"GPIO
import subprocess 
import time

GPIO.setmode(GPIO.BCM) #set GPIO to refers to the pin by Broadcom numberring

#initilize four pins ,set high as normal and low as button is pressed GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True: #continuous run the following code
    time.sleep(0.2)
    if (not GPIO.input(22)): #if low is detected on pin 22
        print(" ")
        print "Button 22 pressed.."
        cmd = "echo seek 10 0 > /home/pi/video_fifo"#create a command to fast forward the video by 10 
        subprocess.check_output(cmd, shell=True)#send the command to terminal
    elif (not GPIO.input(17)): #if low is detected on pin 22
        print(" ")
        print "Button 17 pressed.."
        cmd = "echo pause > /home/pi/video_fifo"#create a command to pause the video
        subprocess.check_output(cmd, shell=True)#send the command to terminal
    elif (not GPIO.input(27)):
        print(" ")
        print "Button 27 pressed.."
        cmd = "echo quit > /home/pi/video_fifo"#create a command to quit the video
        subprocess.check_output(cmd, shell=True)#send the command to terminal
        break #terminate the while loop 
    elif (not GPIO.input(23)):
        print(" ")
        print "Button 23 pressed.."
        cmd = "echo seek -10 0 > /home/pi/video_fifo" #create a command to rewind the video by 10
        subprocess.check_output(cmd, shell=True) #send the command to terminal
