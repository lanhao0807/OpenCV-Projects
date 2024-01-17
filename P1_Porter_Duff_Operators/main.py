import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import header as h

blank = np.zeros((480,640,3), np.uint8)

I1 = cv.circle(blank.copy(), (320,240), 150, (255,0,0), -1)
rec = cv.rectangle(blank.copy(), (62,192), (572,282), (0,0,255), -1)
I2 = cv.rectangle(rec, (256,46), (384,430), (0,0,255), -1)


M1 = cv.circle(blank.copy(), (320,240), 150, (255,255,255), -1)
rec1 = cv.rectangle(blank.copy(), (62,192), (572,282), (255,255,255), -1)
M2 = cv.rectangle(rec1, (256,46), (384,430), (255,255,255), -1)

# cv.imshow('cross', I2)
# cv.imshow('circle', I1)

# # clear
# cv.imshow('clear', blank)

# # copy I1
# cv.imshow('copy I1', I1.copy())

# # I1 over I2
# # (I1 ∧ M1) ∨ (I2 ∧ M2 ∧ ¬M1) 
# cv.imshow('I1 over I2', h.OR( h.AND(I1, M1), h.AND(h.AND(I2, M2), h.NOT(M1) )))

# # I1 in I2
# cv.imshow('I1 in I2', h.AND(I1, M2))
# cv.imshow('I2 in I1', h.AND(I2, M1))

# # I1 out I2
# cv.imshow('I1 out I2', h.AND(I1, h.NOT(M2)))
# cv.imshow('I2 out I1', h.AND(I2, h.NOT(M1)))

# # I1 atop I2
# # (I1 ∧ M1) ∨ (I2 ∧ ¬M2) 
cv.imshow('I1 atop I2', h.AND(h.OR(h.AND(I1, M1), h.AND(I2, h.NOT(M2))), M2))
cv.imshow('I2 atop I1', h.AND(h.OR(h.AND(I2, M2), h.AND(I1, h.NOT(M1))), M1))

# # I1 XOR I2
# cv.imshow('I1 XOR I2', h.OR(h.AND(I1, h.NOT(M2)), h.AND(I2, h.NOT(M1)) ))


cv.waitKey(0)