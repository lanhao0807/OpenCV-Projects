import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# use plt to put img into axis

im = cv.imread('pepe.png')
img = cv.resize(im, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('pepe', img)

blank = np.zeros(img.shape[:2], dtype='uint8') 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Mask 
# mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1 )
# masked = cv.bitwise_and(img,img, mask = mask)
# cv.imshow('mask', masked)


# gray scale histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
print(gray_hist)
plt.xlim([0,256])
plt.show()

l = list()
for i in gray_hist:
	l.append(i[0])
print(l)

# color histogram
# plt.figure() 
# plt.title('color Histogram')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# color = ('b','g','r')
# for i,col in enumerate(color):
#     hist = cv.calcHist([img], [i], mask, [256], [0,256])
#     plt.plot(hist, color = col)
#     plt.xlim([0,256])

# plt.show()


cv.waitKey(0)