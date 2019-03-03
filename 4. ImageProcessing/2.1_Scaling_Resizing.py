'''
You will see these functions: cv.getPerspectiveTransform

Transformations

OpenCV provides two transformation functions, cv.warpAffine and cv.warpPerspective, 
with which you can have all kinds of transformations. cv.warpAffine takes a 2x3 
transformation matrix while cv.warpPerspective takes a 3x3 transformation matrix 
as input.
'''

'''
OpenCV comes with a function cv.resize() for this purpose. The size of the image 
can be specified manually, or you can specify the scaling factor. Different interpolation 
methods are used. 

Preferable interpolation methods are cv.INTER_AREA for shrinking and 
cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming. 

By default, interpolation method used is cv.INTER_LINEAR for all resizing purposes. 
You can resize an input image either of following methods: 
    
'''
import numpy as np
import cv2 as cv
img = cv.imread('fruits.jpg')

# The below code will double the image size
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)

cv.imshow("fruit", res)

#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)