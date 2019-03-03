'''Brut-Force with ORB Descriptors'''

'''
In this case, I have a queryImage and a trainImage. We will try to find the 
queryImage in trainImage using feature matching. 
'''

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread('box.png',0)          # queryImage
img2 = cv.imread('box_in_scene.png',0) # trainImage

# Initiate ORB detector
orb = cv.ORB_create()

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)


'''
Next we create a BFMatcher object with distance measurement cv.NORM_HAMMING 
(since we are using ORB) and crossCheck is switched on for better results. 
Then we use Matcher.match() method to get the best matches in two images. 
We sort them in ascending order of their distances so that best matches 
(with low distance) come to front. Then we draw only first 10 matches 
(Just for sake of visibility. You can increase it as you like) 
'''

# create BFMatcher object
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv.drawMatches(img1,kp1,img2,kp2,matches[:10], None, flags=2)
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