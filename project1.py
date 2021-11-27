import cv2
cap = cv2.VideoCapture(0) #read the facecam 0 means open the default camp if we have multiple camera so 1 or 2
cap.set(3,640) #set the width
cap.set(4,480) #set the height
cap.set(5,100) #set the brightness 5 is id you can use whatever you like




def findColor(img):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV ) ##convert RGB TO hsv image
    # lower = np.array([h_min,s_min,v_min])
    # upper = np.array([h_max,s_max,v_max])
    # mask = cv2.inRange(imgHSV,lower,upper)
    # cv2.imshow("hsv",mask)






while True: #video is a collection of multiple images so we use while loop
    success, img = cap.read() #read the frame one by one
    cv2.imshow("Video",img) #show the frame 
    if cv2.waitKey(1) & 0xFF == ord('q'): #when user press q so program is quit
        break
