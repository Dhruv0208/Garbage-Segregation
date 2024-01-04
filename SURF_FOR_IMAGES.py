# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 07:52:46 2018

@author: dhruv
"""

import cv2
import numpy as np
import glob
import os

def surf_detector(new_image, image_template):
    # Function that compares input image to template
    # It then returns the number of SIFT matches between them
    
    image1 = cv2.cvtColor(new_image, cv2.COLOR_BGR2GRAY)
    
    image2 = image_template
    
    #fast = cv2.FastFeatureDetector()
    #keypoints_1 = fast.detect(image1, None)
    #keypoints_2 = fast.detect(image2, None)
    # Create SIFT detector object
    #sift = cv2.SIFT()
    surf= cv2.SURF()
    surf.hessianThreshold = 500
     
    # Obtain the keypoints and descriptors using SIFT
    keypoints_1, descriptors_1 = surf.detectAndCompute( image1, None)
    keypoints_2, descriptors_2 = surf.detectAndCompute( image2, None)

    # Define parameters for our Flann Matcher
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 3)
    search_params = dict(checks = 100)

    # Create the Flann Matcher object
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    # Obtain matches using K-Nearest Neighbor Method
    # the result 'matchs' is the number of similar matches found in both images
    matches = flann.knnMatch(descriptors_1, descriptors_2, k=2)

    # Store good matches using Lowe's ratio test
    good_matches = []
    for m,n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m) 

    return len(good_matches)

# now we have number of descriptors
cv_img = []
for img in glob.glob("A:\python\inorganic_images\*.jpg"):
    n= cv2.imread(img)
    cv_img.append(n)

path = "A:\python\OUTPUT_IMAGES"
#cap = cv2.imread('F:\python\img_1.jpg')
#cap = cv2.imread('F:\python\inorganic_1.JPG')    
#cap = cv2.resize(cap, (475, 457)) 
image_template = cv2.imread('A:\python\inorganic_2.jpg', 0)
#image_template = cv2.resize(image_template, (24, 24)) 

#cap = cv2.resize(cap, None,fx=0.4, fy=0.5, interpolation = cv2.INTER_LINEAR)
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
i = 0

for cap in cv_img:
    matches = surf_detector(cap, image_template)
    cv2.putText(cap,str(matches),(450,450), cv2.FONT_HERSHEY_COMPLEX, 2,(0,0,0),1)
    
    # Our threshold to indicate object deteciton
    # We use 10 since the SIFT detector returns little false positves
    threshold = 15

# If matches exceed our threshold then object has been detected
    if matches > threshold:
        #cv2.rectangle(frame, (top_left_x,top_left_y), (bottom_right_x,bottom_right_y), (0,255,0), 3)
        cv2.putText(cap,'ino',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
    else:
        cv2.putText(cap,'o',(50,50), cv2.FONT_HERSHEY_COMPLEX, 2 ,(0,255,0), 2)
    i = 1 + i
    cv2.imwrite(os.path.join(path , 'op'+str(i)+'.jpg'), cap)
    
    
    
    
    #cv2.imshow('Object Detector using SIFT', cap)
if cv2.waitKey(1) == 13: #13 is the Enter Key
    cap.release()
    cv2.destroyAllWindows()
