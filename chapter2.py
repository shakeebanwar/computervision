
#convert RGB to GrayScale,blur image,find edges,thick edges,thin edges 
import cv2
import numpy as np
kernal = np.ones((5,5),np.uint8) ##mean define a 5x5 matrix and np.uint8 means integer of 8-bit can range from 0 to 255 

img = cv2.imread('images/car.jpeg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) ##convert your image into grayscale image
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) ##convert your image into grayscale image and add blur (7,7) is a kernal but kernal should be odd number and 0 is a sigma X
imgCanny = cv2.Canny(img,100,100) ##100,100  is a Thresold value this function find the edges in the image
imgDialation=cv2.dilate(imgCanny,kernal,iterations=1) ###covert to thick edges iteration = 5 means more thick
imgEroded = cv2.erode(imgDialation,kernal,iterations=1) ##thin edges

cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur image",imgBlur)
cv2.imshow("Canny image",imgCanny)
cv2.imshow("Dialation image",imgDialation)
cv2.imshow("Eroded image",imgEroded)
cv2.waitKey(0)
