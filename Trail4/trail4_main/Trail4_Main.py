import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color
import time                                  #Import time library
import cv2
import socket
import time
import numpy as np
from threading import Thread
from turn import *


##Motor settings
import RPi.GPIO as GPIO                      #Import GPIO library
GPIO.setwarnings(False)                        

GPIO.setmode(GPIO.BCM)
M1P = 16                                     #Motor 1 terminal 1.
M1N = 20                                     #Motor 1 terminal 2.
M2P = 26                                     #Motor 2 terminal 1.
M2N = 19                                     #Motor 2 terminal 1.


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

turnspd     = 18 ## Speed at turning radius
turnspd1    = 15
speed       = 20
speed1      = 15

def Forward(speed):
##    print"Forward"
    M1P.ChangeDutyCycle(speed)
    M2P.ChangeDutyCycle(speed)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(0)
    

def Right(speed):
##    print"Right"
    M1P.ChangeDutyCycle(speed1)
    M2P.ChangeDutyCycle(0)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(speed1)
    
def Left(speed):
##    print"Left"
    M1P.ChangeDutyCycle(0)
    M2P.ChangeDutyCycle(speed1)
    M1N.ChangeDutyCycle(speed1)
    M2N.ChangeDutyCycle(0)
    
def Stop():
    print"stop"
    M1P.ChangeDutyCycle(0)
    M2P.ChangeDutyCycle(0)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(0)

camera = PiCamera()
camera.resolution = (480,320)
camera.framerate = 10


#set default
camera.sharpness = 0    
camera.contrast = 0     #0 TO 100
camera.brightness = 50  #0 O 100
camera.saturation = 0
camera.ISO = 0              #100, 200, 320, 400, 500, 640, 800. and 1600 
camera.video_stabilization = False
camera.exposure_compensation = 0

camera.meter_mode = 'average'
camera.image_effect = 'none'    #The options are: none, negative, solarize,
                                # sketch, denoise, emboss, oilpaint, hatch,
                                #gpen, pastel, watercolor, film, blur,
                                #saturation, colorswap, washedout, posterise,
                                #colorpoint, colorbalance, cartoon,
                                #deinterlace1, and deinterlace2

#camera.annotate_background = Color('blue')

# Wait for the automatic gain control to settle
time.sleep(2)
# Now fix the values
#camera.shutter_speed = camera.exposure_speed
#camera.exposure_mode = 'off'
#gains = camera.awb_gains
#camera.awb_mode = 'off'
#camera.awb_gains = gains


camera.awb_mode = 'auto'    #off, auto, sunlight, cloudy, shade, tungsten,
                                #fluorescent, incandescent, flash, and horizon


camera.exposure_mode = 'auto'   #off, auto, night, nightpreview, backlight,
                                #spotlight, sports, snow, beach, verylong,
                                #fixedfps, antishake, and fireworks


camera.color_effects = None #(29,50)     #(255,255)#



rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)
np.array([0,0,0])
np.array([30,30,30])


flag = 0
data = "Test"

print"Connect camera"
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Bind the socket to the IP
s.bind(('192.168.161.97',40001))
#continuos listening
s.listen(1)
# include the IP headers
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# accept the connection
connection, addr = s.accept()    
connection.send("Forward")
print"Connected camera", addr


def sock_recv():
    global data
    print "Starting socket"
    #### create a socket
    while True:
                data = connection.recv(10)

try:
    thread = Thread(target = sock_recv)
    thread.start()
except:
    print"Thread Error"
    connection.close()  # socket close


try:    
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image - this array
        # will be 3D, representing the width, height, and # of channels
        print data
        i=GPIO.input(Left_sensor)       #Reading output of left IR sensor
        j=GPIO.input(Right_sensor)      #Reading output of right IR sensor
        if (i == 0 and j== 0):                         #Stop
            Forward(speed)
            rawCapture.truncate(0)
            continue
    
        if data == "STOPBOT   " and flag == 0 :
            print"Going to stop Fish...!!!"
            rawCapture.truncate(0)
            flag = 1
            Stop()
            print"I was in stopbot"
            while(data != "GREEN     "):
                continue
            
        if(data == "GREEN     " and flag == 1):
                Lane()
                break
            
        if data != "STOPBOT   "  :                
            #if data == "MOVEONLINE"
                
            img = frame.array
            imgroi = img[240:260,:]
            #maskblack = cv2.inRange(imgroi,np.array([0,0,0]),np.array([30,30,30]))

            gray = cv2.cvtColor(imgroi,cv2.COLOR_BGR2GRAY)

            
            blur = cv2.bilateralFilter(gray,9,75,75)
            th1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                        cv2.THRESH_BINARY,11,2)
            cnts = cv2.findContours(th1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

            cnts = cnts[0] if imutils.is_cv2() else cnts[1]
            #print cnts
            center = [0]
            for c in cnts:

                M = cv2.moments(c)
                if M["m00"] != 0:
                    cX = int(M["m10"]/M["m00"])
                    cY = int(M["m01"]/M["m00"])
                    #print cX
                    #print cY
                    colorarr = img[cY+240,cX]
    ##                print colorarr
                    if colorarr[0] < 60 and colorarr[1] < 60 and colorarr[2] < 60 :
                        center.append(cX) 
    ##                    cv2.drawContours(th1,[c],-1,(0,255,0),2)
    ##                    cv2.circle(th1,(cX,cY),1,(255,255,255),-1)
    ##                    cv2.circle(img,((cX),(cY+240)),2,(255,255,255),-1)
            
            i = len(center) 
    ##        print center[i-1]
            if center[i-1] > 200 and center[i-1] < 300:
                Forward(speed)
            if center[i-1] > 300 :
                Right(speed1)
            if 0 < center[i-1] < 200 :
                Left(speed1)
            if center[i-1] == 0:
                Forward(speed)
            if center[i-1] == 0:              ##Commented by mayuresh as bot does not need to be stopped by camera
                print"Running on IR"
                if (i == 0 and j== 0):                         #Stop  
                    Forward(speed)
                    rawCapture.truncate(0)
                    continue
                elif (i == 1 and j ==0):                        #Right
                    Right(turnspd)  
                elif (i == 0 and j ==1):                        #Left
                    Left(turnspd)    
                elif (i == 1 and j ==1):                        #forward
                    Forward(speed)   

        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
               break

finally:
    # When everything done, release the capture
    GPIO.cleanup()
    camera.close()
    cv2.destroyAllWindows()
    connection.close()
