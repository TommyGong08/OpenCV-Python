# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:46:20 2020

@author: GONG HAILONG
"""


#Gaussian Blur
import cv2 as cv
import numpy as np

def clamp(pv):
    if pv > 255:
        return 255
    if pv <0:
        return 0
    else:
        return pv
    


def gaussian_noise(image):
    h ,w ,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            b = image[row,col,0]
            g = image[row,col,1]
            r = image[row,col,2]
            image[row,col,0] = clamp(b+s[0])
            image[row,col,1] = clamp(g+s[0])
            image[row,col,2] = clamp(r+s[0])
    cv.imshow("noise_image",image)


src = cv.imread("C:/Users/TOMMY/Desktop/1.JPG")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
t1 = cv.getTickCount()
gaussian_noise(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("time consume :%s ms"%(time*1000))

dst = cv.GaussianBlur(src, (0,0), 15)
cv.imshow("gaussian_blur",dst)
#cv.imshow("gaussian_noise",dst)

cv.waitKey(0)
cv.destroyAllWindows()