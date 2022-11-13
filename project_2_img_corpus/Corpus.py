# September 18. 2022
# CS 5420 project 2
# Hao Lan
# ===================================================================================================================

from genericpath import exists
from importlib.metadata import metadata
import os
import shutil
import cv2 as cv
import numpy as np
import filetype
import header
import argparse

 
parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('-t', '-type', type= str, nargs='?', help='(str) Edit image type, such as [.jpg] [.png] etc..')
parser.add_argument('-r', '-row', type=int, nargs='?', help='(int) Number of row (pixel) of the image [height]', default=512)
parser.add_argument('-c', '-col', type=int, nargs='?', help='(int) Number of col (pixel) of the image [width]',default=512)
parser.add_argument('-g', '-gray', help='(X) Save img as gray scale', action='store_true')
parser.add_argument('-a', '-aspect', help='(X) Save img by original image aspect ratio', action='store_true')
parser.add_argument('-indir', nargs='?', help='(str) A path of the input directory (default= ./Corpus)', default='.\Corpus')
parser.add_argument('-outdir', nargs='?', help='(str) A path of the output directory (default= ./Corpus_output)', default='./Corpus_output')


# image directory
input_dir = parser.parse_args().indir
# store all iamge path
indir_list = header.get_files(input_dir)


# create output dir
output_dir = parser.parse_args().outdir
try:
    header.copy_tree(input_dir, output_dir)
except FileExistsError:
    print("Directory ", output_dir,  " already exists")


# create a list of file in indir
# replace dir name to outdir for later imwrite operation
outdir_lis = indir_list.copy()
outdir_list = []
for i in outdir_lis:
    temp = i.split('\\')
    temp[0] = parser.parse_args().outdir
    if parser.parse_args().t:
        temp[-1] = temp[-1].split('.')[0] + parser.parse_args().t
    outdir_list.append('/'.join(temp))

for i in range(len(indir_list)):

    im = cv.imread(indir_list[i])
    if parser.parse_args().a:
        # if true, apply aspect ratio
        img= header.aspect_ratio_resize(im, parser.parse_args().c, parser.parse_args().r)
    else:
        # if False, simply resize the img
        img= cv.resize(im, (parser.parse_args().c, parser.parse_args().r), interpolation = cv.INTER_AREA)

    if parser.parse_args().g:
        # if true, convert img to gray scale
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    # copy the image source of each section to output directory
    if i == 0:
        shutil.copyfile(os.path.join(input_dir, 'metadata.txt'), os.path.join(output_dir, 'metadata.txt'))

    # creating metadata inside of output directory
    f = open(os.path.join(output_dir, 'metadata.txt'), 'a')
    f.write(f'{str(i): <5} {str(round(os.path.getsize(indir_list[i])/1024)) : >5}KB {str(im.shape[1]): >10} X {str(im.shape[0]): <10} {indir_list[i] : <25}')
    f.write('\n')
    
    w = cv.imwrite(outdir_list[i], img)
