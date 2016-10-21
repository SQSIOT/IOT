# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# change the image to gray scale
path="image4.png"
image=cv2.imread(path)
#cv2.imshow('photo',image)
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('photoGray',gray)
#cv2.waitKey(1)
key = cv2.waitKey(1) & 0xFF
