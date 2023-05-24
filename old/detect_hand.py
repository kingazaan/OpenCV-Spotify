# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 15:31:39 2021

@author: abarlas14
"""

import cv2 as cv
import numpy as np
import os

# set current working director
os.chdir(r"\Users\Orang\Documents\GitHub\OpenCV-Spotify")

# videos to check out to detect hands: https://www.youtube.com/watch?v=HXDD7-EnGBY; https://www.youtube.com/watch?v=tAsbb9p-w8g; https://www.youtube.com/watch?v=h56M5iUVgGs;


# load in Yolo
net = cv.dnn.readNet("yolo_v3.weights", "yolo_v3.cfg")

# get class names
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# now get the input and output layers, and colors
layers_names = net.getLayerNames()
output_layers = [layers_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))

# Loading images from videos
cap = cv.VideoCapture(0)

# show video
while True:
    _, frame = cap.read()
    height, width, channels = frame.shape
    
    # detect objects, or blobs (with scale factor, )
    blob = cv.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    
    # TODO
    net.setInput(blob)
    outs = net.forward(output_layers)
    
    # show the info on screen
    class_ids, confidence, boxes = [], [], []
    
    # TODO
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_ids = np.argmax(scores)
            confidence = scores[class_ids]
            if confidence > 0.5:
                # this is when object is detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                
                # rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                
            cv.imshow('img', img)

    
    # break loop if escape key is pressed
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break


net.setInputSize(320, 320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

#
class_ids, confs, bbox = net.detect()



# detect "blobs" from images
blob = cv







########################
# ending functions

cap.release()
cv.destroyAllWindows()