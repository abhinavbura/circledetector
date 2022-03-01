from cgitb import grey
import cv2
import numpy as np

cap = cv2.VideoCapture("http://192.168.0.104:8080/video")
cap.set(cv2.CAP_PROP_FPS, 1)
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=60,maxRadius=100)
    circles = np.uint16(np.around(circles))
    c=0
    for i in circles[0,:]:
        c+=1 
        # draw the outer circle
        cv2.circle(gray,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(gray,(i[0],i[1]),2,(0,0,255),3)
    print("no of baloons:"+str(c))
    cv2.imshow('detected circles',gray)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()