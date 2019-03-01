

# =============================================================================
# Harris Corner Detector in OpenCV
# 
# OpenCV has the function cv.cornerHarris() for this purpose. Its arguments are :
# 
#     img - Input image, it should be grayscale and float32 type.
#     blockSize - It is the size of neighbourhood considered for corner detection
#     ksize - Aperture parameter of Sobel derivative used.
#     k - Harris detector free parameter in the equation.
# 
# See the example below: 
# 
# =============================================================================
import numpy as np
import cv2 as cv

# Version OpenCV 4.0.1
# filename = 'chessboard.png'
filename = 'peppers_color.tif'
img = cv.imread(filename)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

gray = np.float32(gray)

dst = cv.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]

cv.imshow('dst',img)

if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()