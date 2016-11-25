import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color
import circleDetect as cd

import time                                  #Import time library
import cv2
import numpy as np

import socket
import sys

STOP =  'STOPBOT   '
START = 'STARTBOT  '


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
time.sleep(1)
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



# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.160', 12001)

sock.connect(server_address)
data = "test"
forward = "Forward"
while data != forward :
    sock.sendall("Connected ")
    data = sock.recv(1024)
flag = 0
try:
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image - this array
        # will be 3D, representing the width, height, and # of channels
        image1 = frame.array
        image = cv2.cvtColor(image1.copy(), cv2.COLOR_BGR2HSV)
        red   = cd.redCircleRadius(image)
        green = cd.greenCircleRadius(image)
        rawCapture.truncate(0)
        print "red",red
        print "green",green
        if red > 20 :
            sock.sendall(STOP)
            flag = 1
            print STOP
        else :
            if green :
                flag = 0
                sock.sendall(START)
                print START
            else :
                if flag == 0 :
                    sock.sendall(START)
                    print START
                else:
                    print STOP
                    sock.sendall(STOP)
        data = sock.recv(1024)
        print data
        if data == 'PARK' :
            print "Done"
            camera.close()
            time.sleep(1)
            break
finally:
    cv2.destroyAllWindows()
    camera.close()
