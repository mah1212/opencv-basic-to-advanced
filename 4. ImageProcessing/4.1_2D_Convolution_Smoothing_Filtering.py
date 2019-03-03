'''
2D Convolution ( Image Filtering )

As in one-dimensional signals, images also can be filtered with various low-pass 
filters(LPF), high-pass filters(HPF) etc. LPF helps in removing noises, blurring 
the images etc. HPF filters helps in finding edges in the images.

OpenCV provides a function cv.filter2D() to convolve a kernel with an image. 
As an example, we will try an averaging filter on an image. A 5x5 averaging 
filter kernel will look like below:

K=1/25⎡⎣⎢⎢⎢⎢⎢⎢1111111111111111111111111⎤⎦⎥⎥⎥⎥⎥⎥

Operation is like this: keep this kernel above a pixel, add all the 25 pixels 
below this kernel, take its average and replace the central pixel with the new 
average value. It continues this operation for all the pixels in the image. 
Try this code and check the result:
'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('noisy_bangla.png')

kernel = np.ones((5,5),np.float32)/25

dst = cv.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()