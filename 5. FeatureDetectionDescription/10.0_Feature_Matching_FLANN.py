''' FLANN based Matcher '''

'''
In this case, I have a queryImage and a trainImage. We will try to find the 
queryImage in trainImage using feature matching. 



FLANN based Matcher

FLANN stands for Fast Library for Approximate Nearest Neighbors. It contains a 
collection of algorithms optimized for fast nearest neighbor search in large 
datasets and for high dimensional features. It works faster than BFMatcher for 
large datasets. We will see the second example with FLANN based matcher.

For FLANN based matcher, we need to pass two dictionaries which specifies the 
algorithm to be used, its related parameters etc. First one is IndexParams. 
For various algorithms, the information to be passed is explained in FLANN docs. 
As a summary, for algorithms like SIFT, SURF etc. you can pass following: 
    
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)

While using ORB, you can pass the following. The commented values are recommended 
as per the docs, but it didn't provide required results in some cases. Other 
values worked fine.:
    
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2

Second dictionary is the SearchParams. It specifies the number of times the trees 
in the index should be recursively traversed. Higher values gives better precision, 
but also takes more time. If you want to change the value, 
pass search_params = dict(checks=100).

With this information, we are good to go. 
    
'''

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

print(cv.__version__)

img1 = cv.imread('box.png',0)          # queryImage
img2 = cv.imread('box_in_scene.png',0) # trainImage

# Initiate SIFT detector
sift = cv.xfeatures2d.SIFT_create() # for openCV 3.x
#sift = cv.SIFT() # for openCV 4.0.1

# find the keypoints and descriptors with ORB
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)


# FLANN parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv.FlannBasedMatcher(index_params,search_params)
matches = flann.knnMatch(des1,des2,k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0,0] for i in range(len(matches))]
# ratio test as per Lowe's paper
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]
draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)
img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
plt.imshow(img3,),plt.show()


'''
What is this Matcher Object?

The result of matches = bf.match(des1,des2) line is a list of DMatch objects. 
This DMatch object has following attributes:

    DMatch.distance - Distance between descriptors. The lower, the better it is.
    DMatch.trainIdx - Index of the descriptor in train descriptors
    DMatch.queryIdx - Index of the descriptor in query descriptors
    DMatch.imgIdx - Index of the train image.
'''