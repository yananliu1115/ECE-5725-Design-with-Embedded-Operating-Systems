import time
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)

dc_list=[0,50,100]

f=50
print "frequency = " + str(f)
dc=0.0


p=GPIO.PWM(13,f)

GPIO.output(5,0)
GPIO.output(6,0)
p.start(dc)

GPIO.output(5,1)
for i in dc_list:
	print("clockwise")
	p.ChangeDutyCycle(i)
	print i
	time.sleep(3)
GPIO.output(5,0)

GPIO.output(6,1)
for i in dc_list:
	print("counterclockwise")
	p.ChangeDutyCycle(i)
	print i
	time.sleep(3)
GPIO.output(6,0)

p.ChangeDutyCycle(0)

while GPIO.input(27):
	pass

p.stop()
GPIO.cleanup()
