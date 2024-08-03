import cv2 

#defines video capture object, what camera you are using 
cam = cv2.VideoCapture(0)

#name of window
cv2.namedWindow("Webcam Screenshot")

img_counter = 0

while True:
    ret,frame = cam.read()#capture the video frame by frame and stores it in variable 'frame'
    
    #Checks to see if frame captured
    if not ret:
        print("failed to grab frame")
        break
    
    #display the frame on screen
    cv2.imshow("test",frame)
    
    #detects and waits for user input 
    k = cv2.waitKey(1)
    
    #closes app if escape key pressed
    if k%256 == 27:
        print("Escape hit, closing the app")
        break
    
    #takes picture if space key pressed
    elif k%256 == 32:
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("screenshot taken")
        img_counter += 1
        
        
        

cam.release()

cam.destroyAllWindows()
