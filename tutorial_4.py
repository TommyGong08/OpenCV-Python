 #-*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:51:13 2020

@author: TOMMY
"""

import cv2 as cv

#color space translate
def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    Ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCrCb)
    cv.imshow("Ycrcb",Ycrcb)

src = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
color_space_demo(src)
cv.waitKey(0)

cv.destroyAllWindows()