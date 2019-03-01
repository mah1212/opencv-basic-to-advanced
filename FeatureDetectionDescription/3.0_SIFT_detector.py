# https://docs.opencv.org/4.0.1/da/df5/tutorial_py_sift_intro.html
# Harris does not work if the image is scaled. So, SIFT is introduced. 

import numpy as np
import cv2 as cv

img = cv.imread('home.jpg')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift = cv.xfeatures2d.SIFT_create()

# Calculate only keypoints
# kp = sift.detect(gray,None) 

# Calculate descriptor + keypoints
kp, des = sift.detectAndCompute(gray,None)


# Draw keypoints
img = cv.drawKeypoints(gray,kp,img)

cv.imwrite('sift_keypoints.jpg',img)


# Draw Rich keypoints
img_rich = cv.drawKeypoints(gray,kp,img,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv.imwrite('sift_rich_keypoints.jpg',img_rich)

print("Descriptor Value: ", des)