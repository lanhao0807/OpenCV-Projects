# September 18. 2022
# CS 5420 project 2
# Hao Lan
# ===================================================================================================================
# I think python doesn't usually use header file like the way c++ includes '.h' file. Anyway,
# I create this file to store functions as reusability required in project 1 description
# ===================================================================================================================

from random import sample
import shutil
import os
import cv2 as cv
import numpy as np

def method1(img,depth):

  for i in range(depth):
    # perform deletion (depth) times

    m,n,k = img.shape[0], img.shape[1],img.shape[2]
    # take off alternative rows and columns
    scaleDown = np.ndarray((m//2, n//2, k), dtype=img.dtype)
    for i in range(0, m, 2):
        for j in range(0, n, 2):
            try:
                scaleDown[i//2][j//2] = img[i][j]
            except IndexError:
                print("problem while scale down")
                pass
    img = scaleDown.copy()
  cv.imshow(f"down by {depth} level", img)
  for i in range(depth):
    # replicates the pixel (depth) times

    m,n,k = img.shape[0]*2, img.shape[1]*2,img.shape[2]

    # new size for upsampling
    scaleUp = np.ndarray((m,n,k), dtype=img.dtype)
    for i in range(0, m-1, 2):
        for j in range(0, n-1, 2):
            scaleUp[i, j] = img[i//2][j//2]
    # Replicating rows
    for i in range(1, m-1, 2):
        for j in range(0, n-1):
            scaleUp[i:i+1, j] = scaleUp[i-1, j]
    # Replicating columns
    for i in range(0, m-1):
        for j in range(1, n-1, 2):
            scaleUp[i, j:j+1] = scaleUp[i, j-1]
    img = scaleUp.copy()

  cv.imshow(f'Up by {depth} level from down img', scaleUp)
  cv.waitKey()

def method2(img, depth):
  img= img.astype("uint16")

  for i in range(depth):
    # perform averaging (depth) times

    m,n,k = img.shape[0]//2, img.shape[1]//2,img.shape[2]
    
    # calculate avergae of 4 pixels assign to the first pixel
    scaleDown = np.ndarray((m, n, k), dtype=img.dtype)
    for i in range(m):
        for j in range(n):
            try:
                scaleDown[i][j] = ((img[2*i][2*j]+ img[2*i+1][2*j]+ img[2*i][2*j+1]+img[2*i+1][2*j+1])//4)
            except IndexError:
                print("problem while scale down")
                pass
    img = scaleDown.copy()
  
  for i in range(depth):
    # replicates the pixel (depth) times

    m,n,k = img.shape[0]*2, img.shape[1]*2,img.shape[2]
    # new size for upsampling
    scaleUp = np.ndarray((m,n,k), dtype=img.dtype)
    for i in range(0, m+1, 2):
        for j in range(0, n+1, 2):
          try:
            scaleUp[i, j] = img[i//2][j//2]
            scaleUp[i+1, j] = (img[i//2+1][j//2] + img[i//2][j//2])//2
            scaleUp[i, j+1] = (img[i//2][j//2+1] + img[i//2][j//2])//2
            scaleUp[i+1, j+1] = (img[i//2][j//2]+ img[i//2+1][j//2]+img[i//2][j//2+1]+ img[i//2+1][j//2+1])//4
          except IndexError:
            pass
    img = scaleUp.copy()
  img= img.astype("uint8")
  cv.imshow('Up', img)
  cv.waitKey()

def intensity(img, intensity):
  m,n,k = img.shape[0], img.shape[1], img.shape[2]
  sample = np.ndarray((m,n,k), dtype=img.dtype)
  print(type(img[0][0]), type(sample[0][0]))
  for i in range(m):
    for j in range(n):
      if type(img[i][j]) == np.int8:
        sample[i][j] = (img[i][j]>>intensity)<<intensity
      elif type(img[i][j]) == np.ndarray:
        for z in range(3):
          sample[i][j][z] = (img[i][j][z]>>intensity)<<intensity
  cv.imshow(f'intensity level {intensity} bits', sample)
  cv.waitKey()