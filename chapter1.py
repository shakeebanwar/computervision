##Read Image

# import cv2
# img = cv2.imread('images/car.jpeg') #read the image
# cv2.imshow('Output',img) #display the read image
# cv2.waitKey(0)  #0 means infinite


##Read Video

# import cv2
# cap = cv2.VideoCapture("video/test.mp4") #read the video 
# while True: #video is a collection of multiple images so we use while loop
#     success, img = cap.read() #read the frame one by one
#     cv2.imshow("Video",img) #show the frame 
#     if cv2.waitKey(1) & 0xFF == ord('q'): #when user press q so program is quit
#         break


# Webcam

import cv2
cap = cv2.VideoCapture(0) #read the facecam 0 means open the default camp if we have multiple camera so 1 or 2
cap.set(3,640) #set the width
cap.set(4,480) #set the height
cap.set(5,100) #set the brightness 5 is id you can use whatever you like


while True: #video is a collection of multiple images so we use while loop
    success, img = cap.read() #read the frame one by one
    cv2.imshow("Video",img) #show the frame 
    if cv2.waitKey(1) & 0xFF == ord('q'): #when user press q so program is quit
        break

