##Import Files

import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
import socket
from threading import Thread
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
speed1   = 25
speed_control = 0

##Defining port
TCP_IP   = '192.168.161.97'
TCP_PORT = 60001


print"Connect signal app"
#Server for signal post
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((TCP_IP, TCP_PORT))
print"Connected ..."


def Ultrasonic():
    global dist
    global distance
    global speed
    
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
##        print"Speed is", speed

def Send_Data():
    global data
    while True:
        data = sock.recv(4)
        time.sleep(0.1)
        sock.send("ok")
        time.sleep(0.1)
        print data

try:
    thread  = Thread(target=Ultrasonic)
    thread2 = Thread(target=Send_Data)
    thread2.start()
    thread.start()
except:
    print"Unable to start the thread"
    connection.close()
    GPIO.cleanup()
    sock.close()
    
def Stop():
    M1P.ChangeDutyCycle(0)
    M2P.ChangeDutyCycle(0)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(0)


try:
    Thr = Get_Thr()
    global speed1
    global speed_control
    time.sleep(13)
    end = False
    while True:
#        print"Speed", speed
#        print"distance", dist
                
        i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
        j=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
        k=GPIO.input(middle_sensor)

        if end:
            break

        if dist < Thr:
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(0)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(0)

        elif data == "maaa":
            if (i == 0 and j == 0):                    # moving stop        
                M1P.ChangeDutyCycle(speed - speed_control)
                M2P.ChangeDutyCycle(speed - speed_control)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(0)

            elif (i == 0 and j == 1):                  # moving left
                M1P.ChangeDutyCycle(0)
                M2P.ChangeDutyCycle(speed1)
                M1N.ChangeDutyCycle(speed1)
                M2N.ChangeDutyCycle(0)
                time.sleep(0.1)
             
            elif (i==1 and j == 0):                    # moving right
                M1P.ChangeDutyCycle(speed1)
                M2P.ChangeDutyCycle(0)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(speed1)
                time.sleep(0.1)
             
            elif (i == 1 and j == 1):                  # moving straight
                M1P.ChangeDutyCycle(speed - speed_control)
                M2P.ChangeDutyCycle(speed - speed_control)
                M1N.ChangeDutyCycle(0)
                M2N.ChangeDutyCycle(0)

        elif(data == "park"):
            flag = False
            out = 0
            while True:
                
                print"Destination"
                print"out", out
                i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
                j=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor

                if(out > 20):
                    end = True
                    break
                
                if (i == 0 and j == 0):                    # moving stop
##                    print"Need to turn",i,j
                    M1P.ChangeDutyCycle(25)
                    M2P.ChangeDutyCycle(25)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    time.sleep(0.5)
                    M1P.ChangeDutyCycle(0)
                    M2P.ChangeDutyCycle(30)
                    M1N.ChangeDutyCycle(30)
                    M2N.ChangeDutyCycle(0)
                    time.sleep(0.9)
                    M1P.ChangeDutyCycle(25)
                    M2P.ChangeDutyCycle(25)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    time.sleep(1)
                    flag = True
                    
                elif (i == 0 and j == 1):                  # moving left
##                    print"Need to turn Left",i,j
                    M1P.ChangeDutyCycle(0)
                    M2P.ChangeDutyCycle(speed1)
                    M1N.ChangeDutyCycle(speed1)
                    M2N.ChangeDutyCycle(0)
                    time.sleep(0.1)
                    if(flag):
                        out += 1
                 
                elif (i==1 and j == 0):                    # moving right
##                    print"Need to turn Right",i,j
                    M1P.ChangeDutyCycle(speed1)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(speed1)
                    time.sleep(0.1)
                    if(flag):
                        out += 1                 
                elif (i == 1 and j == 1):                  # moving straight
##                    print"Need to turn Forward",i,j
                    M1P.ChangeDutyCycle(speed - speed_control)
                    M2P.ChangeDutyCycle(speed - speed_control)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    if(flag):
                        out += 1

            while True:
                print"Parking"
                i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
                j=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor

                if (i == 0 and j == 0):                    # moving stop
                    M1P.ChangeDutyCycle(0)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    print"For final park"
                    M1P.ChangeDutyCycle(20)
                    M2P.ChangeDutyCycle(20)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    time.sleep(1.6)
                    M1P.ChangeDutyCycle(0)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
                    time.sleep(0.3)
                    break                    
                elif (i == 0 and j == 1):                  # moving left
##                    print"Parking turn Left"
                    M1P.ChangeDutyCycle(0)
                    M2P.ChangeDutyCycle(speed1)
                    M1N.ChangeDutyCycle(speed1)
                    M2N.ChangeDutyCycle(0)
                    time.sleep(0.1)
                 
                elif (i==1 and j == 0):                    # moving right
##                    print"Parking turn Right"
                    M1P.ChangeDutyCycle(speed1)
                    M2P.ChangeDutyCycle(0)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(speed1)
                    time.sleep(0.1)
                 
                elif (i == 1 and j == 1):                  # moving straight
##                    print"Parking Forward"
                    M1P.ChangeDutyCycle(speed - speed_control)
                    M2P.ChangeDutyCycle(speed - speed_control)
                    M1N.ChangeDutyCycle(0)
                    M2N.ChangeDutyCycle(0)
        
finally:
 GPIO.cleanup()
 sock.close() 
