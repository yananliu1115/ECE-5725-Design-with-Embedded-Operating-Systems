import os
import pygame
import RPi.GPIO as GPIO
import time
import subprocess
from pygame.locals import *

code_run = time.time()
flag=True

os.putenv('SDL_VIDEODRIVER', 'fbcon') #display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1')
os.putenv('SDL_MOUSEDRV', 'TSLIB') #track mouse click on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
black = 0,0,0
white = 255,255,255
screen = pygame.display.set_mode((320,240))
my_font=pygame.font.Font(None,20)
my_button={'quit':(250,200),'start':(70,200)}
screen.fill(black)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def GPIO27_callback(channel):
        print ('Falling detected on 27')
        GPIO.cleanup()
        exit(0)
GPIO.add_event_detect(27,GPIO.FALLING,callback=GPIO27_callback,bouncetime = 300)

#pygame.display.flip()

while time.time()-code_run < 30 and flag:
        for button, position in my_button.items():
                text_surface = my_font.render(button, True, white)
                rect = text_surface.get_rect(center= position)
                screen.blit(text_surface,rect)

        for event in pygame.event.get():
                screen.fill(black)
                if(event.type is MOUSEBUTTONDOWN):
                        pos=pygame.mouse.get_pos()
                elif(event.type is MOUSEBUTTONUP):
                        pos=pygame.mouse.get_pos()
                        x,y=pos
                        print str(pos)
                        a ="touch at: "+str (pos)
                        text_surface1 = my_font.render(a, True, white)
                        rect = text_surface1.get_rect(center= [x,y])
                        screen.blit(text_surface1,rect)
                        if y>120:
                                if x<160:
                                        print "start"
                                else:
                                        flag = False
                                        print "quit button is pressed"

        pygame.display.flip()
