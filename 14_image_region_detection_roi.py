# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:15:18 2018

@author: Mahbub 
"""


# =============================================================================
# You can access a pixel value by its row and column coordinates. For BGR image, 
# it returns an array of Blue, Green, Red values. For grayscale image, just 
# corresponding intensity is returned.
# =============================================================================


import cv2

img = cv2.imread('abs1.jpg')


# Read a pixel value from an image
px = img[100,100] # [x,y]
print(px) # output: [151 200 250] Blue, Green, Red

# accessing only blue pixel
blue = img[100,100,0] # [x,y, channel]
print(blue)



"""
Change pixel value
"""
img[100,100] = [255,255,255]
print(img[100,100])

""""""""""""""""""""""" Warning

Numpy is a optimized library for fast array calculations. So simply accessing 
each and every pixel values and modifying it will be very slow and it is discouraged.

####################### Note

Above mentioned method is normally used for selecting a region of array, say 
first 5 rows and last 3 columns like that. For individual pixel access, Numpy 
array methods, array.item() and array.itemset() is considered to be better. 
But it always returns a scalar. So if you want to access all B,G,R values, 
you need to call array.item() separately for all. 
"""

# Better pixel accessing and editing method :

# accessing RED value
img.item(10,10,2) # Output: 255


# modifying RED value
img.itemset((10,10,2),100)
img.item(10,10,2) # output: 100


# =============================================================================
# Accessing Image Properties
# 
# Image properties include number of rows, columns and channels, type of image data, 
# number of pixels etc.
# 
# Shape of image is accessed by img.shape. It returns a tuple of number of rows, 
# columns and channels (if image is color):
# 
# =============================================================================
print(img.shape)
# Output: (3452, 5472, 3) 
# =============================================================================
# 
# Note
# 
# If image is grayscale, tuple returned contains only number of rows and columns. So it is a good method to check if loaded image is grayscale or color image.
# 
# Total number of pixels is accessed by img.size:
# 
# =============================================================================

print(img.size)
# Output: 56668032

# Image datatype is obtained by img.dtype:

print(img.dtype) # Output: uint8

# =============================================================================
# 
# Note
# 
# img.dtype is very important while debugging because a large number of errors in 
# OpenCV-Python code is caused by invalid datatype.
# 
# =============================================================================


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
