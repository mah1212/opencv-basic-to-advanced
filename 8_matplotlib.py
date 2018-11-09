# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:15:18 2018

@author: Mahbub 
"""





# =============================================================================
# Warning
#
# Color image loaded by OpenCV is in BGR mode. But Matplotlib displays in RGB mode. 
# So color images will not be displayed correctly in Matplotlib if image is read 
# with OpenCV. Please see the exercises for more details.
# 
# =============================================================================


""" Error
TypeError: Image data cannot be converted to float

    Solution
    
    1. Make sure image is properly loaded
""" 


import cv2
import matplotlib.pyplot as plt

img = cv2.imread('abs1.jpg', 0)


plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([])
plt.yticks([])  # to hide tick values on X and Y axis
plt.show()



# =============================================================================
# 
# Note
# 
# There is a special case where you can already create a window and load image to
# it later. In that case, you can specify whether window is resizable or not. It 
# is done with the function cv2.namedWindow(). By default, the flag is 
# cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL, you can 
# resize window. It will be helpful when image is too large in dimension and 
# adding track bar to windows. 
# =============================================================================


