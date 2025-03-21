# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/3/15 下午11:54

import cv2
import numpy as np

image = cv2.imread("poker.jpg")
# 将彩色图转为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = gray[75:105, 235:265]

match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
locations = np.where(match >= 0.9)

h, w = template.shape[0:2]
for p in zip(*locations[::-1]):
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, p[1] + h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow("image", image)
cv2.waitKey(0)
