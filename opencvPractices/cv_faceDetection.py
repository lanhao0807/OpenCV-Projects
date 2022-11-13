import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
# use plt to put img into axis

img = cv.imread('C://Users/22428/Pictures/Saved Pictures/135.jpg')
cv.imshow('Lan', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gary', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
# the file haar_face.xml is used here to do the face detection

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 7)
# higher the minNeighbor value, more noise/faces will be ignored

print(f'Number of facec found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('detected faces', img)


cv.waitKey(0)