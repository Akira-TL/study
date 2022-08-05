# -*- encoding: utf-8 -*-
import cv2 as cv
a = cv.imread('xinhai.jpg') # opencv不支持中文路径
cv.imshow("Display window", a)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("starry_night.png", a)