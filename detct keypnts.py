# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 17:51:47 2018

@author: dhruv
"""

import cv2
import numpy as np
image = cv2.imread("C:/Users/dhruv/Desktop/research/inorganic_images(based on position)/img_16.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
surf = cv2.SURF()
surf.hessianThreshold = 4000
keypoints, descriptors = surf.detectAndCompute(gray, None)
print"Number of keypoints detected:", len(keypoints)
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imwrite("C:/Users/dhruv/Desktop/research/scaled_images2/Image1.jpg", image)
cv2.imshow("Image",image)
cv2.waitKey()
cv2.destroyAllWindows
#C:\Users\dhruv\Desktop\research
#imwrite( "../../images/Gray_Image.jpg", gray_image )