#Number plate detection

import cv2


####################################
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
framewidth = 640
frameheight = 480
minArea = 500
color = (255,0,255)
count = 0
######################################




cap = cv2.VideoCapture(0) #read the facecam 0 means open the default camp if we have multiple camera so 1 or 2
cap.set(3,framewidth) #set the width
cap.set(4,480) #set the height
cap.set(5,frameheight) #set the brightness 5 is id you can use whatever you like




while True: #video is a collection of multiple images so we use while loop
    success, img = cap.read() #read the frame one by one
    
    img = cv2.imread('images/numberplate2.jpeg') ## if use back webcam so skip this line
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray,1.1,4) ##1.1 is a scale factor,4 is a minimum neighbour ,and this line detect the number plate regoin

    for (x,y,w,h) in numberPlates: ##cut the number plate region
        area = w*h
        if area > minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2) 
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRio = img[y:y+h,x:x+w] #cut the numberplate area and show
            cv2.imshow("Region",imgRio)




    cv2.imshow("Video",img) #show the frame 
    if cv2.waitKey(1) & 0xFF == ord('s'): #when user press q so program is quit
        cv2.imwrite("Resources/Scan/NoPlate_"+str(count)+".jpg",imgRio)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1


    if cv2.waitKey(1) & 0xFF == ord('q'): #when user press q so program is quit
        break
