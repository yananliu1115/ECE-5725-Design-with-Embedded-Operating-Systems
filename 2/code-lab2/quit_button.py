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
os.putenv('SDL_MOUSEDRV', '/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
black = 1,0,0
white = 255,255,255
screen = pygame.display.set_mode((320,240))
my_font=pygame.font.Font(None,20)
my_button={'button':(250,200)}
screen.fill(black)

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def GPIO27_callback(channel):
        print ('Falling detected on 27')
        GPIO.cleanup()
        exit(0)
GPIO.add_event_detect(27,GPIO.FALLING,callback=GPIO27_callback,bouncetime = 300)

for button, position in my_button.items():
        text_surface = my_font.render(button, True, white)
        rect = text_surface.get_rect(center= position)
        screen.blit(text_surface,rect)

pygame.display.flip()

while time.time()-code_run < 30 and flag:
        for event in pygame.event.get():
                if(event.type is MOUSEBUTTONDOWN):
                        pos=pygame.mouse.get_pos()
                elif(event.type is MOUSEBUTTONUP):
                        pos=pygame.mouse.get_pos()
                        x,y=pos
                        if y<120 :
                                if x>160:
                                        flag = False
                                        print "quit button is pressed"
