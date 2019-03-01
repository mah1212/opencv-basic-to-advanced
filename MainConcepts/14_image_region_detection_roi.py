# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:15:18 2018

@author: Mahbub 
"""


# =============================================================================
# Image ROI
# 
# Sometimes, you will have to play with certain region of images. For eye 
# detection in images, first face detection is done all over the image and when 
# face is obtained, we select the face region alone and search for eyes inside it 
# instead of searching whole image. It improves accuracy (because eyes are always 
# on faces :D ) and performance (because we search for a small area)
# 
# ROI is again obtained using Numpy indexing. Here I am selecting the ball and 
# copying it to another region in the image:
# =============================================================================



import cv2
import matplotlib.pyplot as plt

img = cv2.imread('roi.jpg')

ball = img[276:310, 330:390] # roi = image[y: y+h, x: x+w]
img[273:333, 100:160] = ball

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.show()



