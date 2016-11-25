import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color
import circleDetect as cd
import RPi.GPIO as GPIO                      #Import GPIO library
import time                                  #Import time library
import cv2
import numpy as np

#To read from TXT file
theFile = open("Enter Distance.txt", "r")
theInts = []
for val in theFile.read().split():
    theInts.append(int(val))
theFile.close()
#Close


GPIO.setmode(GPIO.BCM)                       #Set GPIO pin numbering 

#Defining pins numbers
TRIG = 23                                    #Associate pin 23 to TRIG
ECHO = 24                                    #Associate pin 24 to ECHO
M1P = 16                                     #Motor 1 terminal 1.
M1N = 20                                     #Motor 1 terminal 2.
M2P = 19                                     #Motor 2 terminal 1.
M2N = 26                                     #Motor 1 terminal 2.
Thr = theInts[0]                            #defining the threshold distance
print "Threshold", Thr,"cm"
print "Distance measurement in progress"


GPIO.output(M1P,GPIO.LOW)
GPIO.output(M1N,GPIO.LOW)
GPIO.output(M2P,GPIO.LOW)
GPIO.output(M2N,GPIO.LOW)


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
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
gains = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = gains


#camera.awb_mode = 'auto'    #off, auto, sunlight, cloudy, shade, tungsten,
                                #fluorescent, incandescent, flash, and horizon


#camera.exposure_mode = 'auto'   #off, auto, night, nightpreview, backlight,
                                #spotlight, sports, snow, beach, verylong,
                                #fixedfps, antishake, and fireworks


camera.color_effects = None #(29,50)     #(255,255)#



rawCapture = PiRGBArray(camera)
flag = 0;
# allow the camera to warmup
time.sleep(0.1)
motor = 0
try:
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image - this array
        # will be 3D, representing the width, height, and # of channels
        image1 = frame.array
        image = cv2.cvtColor(image1.copy(), cv2.COLOR_BGR2HSV)

        red   = cd.redCircleRadius(image)
        green = cd.greenCircleRadius(image)
        dist  = cd.dist()

        print "Red =", red
        print "green =", green
        print dist

        if( dist > Thr or green > 0):
        
            if(green > 0):
            
                flag = 0
            
            if(flag == 0 and dist > Thr):
            
                motor = 1 
            
        
        if( ( dist < Thr and ( dist is not None ) ) or red > 30):
        
            motor = 0 
            if(red > 30 ):
            
                flag = 1
            
        

        if(motor == 0):
            GPIO.output(M1P,GPIO.LOW)
            GPIO.output(M1N,GPIO.LOW)
            GPIO.output(M2P,GPIO.LOW)
            GPIO.output(M2N,GPIO.LOW)
            print "motor off"
            
        
        else:
            GPIO.output(M1P,GPIO.HIGH)
            GPIO.output(M1N,GPIO.LOW)
            GPIO.output(M2P,GPIO.HIGH)
            GPIO.output(M2N,GPIO.LOW)
            print "motor on"


        cv2.imshow("Frame", image1)
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
        
finally:
    cv2.destroyAllWindows()
    GPIO.cleanup()

