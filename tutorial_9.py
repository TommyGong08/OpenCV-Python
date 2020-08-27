# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:10:42 2020

@author: GONG HAILONG
"""


import cv2 as cv
import numpy as np


def blur_demo(image):
    dst = cv.blur(image, (10,10))
    cv.imshow("blur_demo",dst)
    
    
def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("madian_blur_demo",dst)
    
def custom_blur_demo(image):
    #kernel = np.ones([5,5],np.float32)/25
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], np.float32)
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("median_blue_demo",dst)
  

src = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
#blur_demo(src)
#median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()