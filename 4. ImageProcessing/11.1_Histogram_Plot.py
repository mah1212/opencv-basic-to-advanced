'''
So what is histogram ? 
You can consider histogram as a graph or plot, which gives you an overall idea 
about the intensity distribution of an image. It is a plot with pixel values 
(ranging from 0 to 255, not always) in X-axis and corresponding number of pixels 
in the image on Y-axis.

It is just another way of understanding the image. By looking at the histogram 
of an image, you get intuition about contrast, brightness, intensity distribution 
etc of that image. Almost all image processing tools today, provides features 
on histogram. Below is an image from Cambridge in Color website, and I recommend 
you to visit the site for more details.
(Remember, this histogram is drawn for grayscale image, not color image)
https://www.cambridgeincolour.com/tutorials/histograms1.htm

Plotting Histograms

There are two ways for this,

    Short Way : use Matplotlib plotting functions
    Long Way : use OpenCV drawing functions

BINS :The above histogram shows the number of pixels for every pixel value, ie 
from 0 to 255. ie you need 256 values to show the above histogram. But consider, 
what if you need not find the number of pixels for all pixel values separately, 
but number of pixels in a interval of pixel values? say for example, you need to 
find the number of pixels lying between 0 to 15, then 16 to 31, ..., 240 to 255. 
You will need only 16 values to represent the histogram. And that is what is 
shown in example given in OpenCV Tutorials on histograms.

So what you do is simply split the whole histogram to 16 sub-parts and value of 
each sub-part is the sum of all pixel count in it. This each sub-part is called 
"BIN". In first case, number of bins were 256 (one for each pixel) while in 
second case, it is only 16. 

BINS is represented by the term histSize in OpenCV 
docs.

DIMS : It is the number of parameters for which we collect the data. In this 
case, we collect data regarding only one thing, intensity value. So here it is 1.

RANGE : It is the range of intensity values you want to measure. Normally, it 
is [0,256], ie all intensity values.


1. Histogram Calculation in OpenCV

So now we use cv.calcHist() function to find the histogram. its parameters :
cv.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])

    images : it is the source image of type uint8 or float32. it should be 
    given in square brackets, ie, "[img]".
    channels : it is also given in square brackets. It is the index of channel 
    for which we calculate histogram. For example, if input is grayscale image, 
    its value is [0]. For color image, you can pass [0], [1] or [2] to calculate 
    histogram of blue, green or red channel respectively.
    mask : mask image. To find histogram of full image, it is given as "None". 
    But if you want to find histogram of particular region of image, you have 
    to create a mask image for that and give it as mask. (I will show an 
                                                          example later.)
    histSize : this represents our BIN count. Need to be given in square brackets. 
    For full scale, we pass [256].
    ranges : this is our RANGE. Normally, it is [0,256].

So let's start with a sample image. Simply load an image in grayscale mode and 
find its full histogram.
img = cv.imread('home.jpg',0)
hist = cv.calcHist([img],[0],None,[256],[0,256])

hist is a 256x1 array, each value corresponds to number of pixels in that image 
with its corresponding pixel value.
'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

imgGray = cv.imread('tajmahal.jpg',0)
plt.hist(imgGray.ravel(),256,[0,256]); plt.show()

imgColor = cv.imread('tajmahal.jpg')

color = ('b','g','r')

for i,col in enumerate(color):
    histr = cv.calcHist([imgColor],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()


'''
from matplotlib import pyplot as plt
# Using openCV
img = cv.imread('tajmahal.jpg',0)

# create a mask
mask = np.zeros(img.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv.bitwise_and(img,img,mask = mask)

# Calculate histogram with mask and without mask
# Check third argument for mask
hist_full = cv.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221), plt.imshow(img, 'gray')
plt.subplot(222), plt.imshow(mask,'gray')
plt.subplot(223), plt.imshow(masked_img, 'gray')
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
plt.xlim([0,256])
plt.show()
'''