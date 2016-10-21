# USAGE
# python detect_color.py --image pokemon_games.png

# import the necessary packages
from matplotlib import pyplot as plt
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import numpy as np
import argparse
import cv2
import matplotlib

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
#camera.brightness = 80
#camera.contrast = 0
rawCapture = PiRGBArray(camera, size=(640, 480))
i=0
flag=0
# allow the camera to warmup
time.sleep(0.1)
#image = camera.capture(rawCapture, format="bgr", use_video_port=True)
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", help = "path to the image")
################args = vars(ap.parse_args())
# load the image
image = cv2.imread("red6.jpg")
plt.imshow(image,cmap='gray',interpolation ='bicubic')
plt.show()
# image= cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# define the list of boundaries
boundaries = [
        ([17, 15, 10],[50, 50, 255])
         # ([17, 15, 100], [50, 56, 200])

        # ,([86, 31, 4], [220, 88, 50]),
        # # ([25, 146, 190], [62, 174, 250]),
        # ([103, 86, 65], [145, 133, 128]
        # )
]

# loop over the boundaries
for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype = "uint8")
        upper = np.array(upper, dtype = "uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        mask= cv2.erode(mask,None,iterations=2)
        mask= cv2.dilate(mask,None,iterations=2)
        output = cv2.bitwise_and(image, image, mask = mask)
        output1 = cv2.bitwise_and(image, output, mask = mask)
        #cv2.imshow("images", output)
        print output
        b,g,r= cv2.split(image)
        print b
        print g
        print r
        cv2.imshow("images",image)
        cv2.waitKey(0)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        ####################cv2.imshow("images",image)
        # show the images
        #cv2.imshow("images", np.hstack([image,output1]))
        center = None
        print len(cnts)
        if len(cnts) > 0:
                # find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                        
                M = cv2.moments(c)
                print len(M)
                print radius

                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                # only proceed if the radius meets a minimum size
                 # Set up the SimpleBlobdetector with default parameters.
                params = cv2.SimpleBlobDetector_Params()
     
                # Change thresholds
                params.minThreshold = 0;
                params.maxThreshold = 256;
     
                # Filter by Area.
                params.filterByArea = True
                params.minArea = 30
     
                # Filter by Circularity
                params.filterByCircularity = True
                params.minCircularity = 0.1
     
                # Filter by Convexity
                params.filterByConvexity = True
                params.minConvexity = 0.5
     
                # Filter by Inertia
                params.filterByInertia =True
                params.minInertiaRatio = 0.5
     
                detector = cv2.SimpleBlobDetector_create(params)
 
                # Detect blobs.
                reversemask=255-mask
                keypoints = detector.detect(reversemask)
                im_with_keypoints = cv2.drawKeypoints(output, keypoints, np.array([]), (255,150,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

                # Show blobs
                cv2.imshow("Keypoints", im_with_keypoints)
                cv2.waitKey(0)
                if radius > 10:
                        # draw the circle and centroid on the frame, then update the list of tracked points
                        cv2.circle(output, (int(x), int(y)), 60,
                                (0, 255, 255), 2)
                        cv2.circle(output, center, 5, (0, 255, 255), -1)
                        cv2.imshow("Frame", output)
                        key = cv2.waitKey(0)    # update the points queue
        #pts.appendleft(center)
