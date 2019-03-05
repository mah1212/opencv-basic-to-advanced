'''
 Please check first reference in additional resources, it has full diagramatic details on image blending, Laplacian Pyramids etc. Simply it is done as follows:

    Load the two images of apple and orange
    Find the Gaussian Pyramids for apple and orange (in this particular example, number of levels is 6)
    From Gaussian Pyramids, find their Laplacian Pyramids
    Now join the left half of apple and right half of orange in each levels of Laplacian Pyramids
    Finally from this joint image pyramids, reconstruct the original image.

Below is the full code. (For sake of simplicity, each step is done separately which may take more memory. You can optimize it if you want so). 
'''

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

A = cv.imread('apple.jpg')
B = cv.imread('orange.jpg')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)
    
# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]

for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i-1],GE)
    lpA.append(L)
    
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i-1],GE)
    lpB.append(L)
    
# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:int(cols/2)], lb[:,int(cols/2):]))
    LS.append(ls)
    
# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])
    
# image with direct connecting each half
real = np.hstack((A[:,:int(cols/2)],B[:, int(cols/2):]))
cv.imwrite('Pyramid_blending2.jpg',ls_)
cv.imwrite('Direct_blending.jpg',real)


plt.subplot(2, 2, 1), plt.imshow(A, cmap = 'gray')
plt.title('Apple'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(B, cmap = 'gray')
plt.title('Orange'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3),plt.imshow(ls_,cmap = 'gray')
plt.title('Pyramid Blending'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4),plt.imshow(real,cmap = 'gray')
plt.title('Direct Blending'), plt.xticks([]), plt.yticks([])

plt.show()