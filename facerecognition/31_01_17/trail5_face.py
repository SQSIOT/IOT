import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color
import time                                  #Import time library
from subprocess import Popen
import cv2
import numpy as np
import socket
import RPi.GPIO as GPIO                      #Import GPIO library
GPIO.setwarnings(False)                         ##Added by Mayuresh   
GPIO.setmode(GPIO.BCM)
import os


##Motor settings
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

##IR Sensor to stop the Bot
Left_sensor = 13
Right_sensor = 6

GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Right sensor connection
GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Left sensor connection
flag1 = 0


path = '/home/pi/Desktop/Integration/LeanOn.mp3'
path1 = '/home/pi/Desktop/songs/CheapThrill.mp3'

def Forward(speed):
    print"Forward"
    M1P.ChangeDutyCycle(speed)
    M2P.ChangeDutyCycle(speed)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(0)
    

    
def Left(speed):
    print"Left"
    M1P.ChangeDutyCycle(0)
    M2P.ChangeDutyCycle(speed)
    M1N.ChangeDutyCycle(speed)
    M2N.ChangeDutyCycle(0)
    
def Stop():
    print"stop"
    M1P.ChangeDutyCycle(0)
    M2P.ChangeDutyCycle(0)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(0)


def Right(speed):
    #global flag1
    print"Right"
    M1P.ChangeDutyCycle(speed)
    M2P.ChangeDutyCycle(0)
    M1N.ChangeDutyCycle(0)
    M2N.ChangeDutyCycle(speed)
    
        
    
camera = PiCamera()
camera.resolution = (192,144)
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

print"Connect Camera Now" 
##Socket Connection for camera to give speed
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('192.168.161.97',50001))
sock.listen(1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
cam, addr1 = sock.accept()
print"Connected camera", addr1

turnspd  = 18 ##18/12 Speed at turning radius
turnspd1 = 12


flag = True
flag1 = 0
flag3 = False
##
##def recv():
##    global flag
##    global flag1
##    flag1 += 1
##    print"Flag1 is", flag1
##    if (flag1 > 13 and flag):
##        Stop()
##        cam.send("ca")
##        while True:
##            print"waiting to receive"
##            data = cam.recv(2)
##            print data
##            if (data == "ok"):
##                flag = False
##                flag1 = 0
##                time.sleep(2)
##                cam.send("on")
##                return


def Cam():
        global flag3
        data = cam.recv(2)
        if(data == "on"):
            cam.send("on")
            for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                # grab the raw NumPy array representing the image - this array
                # will be 3D, representing the width, height, and # of channels
               
                #cam.send("da")
                
                data = cam.recv(2)    
                cam.send("on")

                speed = int(data)
                print data
                if(speed == "99"):
                    Popen(['omxplayer', path])
                    speed = 20
                    cam.send("ok")
                elif(speed == "90"):
                    os.system('killall -s 9 omxplayer.bin')
                    Popen(['omxplayer', path1])
                    cam.send("ok")
                    speed = 20
                        
                print"Speed is", speed
                i=GPIO.input(Left_sensor)       #Reading output of left IR sensor
                j=GPIO.input(Right_sensor)      #Reading output of right IR sensor

                if i ==0 and j == 0:
                    print"Stop coz of IR"
                    rawCapture.truncate(0)
                    Stop()    
                    return
                
                img = frame.array
                imgroi = img[100:110,:]

                gray = cv2.cvtColor(imgroi,cv2.COLOR_BGR2GRAY)

    ##            gray = cv2.erode(gray, None, iterations=2)            #Erode the masked image
    ##            gray = cv2.dilate(gray, None, iterations=2)           #Dilate the Masked image
    ##            blur = cv2.medianBlur(gray,5)
                blur = cv2.bilateralFilter(gray,9,75,75)
                th1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY,11,2)
                cnts = cv2.findContours(th1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

                cnts = cnts[0] if imutils.is_cv2() else cnts[1]
                #print cnts
                center = []
                for c in cnts:

                    M = cv2.moments(c)
                    if M["m00"] != 0:
                        cX = int(M["m10"]/M["m00"])
                        cY = int(M["m01"]/M["m00"])
                        #print cX
                        #print cY
                        colorarr = img[cY+100,cX]
        ##                print colorarr
                        if colorarr[0] < 60 and colorarr[1] < 60 and colorarr[2] < 60 :
                            center.append(cX) 
        ##                    cv2.drawContours(th1,[c],-1,(0,255,0),2)
        ##                    cv2.circle(th1,(cX,cY),1,(255,255,255),-1)
        ##                    cv2.circle(img,((cX),(cY+100)),2,(255,255,255),-1)
           
                pt = len(center)
                
                if pt :
                    print center[0]
                    if center[0] > 76 and center[0] < 116:
                        Forward(speed)
                    if center[0] > 154 :
                        Right(turnspd)
                        rawCapture.truncate(0)
                    if center[0] < 38 :
                        Left(turnspd)    
                    if center[0] > 116 and center[0] < 154 :
                        Right(turnspd1)
                        rawCapture.truncate(0)
                    if center[0] < 76 and center[0] > 38:
                        Left(turnspd1)
                else:
                    print"Running on IR"
                    if (i == 0 and j== 0):                         #Stop  
                        rawCapture.truncate(0)
                        Stop()
                        print"Stop coz of IR"
    ##                    rawCapture.truncate(0)
                        return
                    elif (i == 1 and j ==0):                        #Right
                        Right(turnspd)
                        rawCapture.truncate(0)
                    elif (i == 0 and j ==1):                        #Left
                        Left(turnspd)    
                    elif (i == 1 and j ==1):                        #forward
                        Forward(speed)   
    ##            print"flag 1", flag1
    ##            print flag
                rawCapture.truncate(0)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

try:
    Cam()
            
finally:
    camera.close()
    GPIO.cleanup()
    cam.close()
    os.system('killall -s 9 omxplayer.bin')
