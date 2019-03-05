'''
Introduction

In the first article, we calculated and plotted one-dimensional histogram. It is called one-dimensional because we are taking only one feature into our consideration, ie grayscale intensity value of the pixel. But in two-dimensional histograms, you consider two features. Normally it is used for finding color histograms where two features are Hue & Saturation values of every pixel.

There is a python sample (samples/python/color_histogram.py) already for finding color histograms. We will try to understand how to create such a color histogram, and it will be useful in understanding further topics like Histogram Back-Projection.
2D Histogram in OpenCV

It is quite simple and calculated using the same function, cv.calcHist(). For color histograms, we need to convert the image from BGR to HSV. (Remember, for 1D histogram, we converted from BGR to Grayscale). For 2D histograms, its parameters will be modified as follows:

    channels = [0,1] because we need to process both H and S plane.
    bins = [180,256] 180 for H plane and 256 for S plane.
    range = [0,180,0,256] Hue value lies between 0 and 180 & Saturation lies between 0 and 256.

Now check the code below:
import numpy as np
import cv2 as cv
img = cv.imread('home.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

2D Histogram in Numpy

Numpy also provides a specific function for this : np.histogram2d(). (Remember, for 1D histogram we used np.histogram() ).
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('home.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist, xbins, ybins = np.histogram2d(h.ravel(),s.ravel(),[180,256],[[0,180],[0,256]])

Plotting 2D Histograms
Method - 1 : Using cv.imshow()

The result we get is a two dimensional array of size 180x256. So we can show them as we do normally, using cv.imshow() function. It will be a grayscale image and it won't give much idea what colors are there, unless you know the Hue values of different colors.
Method - 2 : Using Matplotlib

We can use matplotlib.pyplot.imshow() function to plot 2D histogram with different color maps. It gives us a much better idea about the different pixel density. But this also, doesn't gives us idea what color is there on a first look, unless you know the Hue values of different colors. Still I prefer this method. It is simple and better.

Note
    While using this function, remember, interpolation flag should be nearest for better results.

Consider code:

'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('tajmahal.jpg')
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
hist = cv.calcHist( [hsv], [0, 1], None, [180, 256], [0, 180, 0, 256] )
plt.imshow(hist,interpolation = 'nearest')
plt.show()



#!/usr/bin/env python

'''
Video histogram sample to show live histogram of video

Keys:
    ESC    - exit

'''


'''
import numpy as np
import cv2 as cv

# built-in modules
import sys

# local modules
import video

if __name__ == '__main__':

    hsv_map = np.zeros((180, 256, 3), np.uint8)
    h, s = np.indices(hsv_map.shape[:2])
    hsv_map[:,:,0] = h
    hsv_map[:,:,1] = s
    hsv_map[:,:,2] = 255
    hsv_map = cv.cvtColor(hsv_map, cv.COLOR_HSV2BGR)
    cv.imshow('hsv_map', hsv_map)

    cv.namedWindow('hist', 0)
    hist_scale = 10

    def set_scale(val):
        global hist_scale
        hist_scale = val
    cv.createTrackbar('scale', 'hist', hist_scale, 32, set_scale)

    try:
        fn = sys.argv[1]
    except:
        fn = 0
    cam = video.create_capture(fn, fallback='synth:bg=baboon.jpg:class=chess:noise=0.05')

    while True:
        flag, frame = cam.read()
        cv.imshow('camera', frame)

        small = cv.pyrDown(frame)

        hsv = cv.cvtColor(small, cv.COLOR_BGR2HSV)
        dark = hsv[...,2] < 32
        hsv[dark] = 0
        h = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

        h = np.clip(h*0.005*hist_scale, 0, 1)
        vis = hsv_map*h[:,:,np.newaxis] / 255.0
        cv.imshow('hist', vis)

        ch = cv.waitKey(1)
        if ch == 27:
            break
    cv.destroyAllWindows()
'''
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
'''
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