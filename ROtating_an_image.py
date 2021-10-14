# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:15:37 2018

@author: HP
"""
import cv2
import numpy as np
img = cv2.imread('A:\python\images which are scaled\op2.jpg',0)
rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols,rows),90,1)
dst = cv2.warpAffine(img,M,(cols,rows),None)

cv2.imwrite('op.jpg',dst)