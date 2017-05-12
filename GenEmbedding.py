#########################################################################
#                                                                       #
#  Author   : Ankit Shinde                                              #
#  Moto     : To get images from database and align them .Get the       #
#             aligned image and generate embeddings . Save the          #
#             embedding and labels in CSV file.                         #
#                                                                       #
#########################################################################




import csv
import time
import argparse
import cv2
import os
import pickle
import sys
import face_recognition
import numpy as np
import pandas as pd
import dlib
import openface
import openface.helper
from openface.data import iterImgs
from operator import itemgetter
np.set_printoptions(precision=2)


#Get names of all the Directories and files
embeddingDir    = "DataSet/generated-embeddings/"
trainDir        = "DataSet/TrainingImages/"
AlignDir        = "DataSet/AlignedImages/"
labelscsv       = "label.csv"
repscsv         = "rep.csv"

#Get Face Detector
align           = openface.AlignDlib("DataSet/shape_predictor_68_face_landmarks.dat")


#Create labels and embeddings CSV file
with open(embeddingDir+'labels.csv', 'w') as csvfile:
    labelwriter = csv.writer(csvfile,delimiter=',')

    with open(embeddingDir+'reps.csv', 'w') as csvfile:
        repswriter = csv.writer(csvfile,delimiter=',')


        #make list of paths of images from the training directory.
        imgs = list(iterImgs(trainDir))

        #Iterate over all the Images
        for imgObject in imgs:
            print("=== {} ===".format(imgObject.path))

            #Find if the image is already aligned and present in aligned directory
            outDir = os.path.join(AlignDir, imgObject.cls)
            openface.helper.mkdirP(outDir)
            outputPrefix = os.path.join(outDir, imgObject.name)
            imgName = outputPrefix + ".png"
            print(imgName)


            #Check that images is not present in aligned dir    
            if not os.path.isfile(imgName):
                print("1")

                #get the image in RGB format
                rgb = imgObject.getRGB()

                #Get the largest face in the Image
                Face = align.getLargestFaceBoundingBox(rgb)
                if Face:

                    #Align the face and save in the directory
                    outrgb = align.align(96,
                                         rgb,
                                         Face,
                                         landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE,
                                         skipMulti=True)
                    outBgr = cv2.cvtColor(outrgb, cv2.COLOR_RGB2BGR)
                    cv2.imwrite(imgName, outBgr)


            #If Image is already present,Get it in RGB format
            else:
                bgr = cv2.imread(imgName)
                outrgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
                print("2")

            #Not get the Embedding from the aligned face and
            #save them and labels in CSV file
            if outrgb is not None:
                encode = face_recognition.face_encodings(outrgb)
                #print(encode[0])
                if encode:
                    print("3")
                    labelwriter.writerow([imgObject.path])
                    repswriter.writerow(encode[0])

