#FileName:fifo_test.py
#Lab1,Wednesday,group6
#Name(NetID):Suhui Yu(sy466);Yanan Liu(yl2248)

import subprocess

while True:
    cmd = raw_input("Enter a command:") #asking for user's input

    cmd1 = "echo " +'"'+ cmd +'"'+ " > /home/pi/video_fifo" #create a command
    print(cmd1)# check the correctness of the command for debug if needed
    subprocess.check_output(cmd1, shell = True)#pass the command to terminal

    #if user entered exit, break the while loop and terminate the program
    if cmd == "exit": 
        break
