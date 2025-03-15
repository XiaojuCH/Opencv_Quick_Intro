# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/15 上午11:24

import cv2

print(cv2.__version__)

image = cv2.imread("opencv_logo.jpg")
print(image.shape)

cv2.imshow("image", image)
cv2.waitKey(0)
