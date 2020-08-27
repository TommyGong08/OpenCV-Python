# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:22:44 2020

@author: TOMMY
"""


import cv2 as cv
import numpy as np

#ROI Region Of Interst

def fill_color_demo(image):
    copyImg = image.copy()
    h , w = image.shape[:2]
    mask = np.zeros([h+2 , w+2] , np.uint8)
    cv.floodFill(copyImg , mask,(10,10),(150,0,150),(10,10,10),(20,20,20),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo",copyImg)
 
"""  
def fill_binary():
    image = np.zeros([120,120,3],np.uint8)
    image[24:80,13:90,:] = 255
    cv.imshow("fill_binary",image)
    
    mask = np.ones([122,122,1],np.uint8)
    mask =[25:81,14:94] = 0
    cv.floodFill(image, mask, (10,10), (100,2,255),cv.FLOODFILL_MASK_ONLY)
    cv.imshow("filled binary",image)
    """
    
src = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

fill_color_demo(src)
#fill_binary()

face = src[24:80 , 13:93]
gray = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
src[ 24:80 , 13:93 ] = backface
cv.imshow("face",src)

cv.waitKey(0)

cv.destroyAllWindows()