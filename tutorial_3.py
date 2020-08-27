# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:40:45 2020

@author: TOMMY
"""


# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:52:51 2020

@author: TOMMY
"""


import cv2 as cv
import numpy as np

def access_pixels(image):#属性读取
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width : %s,height : %s,channels :%s"%(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row,col,c]
                image[row,col,c] = 255 - pv
    cv.imshow("pixel_demos",image)  

def  creat_image():
    """
    img = np.zeros([120,120,3],np.unit8)
   # img [:,:,0] = np.ones([120,120])*255
    img [:,:,2] = np.ones([120,120])*255#red channel
    cv.imshow("new image",img)
    """
    """
    img = np.zeros([120,120],np.unit8)
    img[:,:,0] = np.ones([120,120])*127 #全部变成0，再乘以127
    cv.imshow("new image", img)
    """
    ml = np.ones([3,3],np.unit8)
    ml .fill(1222.388)
    print(ml)
    
    
print("------------Hello Python------------")
src = cv.imread("D:/BIT_COURSE/OpenCV/1.jpg")
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)
t1 = cv.getTickCount()
creat_image()
access_pixels(src)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency();
print("time : %s ms"%(time*1000))
cv.waitKey(0)

cv.destroyAllWindows()