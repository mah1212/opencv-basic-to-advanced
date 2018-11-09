# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:15:18 2018

@author: Mahbub 
"""

# =============================================================================
# Use the function cv2.imread() to read an image. The image should be in the 
# working directory or a full path of image should be given.
# 
# Second argument is a flag which specifies the way image should be read.
# 
#     cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be 
#                         neglected. It is the default flag.
#     cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
#     cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
# 
# Note 
# 
# Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively. 
# 
# =============================================================================

import cv2


image = cv2.imread('abs1.jpg', 0)

cv2.namedWindow('result', cv2.WINDOW_AUTOSIZE)

cv2.imshow('result',image)

k = cv2.waitKey(0) & 0xFF 

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('abs1-written.png',image)
    cv2.destroyAllWindows()



# =============================================================================
# Warning
# 
# If you are using a 64-bit machine, you will have to modify k = cv2.waitKey(0) 
# line as follows : k = cv2.waitKey(0) & 0xFF 
# 
# k = cv2.waitKey(0)
# 
# =============================================================================

