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
parser.add_argument('-input', nargs='?', help='(str) A path of the input image (no default file)')
parser.add_argument('-i', '-intensity', type=int, nargs='?', help='(int) Intensity level 1 - 7', default=1)
parser.add_argument('-d', '-depth', type=int, nargs='?', help='(int) Number of levels for downsampling (default = 1)',default=1)
parser.add_argument('-s', '-sampling_method', type=int, nargs='?', help='(int) 1 (default) for pixel deletion/replication, 2 for pixel averaging/interpolation', default=1)

# parser validations
input_img = parser.parse_args().input
if not filetype.is_image(input_img):
    print("Not a valid image file")
    exit()
intensity = parser.parse_args().i
if intensity not in [1,2,3,4,5,6,7]:
    print("Invalid intensity, see -h")
    exit()
depth = parser.parse_args().d
if depth <= 0:
    print("Invalid depth, see -h")
    exit()
method = parser.parse_args().s
if method not in [1,2]:
    print("Invalid method, see -h")
    exit()


img = cv.imread(input_img)

if method == 1:
    h.method1(img, depth)
elif method == 2:
    h.method2(img, depth)

print(type(img[0][0]))
h.intensity(img, intensity)
