import cv2
print(cv2.__version__)
import time

count = 1
while True:
      img = cv2.imread("n%d.png" % count)
      cv2.imshow('img',img)
      resized_image = cv2.resize(img, (50, 50))
      cv2.imwrite("n%d.png" % count,img)     # save frame as JPEG file
      print("Resizing Image")
      # write the flipped frame
      count += 1
      
cv2.destroyAllWindows()
