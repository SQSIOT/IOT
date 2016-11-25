import cv2
import numpy as np
import time                                  #Import time library
#import RPi.GPIO as GPIO                      #Import GPIO library
#GPIO.setmode(GPIO.BCM)                       #Set GPIO pin numbering 

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points
greenLower  = np.array([45,30,30])
greenUpper  = np.array([80,255,255])

redLowerlow = np.array([0,30,30])
redUpperlow = np.array([15,255,255])
redLowerup  = np.array([165,30,30])
redUpperup  = np.array([179,255,255])

#Defining pins numbers
#TRIG = 23                                    #Associate pin 23 to TRIG
#ECHO = 24                                    #Associate pin 24 to ECHO
#M1P = 16                                     #Motor 1 terminal 1.
#M1N = 20                                     #Motor 1 terminal 2.
#M2P = 19                                     #Motor 2 terminal 1.
#M2N = 26                                     #Motor 1 terminal 2.

#Defining Pins as input or output
#GPIO.setup(M1P,GPIO.OUT)
#GPIO.setup(M1N,GPIO.OUT)
#GPIO.setup(M2P,GPIO.OUT)
#GPIO.setup(M2N,GPIO.OUT)
#GPIO.setup(TRIG,GPIO.OUT)                    #Set pin as GPIO out
#GPIO.setup(ECHO,GPIO.IN)                     #Set pin as GPIO in

def greenCircleRadius(image):

    #construct a mask for the color "red", then perform
    maskgreen = cv2.inRange(image, greenLower, greenUpper)

    # a series of dilations and erosions to remove any small
    # blobs left in the mask     
    maskgreen = cv2.erode(maskgreen, None, iterations=2)            #Erode the masked image
    maskgreen = cv2.dilate(maskgreen, None, iterations=2)           #Dilate the Masked image
    maskgreen = cv2.medianBlur(maskgreen,5)

    maskgreen = cv2.bitwise_and(image,image,mask = maskgreen)       #And the masked image with original image

    maskgreen = cv2.cvtColor(maskgreen, cv2.COLOR_BGR2GRAY)         #Gray scale the image

    circles = cv2.HoughCircles(maskgreen,cv2.HOUGH_GRADIENT,1,200,param1=150,param2=30,minRadius = 20)
    #circles = cv2.HoughCircles(
    #                 image     :8-bit, single-channel, grayscale input image.
    #               ,method     :Detection method to use. Currently, the only implemented method is CV_HOUGH_GRADIENT
    #               ,dp         :Inverse ratio of the accumulator resolution to the image resolution. For example,
    #                            if dp=1 , the accumulator has the same resolution as the input image.
    #                            If dp=2 , the accumulator has half as big width and height.
    #               ,minDist[   :Minimum distance between the centers of the detected circles.
    #               ,circles[   :Each vector is encoded as a 3-element floating-point vector  (x, y, radius) .
    #               ,param1[    :First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the
    #                            higher threshold of the two passed to the Canny() edge detector
    #               ,param2[    :it is the accumulator threshold for the circle centers at the detection stage.
    #                           :The smaller it is, the more false circles may be detected.
    #               ,minRadius[ :Minimum circle radius
    #               ,maxRadius] :Maximum circle radius.
    #                           ]]]])
    #                   
    if circles is not None :
        #print "Green Circle"
        

        # convert the (x, y) coordinates and radius of the circles to integers
	#circles = np.around(circles[0, :]).astype("int")
        circles = np.uint16(np.around(circles))
	# loop over the (x, y) coordinates and radius of the circles
	#for (x, y, r) in circles:
	#	# draw the circle in the output image, then draw a rectangle
	#	# corresponding to the center of the circle
	#	cv2.circle(output, (x, y), r, (0, 255, 0), 4)
	#	cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        for i in circles[0,:] :
            # draw the outer circle
            return i[2]

