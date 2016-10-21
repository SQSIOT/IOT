import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color

import time                                  #Import time library
import cv2 , os
import numpy as np
from PIL import Image


camera = PiCamera()
camera.resolution = (480,320)
camera.framerate = 10

imagepath = "/home/pi/FaceDetection/Database/images1"
cascPath ="/home/pi/opencv-2.4.10/data/haarcascades/haarcascade_frontalface_default.xml"


# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
# for recognition
recognizer = cv2.face.createLBPHFaceRecognizer()
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
flag = 0
# allow the camera to warmup
time.sleep(0.1)
def get_images_and_labels(imagepath): 
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    print "inside the function"
    image_paths = [os.path.join(imagepath, f)for f in os.listdir(imagepath)]
    # images will contains face images 
    images = []
    # labels will contains the label that is assigned to the image
    labels = [] 
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array 
        image = np.array(image_pil, 'uint8')
        #print "inside the for loop"
        # Get the label of the image 
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("image", "")) 
        # Detect the face in the image 
        faces = faceCascade.detectMultiScale(image)
        # If face is detected, append the face to images and the label to labels 
        for (x, y, w, h) in faces:
                    images.append(image[y: y + h, x: x + w])
                    labels.append(nbr)
                    cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                    cv2.waitKey(50)
    # return the images list and labels list 
    return images, labels
try:
    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
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
        
        file = "two.png"
        #cv2.imwrite(file,image1)
        # Read the image
        #image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        predict_image_1 = np.array(gray, 'uint8')
        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            predict_image_1,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(0, 0),
            flags =0
        )
        print "Found {0} faces!".format(len(faces))
        if len(faces)>1:
           for (x, y, w, h) in faces:
                cv2.rectangle(image1, (x, y), (x+w, y+h), (0, 255, 0), 2)
           cv2.imshow("Faces found" ,image1)
           cv2.imwrite(file,gray)
           print"taking picture"
           
    
   

        

finally:
    cv2.destroyAllWindows()
