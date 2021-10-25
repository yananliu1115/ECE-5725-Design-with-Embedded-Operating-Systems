import os
import pygame
import RPi.GPIO as GPIO
import time
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)
def GPIO27_callback(channel):
        print ('Falling detected on 27')
        GPIO.cleanup()
        exit(0)
GPIO.add_event_detect(27,GPIO.FALLING,callback=GPIO27_callback,bouncetime = 300)



os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')

pygame.init()

size = width,height = 320,240
black = 0,0,0

speed1 = [1,1]
speed2 = [-2,-2]


screen = pygame.display.set_mode(size)
ball1 = pygame.image.load('magic_ball.png')
ball2 = pygame.image.load('golf_ball.png')

ball1 = pygame.transform.scale(ball1,(40,40))
ball2 = pygame.transform.scale(ball2,(30,30))

ballrect1 = ball1.get_rect(center=[100,100])
ballrect2 = ball2.get_rect(center=[50,50])

while 1:
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
                #print ("coll")

                temp = [0,0]
                for i in range (0,2):
                        temp[i] = speed1[i]
                        speed1[i] = speed2[i]
                        speed2[i] = temp[i]
                #speed1[1] = - speed1[1]
                #speed2[1] = - speed2[1]



        screen.fill(black)

        screen.blit(ball1,ballrect1)
        screen.blit(ball2,ballrect2)
        pygame.display.flip()
