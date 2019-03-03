'''
Thresholding is the simplest method of image segmentation. From a grayscale image, 
thresholding can be used to create binary images (Shapiro, et al. 2001:83). 


'''
'''
Simple Thresholding

Here, the matter is straight forward. If pixel value is greater than a threshold 
value, it is assigned one value (may be white), else it is assigned another value 
(may be black). The function used is cv.threshold. First argument is the source 
image, which should be a grayscale image. Second argument is the threshold value 
which is used to classify the pixel values. Third argument is the maxVal which 
represents the value to be given if pixel value is more than (sometimes less than) 
the threshold value. OpenCV provides different styles of thresholding and it is 
decided by the fourth parameter of the function. Different types are:

    cv.THRESH_BINARY
    cv.THRESH_BINARY_INV
    cv.THRESH_TRUNC
    cv.THRESH_TOZERO
    cv.THRESH_TOZERO_INV

Documentation clearly explain what each type is meant for. Please check out the 
documentation.

Two outputs are obtained. First one is a retval which will be explained later. 
Second output is our thresholded image.

Code :

'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png',0)

ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']

images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
