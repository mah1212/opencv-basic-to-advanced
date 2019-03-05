'''
CLAHE (Contrast Limited Adaptive Histogram Equalization)
The first histogram equalization we just saw, considers the global contrast of 
the image. In many cases, it is not a good idea. For example, below image shows 
an input image and its result after global histogram equalization.
'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('tajmahal.jpg',0)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

res = np.hstack((img,cl1)) #stacking images side-by-side
cv.imwrite('clahe_histogram.jpg',res)

# Global Histograms Equalization in OpenCV
'''
OpenCV has a function to do this, cv.equalizeHist(). Its input is just grayscale 
image and output is our histogram equalized image.

Below is a simple code snippet showing its usage for same image we used :

img = cv.imread('tajmahal.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imwrite('histogram_equlOpenCV.png',res)
'''