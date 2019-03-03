'''
You will learn following functions : cv.cvtColor(), cv.inRange() etc.

Changing Color-space

There are more than 150 color-space conversion methods available in OpenCV. 
But we will look into only two which are most widely used ones, BGR ↔ Gray and BGR ↔ HSV.

For color conversion, we use the function cv.cvtColor(input_image, flag) where 
flag determines the type of conversion.

For BGR → Gray conversion we use the flags cv.COLOR_BGR2GRAY. Similarly for 
BGR → HSV, we use the flag cv.COLOR_BGR2HSV. To get other flags, just run 
following commands in your Python terminal : 
'''

# Object Tracking    

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0) # Webcam capture

while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()