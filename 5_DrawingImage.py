# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 05:15:29 2018

@author: Mahbub
"""
import cv2

def main():
    print('This is inside the main function')
    
    # Read Image
    img_path = 'peppers_color.tif'
    img = cv2.imread(img_path, 1) # Load image to img variable


    print(type(img))
    print(img.dtype)
    print(img.shape) # Resolution of the Image
    print(img.ndim)
    print(img.size)
    print(img)
    
    
    #Name and size of window
    cv2.namedWindow('Peppers', cv2.WINDOW_AUTOSIZE)
    
    #Show Image
    cv2.imshow('Peppers', img)
    
    #Destroy Window
    cv2.waitKey(0)
    cv2.destroyWindow('Peppers')
    
    
    '''
    Imaage Output
    Color Image
    <class 'numpy.ndarray'>
    uint8 # Unsigned integer of 8 bit
    (512, 512, 3) # Resolution 512 by 512 and 3 Channels: Blue Green Red
    3 # 3 Dimensional Image
    786432 # Image size 512 * 512 * 3
[[[ 57  97 172]
  [ 57  97 172]
  [ 28  95 170]
  ...
  [107 193 161]
  [111 193 148]
  [132 181 158]]

 [[ 57  97 172]
  [ 57  97 172]
  [ 54  72 176]
  ...
  [107 193 161]
  [132 181 158]
  [132 181 158]]

 [[ 88 107 182]
  [ 57  97 172]
  [ 28  95 170]
  ...
  [107 193 161]
  [107 193 161]
  [131 164 177]]

 ...

 [[ 99 143 137]
  [ 70 123 137]
  [ 64 118 115]
  ...
  [160 193 205]
  [188 214 168]
  [192 218 185]]

 [[ 90 142 143]
  [ 75 103 135]
  [ 64 118 115]
  ...
  [192 218 185]
  [192 218 185]
  [160 193 205]]

 [[ 75 103 135]
  [ 70 123 137]
  [ 44 107 132]
  ...
  [160 193 205]
  [188 214 168]
  [188 214 168]]]
 
 
    Greyscale Image
<class 'numpy.ndarray'>
[[115 115 110 ... 174 170 169]
 [115 115 101 ... 174 169 169]
 [127 115 110 ... 174 174 164]
 ...
 [136 121 111 ... 193 197 205]
 [136 109 111 ... 205 205 193]
 [109 121 107 ... 193 197 197]]
    '''
    
if __name__ == '__main__':
    main()
    
    