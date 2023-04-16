import cv2
from cvzone.PoseModule import PoseDetector
#detector=PoseDetector()
detector = PoseDetector()
cap=cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    test=img
    
    # cv2.imwrite("init image.jpg",img)
    img1 = detector.findPose(test)
    lmList, bboxInfo =detector.findPosition(img, bboxWithHands=True)
    #lmList, bboxInfo =detector.findPosition(test, bboxWithHands=True)
    cv2.imshow("Press ESC To Exit ", img)
    if True:
            # print(bboxInfo)      
            success,image = cap.read()
            count = 0
            success = True
            while success:
                if count<=10:
                    #cv2.waitKey(1000)
                    success,image = cap.read()
                    if bboxInfo!={}:
                        #image.waitKey(1000)
                        cv2.imwrite("D:\\defence system\\Detected Images\\frame%d.jpg" % count, image) 
                        
                        #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
                    if cv2.waitKey(10) == 27:   
                        cv2.destroyAllWindows()                  
                        cap.release()
                                      # exit if Escape is hit
                        break
                else: break
                count += 1
            # cv2.imwrite("detected image.jpg",img1)
    # print(img1)
    cv2.waitKey(9)
