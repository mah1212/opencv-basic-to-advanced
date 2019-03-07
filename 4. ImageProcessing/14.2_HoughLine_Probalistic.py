'''
Theory

The Hough Transform is a popular technique to detect any shape, if you can represent that shape in a mathematical form. It can detect the shape even if it is broken or distorted a little bit. We will see how it works for a line.
'''
'''
OpenCV function, cv.HoughLines(). It simply returns an array of :math:(rho, theta)` 
values. ρ is measured in pixels and θ is measured in radians. First parameter, 
Input image should be a binary image, so apply threshold or use canny edge 
detection before applying hough transform. Second and third parameters are ρ 
and θ accuracies respectively. Fourth argument is the threshold, which means 
the minimum vote it should get to be considered as a line. Remember, number of 
votes depends upon the number of points on the line. So it represents the 
minimum length of line that should be detected. 
'''

'''
Probabilistic Hough Transform

In the hough transform, you can see that even for a line with two arguments, 
it takes a lot of computation. Probabilistic Hough Transform is an optimization 
of the Hough Transform we saw. It doesn't take all the points into consideration. 
Instead, it takes only a random subset of points which is sufficient for line 
detection. Just we have to decrease the threshold. See image below which compares 
Hough Transform and Probabilistic Hough Transform in Hough space. 
'''

import cv2 as cv
import numpy as np
img = cv.imread('sudoku.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray,50,150,apertureSize = 3)
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
cv.imwrite('houghlines5.jpg',img)
