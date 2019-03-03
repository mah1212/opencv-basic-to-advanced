# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:15:18 2018

@author: Mahbub 
"""



import cv2
# import numpy as np

## Read
img = cv2.imread("sunflower.jpg")

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,0,0) ~ (70, 255,255)
mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))

# mask1 = np.zeros_like(mask1)

## mask o yellow (15,0,0) ~ (36, 255, 255)
mask2 = cv2.inRange(hsv, (15,0,0), (36, 255, 255))

## final mask and masked
mask = cv2.bitwise_or(mask1, mask2)
target = cv2.bitwise_and(img,img, mask=mask)

cv2.imwrite("target.png", target)


cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)

cv2.imshow('result',mask1)

k = cv2.waitKey(0) & 0xFF 

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('written-img1.png',mask1)
    cv2.destroyAllWindows()
