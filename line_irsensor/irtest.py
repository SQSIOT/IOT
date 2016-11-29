import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

#Pin Defining
Left_sensor = 6
Right_sensor = 5
M1P = 16                                     #Motor 1 terminal 1.
M1N = 20                                     #Motor 1 terminal 2.
M2P = 26                                     #Motor 2 terminal 1.
M2N = 19                                     #Motor 2 terminal 2.

#Pin Setup as input/output
GPIO.setup(M1P, GPIO.OUT)    #motor A
GPIO.setup(M1N, GPIO.OUT)    #motor A
GPIO.setup(M2P, GPIO.OUT)    #motor B
GPIO.setup(M2N, GPIO.OUT)    #motor B

#Initial status of GPIO pins used
GPIO.output(M1P,GPIO.LOW)
GPIO.output(M1N,GPIO.LOW)
GPIO.output(M2P,GPIO.LOW)
GPIO.output(M2N,GPIO.LOW)

GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Right sensor connection
GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Left sensor connection

#Start PWM to reduce speed of the motor
M1P = GPIO.PWM(M1P , 30)
M2P = GPIO.PWM(M2P , 30)
M1N = GPIO.PWM(M1N , 30)
M2N = GPIO.PWM(M2N , 30)
#PWM started with zero PWm
M1P.start(0)
M2P.start(0)
M1N.start(0)
M2N.start(0)

    
try:   
 while True:
    i=GPIO.input(Left_sensor)                          #Reading output of right IR sensor
    j=GPIO.input(Right_sensor)                         #Reading output of left IR sensor
    print"Values of I & J", i,j

    if i ==0 and j == 0:
     print "Stop"
     M1P.ChangeDutyCycle(0)
     M2P.ChangeDutyCycle(0)
     M1N.ChangeDutyCycle(0)
     M2N.ChangeDutyCycle(0)
     time.sleep(0.1)
    elif i == 1 and j == 0:                              #Right IR sensor detects an object
     print "moving Left",i
     M1P.ChangeDutyCycle(20)
     M2P.ChangeDutyCycle(0)
     M1N.ChangeDutyCycle(0)
     M2N.ChangeDutyCycle(20)
     time.sleep(0.1)
    elif i==0 and j == 1:                              #Left IR sensor detects an object
     print "moving Right",j
     M1P.ChangeDutyCycle(0)
     M2P.ChangeDutyCycle(20)
     M1N.ChangeDutyCycle(20)
     M2N.ChangeDutyCycle(0)
     time.sleep(0.9)
    elif i == 1 and j == 1:
     M1P.ChangeDutyCycle(20)
     M2P.ChangeDutyCycle(20)
     M1N.ChangeDutyCycle(0)
     M2N.ChangeDutyCycle(0)
     print "moving straight",i,j
     time.sleep(0.1)

finally:
 GPIO.cleanup()

