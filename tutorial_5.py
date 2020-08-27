# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 22:52:00 2020

@author: GONG HAILONG
"""

import cv2 as cv
import numpy as np


def extrace_object_demo():
    capture = cv.VideoCapture("C:/Users/TOMMY/Desktop/XXXX")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break;
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37,43,46])
        upper_hsv = np.array([77,255,255])
        mask = cv.inRange(hsv, lowerb=lower_hsv,upperb=ipper_hsv)
        cv.imshow("video",frame)
        cv.imshow("mask",mask)
        c = cv.waitkey(40)
        if c == 27:
            break
        
print("-----Hello Python-----")
src = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
b, g, r = cv.split(src)
cv.imshow("blue",b)
cv.imshow("red",r)
cv.imshow("green",g)

src = cv.merge([b,g,r])
src[:,:,2] = 0
cv.imshow("change image",src)


#extrace_object_demo()
cv.waitKey(0)

cv.destroyAllWindows()