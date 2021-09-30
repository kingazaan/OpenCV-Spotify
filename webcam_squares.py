# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\ab\Documents\GitHub\OpenCV-notes")


# capture video (use 0 for webcam)
cap = cv.VideoCapture(0)

#baseline image
baselin_image = None

while True:
    _, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (25,25), cv.BORDER_DEFAULT)
    
    # Calculating the difference and image thresholding (aka gray minus image)
    delta = cv.absdiff(baseline_image, gray)
    threshold = cv.threshold(delta, 35, 255, cv.THRESH_BINARY)[1]
    
    # Finding all the contours (needs arguments for image, contour retreival method, and approximation method)
    (contours,_) = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Drawing rectangles bounding the contours (whose area is > 5000)
    # get rid of smaller contours basically
    for contour in contours:
        if cv.contourArea(contour) < 5000:
            continue
        (x, y, w, h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)
        
    ## create rectangles
    # left side
    cv.rectangle(img, (0,0), (img.shape[1]//6, img.shape[0]), (0, 255, 0), thickness=2)
    # right side
    cv.rectangle(img, (img.shape[1],0), ((img.shape[1]//6)*5, img.shape[0]), (0, 255, 0), thickness=2)
    # top
    cv.rectangle(img, (0, 0), (img.shape[1], (img.shape[0]//6)), (0, 0, 255), thickness=2)
    # bottom
    cv.rectangle(img, (0, (img.shape[0]//6)*5), (img.shape[1], img.shape[0]), (0, 0, 255), thickness=2)
    
    
    cv.imshow('img', img)
    
    # break loop if escape key is pressed
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

# release the camera
cap.release()


########################
# ending functions

cv.destroyAllWindows()