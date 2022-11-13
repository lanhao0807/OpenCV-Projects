# September 18. 2022
# CS 5420 project 4
# Hao Lan
# ===================================================================================================================

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def equalization(img):
    m,n, = img.shape[0], img.shape[1]
    img_size = m*n
    lookup_table, temp = {},0

    # 2d np.array that stores the frequency of each intensity
    gray_hist = cv.calcHist([img], [0], None, [256], [0,256])

    # showing the histogram
    x = [i for i in range(256)]
    y = [i[0] for i in gray_hist]
    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.bar(x,y)
    plt.xlim([0,256])
    plt.show()

    # normalized frequency of each intensity to proportions (add up to 1)
    normalized_gray_hist = [i/img_size for i in gray_hist]

    # build lookup table, each intensity is the sum of (all previous intensities' proportion) * 255
    for i in range(len(normalized_gray_hist)):
        temp += normalized_gray_hist[i][0]
        lookup_table[i] = round(temp*255)

    # new img created according to travling through the original img with lookup value
    new_gray = np.ndarray((m,n), dtype=img.dtype)
    for i in range(m):
        for j in range(n):
            try:
                new_gray[i][j] = lookup_table[img[i][j]] 
            except ValueError or IndexError:
                pass
    cv.imshow('new grayscale', new_gray)
    cv.waitKey()

def matching(src_image, ref_image):

    src_hist = np.histogram(src_image.flatten(), 256, [0,256])[0]
    ref_hist = np.histogram(ref_image.flatten(), 256, [0,256])[0]

    # showing the histogram comparation
    plt.figure()
    plt.title('Grayscale Histogram comparation')
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.plot(ref_hist, color = 'g')
    plt.legend(['ref_img'])
    plt.xlim([0,256])
    plt.show()

    plt.plot(src_hist, color = 'r')
    plt.legend(['src_img'])
    plt.xlim([0,256])
    plt.show()

    # Compute the normalized cdf for the source and reference image
    src_cdf = calculate_cdf(src_hist)
    ref_cdf = calculate_cdf(ref_hist)
    # Make a separate lookup table for each color
    lookup_table = calculate_lookup(src_cdf, ref_cdf)

    # Use the lookup function to transform the colors of the original
    after_transform = cv.LUT(src_image, lookup_table)

    image_after_matching = cv.convertScaleAbs(after_transform)
    cv.imshow('img after matching', image_after_matching)
    cv.waitKey()


def UseHisto(img, gray_hist):
    src_hist = np.histogram(img.flatten(), 256, [0,256])[0]
    
    # reading a string of data from a txt file and make it an 1D integer array
    with open(gray_hist) as a:
        gray_hist = a.read().split('\n')
        a.close()
    # detection for non int values
    for i in range(len(gray_hist)):
        if not gray_hist[i].isdigit():
            print('input histogram has non-int element')
            exit()
        gray_hist[i] = int(gray_hist[i])
    # detection for length of the hist
    if len(gray_hist) != 256:
        print('invalid length of the input histogram')
        exit()

    # showing the histogram comparation
    plt.figure()
    plt.title('Grayscale Histogram of reference img')
    plt.xlabel('bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_hist, color = 'g')
    plt.legend(['provided hist'])
    plt.xlim([0,256])
    plt.show()

    plt.plot(src_hist, color = 'r')
    plt.legend(['source img'])
    plt.xlim([0,256])
    plt.show()

    hist_cdf = calculate_cdf(np.array(gray_hist))
    img_cdf = calculate_cdf(src_hist)

    lookup_table = calculate_lookup(img_cdf, hist_cdf)

    # Use the lookup function to transform the colors of the original
    after_transform = cv.LUT(img, lookup_table)

    image_after_matching = cv.convertScaleAbs(after_transform)
    cv.imshow('img after matching', image_after_matching)
    cv.waitKey()


def calculate_lookup(src_cdf, ref_cdf):

    lookup_table = np.zeros(256)
    lookup_val = 0
    for i in range(len(src_cdf)):
        for j in range(len(ref_cdf)):
            if ref_cdf[j] >= src_cdf[i]:
                lookup_val = j
                break
        lookup_table[i] = lookup_val
    return lookup_table

def calculate_cdf(histogram):
    
    # Get the cumulative sum of the elements
    cdf = histogram.cumsum()
    # Normalize the cdf
    normalized_cdf = cdf / float(cdf.max())
    return normalized_cdf