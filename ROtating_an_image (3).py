# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:15:37 2018

@author: dhruv
"""
#import cv2
#img = cv2.imread('F:\python\IMG_1.jpg')
#rows,cols = img.shape[:2]
#
#
#M = cv2.getRotationMatrix2D((cols,rows),90,1)
#dst = cv2.warpAffine(img,M,(cols,rows))
#cv2.imwrite('op.jpg',dst)

import cv2
import glob
import random
import os
i = 1
cv_img = []
cv_img_2 = []
for img in glob.glob("F:\python\Images_organic\*.jpg"):
    n= cv2.imread(img)
    cv_img.append(img)
    cv_img_2.append(n)

#for x in range(10):
  #print random.randint(90,350)
path = 'F:\python\OUTPUT_IMAGES'
for img in cv_img_2:
     
    n = random.randint(90,300)
    num_rows, num_cols = img.shape[:2]
    
    i = i+1
    rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), n, 1)
    dst = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
    cv2.imwrite(os.path.join(path , 'op'+str(i)+'.jpg'), dst)

#import cv2
#import numpy as np
#
#img = cv2.imread('F:\python\IMG_1.jpg')
#num_rows, num_cols = img.shape[:2]
#
#rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 1)
#dst = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
##cv2.imshow('Rotation', img_rotation)
##cv2.waitKey()
#cv2.imwrite('op.jpg',dst)
