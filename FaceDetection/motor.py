import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color
import RPi.GPIO as GPIO                      #Import GPIO library          
import time                                  #Import time library
import cv2
import numpy as np


camera = PiCamera()
camera.resolution = (480,320)
camera.framerate = 10

imagePath = "/home/pi/boypic.jpg"
cascPath ="/home/pi/opencv-2.4.10/data/haarcascades/haarcascade_frontalface_default.xml"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Pin Defining

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

#GPIO.setup(Left_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Right sensor connection
#GPIO.setup(Right_sensor, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #Left sensor connection

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




# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
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
# allow the camera to warmup
time.sleep(0.1)
i=0

try:
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        print "motor running forward"
        M1P.ChangeDutyCycle(15)
        M2P.ChangeDutyCycle(15)
        M1N.ChangeDutyCycle(0)
        M2N.ChangeDutyCycle(0)
        # grab the raw NumPy array representing the image - this array
        # will be 3D, representing the width, height, and # of channels
        image1 = frame.array
        cv2.imshow('asd',image1)
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
        gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        predict_image_1 = np.array(gray, 'uint8')
        # Detect faces in the image
        #print "one  image"
        faces = faceCascade.detectMultiScale(
            predict_image_1,
            scaleFactor=1.2,
            minNeighbors=3,
            minSize=(0, 0),
            flags =0
        )
         #print "Found {0} faces!".format(len(faces))
        if len(faces)>=1:
           for (x, y, w, h) in faces:
                cv2.rectangle(image1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                crop_image = image1[y: y + h, x: x + w]
                crop_gray =  cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
                crop_image1 = np.array(crop_gray, 'uint8') 
                cv2.imshow("Faces found" ,image1)
                cv2.waitKey(50)
                file = "motor"+str(i)+".png"
                cv2.imwrite(file,image1)
                i = i+1;
        
    # capture frames from the camera


finally:
    cv2.destroyAllWindows()
    GPIO.cleanup()
