import numpy as np
import cv2
import sys
import dlib
from skimage import io

# You can download the required pre-trained face detection model here:
# http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
predictor_model = "shape_predictor_68_face_landmarks.dat"

# Create a HOG face detector using the built-in dlib class
face_detector = dlib.get_frontal_face_detector()
face_pose_predictor = dlib.shape_predictor(predictor_model)

#win = dlib.image_window()

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, image = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',image)

    # Run the HOG face detector on the image data
    detected_faces = face_detector(image, 1)

    print("Found {} faces in the image file ".format(len(detected_faces)))

    # Show the desktop window with the image
    #win.set_image(image)

    # Loop through each face we found in the image
    for i, face_rect in enumerate(detected_faces):

        Face = image[(face_rect.top()-20):(face_rect.bottom()+20),(face_rect.left()-20):(face_rect.right()+20)]
        cv2.imshow('frame',Face)
        # Detected faces are returned as an object with the coordinates
        # of the top, left, right and bottom edges
        print("- Face #{} found at Left: {} Top: {} Right: {} Bottom: {}".format(i, face_rect.left(), face_rect.top(),face_rect.right(), face_rect.bottom()))
        # Draw a box around each face we found
        #win.add_overlay(face_rect)
        # Get the the face's pose
        #pose_landmarks = face_pose_predictor(image, face_rect)
        # Draw the face landmarks on the screen.
        #win.add_overlay(pose_landmarks)
        #print(face_rect)
    #win.clear_overlay()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
