# Oct 04. 2022
# CS 5420 project 5
# Hao Lan

import os

from cv2 import blur
import header as h
import cv2 as cv
import numpy as np
import filetype
import argparse
from math import e
 
parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('-img', nargs='?', help='A path of the input img')

# input img is required and only img, otherwise, quit
input_img = parser.parse_args().img
if not filetype.is_image(input_img) or input_img is None:
    print("Invalid image file")
    exit()

img = cv.imread(input_img)
img = cv.resize(img, (600,600))
img_copy1 = img.copy()
img_copy2 = img.copy()

cv.namedWindow('image')

m,n = img.shape[:2]
maxRadius = min(m,n)//2
center = (m//2 , n//2)

def callback1(s):
    global img, img_copy1,img_copy2
    if s<8:
        print("S shouldn't be less than 8!!!")
        s = 8
        cv.setTrackbarPos('s', 'image', 8)
    # making s to reasonable range 0.08 - 0.2
    s /= 100
    # call back function
    # split the color img
    b,g,r = cv.split(img_copy1)

    # LUT
    LUT = h.Task_1_LUT(s)

    # change red channel using LUT
    for i in range(len(r)):
        for j in range(len(r[0])):
            r[i][j] = LUT[r[i][j]]

    # merge 3 channels back to 1 and return it
    img_copy1 = cv.merge([b,g,r])

    img_copy2 = img_copy1.copy()


def callback2(percentage):
    global img, maxRadius, img_copy1, img_copy2

    # calculate Radius
    maxRadius_copy = maxRadius
    maxRadius_copy = maxRadius_copy - (percentage/100)*maxRadius_copy

    # since I'm using Gaussian blur, the r has to be odd number
    if (maxRadius//2) %2 == 1:
        r= maxRadius//2
    else:
        r = (maxRadius//2)+1

    img_copy2 = img_copy1.copy()

    # setting the pixel in the cirle to 1
    dst = np.ndarray(img.shape, np.float32)
    dst = np.full_like(dst, 0.75)
    for i in range(m):
        for j in range(n):
            if h.distance((i,j), center) < maxRadius_copy:
                dst[i, j , :] = 1

    # blurring the halo filter using dynamic radius
    blur = cv.GaussianBlur(dst,(r,r),0)

    img_copy2 = img_copy2.astype(np.float32)
    img_copy2 *= blur 
    img_copy2 = img_copy2.astype(np.uint8)

                
cv.createTrackbar('s', 'image', 10, 20, callback1)
cv.createTrackbar('halo', 'image', 100, 100, callback2)

while(True):
    cv.imshow('image', img_copy2)

    key_pressed = cv.waitKey(1)
    if key_pressed == ord('s'):
        cv.imwrite('savedImg.jpg', img_copy2)
        break
    elif key_pressed == ord('q'):
        break

cv.destroyAllWindows()
