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





