import cv2
import numpy as np
img = cv2.imread('baloons.jpg',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=25,maxRadius=45)
circles = np.uint16(np.around(circles))
c=0
for i in circles[0,:]:
    c+=1 
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
print("no of baloons:"+str(c))
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()