import cv2 as cv
import numpy as np

im = cv.imread('pepe.png')
img = cv.resize(im, (500,500), interpolation= cv.INTER_AREA)
cv.imshow('pepe', img)



# Translation (moving the img yields black backgroud)===================================================
def translate(img, x, y):
    # x ==> right
    # y ==> down
    transMat = np.float32([[1,0,x], [0,1,y]])
    print(transMat.shape)
    dimensions = (img.shape[1], img.shape[0])
    print(dimensions)
    return cv.warpAffine(img, transMat, dimensions)
    
translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# Translation============================================================================================



# Rotation===============================================================================================
def rotate(img, angle, rotPoint = None):
    (height, width)= img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2) 
    # rotating by the central points if no point passed in function call
    
    # angle is anti-clockwise
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

# Rotation===============================================================================================


# Flip
flip = cv.flip(img, -1)
# 0: vertical
# 1: horizontal
# -1: both vertical and horizontal
cv.imshow('flip', flip)


cv.waitKey(0)