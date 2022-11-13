import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# use plt to put img into axis

im = cv.imread('pepe.png')
img = cv.resize(im, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('pepe', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# blank = np.zeros(img.shape[:2], dtype='uint8') 

# Simple thresholding======================================================================
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# pixel intensity greater than 150 will be set to 255, less then 150 will be set to 0
cv.imshow('simple Threshold', thresh)
# =========================================================================================


# Adaptive Thresholding====================================================================
# instead of setting thresh by hand, let computer to find suitable thresh
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 9)
cv.imshow('adaptive thresh', adaptive_thresh)
#==========================================================================================



cv.waitKey(0)