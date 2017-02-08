import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color
import time                                  
import cv2 ,os
from PIL import Image
import numpy as np
import socket
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

#=============Declaration Start==============
LYellow = np.array([0,0,0])
HYellow = np.array([255,255,250])
Sign = "20" #Default value for Speed
StopRequested = False
s = 0
TCP_IP = '192.168.161.97'
TCP_PORT = 50001
path = "./database_priya1"   # image path
cascPath ="/home/pi/opencv-2.4.10/data/haarcascades/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)  # Create the haar cascade
recognizer = cv2.face.createLBPHFaceRecognizer()   # for recognition
i = 20
file = "./database_priya1/subject"+str(i)+".png"    # path of database

camera = PiCamera()
camera.resolution = (480,320)
camera.framerate = 10
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
                                    
# Wait for the automatic gain control to settle
time.sleep(1)

camera.awb_mode = 'auto'    #off, auto, sunlight, cloudy, shade, tungsten,
                                    #fluorescent, incandescent, flash, and horizon


camera.exposure_mode = 'auto'   #off, auto, night, nightpreview, backlight,
                                    #spotlight, sports, snow, beach, verylong,
                                    #fixedfps, antishake, and fireworks

camera.color_effects = None #(29,50)     #(255,255)#

rawCapture = PiRGBArray(camera)
fBotConnected = False
fSignalDetected = False;
fFaceDetected = False;
MusicNumber = 0;
cnt = '0'
#=============Declaration End==============


#=============Macro's Start============

# Define macro for message sending
def SendHeartBeats():
    
    global Sign
    global data
    while(True):#StopRequested != True):
        print"Sending heartbeats on socket... ", Sign
        s.send(Sign)
        data = s.recv(2)
##        time.sleep(1)

# database training function
def get_images_and_labels(path):
    # Append all the absolute image paths in a list image_paths
    # We will not read the image with the .sad extension in the training set
    # Rather, we will use them to test our accuracy of the training
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if not f.endswith('.png')]
    # images will contains face images
    images = []
    # labels will contains the label that is assigned to the image
    labels = []
    for image_path in image_paths:
        # Read the image and convert to grayscale
        image_pil = Image.open(image_path).convert('L')
        # Convert the image format into numpy array
        image = np.array(image_pil, 'uint8')
        # Get the label of the image
        nbr = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
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


# Signal Detection Code 
def IsSignalDetectedInFrame(frame , fSignalDetected):

            retValue = False
    
     #grab the raw NumPy array representing the image - this array
            #will be 3D, representing the width, height, and # of channels
            image1  = frame.array
            cv2.imshow("Frame", image1)
            key = cv2.waitKey(1) & 0xFF

            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)

            # if the `q` key was pressed, break from the loop
##            if key == ord("q"):
##                break


            blur    = cv2.erode(image1, None, iterations=2)            #Erode the masked image
            blur    = cv2.dilate(blur, None, iterations=2)           #Dilate the Masked image
            blur    = cv2.medianBlur(blur,5)

            image   = cv2.cvtColor(blur, cv2.COLOR_RGB2GRAY)

            circles = cv2.HoughCircles(image,cv2.HOUGH_GRADIENT,1,200,param1=150,param2=70,minRadius = 25)
    
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


                    LY      = np.greater_equal(color,LYellow)
                    HY      = np.less_equal(color,HYellow)
    ##                print LBl
    ##                print HBl
                    Yellow  = ((LY == True).all() and (HY == True).all())
  
                    if( Yellow and (i[2] > 30 )) :
                        print "Yellow 20"
                        retValue = True
##                        Sign = "00" # On signal detection stop Bot
    
            fSignalDetected = retValue
            return fSignalDetected

#Face Detection Code 
def IsFaceDetectedInFrame(frame , fFaceDetected):
    
    retValue = False
    
    subject20 = frame.array
    cv2.imshow('asd',subject20)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
##    if key == ord("q"):
##        break
    gray = cv2.cvtColor(subject20, cv2.COLOR_BGR2GRAY)
    predict_image_1 = np.array(gray, 'uint8')
    print "hello5"
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        predict_image_1,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(0, 0),
        flags =0
        )
    print "Found {0} faces!".format(len(faces))
    if len(faces)>=1:
        for (x, y, w, h) in faces:
            cv2.rectangle(subject20, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imwrite(file,subject20)
            crop_image = subject20[y: y + h, x: x + w]
            crop_gray =  cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
            crop_image = np.array(crop_gray, 'uint8')
            cv2.imshow("Faces found" ,subject20)
            print"taking picture"
            # Append the images with the extension .sad into image_paths
            image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]
            for image_path in image_paths:
                #print image_path
                predict_image_pil = Image.open(image_path).convert('L')
                predict_image = np.array(predict_image_pil, 'uint8')
                faces = faceCascade.detectMultiScale(predict_image)
                for (x, y, w, h) in faces:
                    result = cv2.face.MinDistancePredictCollector()
                    recognizer.predict(predict_image[y: y + h, x: x + w],result, 0)
                    nbr_predicted = result.getLabel()
                    conf = result.getDist()

                    #nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
                    #print "nbr_predicted ",nbr_predicted
                    print "conf",conf
                    nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", ""))
                    #print "nbr_actual ",nbr_actual
                    if (conf >=100):
                        print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
                        retValue = True
                    
    
    fFaceDetected = retValue
    return fFaceDetected
#=============Macro's End==============




#==============Main code Start=============================

#While Bot is not connected, try again and continue...
print "trying to connect BOT Socket server..."
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print "Connected to BOT Socket..."
##fBotConnected = True

##while (fBotConnected != True):
try:
    thread = Thread(target=SendHeartBeats)
    thread.start()
   
except:
   print "Unable to connect to BOT Socket server..."
   connection.close()
##
##time.sleep(1)      
 
try:

    print "Database initialization started..."
    images, labels = get_images_and_labels(path)
    recognizer.train(images, np.array(labels))
    print "Database initialization completed..."
##    Sign = "20"

    # Start monitoring each frame
    for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
        # do processing on each frame captured from camera

        if (fSignalDetected != True):  #if no signal detected in previous frame then try to detect signal in present frame
            fSignalDetected = IsSignalDetectedInFrame(frame,fSignalDetected)
            fFaceDetected = False; #Reset the face detected flag as we have just got signal
            if (fSignalDetected == True):
                Sign = "00"
            
         
        else:   #Signal detected in previous frame

            #Face Detection

            fFaceDetected = IsFaceDetectedInFrame(frame ,fFaceDetected)

            if (fFaceDetected):
                #Face detected in frame then perform next steps and again look for signal

##                MusicNumber = MusicNumber +1
##                if (MusicNumber > 2):
##                    MusicNumber = 1
           
                fSignalDetected = False
                

                ##//TODO:Append zero to musicnumber
##                data1 = str('0')+str(MusicNumber) #Send message to start music
                print 'above_if_cnt'
                if (cnt == '0'):
                    print 'in_if_cnt' 
                    Sign = "01"
                    time.sleep(1.8)
                    cnt = '1'
                    Sign = "20" #Send message to start BOT

                else:#elif (cnt == '1'):
                    Sign = "02"
                    time.sleep(1.8)
                    cnt = '0'
##                    music_two = True
                    Sign = "20" #Send message to start BOT
                    

finally:
    StopRequested = True
    cv2.destroyAllWindows()
    s.close()
