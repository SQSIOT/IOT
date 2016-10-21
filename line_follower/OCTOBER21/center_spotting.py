# import the necessary packages

import cv2
import numpy as np

image = cv2.imread("red5.jpg",0)
# cv2.imshow("img",image)


# get image properties.
h,w = np.shape(image)
print h,w
py=h-1
px=0

# for py in range(0):
while py>0:
    for px in range(w):
       # forward=px
       if image[py][px]==91:
          cv2.circle(image, (int(px+50), int(py+50)), 2, (0, 0, 255), -1)
          basic_value=py
          print px+50,py+50
          if(260<px+50<282):
                  print "motor running forward"
          if(282<px+50<347):
                  print "motor turn right"
          break
    
    
    py=py-100
       
    
        
cv2.imshow("Frame",image)
cv2.waitKey(0)

