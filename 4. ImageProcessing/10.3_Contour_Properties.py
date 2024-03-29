'''
Here we will learn to extract some frequently used properties of objects like 
Solidity, Equivalent Diameter, Mask image, Mean Intensity etc. More features 
can be found at Matlab regionprops documentation.

*(NB : Centroid, Area, Perimeter etc also belong to this category, but we have 
seen it in last chapter)*
1. Aspect Ratio

It is the ratio of width to height of bounding rect of the object.
'''

AspectRatio=WidthHeight
x,y,w,h = cv.boundingRect(cnt)
aspect_ratio = float(w)/h
'''

2. Extent

Extent is the ratio of contour area to bounding rectangle area.
'''
Extent=ObjectAreaBoundingRectangleArea
area = cv.contourArea(cnt)
x,y,w,h = cv.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area

'''
3. Solidity

Solidity is the ratio of contour area to its convex hull area.
'''
Solidity=ContourAreaConvexHullArea
area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area)/hull_area

'''
4. Equivalent Diameter

Equivalent Diameter is the diameter of the circle whose area is same as the contour area.

'''

area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4*area/np.pi)

'''
5. Orientation

Orientation is the angle at which object is directed. Following method also gives the Major Axis and Minor Axis lengths.
'''

(x,y),(MA,ma),angle = cv.fitEllipse(cnt)

'''

6. Mask and Pixel Points

In some cases, we may need all the points which comprises that object. It can be done as follows:
'''
    
mask = np.zeros(imgray.shape,np.uint8)
cv.drawContours(mask,[cnt],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))
#pixelpoints = cv.findNonZero(mask)

'''
Here, two methods, one using Numpy functions, next one using OpenCV function (last commented line) are given to do the same. Results are also same, but with a slight difference. Numpy gives coordinates in **(row, column)** format, while OpenCV gives coordinates in **(x,y)** format. So basically the answers will be interchanged. Note that, row = x and column = y.
7. Maximum Value, Minimum Value and their locations

We can find these parameters using a mask image.
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgray,mask = mask)
8. Mean Color or Mean Intensity

Here, we can find the average color of an object. Or it can be average intensity of the object in grayscale mode. We again use the same mask to do it.
mean_val = cv.mean(im,mask = mask)
9. Extreme Points

Extreme Points means topmost, bottommost, rightmost and leftmost points of the object.
'''

leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])

'''
For eg, if I apply it to an Bangladesh map, I get the following result :
''' 