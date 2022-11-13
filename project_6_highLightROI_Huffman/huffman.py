# Nov 11. 2022
# CS 5420 project 6
# Hao Lan

import header as h
import cv2 as cv
import numpy as np
import filetype
import argparse

 
parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('-img', nargs='?', help='A path of the input img')

# input img is required and only img, otherwise, quit
input_img = parser.parse_args().img
if not filetype.is_image(input_img) or input_img is None:
    print("Invalid image file")
    exit()

#=============================================================================================================================
#=============================================================================================================================
#=============================================================================================================================

def main():
    img = h.setup_img(input_img)

    # count frequency of each intensity
    unique, counts = np.unique(img, return_counts=True)

    # [ [frequency, intensity] ... ]  pairs 2D list
    CNT = [[counts[i],[unique[i]]] for i in range(len(unique))]

    # sort from lowest frequency to highest
    CNT.sort()
    huff_tree = []

    # huff_tree for all cases combined
    huff_tree = h.combine_nodes(CNT, huff_tree)

    # Since huff_tree only have combined nodes, I added CNT back in
    # note: at this time every base node has its tail "1" or "0" already
    huff_tree += CNT
    huff_tree.sort()
  
    LUT = h.make_huff_code(huff_tree)
    for i in range(len(LUT)):
        print(f'{i}', LUT[i])
    print('\nmax code length:', max([len(i) for i in LUT]))
    print('min code length:', min([len(i) for i in LUT]))

    avg = h.calculate_avg_bit(LUT, CNT)
    print('average bit: ', avg)
    print('Compression ratio: ', 8/avg)
    print('relative redundancy: ', 1-1/(8/avg))


if __name__ == "__main__":
    main()