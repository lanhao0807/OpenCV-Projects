import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# use plt to put img into axis

im = cv.imread('pepe.png')
img = cv.resize(im, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('pepe', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobel X', sobelx)
cv.imshow('sobel Y', sobely)
cv.imshow('Combine Sobel', combine_sobel)

canny = cv.Canny(gray, 150,175)
cv.imshow('canny', canny)

cv.waitKey(0)