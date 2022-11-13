# Nov 11. 2022
# CS 5420 project 6
# Hao Lan


import header as h
import cv2 as cv
import numpy as np
import filetype

def setup_img(input_img):
    # imread, resize, gray
    img = cv.imread(input_img)
    img = cv.resize(img, (640,640))
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img

def get_filter(img, num):
    img1 = img.copy()
    # original img with a filter of 0.75 applied on (gets darker)
    img1 = (img1.astype(np.float32)*num).astype(np.uint8)
    return img1

def combine_nodes(nodes,huff_tree):
    pos = 0
    newnode = []
    # get 2 lowest intensity frequencies
    if len(nodes)>1:
        nodes.sort()
        nodes[pos].append("0")
        nodes[pos+1].append("1")
        combined_freq = nodes[pos][0]+ nodes[pos+1][0]
        combined_inten = nodes[pos][1]+ nodes[pos+1][1]
        newnode.append(combined_freq)
        newnode.append(combined_inten)

        newnodes = []
        # add the combined node back to the lsit
        newnodes.append(newnode)
        
        # have the combined node in huff_tree
        huff_tree.append(newnode)
        
        # have the rest nodes added up with combined node and recursively call it
        newnodes.extend(nodes[2:])
        nodes = newnodes
        combine_nodes(nodes, huff_tree)
    return huff_tree

def make_huff_code(nodes):
    LUT = ['' for i in range(256)]
    nodes.sort()
    
    # Since root has no "1" or "0" attach, we start from "len(nodes) - 2"
    # every node in [intensity] increased by its tail of "1" or "0"
    for i in range(len(nodes)-2, -1, -1):
        for each_status in nodes[i][1]:
            try:
                LUT[each_status] += nodes[i][2]
            except IndexError:
                pass
    return LUT

def calculate_avg_bit(LUT, CNT):
    s = 0
    for i in range(len(CNT)):
        # intensity
        a = CNT[i][1][0]
        # frequency
        b = CNT[i][0]
        # huff_code length
        c = len(LUT[a])
        
        s += c*b
    return s/sum([CNT[i][0] for i in range(len(CNT))])
    



    

