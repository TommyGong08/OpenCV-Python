 #-*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:19:12 2020

@author: TOMMY
"""

import cv2 as cv

def add_demo(m1,m2):
    dst = cv.add(m1,m2)
    cv.imshow("add_demo",dst)

def subtract_demo(m1,m2):
    dst = cv.subtract(m1,m2)
    cv.imshow("subtract_demo",dst)
    
def divide_demo(m1,m2):
    dst = cv.divide(m1,m2)
    cv.imshow("divide_demo",dst)
    
def multiply_demo(m1,m2):
    dst = cv.multiply(m1,m2)
    cv.imshow("multiply_demo",dst)
    
def others(m1,m2):
    mean1 = cv.mean(m1)
    mean2 = cv.mean(m2)
    print(mean1)
    print(mean2)
    
    

src1 = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
src2 = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
print(src1.shape)
print(src2.shape)
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image1",src1)
cv.imshow("input image2",src2)

#add_demo(src1,src2)
#subtract_demo(src1,src2)
#divide_demo(src1,src2)
multiply_demo(src1,src2)
others(src1,src2)
cv.waitKey(0)

cv.destroyAllWindows()