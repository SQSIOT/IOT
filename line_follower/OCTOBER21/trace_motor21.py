#import imutils
#from imutils.video import VideoStream
#from picamera.array import PiRGBArray
#from picamera import PiCamera, Color
#import circleDetect as cd
import RPi.GPIO as GPIO                      #Import GPIO library
import time                                  #Import time library
import cv2
import numpy as np

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)    #motor A
GPIO.setup(20, GPIO.OUT)    #motor A

GPIO.setup(19, GPIO.OUT)    #motor B
GPIO.setup(26, GPIO.OUT)    #motor B


image = cv2.imread('red5.jpg')
#print image.shape
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def do_threshold(image, threshold = 170):
    (thresh, im_bw) = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return (thresh, im_bw)
(thresh, img_threshold) = do_threshold(gray_image, 35)
threshold = 170
blck_wht = cv2.threshold(gray_image, threshold, 100, cv2.THRESH_BINARY)[1]
cv2.imshow('binary',blck_wht)
#print blck_wht.shape
cv2.imwrite("blackwhite.png", blck_wht)
image1=cv2.imread("blackwhite.png",0)
#print image1.shape

height, width = np.shape(image1)
#print height,width
#for x in range(width-10):
    #print image1[height-10][x]

# get image properties.
h,w = np.shape(blck_wht)
#print h,w
py=h-1
px=0

# for py in range(0):
while py>0:
    for px in range(w):
       #print image1[py][px]
       # forward=px
       if image1[py][px]==0:
          print py,px
          cv2.circle(image1, (int(px+50), int(py+50)), 2, (255, 255, 255), -1)
          #cv2.putText(image1,"Hello World!!!", (int(px+50), int(py+50)), cv2.FONT_HERSHEY_SIMPLEX, 2, 255)
          print"wel222222222222222222222222222222222"
          print px+50,py+50
          if(260<px+50<282):
                  print "motor running forward"
                  GPIO.output(16, GPIO.HIGH)  #Forward A
                  GPIO.output(20, GPIO.LOW)

                  GPIO.output(19, GPIO.HIGH)  #Forward B
                  GPIO.output(26, GPIO.LOW)

                  time.sleep(1)



          if(282<px+50<347):
                  print "motor turn right"
                  cv2.putText(image1,"turn right", (int(px+10), int(py+2)), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
                  GPIO.output(16, GPIO.LOW)  #Forward A
                  GPIO.output(20, GPIO.LOW)

                  GPIO.output(19, GPIO.HIGH)  #Forward B
                  GPIO.output(26, GPIO.LOW)

                  time.sleep(1)

          break
    
    
    py=py-100
       
    
        
cv2.imshow("Frame",image1)
cv2.waitKey(0)















cv2.waitKey(0)
