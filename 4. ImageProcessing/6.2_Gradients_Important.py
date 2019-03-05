'''
One Important Matter!

In our last example, output datatype is cv.CV_8U or np.uint8. But there is a 
slight problem with that. Black-to-White transition is taken as Positive slope 
(it has a positive value) while White-to-Black transition is taken as a 
Negative slope (It has negative value). So when you convert data to np.uint8, 
all negative slopes are made zero. In simple words, you miss that edge.

If you want to detect both edges, better option is to keep the output datatype 
to some higher forms, like cv.CV_16S, cv.CV_64F etc, take its absolute value 
and then convert back to cv.CV_8U. Below code demonstrates this procedure for 
a horizontal Sobel filter and difference in results.
'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('box.png',0)

# Output dtype = cv.CV_8U
sobelx8u = cv.Sobel(img,cv.CV_8U,1,0,ksize=5)

# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)

abs_sobel64f = np.absolute(sobelx64f)

sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()