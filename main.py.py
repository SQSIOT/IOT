# -*- coding: utf-8 -*-
import time
import cv2
print(cv2.__version__)

cascade_src = 'cars.xml'
video_src = '/Users/ShindeA03/Desktop/Car-detection/database_videos/output11.avi'
#video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)
text = "CAR"

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test10.avi',fourcc, 20.0, (640,480))

try:
    while True:
        ret, img = cap.read()
        if (type(img) == type(None)):
            break
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)

        for (x,y,w,h) in cars:
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)      
            cv2.putText(img,text,(x,y),font,0.4,(0,255,0),2,cv2.LINE_AA)
            ##time.sleep(1)
        cv2.imshow('video', img)
        out.write(img)
        if cv2.waitKey(33) == 27:
           break

finally:
    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()
