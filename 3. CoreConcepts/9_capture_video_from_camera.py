# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 18:37:24 2018

@author: Mahbub
"""



# =============================================================================
# Capture Video from Camera
# 
# Often, we have to capture live stream with camera. OpenCV provides a very simple 
# interface to this. Let’s capture a video from the camera (I am using the in-built 
# webcam of my laptop), convert it into grayscale video and display it. Just a simple 
# task to get started.
# 
# To capture a video, you need to create a VideoCapture object. Its argument can be 
# either the device index or the name of a video file. Device index is just the number 
# to specify which camera. Normally one camera will be connected (as in my case). 
# So I simply pass 0 (or -1). You can select the second camera by passing 1 and so on. 
# After that, you can capture frame-by-frame. But at the end, don’t forget to release 
# the capture.
# =============================================================================

import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



"""
# =============================================================================
# cap.read() returns a bool (True/False). If frame is read correctly, it will be True. 
# So you can check end of the video by checking this return value.
# 
# Sometimes, cap may not have initialized the capture. In that case, this code shows error. 
# You can check whether it is initialized or not by the method cap.isOpened(). If it is True, OK. 
# Otherwise open it using cap.open().
# 
# You can also access some of the features of this video using cap.get(propId) method where 
# propId is a number from 0 to 18. Each number denotes a property of the video (if it is 
# applicable to that video) and full details can be seen here: Property Identifier. Some of 
# these values can be modified using cap.set(propId, value). Value is the new value you want.
# 
# For example, I can check the frame width and height by cap.get(3) and cap.get(4). It gives 
# me 640x480 by default. But I want to modify it to 320x240. Just use ret = cap.set(3,320) 
# and ret = cap.set(4,240).
# =============================================================================
"""

