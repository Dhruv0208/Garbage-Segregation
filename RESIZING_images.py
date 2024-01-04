# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:15:37 2018

@author: dhruv
"""
import cv2
import glob
import random
import os
i = 0l
cv_img = []
cv_img_2 = []
for img in glob.glob("A:\python\inorganic_images\*.jpg"):
    n= cv2.imread(img)
    cv_img.append(img)
    cv_img_2.append(n)

#for x in range(10):
  #print random.randint(90,350)
path = 'A:\python\scaled_images'
for img in cv_img_2:
     
    n = random.randint(1,2)
    m = random.randint(1,2)
    rows,cols = img.shape[:2]
    
    i = i+1
    dst = cv2.resize(img, (0,0), fx=n, fy=m) 
    cv2.imwrite(os.path.join(path , 'op'+str(i)+'.jpg'), dst)
