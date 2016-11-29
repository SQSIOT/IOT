import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
import socket
import time

#AMBULANCE SOUND
path = '/home/pi/Desktop/Ambulance/siren.mp3'
from subprocess import Popen

#Read from TXT file
theFile = open("Enter Distance.txt", "r")
theInts = []
for val in theFile.read().split():
    theInts.append(int(val))
theFile.close()
#Close

#Sensor and Motor Pin Defining

TRIG = 23                                    #Associate pin 23 to TRIG
ECHO = 24                                    #Associate pin 24 to Echo 
Thr = theInts[0]                             #defining the threshold distance
Left_sensor = 6
Right_sensor = 13
middle_sensor = 5
M1P = 16                                     #Motor 1 terminal 1
M1N = 20                                     #Motor 1 terminal 2
M2P = 26                                     #Motor 2 terminal 1
M2N = 19                                     #Motor 2 terminal 2


#Pin Setup as input/output
GPIO.setup(TRIG,GPIO.OUT)                    #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)                     #Set pin as GPIO in
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

#PWM started with zero PWm
M1P.start(0)
M2P.start(0)
M1N.start(0)
M2N.start(0)

GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    #Right sensor connection
GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)   #Left sensor connection
GPIO.setup(middle_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #middle sensor connection

            
try:

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
    if distance < 2 and distance > 400:
        distance = 300
        
    if distance >= 2 and distance <= 400:      #Check whether the distance is within range
        print "Distance:", round(distance)
        omx = Popen(['omxplayer', path])
##        
##        data = clientsocket.recv(10)   
##        clientsocket.send("ACK")    
##        print"Client data: -", data
                          
        i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
        k=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
        j=GPIO.input(middle_sensor)

        if(distance <= Thr):
            break
        
        if (i == 0 and j == 0):                    # moving stop    
            M1P.ChangeDutyCycle(25)
            M2P.ChangeDutyCycle(25)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(0)

        elif (i == 1 and j == 0):                  # moving left
            M1P.ChangeDutyCycle(20)
            M2P.ChangeDutyCycle(0)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(20)
       #     time.sleep(0.1)
         
        elif (i==0 and j == 1):                    # moving right
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(20)
            M1N.ChangeDutyCycle(20)
            M2N.ChangeDutyCycle(0)
        #    time.sleep(0.1)
         
        elif (i == 1 and j == 1):                  # moving straight
            M1P.ChangeDutyCycle(25)
            M2P.ChangeDutyCycle(25)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(0)


   
  i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
  k=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
  j=GPIO.input(middle_sensor)                                 #Reading output of middle IR sensor
  
  if j == 0 :
      M1P.ChangeDutyCycle(35)
      M2P.ChangeDutyCycle(0)
      M1N.ChangeDutyCycle(0)
      M2N.ChangeDutyCycle(35)
      time.sleep(0.6)
  if i == 0 :
      M1P.ChangeDutyCycle(35)
      M2P.ChangeDutyCycle(0)
      M1N.ChangeDutyCycle(0)
      M2N.ChangeDutyCycle(35)
      time.sleep(0.4)
  if k == 0 :
      M1P.ChangeDutyCycle(35)
      M2P.ChangeDutyCycle(0)
      M1N.ChangeDutyCycle(0)
      M2N.ChangeDutyCycle(35)
      time.sleep(0.5)
  if (i == 1 and j ==1 and k == 1):  
      M1P.ChangeDutyCycle(35)
      M2P.ChangeDutyCycle(0)
      M1N.ChangeDutyCycle(0)
      M2N.ChangeDutyCycle(35)
      time.sleep(0.4)


  flag = 0      
  omx = Popen(['omxplayer', path])
  while True:
            i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
            k=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
            j=GPIO.input(middle_sensor)                                 #Reading output of middle IR sensor
            print"Values of I J & k", i,j,k

            if(i == 0 and k == 0 and j ==0):
              M1P.ChangeDutyCycle(0)
              M2P.ChangeDutyCycle(35)
              M1N.ChangeDutyCycle(35)
              M2N.ChangeDutyCycle(0)
              time.sleep(0.4)
            
            if (i == 0 and j == 0):                    # moving stop    
                   M1P.ChangeDutyCycle(0)
                   M2P.ChangeDutyCycle(0)
                   M1N.ChangeDutyCycle(0)
                   M2N.ChangeDutyCycle(0)

            elif (i == 1 and j == 0):                  # moving left
                   M1P.ChangeDutyCycle(25)
                   M2P.ChangeDutyCycle(0)
                   M1N.ChangeDutyCycle(0)
                   M2N.ChangeDutyCycle(25)
             
            elif (i==0 and j == 1):                    # moving right
                   M1P.ChangeDutyCycle(0)
                   M2P.ChangeDutyCycle(25)
                   M1N.ChangeDutyCycle(25)
                   M2N.ChangeDutyCycle(0)
             
            elif (i == 1 and j == 1):                  # moving straight
                   M1P.ChangeDutyCycle(25)
                   M2P.ChangeDutyCycle(25)
                   M1N.ChangeDutyCycle(0)
                   M2N.ChangeDutyCycle(0)
                   flag += 1
                   if flag >= 70:
                      M1P.ChangeDutyCycle(0)
                      M2P.ChangeDutyCycle(0)
                      M1N.ChangeDutyCycle(0)
                      M2N.ChangeDutyCycle(0)
                      print "Stopped"
                      break
            
  time.sleep(0.2)
  if j == 0 :
      M1P.ChangeDutyCycle(0)
      M2P.ChangeDutyCycle(35)
      M1N.ChangeDutyCycle(35)
      M2N.ChangeDutyCycle(0)
      time.sleep(0.4)
  if i == 0 :
      M1P.ChangeDutyCycle(0)
      M2P.ChangeDutyCycle(35)
      M1N.ChangeDutyCycle(35)
      M2N.ChangeDutyCycle(0)
      time.sleep(0.6)
  if k == 0 :
      M1P.ChangeDutyCycle(0)
      M2P.ChangeDutyCycle(35)
      M1N.ChangeDutyCycle(35)
      M2N.ChangeDutyCycle(0)
      time.sleep(0.5)
  if (i == 1 and j ==1 and k == 1):  
      M1P.ChangeDutyCycle(0)
      M2P.ChangeDutyCycle(35)
      M1N.ChangeDutyCycle(35)
      M2N.ChangeDutyCycle(0)
      time.sleep(0.5)


  flag = 0
  omx = Popen(['omxplayer', path])
  while True:
            i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
            k=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
            j=GPIO.input(middle_sensor)                                  #Reading output of middle IR sensor
            print"Values of I J & k", i,j,k


            if(i == 0 and k == 0 and j ==0):
              M1P.ChangeDutyCycle(35)
              M2P.ChangeDutyCycle(0)
              M1N.ChangeDutyCycle(0)
              M2N.ChangeDutyCycle(35)
              time.sleep(0.4)
    

            elif (i == 1 and j == 0):                  # moving left
                   M1P.ChangeDutyCycle(25)
                   M2P.ChangeDutyCycle(0)
                   M1N.ChangeDutyCycle(0)
                   M2N.ChangeDutyCycle(25)
                   
             
            elif (i==0 and j == 1):                    # moving right
                   M1P.ChangeDutyCycle(0)
                   M2P.ChangeDutyCycle(25)
                   M1N.ChangeDutyCycle(25)
                   M2N.ChangeDutyCycle(0)
    
             
            elif (i == 1 and j == 1):                  # moving straight
                   M1P.ChangeDutyCycle(25)
                   M2P.ChangeDutyCycle(25)
                   M1N.ChangeDutyCycle(0)
                   M2N.ChangeDutyCycle(0)
                   flag += 1
                   if flag >= 20:
                       break
  omx = Popen(['omxplayer', path])
  while True :
        i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
        k=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
        j=GPIO.input(middle_sensor)

        if (i == 0 and j == 0):                    # moving stop    
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(0)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(0)

        elif (i == 1 and j == 0):                  # moving left
            M1P.ChangeDutyCycle(25)
            M2P.ChangeDutyCycle(0)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(25)
            time.sleep(0.1)
         
        elif (i==0 and j == 1):                    # moving right
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(25)
            M1N.ChangeDutyCycle(25)
            M2N.ChangeDutyCycle(0)
            time.sleep(0.1)
         
        elif (i == 1 and j == 1):                  # moving straight
            M1P.ChangeDutyCycle(25)
            M2P.ChangeDutyCycle(25)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(0)
finally:
 GPIO.cleanup()
