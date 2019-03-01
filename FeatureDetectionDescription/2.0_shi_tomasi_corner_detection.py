
# https://github.com/opencv/opencv/tree/master/samples/python/tutorial_code
# =============================================================================
# OpenCV has a function, cv.goodFeaturesToTrack(). It finds N strongest corners 
# in the image by Shi-Tomasi method (or Harris Corner Detection, if you specify 
# it). As usual, image should be a grayscale image. Then you specify number of 
# corners you want to find. Then you specify the quality level, which is a value 
# between 0-1, which denotes the minimum quality of corner below which everyone 
# is rejected. Then we provide the minimum euclidean distance between corners 
# detected.
# 
# With all this information, the function finds corners in the image. All corners 
# below quality level are rejected. Then it sorts the remaining corners based on 
# quality in the descending order. Then function takes first strongest corner, 
# throws away all the nearby corners in the range of minimum distance and returns 
# N strongest corners.
# 
# In below example, we will try to find 25 best corners: 
# =============================================================================


import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('blox.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray,25,0.01,10)

corners = np.int0(corners)
for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()

# what does ravel() funciton do?
# what does cv.circle() function do?

"""
goodFeaturesToTrack() [1/2]
void cv::goodFeaturesToTrack 	( 	
        InputArray  	image,
		OutputArray  	corners,
		int  	maxCorners,
		double  	qualityLevel,
		double  	minDistance,
		InputArray  	mask = noArray(),
		int  	blockSize = 3,
		bool  	useHarrisDetector = false,
		double  	k = 0.04 
	) 		
Python:
	corners	=	cv.goodFeaturesToTrack(	image, maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]]	)
	corners	=	cv.goodFeaturesToTrack(	image, maxCorners, qualityLevel, minDistance, mask, blockSize, gradientSize[, corners[, useHarrisDetector[, k]]]	)

Determines strong corners on an image.

The function finds the most prominent corners in the image or in the specified image region, as described in [177]

    Function calculates the corner quality measure at every source image pixel using the cornerMinEigenVal or cornerHarris .
    Function performs a non-maximum suppression (the local maximums in 3 x 3 neighborhood are retained).
    The corners with the minimal eigenvalue less than qualityLevel⋅maxx,yqualityMeasureMap(x,y) are rejected.
    The remaining corners are sorted by the quality measure in the descending order.
    Function throws away each corner for which there is a stronger corner at a distance less than maxDistance.

The function can be used to initialize a point-based tracker of an object.
"""