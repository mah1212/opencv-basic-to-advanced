'''
Consider an image whose pixel values are confined to some specific range of 
values only. For eg, brighter image will have all pixels confined to high values. 
But a good image will have pixels from all regions of the image. So you need to 
stretch this histogram to either ends (as given in below image, from wikipedia) 
and that is what Histogram Equalization does (in simple words). This normally 
improves the contrast of the image.

'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('tajmahal.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()

cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()


# Using Masked

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('tajmahal.jpg',0)

hist,bins = np.histogram(img.flatten(),256,[0,256])

cdf = hist.cumsum()

cdf_normalized = cdf * float(hist.max()) / cdf.max()


cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
img2 = cdf[img]

hist,bins = np.histogram(img2.flatten(),256,[0,256])

cdf = hist.cumsum()

cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(img2.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cv.imshow("Image", img)
cv.imshow("Image2", img2)


# Histograms Equalization in OpenCV
'''
OpenCV has a function to do this, cv.equalizeHist(). Its input is just grayscale 
image and output is our histogram equalized image.

Below is a simple code snippet showing its usage for same image we used :
'''
img = cv.imread('tajmahal.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv.imwrite('histogram_equlOpenCV.png',res)
