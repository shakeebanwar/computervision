#Face Detection
import cv2
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('images/group.jpeg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4) ##1.1 is a scale factor,4 is a minimum neighbour

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),)   ##(x,y is a initial point) and (x+w,y+h) is a daigonal and (255,0,0) is a thickness and 2 is a thickness
    print(x,y,w,h)

cv2.imshow("Result",img)
cv2.imshow("Grayscale",imgGray)
cv2.waitKey(0)