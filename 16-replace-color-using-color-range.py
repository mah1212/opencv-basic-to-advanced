# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:15:18 2018

@author: Mahbub 
"""
# =============================================================================
# 
# Tutorial: 
# https://stackoverflow.com/questions/46112326/what-is-the-range-of-hsv-values-for-brown-color-in-opencv
# https://stackoverflow.com/questions/45070661/pythonopencv-how-to-plot-hsv-range/45071147#45071147
# 
# =============================================================================

import cv2
import numpy as np

## Read
img = cv2.imread("sunflower.jpg")

## convert to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "brown"
light_green_lo = np.array([36, 0, 0])
light_green_hi = np.array([44, 255,255])

# Mask image to only select browns
mask=cv2.inRange(hsv,light_green_lo,light_green_hi)

# Change image to red where we found brown
img[mask>0]=(0,0,255)

cv2.imwrite("replaced-sunflower.png",img)

cv2.imshow("result", img)
# =============================================================================
# # Define lower and uppper limits of what we call "brown"
# brown_lo=np.array([10,0,0])
# brown_hi=np.array([20,255,255])
# 
# # Mask image to only select browns
# mask=cv2.inRange(hsv,brown_lo,brown_hi)
# 
# # Change image to red where we found brown
# img[mask>0]=(0,0,255)
# 
# cv2.imwrite("replaced.png",img)
# =============================================================================



# =============================================================================
# ## mask of green (36,0,0) ~ (70, 255,255)
# mask1 = cv2.inRange(hsv, (36, 0, 0), (70, 255,255))
# 
# mask1 = np.ones_like(mask1)
# 
# ## mask o yellow (15,0,0) ~ (36, 255, 255)
# mask2 = cv2.inRange(hsv, (15,0,0), (36, 255, 255))
# 
# ## final mask and masked
# mask = cv2.bitwise_or(mask1, mask2)
# target = cv2.bitwise_and(img,img, mask=mask)
# 
# cv2.imwrite("target.png", target)
# 
# 
# cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)
# 
# cv2.imshow('result',mask1)
# =============================================================================



# Create green hsv programmatically
light_green = np.uint8([[[36, 77, 17]]])

hsv_light_green = cv2.cvtColor(light_green,cv2.COLOR_BGR2HSV)

print(hsv_light_green)
# Output: [[[ 60 255 255]]]
# Light green lower bound: [[[ 83 198 209]]]
# Light green upper bound: [[[ 70 199  77]]]


"""
For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]. 
Different softwares use different scales. So if you are comparing OpenCV values 
with them, you need to normalize these ranges.
"""

k = cv2.waitKey(0) & 0xFF 

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('written-img1.png',img)
    cv2.destroyAllWindows()



""" Color Space Video File
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
"""


"""

How to find HSV values to track?

This is a common question found in stackoverflow.com. It is very simple and you
can use the same function, cv2.cvtColor(). Instead of passing an image, you just 
pass the BGR values you want. For example, to find the HSV value of Green, try 
following commands in Python terminal:

>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
>>> print hsv_green
[[[ 60 255 255]]]

Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively. Apart from this method, you can use any image editing tools like GIMP or any online converters to find these values, but don’t forget to adjust the HSV ranges.

"""
"""
light green:
    lower: rgb(170, 209, 47)
    upper: rgb(36, 77, 17)
"""    