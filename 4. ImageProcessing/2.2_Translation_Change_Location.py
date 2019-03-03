'''
You will see these functions: cv.getPerspectiveTransform

Transformations

OpenCV provides two transformation functions, cv.warpAffine and cv.warpPerspective, 
with which you can have all kinds of transformations. cv.warpAffine takes a 2x3 
transformation matrix while cv.warpPerspective takes a 3x3 transformation matrix 
as input.
'''

'''
Translation

Translation is the shifting of object's location. If you know the shift in (x,y) direction, 

You can take make it into a Numpy array of type np.float32 and pass it into cv.warpAffine() 
function. See below example for a shift of (100,50):
'''

import numpy as np
import cv2 as cv

img = cv.imread('fruits.jpg',0)

rows, cols = img.shape

M = np.float32([[1,0,100],[0,1,50]]) # M = numpy array

dst = cv.warpAffine(img,M,(cols,rows))

cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

'''
warning

Third argument of the cv.warpAffine() function is the size of the output image, 
which should be in the form of **(width, height)**. 

Remember width = number of columns, and height = number of rows.
'''