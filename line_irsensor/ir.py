
import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

#Pin Defining
Left_sensor = 6
Right_sensor = 13
LM1P = 16                                     #Motor 1 terminal 1.
LM1N = 20                                     #Motor 1 terminal 2.
RM2P = 26                                     #Motor 2 terminal 1.
RM2N = 19                                     #Motor 2 terminal 2.

#Pin Setup as input/output

GPIO.output(M1P,GPIO.LOW)
GPIO.output(M1N,GPIO.LOW)
GPIO.output(M2P,GPIO.LOW)
GPIO.output(M2N,GPIO.LOW)
GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Right sensor connection
GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)  #Left sensor connection

M1 = GPIO.PWM(M1P , 50)
M2 = GPIO.PWM(M2P , 50)

M1.start(0)
M2.start(0)


#Motor Setup
#        if(motor == 0):
#            M1.ChangeDutyCycle(0)
#            M2.ChangeDutyCycle(0)
#        if(motor == 1):
#            M1.ChangeDutyCycle(35)
#            M2.ChangeDutyCycle(35)
    
try:   
 while True:
    i=GPIO.input(Left_sensor)                          #Reading output of right IR sensor
    j=GPIO.input(Right_sensor)                         #Reading output of left IR sensor
    if i == 1 and j == 0:                                 #Right IR sensor detects an object
     print "moving Right",i
     time.sleep(0.1)
    elif i==0 and j == 1:                               #Left IR sensor detects an object
     print "moving Left",j
     time.sleep(0.1)
    elif i == 1 and j == 1:
     print "moving straight"

finally:
 GPIO.cleanup()
     
               
