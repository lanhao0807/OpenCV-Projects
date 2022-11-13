import cv2 as cv
import numpy as np

im = cv.imread('pepe.png')
img = cv.resize(im, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('pepe', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gary', gray)

blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

canny = cv.Canny(blur, 125,175)
cv.imshow('canny', canny)

# thresh coverts img to binary form (black/white)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)

# contours 轮廓数量
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')


# draw contours in blank img
cv.drawContours(blank, contours, -1, (0,0,255), 1)
# cv.drawContours(surface, contours, -1 to draw all contours, color, thickness)
cv.imshow('Contours drawing', blank)









cv.waitKey(0)