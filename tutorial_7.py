# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:57:46 2020

@author: TOMMY
"""


import cv2 as cv
import numpy as np

#logic operation
def logic_demo(m1,m2):
    dst1 = cv.bitwise_and(m1,m2)
    dst2 = cv.bitwise_or(m1,m2)
    dst3 = cv.bitwise_not(m1)
    cv.imshow("logic_and",dst1)
    cv.imshow("logic_or",dst2)
    cv.imshow("logic_not",dst3)
    cv.imwrite("C:/Users/TOMMY/Desktop/2.JPG",dst3)

#adjust contrast&brightness
def constrast_brightness_demo(image,c,b):
    h, w ,ch = image.shape
    blank = np.zeros([h,w,ch],image.dtype)
    dst = cv.addWeighted(image,c, blank,1-c,b)
    cv.imshow("con-bri-demo",dst)

src1 = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
src2 = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
print(src1.shape)
print(src2.shape)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image1",src1)
cv.imshow("input image2",src2)

constrast_brightness_demo(src1, 1.2, 1)
logic_demo(src1,src2)
cv.waitKey(0)

cv.destroyAllWindows()