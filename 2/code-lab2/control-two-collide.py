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

game_button={'pause':(70,200),'fast':(130,200),'slow':(190,200),'back':(250,200)}

screen.fill(black)

size = width,height = 320,240
speed1 = [1,1]
speed2 = [-2,-2]

ball1 = pygame.image.load('magic_ball.png')
ball2 = pygame.image.load('golf_ball.png')

ball1 = pygame.transform.scale(ball1,(40,40))
ball2 = pygame.transform.scale(ball2,(30,30))

ballrect1 = ball1.get_rect(center=[100,100])
ballrect2 = ball2.get_rect(center=[50,50])

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def GPIO27_callback(channel):
        print ('Falling detected on 27')
        GPIO.cleanup()
        exit(0)
GPIO.add_event_detect(27,GPIO.FALLING,callback=GPIO27_callback,bouncetime = 300)

def change_speed(speed1,speed2,para):
        for i in range (0,2):
                speed1[i]=speed1[i]*para
                speed2[i]=speed2[i]*para
        return speed1,speed2

#pygame.display.flip()

first_page=True
second_page=False
counter1=1;
speedt1=[0,0]
speedt2=[0,0]
while time.time()-code_run < 3000 and flag:
        #the first page
        if (first_page):
                for button, position in my_button.items():
                        text_surface = my_font.render(button, True, white)
                        rect = text_surface.get_rect(center= position)
                        screen.blit(text_surface,rect)
                #hit the first page button
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
                                                first_page=False
                                                second_page=True
                                        else:
                                                flag = False
                                                print "quit button is pressed"
                pygame.display.flip()

        if (second_page):
                screen.fill(black)
                time.sleep(0.01)
                ballrect1 = ballrect1.move(speed1)
                if ballrect1.left<0 or ballrect1.right > width:
                        speed1[0] = - speed1[0]
                if ballrect1.top < 0 or ballrect1.bottom > height:
                        speed1[1] = - speed1[1]

                ballrect2 = ballrect2.move(speed2)
                if ballrect2.left<0 or ballrect2.right > width:
                        speed2[0] = - speed2[0]
                if ballrect2.top < 0 or ballrect2.bottom > height:
                        speed2[1] = - speed2[1]

                if pygame.Rect.colliderect (ballrect1,ballrect2):
                        temp = [0,0]
                        for i in range (0,2):
                                temp[i] = speed1[i]
                                speed1[i] = speed2[i]
                                speed2[i] = temp[i]
                screen.blit(ball1,ballrect1)
                screen.blit(ball2,ballrect2)

                for button, position in game_button.items():
                        text_surface = my_font.render(button, True, white)
                        rect = text_surface.get_rect(center= position)
                        screen.blit(text_surface,rect)


                for event in pygame.event.get():
                        if(event.type is MOUSEBUTTONDOWN):
                                pos=pygame.mouse.get_pos()
                        elif(event.type is MOUSEBUTTONUP):
                                pos=pygame.mouse.get_pos()
                                x,y=pos
                                print str(pos)


                                if y>120:
                                        if x<100:
                                                print "pause"
                                                print counter1
                                                if (counter1%2==1):
                                                        for i in range (0,2):
                                                                speedt1[i]=speed1[i]
                                                                speedt2[i]=speed2[i]
                                                                speed1[i]=0
                                                                speed2[i]=0
                                                else:
                                                        for i in range(0,2):
                                                                speed1[i]=speedt1[i]
                                                                speed2[i]=speedt2[i]
                                                counter1 += 1
                                        elif x>=100 and x<160:
                                                speed1,speed2 = change_speed(speed1,speed2,2)
                                                print "faster"
                                        elif x>=160 and x<220:
                                                speed1,speed2 = change_speed(speed1,speed2,0.5)
                                                print "slower"
                                        else:
                                                second_page = False
                                                first_page=True
                                                print "back"
                                                screen.fill(black)
                                        #else:
                                                #flag = False
                                                #print "quit button is pressed"
                pygame.display.flip()
