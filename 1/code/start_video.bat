#FileName:start_video
#Lab1,Wednesday,group6
#Name(NetID):Suhui Yu(sy466);Yanan Liu(yl2248)

#!/bin/bash

python video_control.py &

sudo SDL_VIDEODRIVER=fbcon SDL_FBDEV=/dev/fb1 mplayer -input file=/home/pi/video_fifo -vo sdl -framedrop /home/pi/bigbuckbunny320p.mp4
