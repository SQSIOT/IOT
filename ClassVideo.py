import time

import argparse
import cv2
import os
import pickle
import sys

from operator import itemgetter

import numpy as np
np.set_printoptions(precision=2)
import pandas as pd

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



if __name__ == '__main__' :
    align = openface.AlignDlib("shape_predictor_68_face_landmarks.dat")
    net = openface.TorchNeuralNet("/home/iot/Installations/OpenFace/models/openface/nn4.small2.v1.t7",
                                  imgDim=96,
                                  cuda=False)

    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    out = cv2.VideoWriter('FaceRec.avi',fourcc, 10, (1280,720))
    multiple = True
    # Start default camera
    video = cv2.VideoCapture("vid2.mp4");


    font = cv2.FONT_HERSHEY_SIMPLEX

    win = dlib.image_window()
     
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
    # With webcam get(CV_CAP_PROP_FPS) does not work.
    # Let's see for ourselves.
     
    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
    else :
        fps = video.get(cv2.CAP_PROP_FPS)
        print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    #print("HEIGHT : {0}".format(video.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)))
    #print("WIDTH : {0}".format(video.get(cv2.CV_CAP_PROP_FRAME_WIDTH)))
    video.set(cv2.CAP_PROP_POS_MSEC,500)
    count = 0

    with open("/home/iot/Desktop/FaceRecog/DataSet/generated-embeddings/classifier.pkl", 'rb') as f:
        if sys.version_info[0] < 3:
                (le, clf) = pickle.load(f)
        else:
                (le, clf) = pickle.load(f, encoding='latin1')
                
        ret,frames = video.read()
        # Grab a few frames
        while ret:
            ret,bgrImg = video.read()

##            win.clear_overlay()
##            win.set_image(bgrImg)

            rgbImg = cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB)


            bbs = align.getAllFaceBoundingBoxes(rgbImg)
##            print("BBS",bbs)
            reps = []
            for bb in bbs:
                win.add_overlay(bb)
                cv2.rectangle(bgrImg,(bb.left(),bb.top()),(bb.right(),bb.bottom()),(0,255,0),3)
                alignedFace = align.align(
                    96,
                    rgbImg,
                    bb,
                    landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
                if alignedFace is None:
                    raise Exception("Unable to align image: {}".format(imgPath))
                    print("This bbox is centered at {}, {}".format(bb.center().x, bb.center().y))

                 
                rep = net.forward(alignedFace)
     
                reps.append((bb.left(),bb.top(), rep))
            reps = sorted(reps, key=lambda x: x[0])
            if len(reps) > 1:
                print("List of faces in image from left to right")
            for r in reps:
##                print(r)
                rep = r[2].reshape(1, -1)
                bbl = r[0]
                bbt = r[1]
                
                predictions = clf.predict_proba(rep).ravel()
                maxI = np.argmax(predictions)
                person = le.inverse_transform(maxI)
                confidence = predictions[maxI]
                text = "{}.{:.2f} ".format(person,confidence)
                
                cv2.putText(bgrImg,text,(bbl,bbt), font, 1,(255,255,255),2,cv2.LINE_AA)
                if multiple:
                    print("Predict {} @ x={} with {:.2f} confidence.".format(person, bbl,confidence))
                else:
                    print("Predict {} with {:.2f} confidence.".format(person, confidence))
##            cv2.imshow("SHOW",bgrImg)



            out.write(bgrImg)


##            cv2.imwrite("Image.png", bgrImg,[int(cv2.IMWRITE_PNG_COMPRESSION),4])
