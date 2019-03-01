# https://docs.opencv.org/4.0.1/da/df5/tutorial_py_sift_intro.html
# SIFT is slow, so SURF introduced.  
# In short, SURF adds a lot of features to improve the speed in every step. 
# Analysis shows it is 3 times faster than SIFT while performance is comparable to SIFT. 
# SURF is good at handling images with blurring and rotation, but not good at 
# handling viewpoint change and illumination change.

"""Incomplete"""
import numpy as np
import cv2 as cv

img = cv.imread('fly.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


# Create SURF object. You can specify params here or later.
# Here I set Hessian Threshold to 400
surf = cv.xfeatures2d.SURF_create(400)

# Calculate only keypoints
# kp = surf.detect(gray,None) 

# Calculate descriptor + keypoints
kp, des = surf.detectAndCompute(gray,None)

print("Length of kp: ", len(kp))


# Check present Hessian threshold
print( surf.getHessianThreshold() )

# We set it to some 50000. Remember, it is just for representing in picture.
# In actual cases, it is better to have a value 300-500
surf.setHessianThreshold(50000)

# Again compute keypoints and check its number.
kp, des = surf.detectAndCompute(img,None)
print( len(kp) )

# Draw keypoints
img = cv.drawKeypoints(gray,kp,img)

cv.imwrite('surf_keypoints.png',img)


# Draw Rich keypoints
img_rich = cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imwrite('surf_rich_keypoints.png',img_rich)

print("Descriptor Value: ", des)