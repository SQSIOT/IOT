import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
import socket
import os
import urllib2
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False)

#Read from TXT file
theFile = open("Enter_Distance.txt", "r")
theInts = []
for val in theFile.read().split():
    theInts.append(int(val))
theFile.close()
#Close


#Pin Defining
cam_data = "STOPBOT   "
TRIG = 23                                    #Associate pin 23 to TRIG
ECHO = 24                                    #Associate pin 24 to ECHO
Left_sensor = 6
middle_sensor = 13
Right_sensor = 5

M1P = 16                                     #Motor 1 terminal 1.
M1N = 20                                     #Motor 1 terminal 2.
M2P = 26                                     #Motor 2 terminal 1.
M2N = 19                                     #Motor 2 terminal 2.
Thr = theInts[0]                             #defining the threshold distance

print "Threshold", Thr,"cm"
print "Distance measurement in progress"

#Pin Setup as input/output
GPIO.setup(M1P, GPIO.OUT)    #motor A
GPIO.setup(M1N, GPIO.OUT)    #motor A
GPIO.setup(M2P, GPIO.OUT)    #motor B
GPIO.setup(M2N, GPIO.OUT)    #motor B
GPIO.setup(TRIG,GPIO.OUT)    #Set pin as GPIO out
GPIO.setup(ECHO,GPIO.IN)     #Set pin as GPIO in

#Initial status of GPIO pins used
GPIO.output(M1P,GPIO.LOW)
GPIO.output(M1N,GPIO.LOW)
GPIO.output(M2P,GPIO.LOW)
GPIO.output(M2N,GPIO.LOW)

GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Right sensor connection
GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Left sensor connection
GPIO.setup(middle_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #middle sensor connection

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

flag = 0

def MainOff():
    req = urllib2.Request('http://192.168.1.150/LED=OFF')
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print e.code
        print e.read()
    page = response.read()
    print page
    return;

def Main1ON():
    req = urllib2.Request('http://192.168.1.150/LED1=ON')
    response = urllib2.urlopen(req)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print e.code
        print e.read()
    page = response.read()
    print page
    return;

def MainON():
    req = urllib2.Request('http://192.168.1.150/LED=ON')
    response = urllib2.urlopen(req)
    try:
        response = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        print e.code
        print e.read()
    page = response.read()
    print page
    return;

def follow_cam():
    
    print"I was in follow cam"
    global flag
    flag = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1 = sock.connect(('192.168.1.160', 11001))
        
    try:
     sock.send("START")
     M1P.ChangeDutyCycle(25)
     M2P.ChangeDutyCycle(25)
     M1N.ChangeDutyCycle(0)
     M2N.ChangeDutyCycle(0)
     time.sleep(1)
     M1P.ChangeDutyCycle(0)
     M2P.ChangeDutyCycle(0)
     M1N.ChangeDutyCycle(0)
     M2N.ChangeDutyCycle(0)     
     while True:

        cam_data = sock.recv(11)
        data = sock.recv(1024)
        print"Camera Data: -", cam_data

        print"Client/Server data: -", data
        
#        i=GPIO.input(Left_sensor)   #Reading output of right IR sensor#left sensor turn left
#        j=GPIO.input(middle_sensor) #Reading output of left IR sensor#right sensor turn right
#        k=GPIO.input(Right_sensor)  #Reading output of middle IR sensor #forward
        i=GPIO.input(Left_sensor)       #Reading output of left IR sensor
        j=GPIO.input(middle_sensor)     #Reading output of middle IR sensor
        k=GPIO.input(Right_sensor)      #Reading output of right IR sensor



        print"Values of I J & k", i,j,k


        GPIO.output(TRIG, False)                   #Set TRIG as LOW
        #time.sleep(.5)
        GPIO.output(TRIG, True)                    #Set TRIG as HIGH
        time.sleep(0.00001)                         #Delay of 0.00001 seconds
        GPIO.output(TRIG, False)                   #Set TRIG as LOW

        timeout = time.time() + 0.05
        while GPIO.input(ECHO)==0 and time.time() < timeout:    #Check whether the ECHO is LOW
            pulse_start = time.time()                               #Saves the last known time of LOW pulse

        timeout = time.time() + 0.05
        while GPIO.input(ECHO)==1 and time.time() < timeout:    #Check whether the ECHO is HIGH
            pulse_end = time.time()                    #Saves the last known time of HIGH pulse

        pulse_duration = pulse_end - pulse_start   #Get pulse duration to a variable

        distance = pulse_duration * 17150          #Multiply pulse duration by 17150 to get distance

        if distance >= 2 and distance <= 400:      #Check whether the distance is within range
            

            if cam_data == "STOPBOT   " or distance < Thr or (i ==0 and j == 0):             #stop
              sock.send("STOP")
              print"Stop"
              M1P.ChangeDutyCycle(0)
              M2P.ChangeDutyCycle(0)
              M1N.ChangeDutyCycle(0)
              M2N.ChangeDutyCycle(0)
              if (i ==0 and j == 0 and k == 0):
                  flag += 1
                  if(flag > 2):
                      print "returning from follow cam"
                      break
                    
            elif (i == 0 and j== 0):                         #Stop  
              sock.send("STOP")
              M1P.ChangeDutyCycle(0)
              M2P.ChangeDutyCycle(0)
              M1N.ChangeDutyCycle(0)
              M2N.ChangeDutyCycle(0)

            elif (i == 1 and j ==0):                        #Right
              sock.send("RIGHT")  
              M1P.ChangeDutyCycle(20)
              M2P.ChangeDutyCycle(0)
              M1N.ChangeDutyCycle(0)
              M2N.ChangeDutyCycle(20)

            elif (i == 0 and j ==1):                        #Left
              sock.send("LEFT")  
              M1P.ChangeDutyCycle(0)
              M2P.ChangeDutyCycle(20)
              M1N.ChangeDutyCycle(20)
              M2N.ChangeDutyCycle(0)

            elif (i == 1 and j ==1):                        #forward
              sock.send("Forward")  
              M1P.ChangeDutyCycle(20)
              M2P.ChangeDutyCycle(20)
              M1N.ChangeDutyCycle(0)
              M2N.ChangeDutyCycle(0)

    finally:
     sock.close()

def d_to_p():
 print"I was in d to p"
 global flag
 flag = 0
 M1P.ChangeDutyCycle(30)
 M2P.ChangeDutyCycle(30)
 M1N.ChangeDutyCycle(0)
 M2N.ChangeDutyCycle(0)
 time.sleep(0.8)
 M1P.ChangeDutyCycle(0)
 M2P.ChangeDutyCycle(0)
 M1N.ChangeDutyCycle(0)
 M2N.ChangeDutyCycle(0)

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
       break

def p_to_s():
    print"I was in p to s"
    global flag
    flag = 0
    M1P.ChangeDutyCycle(40)
    M2P.ChangeDutyCycle(40)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(0)
    time.sleep(0.5)
    
    while True:
        i=GPIO.input(Left_sensor)       #Reading output of left IR sensor
        k=GPIO.input(middle_sensor)     #Reading output of middle IR sensor
        j=GPIO.input(Right_sensor)      #Reading output of right IR sensor
        #print"Values of I J & k", i,j,k
            
        print"Values of I J & k\n", i,j,k
        if i ==0 and j == 0 and k == 0:             #stop        
         print "Stop"
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         flag += 1
         if(flag > 5):
             print"returning from p to s"
             return;
        elif i ==0 and j == 0 and k == 1:             #left       
         print "left"
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(40)
         M1N.ChangeDutyCycle(40)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
         
        elif i ==0 and j == 1 and k == 0:             #left      
         print "left"
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(40)
         M1N.ChangeDutyCycle(40)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
         
        elif i ==0 and j == 1 and k == 1:             #left       
         print "left"
         M1P.ChangeDutyCycle(0)
         M2P.ChangeDutyCycle(40)
         M1N.ChangeDutyCycle(40)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.2)
        
        elif i ==1 and j == 0 and k == 0:             #right      
         print "right"
         M1P.ChangeDutyCycle(40)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(40)
         time.sleep(0.1)
        
        elif i ==1 and j == 0 and k == 1:             #forward      
         print "forward"
         M1P.ChangeDutyCycle(40)
         M2P.ChangeDutyCycle(40)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         
        elif i ==1 and j == 1 and k == 0:             #right      
         print "right"
         M1P.ChangeDutyCycle(40)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(40)
         time.sleep(0.1)
        
        elif i ==1 and j == 1 and k == 1:             #forward  
         print "left"
         M1P.ChangeDutyCycle(40)
         M2P.ChangeDutyCycle(0)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(40)
         time.sleep(0.1)
         M1P.ChangeDutyCycle(40)
         M2P.ChangeDutyCycle(40)
         M1N.ChangeDutyCycle(0)
         M2N.ChangeDutyCycle(0)
         time.sleep(0.1)
         
         #M1P.ChangeDutyCycle(10)
         #M2P.ChangeDutyCycle(10)
         ##M1N.ChangeDutyCycle(0)
         #M2N.ChangeDutyCycle(0)
         ##time.sleep(0.1)

try:
    p_to_s()
    MainOff()
    follow_cam()
    Main1ON()
    d_to_p()
    MainON()
    print"Thank you"

finally:
    GPIO.cleanup()
