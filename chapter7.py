##Color detection

import cv2
import numpy as np


def empty(a):
  
    pass


cv2.namedWindow("TrackBar")
cv2.resizeWindow("TrackBar",640,240)
cv2.createTrackbar("Hue Min","TrackBar",0,179,empty)
cv2.createTrackbar("Hue Max","TrackBar",159,179,empty)
cv2.createTrackbar("Sat Min","TrackBar",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBar",232,255,empty)
cv2.createTrackbar("Val Min","TrackBar",153,255,empty)
cv2.createTrackbar("Val Max","TrackBar",255,255,empty)


while True:
    img = cv2.imread('images/1.jpeg')
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV ) ##convert RGB TO hsv image
    h_min = cv2.getTrackbarPos("Hue Min","TrackBar")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBar")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBar")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBar")
    v_min = cv2.getTrackbarPos("Val Min","TrackBar")
    v_max = cv2.getTrackbarPos("Val Max","TrackBar")
    
    print("h_min",h_min)
    print("h_max",h_max)
    print("s_min",s_min)
    print("s_max",s_max)
    print("v_min",v_min)
    print("v_max",v_max)

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Orignal",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("mask",mask )
    cv2.imshow("imgResult ",imgResult )
    cv2.waitKey(1)
