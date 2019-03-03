

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

# =============================================================================
# Corner with SubPixel Accuracy
# 
# Sometimes, you may need to find the corners with maximum accuracy. OpenCV comes 
# with a function cv.cornerSubPix() which further refines the corners detected 
# with sub-pixel accuracy. Below is an example. As usual, we need to find the 
# harris corners first. Then we pass the centroids of these corners (There may 
# be a bunch of pixels at a corner, we take their centroid) to refine them. 
# Harris corners are marked in red pixels and refined corners are marked in 
# green pixels. For this function, we have to define the criteria when to stop 
# the iteration. We stop it after a specified number of iteration or a certain 
# accuracy is achieved, whichever occurs first. We also need to define the size 
# of neighbourhood it would search for corners. 
# 
# =============================================================================

import numpy as np
import cv2 as cv


filename = 'peppers_color.tif'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# find Harris corners
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
dst = cv.dilate(dst,None)
ret, dst = cv.threshold(dst,0.01*dst.max(),255,0)
dst = np.uint8(dst)

# find centroids
ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)

# define the criteria to stop and refine the corners
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# Now draw them
res = np.hstack((centroids,corners))
res = np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]] = [0,255,0]
cv.imwrite('subpixel5.png',img)