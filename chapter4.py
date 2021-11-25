#shapes And texts
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) ##create a zeros array

##Color the Image
#img[:] = 252, 128, 3 ##color the whole image 136,136,136 BGR
#img[200:300,300:] = 252, 128, 3  #color the specific part of image height*width


##Draw a line
#cv2.line(img,(0,0),(300,300),(0,255,0),3)  #starting point (0,0) endpoint (300,300)  color(0,255,0) and 3 is a thickness 

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) ##(img.shape[1],img.shape[0]) means width*height  
# cv2.imshow("Image",img)


##Draw a Rectangle
# cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(240,207),(120,120,150),cv2.FILLED) ##cv2.FILLED fill the rectangle color

#Draw a circle
cv2.circle(img,(400,50),30,(255,255,0),5) #(400,50) is a central point of circle 30 is a radius and (255,255,0) is color and 5 is a thickness 

#put a text on image
cv2.putText(img,"open cv",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1) #(300,100) is a origin,cv2.FONT_HARSHEY_COMPLEX is a font,1 is scale,(0,150,0) is a color,1 is a thickness 


cv2.imshow("Image",img)


cv2.waitKey(0)