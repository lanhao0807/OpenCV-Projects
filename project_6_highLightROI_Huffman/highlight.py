# Nov 11. 2022
# CS 5420 project 6
# Hao Lan

import header as h
import cv2 as cv
import numpy as np
import filetype
import argparse
 
parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('-img', nargs='?', help='A path of the input img')

# input img is required and only img, otherwise, quit
input_img = parser.parse_args().img
if not filetype.is_image(input_img) or input_img is None:
    print("Invalid image file")
    exit()

#=============================================================================================================================
#=============================================================================================================================
#=============================================================================================================================

def main():
    # setups for original img
    img = h.setup_img(input_img)

    # get filter of 0.75 for entire img
    img1 = h.get_filter(img, 0.75)

    # Select ROI (imshow)
    r = cv.selectROI("image", img, showCrosshair= False)
    cv.imshow('image', r)

    # Crop image
    ROI = img[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    if len(ROI):
        cv.imshow("ROI", ROI)

    # OpenCV predefined hist equalization method as instruction required
    equ = cv.equalizeHist(ROI)
    img1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])] = equ
    img = img1
    cv.imshow("image", img)

    cv.waitKey()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()