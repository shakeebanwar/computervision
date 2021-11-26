import cv2
import numpy as np



def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print("area==>",area)
        if area > 1:
            #Outline the shapes
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3) #(255,0,0) color,3 is a thickness,imgContour is a real image
            
            ###Draw a boundary for each shape

            peri = cv2.arcLength(cnt,True)
            print("peri",peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print("approx",len(approx)) #if len=4 means square or 3 is triangle

            objCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)


            if objCor == 3:
                objectType = "Tri"

            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"

                else:
                    objectType = "Rectangle"

            elif objCor > 4:
                objectType = "Circle"


            else:
                objectType = "None"
            
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)  #put text on center


     

path = "images/shape4.jpeg"
img = cv2.imread(path)
imgContour = img.copy()


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #covert to grayscale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1) # then add some blur
imgCanny = cv2.Canny(imgBlur,50,50) #find the edfges
getContours(imgCanny) ##highligh boundary and identify things


print(img.shape,imgGray.shape,imgBlur.shape)

cv2.imshow("Orignal",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("imgCanny",imgCanny)
cv2.imshow("outline",imgContour)


cv2.waitKey(0)