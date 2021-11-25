import cv2

img = cv2.imread('images/car.jpeg')
print(img.shape) #(320, 480, 3) 320 is a height,480 is a width,3 means rgb 

#Resize
imgResize = cv2.resize(img,(300,200)) #Resize your image (300,200) width*height
print(imgResize.shape)

#Croping
imgCropped = img[0:200,:200] ##original image size is 320x480 means height*width so we easily slice height,width
print(imgCropped.shape)

cv2.imshow("Orignal",img)
cv2.imshow("Resize",imgResize)
cv2.imshow("Crop",imgCropped)

cv2.waitKey(0)