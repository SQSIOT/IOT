import imutils
from imutils.video import VideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera, Color
import time                                  #Import time library
import cv2 ,os
from PIL import Image
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
TCP_PORT = 50001


# Define a function for the thread
def SendSign():
    
##    global Sign
##    global Stop
##    global s
##    global Var
##    flag1 = 0    
##
##    while(True):
##        if Stop :
##            break
##        if Sign == 15:
##            Sign = 0
##            Sign += 1
##            if flag1 > 20:
##                Sign = 20
##        print Sign
##        s.send(Sign)
##        s.recv(2)
##        time.sleep(0.15)

    global sign
    global data
    while(True):
        print"Sending.. ", Sign
        s.send(Sign)
        data = s.recv(2)




# image path
path = "./database_priya1"
cascPath ="/home/pi/opencv-2.4.10/data/haarcascades/haarcascade_frontalface_default.xml"
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
# for recognition
recognizer = cv2.face.createLBPHFaceRecognizer()



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
i = 20
# path of database
file = "./database_priya1/subject"+str(i)+".png"

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
#s.send("bb")
#Str = s.recv(2)
#print Str
# Create threads as follows
try:
   thread = Thread(target=SendSign)
   thread.start()
   
except:
   print "Error: unable to start thread"
   connection.close() 

try:

    # call to the database function
    print "start"
    images, labels = get_images_and_labels(path)
    recognizer.train(images, np.array(labels))
    Sign = "on"
    print "complete"
##    s.send("ca")
    s.recv(2)

    while True:
        print "in color detection"
        # for color detection         
        # capture frames from the camera
        for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
            #grab the raw NumPy array representing the image - this array
            #will be 3D, representing the width, height, and # of channels
            image1  = frame.array
            cv2.imshow("Frame", image1)
            key = cv2.waitKey(1) & 0xFF

            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break


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
                            detect = 1
                            #s.send("")
                            Sign = "00"
                            #time.sleep(10)
                        #Sign = "15"
                    if detect == 1:
                              while True:
                                    detect = 0
                                  #for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                                    print "in face detection"
                            #    if flag == 0:
                                    #data_send = "STARTBOT  "
                                    #sock.send(data_send)
                                    # grab the raw NumPy array representing the image - this array
                                    # will be 3D, representing the width, height, and # of channels 
                                    
##                                    subject20 = frame.array
##                                    cv2.imshow('asd',subject20)
##                                    key = cv2.waitKey(1) & 0xFF
##                                    # clear the stream in preparation for the next frame
##                                    rawCapture.truncate(0)
##                                    # if the `q` key was pressed, break from the loop
##                                    if key == ord("q"):
##                                        break
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
                                    #print "Found {0} faces!".format(len(faces))
                                    if len(faces)==1:
                                        for (x, y, w, h) in faces:
                                            cv2.rectangle(image1, (x, y), (x+w, y+h), (0, 255, 0), 2)
                                            cv2.imwrite(file,subject20)
                                            crop_image = image1[y: y + h, x: x + w]
                                            crop_gray =  cv2.cvtColor(crop_image, cv2.COLOR_BGR2GRAY)
                                            crop_image = np.array(crop_gray, 'uint8')
                                            #cv2.imshow("Faces found" ,image1)
                                            #print"taking picture"
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
                                                    if (conf <=150):
                                                        print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
                                                        #s.send("ok")
                                                        Sign = "99" 
                                                        flag1 = 1
                                                        break
                                                    
                                                    if (data == "ok"):
                                                        print"second time"
                                                        if (conf >= 150):
                                                            Sign = "90"
                                                            print"{} is Correctly Recognized with confidence {}".format(nbr_actual, conf)
                                                            #s.send("no")
                                                            break
                                                        
                                                    else:
                                                        #print "not recognized {}".format(nbr_actual, conf)
                                                        print "{} is Incorrect Recognized as {}".format(nbr_actual, conf)
                        ##                                cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
                        ##                                cv2.waitKey(1000)
                        ##            cam.send(ok)
                              time.sleep(0.1)
                              


           
    time.sleep(0.1)

finally:
    Stop = True
    cv2.destroyAllWindows()
    s.close()
