import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# use plt to put img into axis

im = cv.imread('pepe.png')
img = cv.resize(im, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('pepe', img)

# note:
#     BGR can convert to these form and they can 
#     convert back to BGR, but gray can't be transformed
#     to HSV or other directly, to do it, we have to 
#     transfer it to BGR then BGR to whatever we want

# BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
cv.imwrite('C://Users/22428/Desktop/CS5420/project_1_img_browser/dirA/pepe_gray.png',gray)


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)


plt.imshow(rgb)
plt.show()

# color channel===================================================================================
b,g,r = cv.split(img) 
# split blue green red color from original color

# simply use b,g,r will yield gray scale img, to solve this
# use a blank to merge each color
blank = np.zeros(img.shape[:2], dtype= 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

# cv.imshow('blue', b) is gray scaled img
cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('merged', merged)





cv.waitKey(0)
