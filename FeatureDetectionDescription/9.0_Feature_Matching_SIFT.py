''' Brute-Force Matching with SIFT Descriptors and Ratio Test '''

'''
In this case, I have a queryImage and a trainImage. We will try to find the 
queryImage in trainImage using feature matching. 



This time, we will use BFMatcher.knnMatch() to get k best matches. In this 
example, we will take k=2 so that we can apply ratio test explained by D.Lowe 
in his paper. 
'''

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

print(cv.__version__)

img1 = cv.imread('box.png',0)          # queryImage
img2 = cv.imread('box_in_scene.png',0) # trainImage

# Initiate SIFT detector
sift = cv.xfeatures2d.SIFT_create() # for openCV 3
#sift = cv.SIFT() # for openCV 4.0.1

# find the keypoints and descriptors with ORB
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)


# BFMatcher with default params
bf = cv.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# cv.drawMatchesKnn expects list of lists as matches.
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good, None, flags=2)
plt.imshow(img3),plt.show()


'''
What is this Matcher Object?

The result of matches = bf.match(des1,des2) line is a list of DMatch objects. 
This DMatch object has following attributes:

    DMatch.distance - Distance between descriptors. The lower, the better it is.
    DMatch.trainIdx - Index of the descriptor in train descriptors
    DMatch.queryIdx - Index of the descriptor in query descriptors
    DMatch.imgIdx - Index of the train image.
'''