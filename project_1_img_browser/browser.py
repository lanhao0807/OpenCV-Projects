# September 04. 2022
# CS 5420 project 1
# Hao Lan
# ===================================================================================================================

import os
import cv2 as cv
import numpy as np
import filetype
import header
import argparse
 
parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('--row', type=int, nargs='?', help='Number of row of the image', default=512)
parser.add_argument('--col', type=int, nargs='?', help='Number of col of the image',default=512)
parser.add_argument('--input_dir', nargs='?', help='A path string of the input directory', default='.\dirA')

# image directory
dirA = parser.parse_args().input_dir

# store all iamge path
file_list = header.get_files(dirA)

# counter used to nevigate the images
cnt = 0

while True:
    # when cnt changes, img got overwritten by another path
    im = cv.imread(file_list[cnt])
    img= header.aspect_ratio_resize(im, parser.parse_args().col, parser.parse_args().row)
    cv.imshow('Image_browser_Hao_Lan', img)

    # metadata display
    print(f'{str(cnt): <5} {str(round(os.path.getsize(file_list[cnt])/1024)) : >5}KB {str(im.shape[1]): >10} X {str(im.shape[0])} {file_list[cnt] : >25}')

    key_pressed = cv.waitKey(0)
    if key_pressed == ord('n') or key_pressed == 32:
        cnt += 1
    elif key_pressed == ord('p'):
        cnt -= 1
    elif key_pressed == ord('q'):
        break
    
    if cnt < 0:
        cnt += 1
    elif cnt > len(file_list)-1:
        cnt -= 1