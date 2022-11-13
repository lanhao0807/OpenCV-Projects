import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# use plt to put img into axis

im = cv.imread('pepe.png')
img = cv.resize(im, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('pepe', img)

# Smooth img // Reduce noise ==================================================================

# averaging
# tweak surrounding pixel when center changes, average the intensity of the entire window
average = cv.blur(img, (7,7))
cv.imshow('aver blur', average)

# Guassian blur
# more nature than averaging, use the average weight of each pixel in the window
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("guass", gauss)

# median blur
# like averaging, but it finds the median of surrounding pixel
median = cv.medianBlur(img, 7)
cv.imshow('median', median)

# Bilateral blur
# many case most effective
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)