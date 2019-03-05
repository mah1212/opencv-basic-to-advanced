'''

OpenCV provides three types of gradient filters or High-pass filters, Sobel, 
Scharr and Laplacian. We will see each one of them.

1. Sobel and Scharr Derivatives

Sobel operators is a joint Gausssian smoothing plus differentiation operation, 
so it is more resistant to noise. You can specify the direction of derivatives 
to be taken, vertical or horizontal (by the arguments, yorder and xorder respectively). 
You can also specify the size of kernel by the argument ksize. If ksize = -1, 
a 3x3 Scharr filter is used which gives better results than 3x3 Sobel filter. 
Please see the docs for kernels used.

2. Laplacian Derivatives

It calculates the Laplacian of the image given by the relation, 
where each derivative is found using Sobel derivatives. If ksize = 1, then 
following kernel is used for filtering:
    
'''
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('sudoku.png', 0)

laplacian = cv.Laplacian(img,cv.CV_64F)
sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()


