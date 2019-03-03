'''
Rotation

Rotation of an image for an angle θ is achieved by the transformation matrix

α=scale⋅cosθ,β=scale⋅sinθ

To find this transformation matrix, OpenCV provides a function, cv.getRotationMatrix2D. 
Check below example which rotates the image by 90 degree with respect to center without any scaling. 
'''

import numpy as np
import cv2 as cv

img = cv.imread('fruits.jpg',0)

rows,cols = img.shape

# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
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