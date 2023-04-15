import tkinter as tk
import cv2
from cvzone.PoseModule import PoseDetector
from PIL import Image,ImageTk
from tkinter import PhotoImage
from tkinter import messagebox


#detector=PoseDetector()

#cv2.title("human detection")
#iconphoto(False,PhotoImage(file="img\\logo.png"))
detector = PoseDetector()
cap=cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    test=img
    
    # cv2.imwrite("init image.jpg",img)
    img1 = detector.findPose(test)
    lmList, bboxInfo =detector.findPosition(img, bboxWithHands=True)
    #lmList, bboxInfo =detector.findPosition(test, bboxWithHands=True)
    cv2.imshow("AI-CAMERA", img)
    
    if True:
            # print(bboxInfo)      
            success,image = cap.read()
            count = 0
            success = True
            while success:
                if count<=10:
                   
                    success,image = cap.read()
                    
                    if bboxInfo!={}:
                        cv2.imwrite("Desktop\\ai-camera\\captured img\\frame%d.jpg" % count, image)
                        
                        #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
                    if cv2.waitKey(10) == 27:   
                        cv2.destroyAllWindows() 
                        vid.release()                 # exit if Escape is hit
                        break
                else: break
                count += 1
            # cv2.imwrite("detected image.jpg",img1)
    # print(img1)
    cv2.waitKey(9)

