# import the necessary packages

import cv2
import numpy as np

image = cv2.imread("red7.jpg",0)
#blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#print gray.shape
#print image
#x=0
#px = image[100,100]
# get image properties.
w,h = np.shape(image)
print w,h	

for py in range(0,w):
    for px in range(0,h):
        if image[py][px]==91:
	#l=image[px][py]
	#print "success"
            cv2.circle(image, (int(px), int(py)), 2, (0, 0, 255), -1)
            break
cv2.imshow("Frame", image)
#key = cv2.waitKey(1) & 0xFF
cv2.waitKey(0)
