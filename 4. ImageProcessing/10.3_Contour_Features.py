'''
    features of contours, like area, perimeter, centroid, bounding box etc
    

1. Moments

Image moments help you to calculate some features like 
center of mass of the object, 
area of the object etc. 
Check out the wikipedia page on Image Moments

The function cv.moments() gives a dictionary 
of all moment values calculated. 

See below:
'''

import numpy as np
import cv2 as cv

original = cv.imread('shape.jpg')
img = cv.imread('shape.jpg',0)

ret,thresh = cv.threshold(img,127,255,0)

img, contours,hierarchy = cv.findContours(thresh, 1, 2)

cnt = contours[0]

M = cv.moments(cnt)

print('cv.moments gives a dictionary of all moments:')
print( M )

img_cont = cv.drawContours(original, contours, 0, (0,255,0), 3)
cv.imshow('Image', img)
cv.imshow('Image Contours', img_cont)
'''

From this moments, you can extract useful data like area, centroid etc. 
Centroid is given by the relations, Cx=M10M00 and Cy=M01M00. 
This can be done as follows:
'''    
    
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

print('Centroid of the Image using Moments')
print('cx', cx)
print('cy', cy)

'''
2. Contour Area

Contour area is given by the function cv.contourArea() or from moments, M['m00'].
'''

area = cv.contourArea(cnt)
print('Area', area)

'''
3. Contour Perimeter

It is also called arc length. It can be found out using cv.arcLength() function. Second argument specify whether shape is a closed contour (if passed True), or just a curve.
'''

perimeter = cv.arcLength(cnt,True)
print('Perimeter', perimeter)

'''
4. Contour Approximation

It approximates a contour shape to another shape with less number of vertices 
depending upon the precision we specify. 

It is an implementation of Douglas-Peucker algorithm. Check the wikipedia page 
for algorithm and demonstration.

To understand this, suppose you are trying to find a square in an image, 
but due to some problems in the image, you didn't get a perfect square, 

but a "bad shape" (As shown in first image below). Now you can use this 
function to approximate the shape. 

In this, second argument is called epsilon, 
which is maximum distance from contour to approximated contour. 
It is an accuracy parameter. A wise selection of epsilon is needed to get the 
correct output.
'''
epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)
print('epsilon', epsilon)
print('approx', approx)


'''
How to draw the contours?

To draw the contours, cv.drawContours function is used. It can also be used to draw any shape provided you have its boundary points. Its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc.

    To draw all the contours in an image:
    cv.drawContours(img, contours, -1, (0,255,0), 3)
    To draw an individual contour, say 4th contour:
    cv.drawContours(img, contours, 3, (0,255,0), 3)
    But most of the time, below method will be useful:
    cnt = contours[4]
    cv.drawContours(img, [cnt], 0, (0,255,0), 3)
    '''

'''    
There is a little bit things to discuss about it its syntax:
hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]]

Arguments details:

    points are the contours we pass into.
    hull is the output, normally we avoid it.
    clockwise : Orientation flag. If it is True, the output convex hull is oriented clockwise. Otherwise, it is oriented counter-clockwise.
    returnPoints : By default, True. Then it returns the coordinates of the hull points. If False, it returns the indices of contour points corresponding to the hull points.

So to get a convex hull as in above image, following is sufficient:
hull = cv.convexHull(cnt)

But if you want to find convexity defects, you need to pass returnPoints = False. To understand it, we will take the rectangle image above. First I found its contour as cnt. Now I found its convex hull with returnPoints = True, I got following values: [[[234 202]], [[ 51 202]], [[ 51 79]], [[234 79]]] which are the four corner points of rectangle. Now if do the same with returnPoints = False, I get following result: [[129],[ 67],[ 0],[142]]. These are the indices of corresponding points in contours. For eg, check the first value: cnt[129] = [[234, 202]] which is same as first result (and so on for others).
'''

'''
7. Bounding Rectangle

There are two types of bounding rectangles.
7.a. Straight Bounding Rectangle

It is a straight rectangle, it doesn't consider the rotation of the object. So area of the bounding rectangle won't be minimum. It is found by the function cv.boundingRect().

Let (x,y) be the top-left coordinate of the rectangle and (w,h) be its width and height.
'''
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

'''
7.b. Rotated Rectangle

Here, bounding rectangle is drawn with minimum area, so it considers the rotation also. The function used is cv.minAreaRect(). It returns a Box2D structure which contains following detals - ( center (x,y), (width, height), angle of rotation ). But to draw this rectangle, we need 4 corners of the rectangle. It is obtained by the function cv.boxPoints()
'''
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),2)

'''
Both the rectangles are shown in a single image. Green rectangle shows the normal bounding rect. Red rectangle is the rotated rect.
'''
'''
8. Minimum Enclosing Circle

Next we find the circumcircle of an object using the function cv.minEnclosingCircle(). It is a circle which completely covers the object with minimum area.
'''
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)

'''

9. Fitting an Ellipse

Next one is to fit an ellipse to an object. It returns the rotated rectangle in which the ellipse is inscribed.
'''

ellipse = cv.fitEllipse(cnt)
cv.ellipse(img,ellipse,(0,255,0),2)

'''
fitellipse.png

10. Fitting a Line

Similarly we can fit a line to a set of points. Below image contains a set of white points. We can approximate a straight line to it.
'''

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

'''
fitline.jpg
'''