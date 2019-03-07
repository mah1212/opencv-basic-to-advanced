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
import cv2 as cv
import numpy as np

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray,50,150,apertureSize = 3)
lines = cv.HoughLines(edges,1,np.pi/180,200)

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)
cv.imwrite('houghlines3.jpg',img)
