# September 18. 2022
# CS 5420 project 3
# Hao Lan
# ===================================================================================================================
import cv2 as cv
import numpy as np
import filetype
import header as h
import argparse
import matplotlib.pyplot as plt

# parsers
parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('-img', nargs='?', help='(str) A path of the input image (no default file)')
parser.add_argument('-rimg', nargs='?', help='(str) A path of the reference image (no default file)')
parser.add_argument('-hist', nargs='?', help='(str) A path of the input histogram (no default file)')
parser.add_argument('-m', type=int, nargs='?', help='(int) 1: equalization 2: matching 3: Use histogram (no default)')

def main():
    input_img = parser.parse_args().img
    if not filetype.is_image(input_img):
        print("Not a valid image file")
        exit()
        
    if not parser.parse_args().m:
        print('Method required see -h')
        exit()
    else:
        method = parser.parse_args().m

    if method not in [1,2,3]:
        print("Invalid method, see -h")
        exit()

    if method == 1:
        if parser.parse_args().rimg:
            print(parser.parse_args().rimg, ' is not needed for method 1')
        if parser.parse_args().hist:
            print(parser.parse_args().hist, ' is not needed for method 1')

    if method ==2:
        if not parser.parse_args().rimg:
            print("No reference img provided, see -h")
            exit()
        m2_img = parser.parse_args().rimg
        if parser.parse_args().hist:
            print(parser.parse_args().hist, ' is not needed for method 2')

    if method ==3:
        if not parser.parse_args().hist:
            print("No histogram data provided, see -h")
            exit()
        hist = parser.parse_args().hist
        if parser.parse_args().rimg:
            print(parser.parse_args().rimg, ' is not needed for method 3')


    gray_img = cv.imread(input_img, cv.IMREAD_GRAYSCALE)
    # In case convert img to grayscale since we are working on grayscale img
    cv.imshow('gray',gray_img)


    if method == 1:
        h.equalization(gray_img)
    elif method == 2:
        gray_rimg = cv.imread(m2_img, cv.IMREAD_GRAYSCALE)
        cv.imshow("gray reference img", gray_rimg)
        h.matching(gray_img, gray_rimg)
    elif method == 3:
        h.UseHisto(gray_img, hist)

    cv.waitKey()

if __name__ == '__main__':
    main()