import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
import webbrowser

GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

#Pin Defining
Left_sensor = 6
middle_sensor = 13
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
GPIO.setup(middle_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #middle sensor connection

#Start PWM to reduce speed of the motor
M1P = GPIO.PWM(M1P , 40)
M2P = GPIO.PWM(M2P , 40)
M1N = GPIO.PWM(M1N , 40)
M2N = GPIO.PWM(M2N , 40)
#PWM started with zero PWm
M1P.start(0)
M2P.start(0)
M1N.start(0)
M2N.start(0)
flag = 0

try:

 while True:
    i=GPIO.input(Left_sensor)   #Reading output of left IR sensor
    j=GPIO.input(middle_sensor) #Reading output of middle IR sensor
    k=GPIO.input(Right_sensor)  #Reading output of right IR sensor                                                    
    print"Values of I J & k", i,j,k
    print flag
       
    if (i == 1 and j == 0):                  # moving right
       M1P.ChangeDutyCycle(40)
       M2P.ChangeDutyCycle(0)
       M1N.ChangeDutyCycle(0)
       M2N.ChangeDutyCycle(40)
         
    elif (i==0 and j == 1):                    # moving left
        M1P.ChangeDutyCycle(0)
        M2P.ChangeDutyCycle(40)
        M1N.ChangeDutyCycle(40)
        M2N.ChangeDutyCycle(0)
         
    elif (i == 1 and j == 1):                  # moving straight
       M1P.ChangeDutyCycle(40)
       M2P.ChangeDutyCycle(40)
       M1N.ChangeDutyCycle(0)
       M2N.ChangeDutyCycle(0)
       
    if ( i == 0 and j == 0 and k == 0 and flag < 5 ):         #
        M1P.ChangeDutyCycle(0)              
        M2P.ChangeDutyCycle(40)
        M1N.ChangeDutyCycle(40)
        M2N.ChangeDutyCycle(0)
        flag += 1
        time.sleep(0.1)
    if((i == 1 and (k == 0) and j == 0 )):      #
       M1P.ChangeDutyCycle(40)
       M2P.ChangeDutyCycle(40)
       M1N.ChangeDutyCycle(0)
       M2N.ChangeDutyCycle(0)

    if flag >= 5:
       M1P.ChangeDutyCycle(0)
       M2P.ChangeDutyCycle(0)
       M1N.ChangeDutyCycle(0)
       M2N.ChangeDutyCycle(0)
       
finally:
 GPIO.cleanup()
