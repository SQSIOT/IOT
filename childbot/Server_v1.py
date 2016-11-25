import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)
import socket
import time

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

#server 1 for follower
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.168.1.160',11001))
sock.listen(1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
clientsocket, addr = sock.accept()

#Server 2 for Camera
cam = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cam.bind(('192.168.1.160',12001))
cam.listen(1)
cam.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
cam_sock, cam_addr = cam.accept()

flag = 0

def Motor(distance,i,j):
         
    if (i == 1 and j == 0):                  # moving left
       M1P.ChangeDutyCycle(17)
       M2P.ChangeDutyCycle(0)
       M1N.ChangeDutyCycle(0)
       M2N.ChangeDutyCycle(17)
       time.sleep(0.1)  
    elif (i==0 and j == 1):                    # moving right
       M1P.ChangeDutyCycle(0)
       M2P.ChangeDutyCycle(17)
       M1N.ChangeDutyCycle(17)
       M2N.ChangeDutyCycle(0)
       time.sleep(0.1)

    elif (i == 1 and j == 1):                  # moving straight
       M1P.ChangeDutyCycle(13)
       M2P.ChangeDutyCycle(13)
       M1N.ChangeDutyCycle(0)
       M2N.ChangeDutyCycle(0)
       #time.sleep(0.1)

    return;


try:
 follow_data = "Connected"   
 while True:  
  GPIO.output(TRIG, False)                   #Set TRIG as LOW
  time.sleep(.5)
  GPIO.output(TRIG, True)                    #Set TRIG as HIGH
  time.sleep(0.00001)                         #Delay of 0.00001 seconds
  GPIO.output(TRIG, False)                   #Set TRIG as LOW

  timeout = time.time() + 0.05
  while GPIO.input(ECHO)==0 and time.time() < timeout:                 #Check whether the ECHO is LOW
    pulse_start = time.time()                #Saves the last known time of LOW pulse

  timeout = time.time() + 0.05
  while GPIO.input(ECHO)==1 and time.time() < timeout:                 #Check whether the ECHO is HIGH
    pulse_end = time.time()                  #Saves the last known time of HIGH pulse

  pulse_duration = pulse_end - pulse_start   #Get pulse duration to a variable

  distance = pulse_duration * 17150          #Multiply pulse duration by 17150 to get distance

  if distance >= 2 and distance <= 400:       #Check whether the distance is within range
    print "Distance:", round(distance)
    i=GPIO.input(Left_sensor)                                    #Reading output of right IR sensor
    #k=GPIO.input(Right_sensor)                                   #Reading output of left IR sensor
    j=GPIO.input(middle_sensor)                                 #Reading output of middle IR sensor
    #print"Values of I J & k", i,j,k

    cam_data = cam_sock.recv(10)    
    data = clientsocket.recv(1024)

    
    cam_sock.send(data)
    
    clientsocket.send(cam_data)
    clientsocket.send(follow_data)
    
    print"Server data: -", follow_data
    print"Camera data: -", cam_data
    print"Client data: -", data
    
    if (i == 0 and j == 0):                                      #stop 
       if ((i == 0 and j == 0) and flag == 0) :
            M1P.ChangeDutyCycle(30)
            M2P.ChangeDutyCycle(30)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(0)
            flag += 1
       elif((i == 0 and j == 0) and flag > 0) :
            M1P.ChangeDutyCycle(0)
            M2P.ChangeDutyCycle(0)
            M1N.ChangeDutyCycle(0)
            M2N.ChangeDutyCycle(0)
            
    elif (distance < Thr) or  data == "STOP" :
        follow_data = "STOP"
        M1P.ChangeDutyCycle(0)
        M2P.ChangeDutyCycle(0)
        M1N.ChangeDutyCycle(0)
        M2N.ChangeDutyCycle(0)

    elif data == "LEFT":
      follow_data = "LEFT"
      Motor(distance,i,j)
    elif data == "RIGHT":
      follow_data = "RIGHT"
      Motor(distance,i,j)
    elif data == "Forward":
      follow_data = "Forward"
      Motor(distance,i,j)
     
finally:
 sock.close()
 GPIO.cleanup()
