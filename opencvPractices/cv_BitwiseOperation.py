import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# use plt to put img into axis


blank = np.zeros((400,400), dtype='uint8')
rec = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rec', rec)
cv.imshow('circle', circle)

# AND
# overlap area of 2 img
bitwise_and = cv.bitwise_and(rec, circle)
cv.imshow('bitwise AND', bitwise_and)

# OR
# all area 2 img occupied 
bitwise_or = cv.bitwise_or(rec,circle)
cv.imshow('bitwise OR', bitwise_or)

# XOR
# area occupied by only 1 img || non-intersecting area
bitwise_xor = cv.bitwise_xor(rec,circle)
cv.imshow('bitwise XOR', bitwise_xor)

# NOT
# invert img black --> white, and white --> black   
bitwise_not = cv.bitwise_not(rec)
cv.imshow('bitwise NOT', bitwise_not)




cv.waitKey(0)