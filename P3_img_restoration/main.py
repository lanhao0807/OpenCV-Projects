import cv2 as cv
import numpy as np
import filetype
import argparse
import header as h

parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('-img', nargs='?', help='A path of the input img')
parser.add_argument('-out', nargs='?', help='A path of the output img', default= 'output.jpg')
parser.add_argument('-m', '-method', type=int, nargs='?', help='1 (default) for adaptive mean filter, 2 for adaptive median filter', default=1)


# input img is required and only img, otherwise, quit
input_img = parser.parse_args().img
if not filetype.is_image(input_img) or input_img is None:
    print("Invalid image file")
    exit()
option = parser.parse_args().m
if option not in [1,2]:
    print("Invalid method")
    exit()
# ===================================================================================================================

img  = cv.imread(input_img, cv.IMREAD_GRAYSCALE)
print('img shape: ', img.shape, 'total pixels: ', img.shape[0]*img.shape[1])


noisy_img = h.add_proportional_noise(img, 0.1)
cv.imshow("noisy image", noisy_img)

if option == 1:
    mean_img = h.adaptive_mean_filter(noisy_img, 3)
    cv.imshow('ad-mean-flt', mean_img)
    print('Euclidean distance between Adpt Mean filter and Original image is:\n', h.Euclidean(img, mean_img))

else:
    median_img = h.adaptive_median_filter(img, 3, 7)
    cv.imshow('ad-median-flt', median_img)
    print('Euclidean distance between Adpt Median filter and Original image is:\n', h.Euclidean(img, median_img))


cv.waitKey()