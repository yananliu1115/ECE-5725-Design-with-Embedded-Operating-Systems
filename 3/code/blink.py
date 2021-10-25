import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)


GPIO_pin=13
f=1
dc=50.0

p=GPIO.PWM(GPIO_pin,f)
p.start(dc)

while GPIO.input(27):
	pass

p.stop()
GPIO.cleanup()
