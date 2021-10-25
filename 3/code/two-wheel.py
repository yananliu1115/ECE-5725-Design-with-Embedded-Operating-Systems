import time
import RPi.GPIO as GPIO

time_start = time.time()
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT) #A pwm
GPIO.setup(16,GPIO.OUT) #B pwm
GPIO.setup(5,GPIO.OUT)  #A
GPIO.setup(6,GPIO.OUT)
GPIO.setup(20,GPIO.OUT) #B
GPIO.setup(21,GPIO.OUT)
GPIO.setup(27,GPIO.IN,pull_up_down = GPIO.PUD_UP)

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

pl=GPIO.PWM(13,f)#l
pr=GPIO.PWM(16,f)#r

def wheel_control(motor,mode):
	if motor == 1:
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
			
#main
while time.time()-time_start<60:
    time.sleep(0.2)
    if (not GPIO.input(17)):
        print(" ")
        wheel_control(1,0)
        print "left wheel stop.."
    elif (not GPIO.input(22)):
        print(" ")
        wheel_control(1,1)
        print "left wheel cw"
    elif (not GPIO.input(23)):
        print(" ")
        wheel_control(1,2)
        print "left wheel ccw"
    elif (not GPIO.input(27)):
        print(" ")
        wheel_control(2,0)
        print "right wheel stop"
    elif (not GPIO.input(19)):
        print(" ")
        wheel_control(2,1)
        print "right wheel cw"
    elif (not GPIO.input(26)):
        print(" ")
        wheel_control(2,2)
        print "right wheel ccw"
    if (not GPIO.input(27)) and (not GPIO.input(23)):
	print "quit"
	break

pl.stop()
pr.stop()		
GPIO.cleanup()
