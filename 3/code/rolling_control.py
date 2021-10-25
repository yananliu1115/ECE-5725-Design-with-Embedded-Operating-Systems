import time
import RPi.GPIO as GPIO
import os
import pygame
import subprocess
from pygame.locals import *
from collections import deque
from timeit import timeit

code_run = time.time()
time_start = time.time()
flag=True

os.putenv('SDL_VIDEODRIVER', 'fbcon') #display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb1') 
os.putenv('SDL_MOUSEDRV', 'TSLIB') #track mouse click on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen') 

pygame.init()
pygame.mouse.set_visible(False)


GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT) #A pwm
GPIO.setup(16,GPIO.OUT) #B pwm
GPIO.setup(5,GPIO.OUT)  #A
GPIO.setup(6,GPIO.OUT)
GPIO.setup(20,GPIO.OUT) #B
GPIO.setup(21,GPIO.OUT)

GPIO.setmode(GPIO.BCM)


black = 0,0,0
white = 255,255,255
screen = pygame.display.set_mode((320,240))
my_font=pygame.font.Font(None,25)
dire_font = pygame.font.Font(None,20)
components={'Left History':(60,25),'Right History':(260,25),'quit':(250,200)}
screen.fill(black)

#button init
#left
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)#stop
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)#cw
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#ccw

#right
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)#stop
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)#cw
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)#ccw

#init f, dc, state
f=50
print "frequency = " + str(f)
dc=50.0
counter = 0
text=["Stop","Resume"]

#init ordered direction
left_log = deque([])
left_log.append(("Stop",0))
left_log.append(("Stop",0))
left_log.append(("Stop",0))
right_log = deque([])
right_log.append(("Stop",0))
right_log.append(("Stop",0))
right_log.append(("Stop",0))

left_coord=[(65,60),(65,100),(65,140)]
right_coord=[(255,60),(255,100),(255,140)]

pl=GPIO.PWM(13,f)#l
pr=GPIO.PWM(16,f)#r

left_his=0
right_his=0

def wheel_control(motor,mode):
	if motor == 1:
		left_his=mode
		if mode == 0:#l_stop
			pl.stop()
		elif mode == 1: #l_cw
			GPIO.output(5,1)
			GPIO.output(6,0)
			pl.start(dc)
		elif mode==2: #l_ccw
			GPIO.output(5,0)
			GPIO.output(6,1)
			pl.start(dc)
	elif motor == 2:
		right_his=mode
		if mode == 0:#r_stop
			pr.stop()
		elif mode == 1: #r_cw
			GPIO.output(20,1)
			GPIO.output(21,0)
			pr.start(dc)
		elif mode==2: #r_cww
			GPIO.output(20,0)
			GPIO.output(21,1)
			pr.start(dc)

while time.time()-code_run<100 and flag:
	screen.fill(black)
	for button, position in components.items():
		text_surface = my_font.render(button, True, white)
		rect = text_surface.get_rect(center= position)
		screen.blit(text_surface,rect)
		
	if counter%2==0:
		pygame.draw.circle(screen,(255,0,0),(160,120),40)
		print left_his
		print right_his
		wheel_control(1,left_his)
		wheel_control(2,right_his)
		
		time.sleep(0.2)
		if (not GPIO.input(27)) and (not GPIO.input(23)):
			print "quit"
			break
		if (not GPIO.input(17)):
			print(" ")
			wheel_control(1,0)
			left_his = 0
			left_log.appendleft(("stop",int(time.time()-time_start)))
			left_log.pop()
			print "left wheel stop.."
		elif (not GPIO.input(22)):
			print(" ")
			wheel_control(1,1)
			left_his = 1
			left_log.appendleft(("CLK",int(time.time()-time_start)))
			left_log.pop()
			print "left wheel cw"
		elif (not GPIO.input(23)):
			print(" ")
			wheel_control(1,2)
			left_his = 2
			left_log.appendleft(("CCLK",int(time.time()-time_start)))
			left_log.pop()
			print "left wheel ccw"
		elif (not GPIO.input(27)):
			print(" ")
			wheel_control(2,0)
			right_his=0
			right_log.appendleft(("stop",int(time.time()-time_start)))
			right_log.pop()
			print "right wheel stop"
		elif (not GPIO.input(19)):
			print(" ")
			wheel_control(2,1)
			right_his=1
			right_log.appendleft(("CLK",int(time.time()-time_start)))
			right_log.pop()
			print "right wheel cw"
		elif (not GPIO.input(26)):
			print(" ")
			wheel_control(2,2)
			right_his=2
			right_log.appendleft(("CCLK",int(time.time()-time_start)))
			right_log.pop()
			print "right wheel ccw"
		
	else:
		pygame.draw.circle(screen,(0,255,0),(160,120),40)
		
		wheel_control(1,0)
		wheel_control(2,0)
	text_surface1 = my_font.render(text[counter%2], True, white)
	rect = text_surface1.get_rect(center= [160,120])
	screen.blit(text_surface1,rect)

	for event in pygame.event.get():
		screen.fill(black)
		if(event.type is MOUSEBUTTONDOWN):
			pos=pygame.mouse.get_pos()
		elif(event.type is MOUSEBUTTONUP):
			pos=pygame.mouse.get_pos()
			x,y=pos
			print str(pos)
			if y>80 and y<200 and x>120 and x<200:
				print counter
				counter+=1
			if y>180 and x>240:
			    print "quit"
			    flag = False
				
	for i in range (3):
		direction = left_log[i][0]
		left_time = left_log[i][1]			
		text_surface1 = dire_font.render(direction + "   "+ str(left_time), True, white)		
		rect = text_surface1.get_rect(center=left_coord[i])
		screen.blit(text_surface1,rect)
	for i in range (3):
		direction = right_log[i][0]
		right_time = right_log[i][1]			
		text_surface1 = dire_font.render(direction + "   "+ str(right_time), True, white)		
		rect = text_surface1.get_rect(center=right_coord[i])
		screen.blit(text_surface1,rect)			
				
	
	
	pygame.display.flip()

pl.stop()
pr.stop()
GPIO.cleanup()

