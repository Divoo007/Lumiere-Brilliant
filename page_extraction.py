import cv2
import numpy as np

if __name__ == "__main__":
    capture = cv2.VideoCapture(0)
    while (True):
        ret, roi = capture.read()
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY) #convert roi into gray
        Blur=cv2.GaussianBlur(gray,(5,5),1) #apply blur to roi
        Canny=cv2.Canny(Blur,10,50) #apply canny to roi

        #Find my contours
        contours =cv2.findContours(Canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)[0]

        #Loop through my contours to find rectangles and put them in a list, so i can view them individually later.
        biggest = np.array([[[0, 0]],
            [[0, 0]],
            [[0, 0]],
            [[0, 0]]])
        for i in contours:
                
                epsilon = 0.05*cv2.arcLength(i,True)
                approx = cv2.approxPolyDP(i,epsilon,True)
                if len(approx) == 4:
                    area = cv2.contourArea(i)

                    if area > cv2.contourArea(biggest):
                        biggest = i
                    

    
        cv2.drawContours(roi,[biggest],-1,(0,255,0),2)
        cv2.imshow('Roi Rect ONLY',roi)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()