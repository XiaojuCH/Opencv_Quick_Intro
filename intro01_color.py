# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/15 上午11:30

import cv2

image = cv2.imread("opencv_logo.jpg")

cv2.imshow("blue", image[:, :, 0])
cv2.imshow("green", image[:, :, 1])
cv2.imshow("red", image[:, :, 2])

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

cv2.waitKey(0)
