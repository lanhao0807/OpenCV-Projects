# September 18. 2022
# CS 5420 project 2
# Hao Lan
# ===================================================================================================================
# I think python doesn't usually use header file like the way c++ includes '.h' file. Anyway,
# I create this file to store functions as reusability required in project 1 description
# ===================================================================================================================

import shutil
import os
import cv2 as cv
import numpy as np
import filetype

# traverse the input dir to get path of every img type file
def get_files(dirA):
  file_list = []
  for dirpath, dirnames, filenames in os.walk(dirA):
    for filename in filenames:
      if filetype.is_image(os.path.join(dirpath, filename)):
        file_list.append(os.path.join(dirpath, filename))
      else:
        # if a file is not a valid image, it will be printed on the terminal and will not be added
        print(f'{dirpath : <15} file: {filename} is not an image')
  return file_list

def aspect_ratio_resize(img, width, height):
  aspect = img.shape[1]/img.shape[0] # width / height
  if width/height < aspect:
    height = width / aspect
  else:
    width = height * aspect
  a = cv.resize(img, (int(width), int(height)), interpolation = cv.INTER_AREA)
  return a

# ignore all the file in the dir and its sub-dir
def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]

# duplicate the source dir hieriachy in the new dir with only dirs, no files
def copy_tree(src, dst):
    shutil.copytree(src, dst, ignore=ignore_files)