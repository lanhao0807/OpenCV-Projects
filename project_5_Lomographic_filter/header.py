# Oct 04. 2022
# CS 5420 project 5
# Hao Lan

import os
import cv2 as cv
import numpy as np
import filetype
import argparse
from math import e, sqrt


def Task_1_LUT(s):
    # using formula provided
    if s==0:
        print('division by Zero')
        return
    else:
        LUT = np.zeros((256,), np.uint8)
        for i in range(256):
            LUT[i] = 256/(1+e**-((i/256-0.5)/s))
    return LUT

def distance(pixel, center):
    dist = sqrt((center[0]-pixel[0])**2 + (center[1]-pixel[1])**2)
    return dist


