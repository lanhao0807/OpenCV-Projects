# September 18. 2022
# CS 5420 project 2
# Hao Lan
# ===================================================================================================================
import cv2 as cv
import numpy as np
import filetype
import header
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
    print(intensity)
    exit()
depth = parser.parse_args().d
if depth <= 0:
    print("Invalid depth, see -h")
    print(depth)
    exit()
method = parser.parse_args().s
if method not in [1,2]:
    print("Invalid method, see -h")
    print(method)
    exit()


img = cv.imread(input_img)
cv.imshow("img",img)

m,n,k = img.shape[0], img.shape[1],img.shape[2]
scaleDown = np.zeros((m//depth, n//depth, k), dtype=np.int8)
for i in range(0, m, depth):
    for j in range(0, n, depth):
        try:
            scaleDown[i//depth][j//depth] = img[i][j]   
        except IndexError:
            print("problem while scale down")
            pass  
# new size
scaleUp = np.zeros((m, n, k), dtype=np.int8)
for i in range(0, m-1, depth):
    for j in range(0, n-1, depth):
        scaleUp[i, j] = scaleDown[i//depth][j//depth]
# Replicating rows
for i in range(1, m-(depth-1), depth):
    for j in range(0, n-(depth-1)):
        scaleUp[i:i+(depth-1), j] = scaleUp[i-1, j]
# Replicating columns
for i in range(0, m-1):
    for j in range(1, n-1, depth):
        scaleUp[i, j:j+(depth-1)] = scaleUp[i, j-1]

cv.imshow('Up', scaleUp)
cv.waitKey()