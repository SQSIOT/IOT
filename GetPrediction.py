#########################################################
#                                                       #
#  Author   : Ankit Shinde                              #
#  Moto     : To get frames from Video or WebCamera     #
#             and predict the faces in the video.       #
#                                                       #
#########################################################


import time

import argparse
import cv2
import os
import pickle
import sys
import numpy as np
import pandas as pd
import face_recognition
import openface
import dlib
from sklearn.pipeline import Pipeline
from sklearn.lda import LDA
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.mixture import GMM
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from operator import itemgetter
np.set_printoptions(precision=2)


if __name__ == '__main__' :
    #Get the FaceDetector model that can predict 68 facial landmarks 
    align = openface.AlignDlib("DataSet/shape_predictor_68_face_landmarks.dat")

    #To create a output video 
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    out = cv2.VideoWriter('FaceRec.avi',fourcc, 29, (1280,720))

    #default variables
    multiple = True
    thre = 0.90
    count = 0

    
    # Start default camera
    video = cv2.VideoCapture("DataSet/all.mp4");

    #font for output video
    font = cv2.FONT_HERSHEY_SIMPLEX

    #Window to show the frames of the input Video
    win = dlib.image_window()
     
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
     

    fps = video.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    #print("HEIGHT : {0}".format(video.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)))
    #print("WIDTH : {0}".format(video.get(cv2.CV_CAP_PROP_FRAME_WIDTH)))
    video.set(cv2.CAP_PROP_POS_MSEC,500)
    count = 0


    #Get the classifier that we trained for face recognition
    with open("/home/iot/Desktop/FaceRecog/DataSet/generated-embeddings/classifier.pkl", 'rb') as f:
        if sys.version_info[0] < 3:
                (le, clf) = pickle.load(f)
        else:
                (le, clf) = pickle.load(f, encoding='latin1')
                
        ret,frames = video.read()
        
        # Grab a few frames from the video
        while ret:
            ret,bgrImg = video.read()

##            win.clear_overlay()
            #Set frame to the window
            win.set_image(bgrImg)

            #convert to RGB as Face Recognition needs RGB image format
            rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)

            #Get all the Faces in the Video frame
            Faces = align.getAllFaceBoundingBoxes(rgbImg)
##            print("BBS",bbs)

            
            reps = []

            #For Each Face in the Faces
            for Face in Faces:
##                win.add_overlay(Face)

                #Draw rectangle on the Face
                cv2.rectangle(bgrImg,(Face.left(),Face.top()),(Face.right(),Face.bottom()),(0,255,0)),np.set_printoptions(precision=2)

                #Align the found face 
                alignedFace = align.align(
                    96,
                    rgbImg,
                    Face,
                    landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                #If Face does not get aligned
                if alignedFace is None:
##                    raise Exception("Unable to align image: {}".format(imgPath))
                    print("This Faceox is centered at {}, {}".format(Face.center().x, Face.center().y))

                #If Face get aligned
                else:

                    #Get the Face Encodings
                    encode = face_recognition.face_encodings(alignedFace)#,face_locations)
##                    print(encode)

                    #If we get the embedings successfuly
                    if encode:
                        #append the info to an object for prediction
                        reps.append((Face.left(),Face.top(),encode[0]))

                    #If dont get the embedding
                    else:
                        #append the info to an object for prediction
                        reps.append((Face.left(),Face.top()))
##                        save = cv2.cvtColor(alignedFace, cv2.COLOR_RGB2BGR)
##                        cv2.imwrite("ImageUn%d.png"%count,save)
                        count += 1

            #Sort it according to X which will go from Left to right            
            reps = sorted(reps, key=lambda x: x[0])

            #Chech if more than 1 Face
            if len(reps) > 1:
                print("List of faces in image from left to right")

            #For each Face in Frame
            for r in reps:
##                print(r)
                
                bbl = r[0]
                bbt = r[1]

                #Check if no Embeddings
                if len(r) < 3:
                    text = "Unknown"
                    cv2.putText(bgrImg,text,(bbl,bbt), font, 1,(0,0,255),2,cv2.LINE_AA)

                #If embeddings predict the Face
                else:
                    rep = r[2].reshape(1, -1)
                    predictions = clf.predict_proba(rep).ravel()
                    maxI = np.argmax(predictions)
                    person = le.inverse_transform(maxI)
                    confidence = predictions[maxI]

                    #If confidence more than thre = 0.90 consider person
                    #else say unknow person
                    if confidence > thre :
                        text = "{}.{:.2f} ".format(person,confidence)
                    else:
                        text = "Unknown"
##                        cv2.imwrite("ImageUn%d.png"%count,bgrImg)
                        count += 1

                    #Write the Info on the OutPut Video
                    cv2.putText(bgrImg,text,(bbl,bbt), font, 1,(0,255,0),2,cv2.LINE_AA)

                    #Write info on terminal
                    if multiple:
                        print("Predict {} @ x={} with {:.2f} confidence.".format(person, bbl,confidence))
                    else:
                        print("Predict {} with {:.2f} confidence.".format(person, confidence))

            #Write the fram in output video
            out.write(bgrImg)

