'''
Otsu’s Binarization

In the first section, I told you there is a second parameter retVal. Its usage 
comes when we go for Otsu’s Binarization. So what is it?

In global thresholding, we used an arbitrary value for threshold value, right? 
So, how can we know a value we selected is good or not? Answer is, trial and 
error method. But consider a bimodal image (In simple words, bimodal image is 
an image whose histogram has two peaks). For that image, we can approximately 
take a value in the middle of those peaks as threshold value, right? That is 
what Otsu binarization does. So in simple words, it automatically calculates 
a threshold value from image histogram for a bimodal image. 
(For images which are not bimodal, binarization won’t be accurate.)

For this, our cv.threshold() function is used, but pass an extra flag, 
cv.THRESH_OTSU. For threshold value, simply pass zero. Then the algorithm finds 
the optimal threshold value and returns you as the second output, retVal. 
If Otsu thresholding is not used, retVal is same as the threshold value you used.

Check out below example. Input image is a noisy image. In first case, I applied 
global thresholding for a value of 127. In second case, I applied Otsu’s 
thresholding directly. In third case, I filtered image with a 5x5 gaussian 
kernel to remove the noise, then applied Otsu thresholding. See how noise 
filtering improves the result. 
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('noisy_bangla.png',0)

blur = cv.GaussianBlur(img,(5,5),0)

# find normalized_histogram, and its cumulative distribution function
hist = cv.calcHist([blur],[0],None,[256],[0,256])

hist_norm = hist.ravel()/hist.max()

Q = hist_norm.cumsum()

bins = np.arange(256)

fn_min = np.inf

thresh = -1

for i in range(1,256):
    p1,p2 = np.hsplit(hist_norm,[i]) # probabilities
    q1,q2 = Q[i],Q[255]-Q[i] # cum sum of classes
    b1,b2 = np.hsplit(bins,[i]) # weights
    # finding means and variances
    m1,m2 = np.sum(p1*b1)/q1, np.sum(p2*b2)/q2
    v1,v2 = np.sum(((b1-m1)**2)*p1)/q1,np.sum(((b2-m2)**2)*p2)/q2
    # calculates the minimization function
    fn = v1*q1 + v2*q2
    if fn < fn_min:
        fn_min = fn
        thresh = i
# find otsu's threshold value with OpenCV function
ret, otsu = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
print( "{} {}".format(thresh,ret) )