def redCircleRadius(image):
    # construct a mask for the color "red", then perform
    maskredlow = cv2.inRange(image, redLowerlow, redUpperlow)   #Mask the image with the Color Range
    maskredup = cv2.inRange(image, redLowerup, redUpperup)      #Mask the image with the Color Range
    maskred = cv2.addWeighted(maskredlow, 1.0, maskredup, 1.0, 0.0)

    # a series of dilations and erosions to remove any small
    # blobs left in the mask     
    maskred = cv2.erode(maskred, None, iterations=2)            #Erode the masked image
    maskred = cv2.dilate(maskred, None, iterations=2)           #Dilate the Masked image
    maskred = cv2.medianBlur(maskred,5)

    maskred = cv2.bitwise_and(image,image,mask = maskred)       #And the masked image with original image

    maskred = cv2.cvtColor(maskred, cv2.COLOR_BGR2GRAY)         #Gray scale the image
    #cv2.imshow('Videored',maskred)
    circles = cv2.HoughCircles(maskred,cv2.HOUGH_GRADIENT,1,200,param1=100,param2=30,minRadius = 20)
    #circles = cv2.HoughCircles(
    #                 image     :8-bit, single-channel, grayscale input image.
    #               ,method     :Detection method to use. Currently, the only implemented method is CV_HOUGH_GRADIENT
    #               ,dp         :Inverse ratio of the accumulator resolution to the image resolution. For example,
    #                            if dp=1 , the accumulator has the same resolution as the input image.
    #                            If dp=2 , the accumulator has half as big width and height.
    #               ,minDist[   :Minimum distance between the centers of the detected circles.
    #               ,circles[   :Each vector is encoded as a 3-element floating-point vector  (x, y, radius) .
    #               ,param1[    :First method-specific parameter. In case of CV_HOUGH_GRADIENT , it is the
    #                            higher threshold of the two passed to the Canny() edge detector
    #               ,param2[    :it is the accumulator threshold for the circle centers at the detection stage.
    #                           :The smaller it is, the more false circles may be detected.
    #               ,minRadius[ :Minimum circle radius
    #               ,maxRadius] :Maximum circle radius.
    #                           ]]]])
    #                   
    if circles is not None :
        #print "Red Circle"
        

        # convert the (x, y) coordinates and radius of the circles to integers
	#circles = np.around(circles[0, :]).astype("int")
        circles = np.uint16(np.around(circles))
	# loop over the (x, y) coordinates and radius of the circles
	#for (x, y, r) in circles:
	#	# draw the circle in the output image, then draw a rectangle
	#	# corresponding to the center of the circle
	#	cv2.circle(output, (x, y), r, (0, 255, 0), 4)
	#	cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        for i in circles[0,:] :
            # draw the outer circle
            return i[2]

#def dist():  
#    GPIO.output(TRIG, False)                   #Set TRIG as LOW
#    time.sleep(.1)
#    GPIO.output(TRIG, True)                    #Set TRIG as HIGH
#    time.sleep(0.00001)                         #Delay of 0.00001 seconds
#    GPIO.output(TRIG, False)                   #Set TRIG as LOW
#
#    timeout = time.time() + 0.05
#    while GPIO.input(ECHO)==0 and time.time() < timeout:                 #Check whether the ECHO is LOW
#        pulse_start = time.time()                #Saves the last known time of LOW pulse#
#
#    timeout = time.time() + 0.05
#    while GPIO.input(ECHO)==1 and time.time() < timeout:                 #Check whether the ECHO is HIGH
#        pulse_end = time.time()                  #Saves the last known time of HIGH pulse 
#
#    pulse_duration = pulse_end - pulse_start   #Get pulse duration to a variable
#
#    distance = pulse_duration * 17150          #Multiply pulse duration by 17150 to get distance
#    distance = round(distance, 2)
#    if(distance > 2 and distance < 400 ):
#        return distance
#    else:
#        return 0
