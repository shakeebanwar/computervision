##Joing images
import cv2
import numpy as np

img = cv2.imread('images/1.jpeg')
img2 = cv2.imread('images/2.jpeg')
imgHor = np.hstack((img,img2)) ##horizontal join
imgVer = np.vstack((img,img2)) ##vertical join



cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)