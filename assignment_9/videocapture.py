#! /usr/bin/env python3
import numpy as np 
import cv2
from numpy.lib.type_check import imag

video=cv2.VideoCapture('robot.mp4',0)
while(True):
    ret , frame=video.read()
    cv2.rectangle(frame,(100,100),(400,400),(0,255,0),5)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #q being made break key 
        break 

video.release()
cv2.destroyAllWindows()



