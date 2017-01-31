##Import Files

import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
import socket
import time
import os
from threading import Thread

path = '/home/pi/Desktop/Ambulance/Siren.m4a'
from subprocess import Popen


##Ultrasonic Sensor pin numbers
TRIG = 23                                    #Associate pin 23 to TRIG
ECHO = 24                                    #Associate pin 24 to Echo 

##IR sensor pin numbers
Left_sensor = 13
Right_sensor = 6
middle_sensor = 5

##Motor Pin numbers
M1P = 16                                     #Motor 1 terminal 1
M1N = 20                                     #Motor 1 terminal 2
M2P = 26                                     #Motor 2 terminal 1
M2N = 19                                     #Motor 2 terminal 2


#Pin Setup as input/output for ultrasonic sensor
GPIO.setup(TRIG,GPIO.OUT)                    #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                     #Set pin as GPIO in

#Pin Setup as input/output for Motors
GPIO.setup(M1P, GPIO.OUT)                    #motor A
GPIO.setup(M1N, GPIO.OUT)                    #motor A
GPIO.setup(M2P, GPIO.OUT)                    #motor B
GPIO.setup(M2N, GPIO.OUT)                    #motor B

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

#PWM start
M1P.start(0)
M2P.start(0)
M1N.start(0)
M2N.start(0)

#IR Sensor Pins declaration
GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    #Right sensor connection
GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   #Left sensor connection
GPIO.setup(middle_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #middle sensor connection

##Defining port
TCP_IP   = '192.168.163.10'
TCP_PORT = 30007


print"Connect signal app"
#Server for signal post
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
print"Connected ..."

def Get_Thr():
    #Read from TXT file for ultrasonic sensor to set thresold for ultrasonic sensor
    theFile = open("Enter Distance.txt", "r")
    theInts = []
    for val in theFile.read().split():
        theInts.append(int(val))
    theFile.close()
    #Close
    return theInts[0]                             #Getting threshold distance

flag     = True
flag1    = 0
dist     = 300
distance = 300
speed    = 25
speed2   = 23

def Ultrasonic():
    global dist
    global distance
    global speed
    global speed2
    
    while True:
        GPIO.output(TRIG, False)                   #Set TRIG as LOW
        time.sleep(.5)
        GPIO.output(TRIG, True)                    #Set TRIG as HIGH
        time.sleep(0.00001)                        #Delay of 0.00001 seconds
        GPIO.output(TRIG, False)                   #Set TRIG as LOW

        timeout = time.time() + 0.05
        while GPIO.input(ECHO)==0 and time.time() < timeout:                 #Check whether the ECHO is LOW
            pulse_start = time.time()                #Saves the last known time of LOW pulse

        timeout = time.time() + 0.05
        while GPIO.input(ECHO)==1 and time.time() < timeout:                 #Check whether the ECHO is HIGH
           pulse_end = time.time()                  #Saves the last known time of HIGH pulse
                
        pulse_duration = pulse_end - pulse_start   #Get pulse duration to a variable

        distance = pulse_duration * 17150          #Multiply pulse duration by 17150 to get distance
        
        if distance < 2 or distance > 400:
                distance = 300
        
        dist =round(distance)
        if dist<100 :
            speed1=(dist-10)/3
            speed = round(speed1)
            if speed >= 25:
                 speed =25
            elif speed < 10 and speed > 0:
                 speed  = 12
            elif speed < 0:
                 speed = 0
        else :
            speed=25
        print"Speed is", speed
    

def Stop():
    M1P.ChangeDutyCycle(0)
    M2P.ChangeDutyCycle(0)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(0)
    print "I was in stop"
    
##
def Park():
        print "parking"                 
        i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
        j=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
        if (i == 1 and j == 1):                 # moving left
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(35)
            M1N.ChangeDutyCycle(35)
            M2N.ChangeDutyCycle(0)
            time.sleep(0.9)  
        elif (i == 0 and j == 1):               # moving left
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(45)
            M1N.ChangeDutyCycle(45)
            M2N.ChangeDutyCycle(0)
            time.sleep(1.2)
        elif (i == 1 and j == 0):               # moving left
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(35)
            M1N.ChangeDutyCycle(35)
            M2N.ChangeDutyCycle(0)
            time.sleep(0.7)
        M1P.ChangeDutyCycle(20)
        M2P.ChangeDutyCycle(20)
        M1N.ChangeDutyCycle(0)
        M2N.ChangeDutyCycle(0)
        time.sleep(2)  


try:
    thread = Thread(target=Ultrasonic)
    thread.start()
except:
    print"Unable to start the thread"
    connection.close()
    GPIO.cleanup()
##
def amb_park():
    print "I was in parking car"
    out    = 0
    front  = 0
    speed1 = 8
    global speed2
    while True:
        if speed > 0:
            speed1 = speed
        else:
            speed1
        if(dist <= Thr):
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(0)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(0)            
    
        else:
            i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
            j=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor

            if (i == 0 and j == 0):                    # moving stop    
                M1P.ChangeDutyCycle(speed1)
                M2P.ChangeDutyCycle(speed1)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(0)

            elif (i == 0 and j == 1):                  # moving left
                M1P.ChangeDutyCycle(0)
                M2P.ChangeDutyCycle(speed2)
                M1N.ChangeDutyCycle(speed2)
                M2N.ChangeDutyCycle(0)
                time.sleep(0.1)
                 
            elif (i==1 and j == 0):                    # moving right
                M1P.ChangeDutyCycle(speed2)
                M2P.ChangeDutyCycle(0)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(speed2)
                time.sleep(0.1)
                out += 1
    
            elif (i == 1 and j == 1):                  # moving straight
                M1P.ChangeDutyCycle(speed1)
                M2P.ChangeDutyCycle(speed1)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(0)
                front += 1
                print"front", front
            if(front > 240 and out > 11 ):
                break
            speed1 += 2
            if(speed1 > 25):
                speed1 = 25


try:
  time.sleep(15)
  global flag
  global speed2
  Thr = Get_Thr()
  omx = Popen(['omxplayer', path])
  while True:
        print"distance is", dist

        i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
        j=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
##        k=GPIO.input(middle_sensor)
##        print i,j
        if(dist < Thr):
            Stop()
            if(flag):
                flag = False
                sock.send("green\n")
                Stop()
                amb_park()
                Park()
                os.system('sudo killall -s 9 omxplayer.bin')
                break
            
        elif(dist > Thr):                    
            if (i == 0 and j == 0):                    # moving stop    
                M1P.ChangeDutyCycle(speed)
                M2P.ChangeDutyCycle(speed)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(0)

            elif (i == 0 and j == 1):                  # moving left
                M1P.ChangeDutyCycle(0)
                M2P.ChangeDutyCycle(speed2)
                M1N.ChangeDutyCycle(speed2)
                M2N.ChangeDutyCycle(0)
        ##            time.sleep(0.1)
                 
            elif (i==1 and j == 0):                    # moving right
                M1P.ChangeDutyCycle(speed2)
                M2P.ChangeDutyCycle(0)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(speed2)
        ##      time.sleep(0.1)
                 
            elif (i == 1 and j == 1):                  # moving straight
                M1P.ChangeDutyCycle(speed)
                M2P.ChangeDutyCycle(speed)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(0)
        else:
            Stop()

finally:
 GPIO.cleanup()
 os.system('sudo killall -s 9 omxplayer.bin')   
