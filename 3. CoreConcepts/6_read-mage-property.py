# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 05:15:29 2018

@author: Mahbub
"""
import cv2
import numpy as np

def main():
    print('This is inside the main function')
    
    img = np.zeros((512, 512, 3), np.uint8)
    image_name = 'New Image'
    
    #Draw Line
    cv2.line(img, (0, 100), (100, 0), (0, 255, 0), 3 ) # BGR, 3=thickness
    
    #Draw Rectangle
    cv2.rectangle(img, (100, 200), (200, 300), (0, 0, 255), 3)
    
    #Draw Circle
    cv2.circle(img, (100, 100), 50, (200, 23, 34), 2)
    
    #Draw & Fill Circle
    cv2.circle(img, (220, 220), 50, (0, 0, 255), -1)
    
    #Draw Ellipse
    cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)
    
    #Adding Text to Image
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
    
    #Name and size of window
    cv2.namedWindow(image_name, cv2.WINDOW_AUTOSIZE)
    
    
    #Show Image
    cv2.imshow(image_name, img)
 
    #Destroy Window
    cv2.waitKey(0)
    cv2.destroyWindow(image_name)
    
    #Practice 
    #Draw the flag of Bangladesh
    
    
    '''

    '''
    
if __name__ == '__main__':
    main()
    
    