import cv2 as cv
import numpy as np
import filetype
import argparse


def add_proportional_noise(imgg, percent):
    cv.imshow('original', imgg)

    img = imgg.copy()
    print('pepper: ', np.count_nonzero(img == 0))
    print('salt: ', np.count_nonzero(img == 255))

    # Generate binary masks for salt and pepper noise
    # random gives a new vector with img.shape and random numbers
    # compare to a broadcast percentage, resulting a boolean matrix of mask
    # last, convert it to uint8 values
    salt_mask = (np.random.rand(*img.shape[:2]) < percent/2).astype(np.uint8) * 255
    pepper_mask = (np.random.rand(*img.shape[:2]) > percent/2).astype(np.uint8) * 255

    # add noise
    img = cv.bitwise_and(img, pepper_mask)
    img = cv.bitwise_or(img, salt_mask)

    print('======================= after adding noise ')
    print('pepper: ', np.count_nonzero(img == 0))
    print('salt: ', np.count_nonzero(img == 255))
    return img

def Euclidean(noisy_img, restored_img):
    noise = noisy_img.astype(np.float32)
    restore = restored_img.astype(np.float32)

    # calculate Euclidean distance manually
    sum = 0
    for i in range(noise.shape[0]):
        for j in range(noise.shape[1]):
            sum += (noise[i][j] - restore[i][j])**2
    Euclidean = np.sqrt(sum)
    Euclidean/= (noisy_img.shape[0] * noisy_img.shape[1])
    return Euclidean

# def cal_var(img):
#     mean = np.mean(img)
#     sum = 0
#     for i in range(img.shape[0]):
#         for j in range(img.shape[1]):
#             sum += (img[i][j] - mean)**2
#     var = sum / (img.shape[0] * img.shape[1])
#     return var

def adaptive_mean_filter(img, kernel):
    if kernel%2 is not 1:
        print('odd number for kernel size')
        return None 
    
    global_var = np.var(img)
    
    # padding
    img_padded = np.pad(img, ((kernel//2, kernel//2), (kernel//2, kernel//2)), 'constant')

    # Create an empty image
    img2 = np.zeros_like(img)

    for ii in range(img.shape[0]):
        i = ii + kernel//2
        for jj in range(img.shape[1]):
            j = jj + kernel//2
            local_var = np.var(img_padded[i-kernel//2:i+kernel//2, j-kernel//2:j+kernel//2])
            if local_var == 0:
                img2[ii][jj] = img_padded[i][j]
            else:
                global_over_local = global_var/local_var
                if global_over_local > 1: global_over_local = 1
                local_mean = np.mean(img_padded[i-kernel//2:i+kernel//2, j-kernel//2:j+kernel//2])
                img2[ii][jj] = img_padded[i][j] - (global_over_local)*(img_padded[i][j]-local_mean)

    return img2

def adaptive_median_filter(img, kernel, Smax):
    if Smax > min(*img.shape[:2]):
        print('Maximum kernel size too big!!!')
        return None
    if kernel%2 is not 1:
        print('odd number for kernel size')
        return None 
    
    # Pad the image with zeros
    img_padded = np.pad(img, ((Smax//2, Smax//2), (Smax//2, Smax//2)), 'constant')
    
    # Initialize the output image
    img2 = np.zeros_like(img)
    
    # Iterate over each pixel in the image
    for i in range(Smax//2, img.shape[0]+Smax//2):
        ii = i - Smax//2
        for j in range(Smax//2, img.shape[1]+Smax//2):
            # Start with window size 3x3
            jj = j - Smax//2
            kernel = 3
            
            while True:
                # Get the neighborhood
                mask = img_padded[i-kernel//2:i+kernel//2, j-kernel//2:j+kernel//2]
                
                # Calculate the median, minimum, and maximum of the neighborhood
                zmed = np.median(mask)
                zmin = np.min(mask)
                zmax = np.max(mask)
                
                # Calculate the values A1, A2, B1, and B2
                A1 = zmed - zmin
                A2 = zmed - zmax
                
                # Check if the pixel is an impulse noise
                if A1 > 0 and A2 < 0:
                    B1 = float(img_padded[i][j]) - zmin
                    B2 = float(img_padded[i][j]) - zmax
                    # Check if the pixel is non-impulse noise
                    if B1 > 0 and B2 < 0:
                        img2[ii][jj] = img_padded[i][j]
                    else:
                        img2[ii][jj] = zmed
                    break
                
                # Increase the window size if it is smaller than Smax
                if kernel < Smax:
                    kernel += 2
                else:
                    img2[ii][jj] = zmed
                    break
                    
    return img2


    