import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# use plt to put img into axis

im = cv.imread('pepe.png')
img = cv.resize(im, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('pepe', img)

blank = np.zeros(img.shape[:2], dtype='uint8') 
# dimension of the mask has to be the same size to the img otherwise it wont work

# Mask material
rec = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 75, img.shape[0]//2), 100, 255, -1)
mask1 = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
weird_shape = cv.bitwise_and(circle, rec)

# Apply Mask
masked = cv.bitwise_and(img, img, mask = weird_shape)
#                                 parameter here choose the mask shape from above
cv.imshow('mask img', masked)
                     



cv.waitKey(0)