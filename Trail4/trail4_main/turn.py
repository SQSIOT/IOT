import time                                  #Import time library
import cv2
import numpy as np
##Motor settings
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)


Left_sensor = 13
Right_sensor = 6
GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #left sensor connection
GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #right sensor connection


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

#Start PWM to reduce speed of the motor
M1P = GPIO.PWM(M1P , 50)
M2P = GPIO.PWM(M2P , 50)
M1N = GPIO.PWM(M1N , 50)
M2N = GPIO.PWM(M2N , 50)
#PWM started with zero PWm
M1P.start(0)
M2P.start(0)
M1N.start(0)
M2N.start(0)

def Park():
     while True:
          i=GPIO.input(Left_sensor)  #Reading output of right IR sensor
          j=GPIO.input(Right_sensor) #Reading output of right IR sensor
          if(i == 0 and j == 1):
               print"In i =0 and j = 1"
               M1P.ChangeDutyCycle(0)
               M2P.ChangeDutyCycle(60)
               M1N.ChangeDutyCycle(60)
               M2N.ChangeDutyCycle(0)
               time.sleep(0.7)
               
          elif(i == 1 and j == 0):
               print"In i = 1 and j = 0"
               M1P.ChangeDutyCycle(0)
               M2P.ChangeDutyCycle(60)
               M1N.ChangeDutyCycle(60)
               M2N.ChangeDutyCycle(0)
               time.sleep(0.5)
               
          elif(i == 1 and j == 1):
               print"In i = 1 and j = 1"
               M1P.ChangeDutyCycle(0)
               M2P.ChangeDutyCycle(55)
               M1N.ChangeDutyCycle(55)
               M2N.ChangeDutyCycle(0)
               time.sleep(0.6)

def Lane(): 
     try:
          flag = 0
          print "Forward"
          M1P.ChangeDutyCycle(25)
          M2P.ChangeDutyCycle(25)
          M1N.ChangeDutyCycle(0)
          M2N.ChangeDutyCycle(0)
          time.sleep(4)
          while True:
               i=GPIO.input(Left_sensor)  #Reading output of right IR sensor
               j=GPIO.input(Right_sensor) #Reading output of right IR sensor
               if(i == 0 and j == 1):
                    print"In i =0 and j = 1"
                    M1P.ChangeDutyCycle(55)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(55)
                    time.sleep(0.6)
                    break

               elif(i == 1 and j == 0):
                    print"In i = 1 and j = 0"
                    M1P.ChangeDutyCycle(60)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(60)
                    time.sleep(0.8)
                    break
               elif(i == 1 and j == 1):
     ##               print"In i = 1 and j = 1"
                    M1P.ChangeDutyCycle(55)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(55)
                    time.sleep(0.7)
                    break
##          M1P.ChangeDutyCycle(0)
##          M2P.ChangeDutyCycle(0)
##          M1N.ChangeDutyCycle(0)
##          M2N.ChangeDutyCycle(0)     
##          time.sleep(1)
          M1P.ChangeDutyCycle(30)
          M2P.ChangeDutyCycle(30)
          M1N.ChangeDutyCycle(0)
          M2N.ChangeDutyCycle(0)
          time.sleep(3)
     ##     print "Left"
          M1P.ChangeDutyCycle(0)
          M2P.ChangeDutyCycle(40)
          M1N.ChangeDutyCycle(40)
          M2N.ChangeDutyCycle(0)
          time.sleep(1.7)
     ##     print "stop"
          M1P.ChangeDutyCycle(0)
          M2P.ChangeDutyCycle(0)
          M1N.ChangeDutyCycle(0)
          M2N.ChangeDutyCycle(0)
          time.sleep(10)   
     ##     print "forward"
          while True:
               i=GPIO.input(Left_sensor)  #Reading output of right IR sensor
               j=GPIO.input(Right_sensor) #Reading output of right IR sensor
               print"I was in turing the bot right "
               if( i == 1 and j == 1):
                    M1P.ChangeDutyCycle(20)
                    M2P.ChangeDutyCycle(20)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    
               elif(i == 0 and j == 1):
                    M1P.ChangeDutyCycle(30)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(30)
                    time.sleep(0.6)
                    M1P.ChangeDutyCycle(20)
                    M2P.ChangeDutyCycle(20)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    break
               elif(i == 1 and j == 0):
                    M1P.ChangeDutyCycle(30)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(30)
                    time.sleep(0.6)

                    M1P.ChangeDutyCycle(20)
                    M2P.ChangeDutyCycle(20)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    break                         
               elif(i == 0 and j == 0):
                    M1P.ChangeDutyCycle(30)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(30)
                    time.sleep(0.6)
                    M1P.ChangeDutyCycle(20)
                    M2P.ChangeDutyCycle(20)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    break

          while(1):

               i=GPIO.input(Left_sensor)  #Reading output of right IR sensor
               j=GPIO.input(Right_sensor) #Reading output of right IR sensor   
         
               if (i == 1 and j == 1):
                    print"forward"
                    M1P.ChangeDutyCycle(30)
                    M2P.ChangeDutyCycle(30)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    
               elif (i == 1 and j == 0):
                    print"right"     
                    M1P.ChangeDutyCycle(20)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(20)
                    
               elif (i == 0 and j == 1):
                    print"left1"
                    M1P.ChangeDutyCycle(0)
                    M2P.ChangeDutyCycle(20)
                    M1N.ChangeDutyCycle(20)
                    M2N.ChangeDutyCycle(0)

               elif (i == 0 and j == 0):
                    M1P.ChangeDutyCycle(0)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    print "Breaking out"
                    break

     finally:
         GPIO.cleanup()
