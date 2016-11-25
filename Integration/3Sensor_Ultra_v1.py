import RPi.GPIO as GPIO                             #Import GPIO library
import time                                         #Import time library
import socket
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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1 = sock.connect(('192.168.1.160', 11001))

    
try:
 sock.send("START")  
 while True:
    i=GPIO.input(Left_sensor)   #Reading output of right IR sensor
    j=GPIO.input(middle_sensor) #Reading output of left IR sensor
    k=GPIO.input(Right_sensor)  #Reading output of middle IR sensor                        
                                 
    #print"Values of I J & k", i,j,k
    cam_data = sock.recv(11)
   # if cam_data == 'STOPBOT   ' :
#	i = 0
#	j = 0
#	k = 0
  
    data = sock.recv(1024)
    print"Camera Data: -", cam_data

    if cam_data == "STOPBOT   " :
        i = 0
        j = 0 
        k = 0

    print"Client/Server data: -", data

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
	
        if cam_data == "STOPBOT   " or distance < Thr or (i ==0 and j == 0 and k == 0):             #stop
          sock.send("STOP")
	  print"Stop"
          M1P.ChangeDutyCycle(0)
          M2P.ChangeDutyCycle(0)
          M1N.ChangeDutyCycle(0)
          M2N.ChangeDutyCycle(0)

        elif i ==0 and j == 0 and k == 1:             #left
          sock.send("LEFT")
          print"left"
          M1P.ChangeDutyCycle(0)
          M2P.ChangeDutyCycle(17)
          M1N.ChangeDutyCycle(17)
          M2N.ChangeDutyCycle(0)
          time.sleep(0.1)

        elif i ==0 and j == 1 and k == 0:             #left      
          sock.send("LEFT")
          print"left"
          M1P.ChangeDutyCycle(0)
          M2P.ChangeDutyCycle(17)
          M1N.ChangeDutyCycle(17)
          M2N.ChangeDutyCycle(0)
          time.sleep(0.1)

        elif i ==0 and j == 1 and k == 1:             #left       
          sock.send("LEFT")
          print"left"
          M1P.ChangeDutyCycle(0)
          M2P.ChangeDutyCycle(17)
          M1N.ChangeDutyCycle(17)
          M2N.ChangeDutyCycle(0)
          time.sleep(0.1)

        elif i ==1 and j == 0 and k == 0:               #right\
          sock.send("RIGHT")
          print"right"
          M1P.ChangeDutyCycle(15)
          M2P.ChangeDutyCycle(0)
          M1N.ChangeDutyCycle(0)
          M2N.ChangeDutyCycle(15)
          time.sleep(0.1)

        elif i ==1 and j == 0 and k == 1:             #forward      
          sock.send("Forward")
          print"forward"
          M1P.ChangeDutyCycle(15)
          M2P.ChangeDutyCycle(15)
          M1N.ChangeDutyCycle(0)
          M2N.ChangeDutyCycle(0)
#          time.sleep(0.1)

        elif i ==1 and j == 1 and k == 0:             #right      
          sock.send("RIGHT")
          print"right"
          M1P.ChangeDutyCycle(15)
          M2P.ChangeDutyCycle(0)
          M1N.ChangeDutyCycle(0)
          M2N.ChangeDutyCycle(15)
          time.sleep(0.1)

        elif i ==1 and j == 1 and k == 1:             #forward      
          sock.send("Forward")
          print"forward"
          M1P.ChangeDutyCycle(15)
          M2P.ChangeDutyCycle(15)
          M1N.ChangeDutyCycle(0)
          M2N.ChangeDutyCycle(0)
#          time.sleep(0.1)
    elif cam_data == "STOPBOT   " :
        sock.send("STOP")
        print"Stop"
        M1P.ChangeDutyCycle(0)
        M2P.ChangeDutyCycle(0)
        M1N.ChangeDutyCycle(0)
        M2N.ChangeDutyCycle(0)    	
finally:
 GPIO.cleanup()
 sock.close()
