import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color
import time                                  #Import time library
import cv2
import numpy as np
import socket
#import thread
from threading import Thread



##Definitions

##Color   = np.array([Red,Green,Blue])
##LBlue   = np.array([0,  20, 140])
##HBlue   = np.array([30, 85, 220])
##LBlack  = np.array([0,  0,  0])
##HBlack  = np.array([40, 40, 40])
##LRed    = np.array([200,0,  0])
##HRed    = np.array([255,40, 50])
##LGreen  = np.array([0,  100,0])
##HGreen  = np.array([30, 160,30])
LYellow = np.array([100,100,0])
HYellow = np.array([255,255,250])

##Default value for Speed
Sign = "20"
Stop = False
s = 0
Var = 0
Flag = True
TCP_IP = '192.168.161.97'
TCP_PORT = 20001


# Define a function for the thread
def SendSign():
    
    global Sign
    global Stop
    global s
    global Var
    flag1 = 0    

    while(True):
        if Stop :
            break
        if Sign == 15:
            Sign = 0
            Sign += 1
            if flag1 > 20:
                Sign = 20
        print Sign
        s.send(Sign)
        s.recv(2)
        time.sleep(0.15)



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

camera.awb_mode = 'auto'    #off, auto, sunlight, cloudy, shade, tungsten,
                                #fluorescent, incandescent, flash, and horizon


camera.exposure_mode = 'auto'   #off, auto, night, nightpreview, backlight,
                                #spotlight, sports, snow, beach, verylong,
                                #fixedfps, antishake, and fireworks


camera.color_effects = None #(29,50)     #(255,255)#



rawCapture = PiRGBArray(camera)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
Str = s.recv(2)
print Str
# Create threads as follows
try:
   thread = Thread(target=SendSign)
   thread.start()
except:
   print "Error: unable to start thread"
   connection.close() 

try:
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
        #grab the raw NumPy array representing the image - this array
        #will be 3D, representing the width, height, and # of channels
        image1  = frame.array


        blur    = cv2.erode(image1, None, iterations=2)            #Erode the masked image
        blur    = cv2.dilate(blur, None, iterations=2)           #Dilate the Masked image
        blur    = cv2.medianBlur(blur,5)

        image   = cv2.cvtColor(blur, cv2.COLOR_RGB2GRAY)

        circles = cv2.HoughCircles(image,cv2.HOUGH_GRADIENT,1,200,param1=150,param2=70,minRadius = 25)
##        circles = cv2.HoughCircles(
##                        image       :8-bit, single-channel, grayscale input image.
##                        ,method     :Detection method to use. Currently, the only implemented method is CV_HOUGH_GRADIENT
##                        ,dp         :Inverse ratio of the accumulator resolution to the image resolution. For example,
##                                    if dp=1 , the accumulator has the same resolution as the input image.
##                                    If dp=2 , the accumulator has half as big width and height.
##                        ,minDist[   :Minimum distance between the centers of the detected circles.
##                        ,circles[   :Each vector is encoded as a 3-element floating-point vector  (x, y, radius) .
##                        ,param1[    :First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the
##                                    higher threshold of the two passed to the Canny() edge detector
##                        ,param2[    :it is the accumulator threshold for the circle centers at the detection stage.
##                                    :The smaller it is, the more false circles may be detected.
##                        ,minRadius[ :Minimum circle radius
##                        ,maxRadius] :Maximum circle radius.
##                                   ]]]])


        if circles is not None :

##            #convert the (x, y) coordinates and radius of the circles to integers
##            circles = np.around(circles[0, :]).astype("int")
            circles     = np.uint16(np.around(circles))
##            #loop over the (x, y) coordinates and radius of the circles
##            for (x, y, r) in circles:
##                #draw the circle in the output image, then draw a rectangle
##            	  #corresponding to the center of the circle
##                cv2.circle(image1, (x, y), 1, (255, 255, 255), -1)
##                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            for i in circles[0,:] :
##                #draw the outer circle
                cv2.circle(image1, (i[0], i[1]), i[2], (255, 255, 255), 1)
                color   = image1[i[1],i[0]]
                print color
##                print i[2]                

####                Check for green
##                LG      = np.greater_equal(color,LGreen)
##                HG      = np.less_equal(color,HGreen)
####                print LG
####                print HG
##                Green   = ((LG == True).all() and (HG == True).all())
##                
##
####                Check for Red
##                LR      = np.greater_equal(color,LRed)
##                HR      = np.less_equal(color,HRed)
####                print LR
####                print HR
##                Red     = ((LR == True).all() and (HR == True).all())
##                
##
####                Check for Blue
##                LB      = np.greater_equal(color,LBlue)
##                HB      = np.less_equal(color,HBlue)
####                print LB
####                print HB
##                Blue    = ((LB == True).all() and (HB == True).all())
##                
##
####                Check for Black
##                LBl     = np.greater_equal(color,LBlack)
##                HBl     = np.less_equal(color,HBlack)
####                print LBl
####                print HBl
##                Black   = ((LBl == True).all() and (HBl == True).all())
##                

                LY      = np.greater_equal(color,LYellow)
                HY      = np.less_equal(color,HYellow)
##                print LBl
##                print HBl
                Yellow  = ((LY == True).all() and (HY == True).all())
##                          
##                if( Green and (i[2] > 25 ) and (i[2] < 35 )):
##                    print "Green 20"
##                    Sign = "20"
##                if( Green and (i[2] > 35 )):
##                    print "Green 40"
##                    Sign = "40"
##                if( Red and (i[2] > 25 ) and (i[2] < 35 )) :
##                    print "Red 15"
##                    Sign = "15"
##                if( Red and (i[2] > 40 )) :
##                    print "Red 00"
##                    Sign = "00"
##                if( Blue and (i[2] > 40 )) :
##                    print "Blue 80"
##                    Sign = "80"
##                if( Black and (i[2] > 40 )) :
##                    print "Black 20"
##                    Sign = "20"
##                if( Black and (i[2] > 25 ) and (i[2] < 40)) :
##                    print "Black 40"
##                    Sign = "20"
                if( Yellow and (i[2] > 30 )) :
                    print "Yellow 20"
                    if Flag :
                        Flag = False
                        Sign = "00"
                        time.sleep(10)
                    Sign = "15"


        cv2.imshow("Frame", image1)
        key = cv2.waitKey(1) & 0xFF

        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

finally:
    Stop = True
    cv2.destroyAllWindows()
    s.close()
