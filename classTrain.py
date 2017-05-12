#########################################################################
#                                                                       #
#  Author   : Ankit Shinde                                              #
#  Moto     : Train the classifier in SVM using the embedding stored    #
#             in CSV file                                               #
#########################################################################


import time
import argparse
import cv2
import os
import pickle
import sys
import numpy as np
import pandas as pd
import openface
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

#Get all the directories, files and values
workDir     = "DataSet/generated-embeddings/"
classifier  =  "LinearSvm"
ldaDim      = 96


def train():

    #Get the labels.csv file 
    print("Loading embeddings.")
    fname = "{}/labels.csv".format(workDir)
    labels = pd.read_csv(fname, header=None).as_matrix()[:, 0]
    labels = map(itemgetter(1),
                 map(os.path.split,
                     map(os.path.dirname, labels)))  # Get the directory.
    fname = "{}/reps.csv".format(workDir)
    embeddings = pd.read_csv(fname, header=None).as_matrix()	
    
    labels = list(labels)
##    print(labels)
    le = LabelEncoder().fit(labels)
    labelsNum = le.transform(labels)
    nClasses = len(le.classes_)
    print("Training for {} classes.".format(nClasses))

    if classifier == 'LinearSvm':
        clf = SVC(C=1, kernel='linear', probability=True)
    elif classifier == 'GridSearchSvm':
        print("""
        Warning: In our experiences, using a grid search over SVM hyper-parameters only
        gives marginally better performance than a linear SVM with C=1 and
        is not worth the extra computations of performing a grid search.
        """)
        param_grid = [
            {'C': [1, 10, 100, 1000],
             'kernel': ['linear']},
            {'C': [1, 10, 100, 1000],
             'gamma': [0.001, 0.0001],
             'kernel': ['rbf']}
        ]
        clf = GridSearchCV(SVC(C=1, probability=True), param_grid, cv=5)
    elif classifier == 'GMM':  # Doesn't work best
        clf = GMM(n_components=nClasses)

    # ref:
    # http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html#example-classification-plot-classifier-comparison-py
    elif classifier == 'RadialSvm':  # Radial Basis Function kernel
        # works better with C = 1 and gamma = 2
        clf = SVC(C=1, kernel='rbf', probability=True, gamma=2)
    elif classifier == 'DecisionTree':  # Doesn't work best
        clf = DecisionTreeClassifier(max_depth=20)
    elif classifier == 'GaussianNB':
        clf = GaussianNB()

    # ref: https://jessesw.com/Deep-Learning/
    elif classifier == 'DBN':
        from nolearn.dbn import DBN
        clf = DBN([embeddings.shape[1], 500, labelsNum[-1:][0] + 1],  # i/p nodes, hidden nodes, o/p nodes
                  learn_rates=0.3,
                  # Smaller steps mean a possibly more accurate result, but the
                  # training will take longer
                  learn_rate_decays=0.9,
                  # a factor the initial learning rate will be multiplied by
                  # after each iteration of the training
                  epochs=300,  # no of iternation
                  # dropouts = 0.25, # Express the percentage of nodes that
                  # will be randomly dropped as a decimal.
                  verbose=1)

    if ldaDim > 0:
        clf_final = clf
        clf = Pipeline([('lda', LDA(n_components=ldaDim)),
                        ('clf', clf_final)])

    clf.fit(embeddings, labelsNum)

    fName = "{}/classifier.pkl".format(workDir)
    print("Saving classifier to '{}'".format(fName))
    with open(fName, 'wb') as f:
        pickle.dump((le, clf), f)





if __name__ == '__main__':
    train()
