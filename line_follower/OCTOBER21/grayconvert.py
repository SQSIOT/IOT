#Image Convertor

import cv2
image = cv2.imread('red6.jpg')
print image.shape
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print "this is fr gray image"
#print gray_image
def do_threshold(image, threshold = 170):
    (thresh, im_bw) = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return (thresh, im_bw)
(thresh, img_threshold) = do_threshold(gray_image, 35)
#print "this is fr threshold image"
#print img_threshold
threshold = 70
blck_wht = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('binary',blck_wht)
#print "this is fr binary image"
#print blck_wht
a = cv2.bitwise_not(blck_wht)
cv2.imshow('inverted',a)
print a

print a.shape
#print a.size
#height,width = a.shape
#print height,width
# for pixel value
#value = a[120,180]
#print value
#height,width = image.shape
value = a[290,500]
print value

#black =0
#print a[250,230]
#for i in xrange(588):
   # for j in xrange(679):
       # k = a.all()
    #f black == k:
        #  print i
        # print j



#cv2.imwrite('gray_image.png',gray_image)
#cv2.imshow('color_image',image)
#cv2.imshow('gray_image',gray_image)
#cv2.imshow('threshold',img_threshold) 
cv2.waitKey(0)# Waits forever for user to press any key
cv2.destroyAllWindows()# Closes displayed windows

