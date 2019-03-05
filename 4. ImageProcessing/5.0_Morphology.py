'''
Morphology

Morphological transformations are some simple operations based on the image shape. 
It is normally performed on binary images. It needs two inputs, one is our 
original image, second one is called structuring element or kernel which decides 
the nature of operation. 

Two basic morphological operators are Erosion and Dilation. Then its variant 
forms like Opening, Closing, Gradient etc also comes into play. 

We will see them one-by-one with help of following 
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('j.png')

kernel = np.ones((5,5),np.uint8)

erosion = cv.erode(img,kernel,iterations = 1)
dilation = cv.dilate(img,kernel,iterations = 1)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)


titles = ['Original Image','Erosion','Dilation','Opening','Closing','Gradient', 'Tophat', 'blackhat']

images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]

for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()


'''
Structuring Element

We manually created a structuring elements in the previous examples with help of Numpy. 
It is rectangular shape. But in some cases, you may need elliptical/circular shaped kernels. 
So for this purpose, OpenCV has a function, cv.getStructuringElement(). You just pass 
the shape and size of the kernel, you get the desired kernel.
# Rectangular Kernel
>>> cv.getStructuringElement(cv.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
>>> cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
>>> cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)
'''
