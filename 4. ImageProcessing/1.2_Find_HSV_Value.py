'''How to find HSV values to track? '''

'''This is a common question found in stackoverflow.com. It is very simple and 
you can use the same function, cv.cvtColor(). Instead of passing an image, you 
just pass the BGR values you want. For example, to find the HSV value of Green, 
try following commands in Python terminal:
    
>>> green = np.uint8([[[0,255,0 ]]])
>>> hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
>>> print( hsv_green )
[[[ 60 255 255]]]

Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound 
respectively. Apart from this method, you can use any image editing tools like 
GIMP or any online converters to find these values, but don't forget to adjust 
the HSV ranges.