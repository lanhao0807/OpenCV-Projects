import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# AND
# overlap area of 2 img
def AND(a,b):
    bitwise_and = cv.bitwise_and(a, b)
    return bitwise_and

# OR
# all area 2 img occupied 
def OR(a,b):
    bitwise_or = cv.bitwise_or(a,b)
    return bitwise_or

# XOR
# area occupied by only 1 img || non-intersecting area
def XOR(a,b):
    bitwise_xor = cv.bitwise_xor(a,b)
    return bitwise_xor

# NOT
# invert img black --> white, and white --> black   
def NOT(a):
    bitwise_not = cv.bitwise_not(a)
    return bitwise_not