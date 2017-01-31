import cv2
#import cv2.cv as cv
# Get user supplied values
imagePath = "/home/pi/boypic.jpg"
cascPath ="/home/pi/opencv-2.4.10/data/haarcascades/haarcascade_frontalface_default.xml"
print"welcome in 1.py"
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(0, 0),
    flags =0
)
print "Found {0} faces!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found" ,image)
#cv2.waitKey(0)
