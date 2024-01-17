import cv2 as cv
import numpy as np


def K_means(img):
    # Flatten image into 2D array
    pixel_vals = img.reshape((-1, 3)).astype(np.float32)

    # Apply k-means clustering
    k = 100
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    attempts = 10
    ret, labels, centers = cv.kmeans(pixel_vals, k, None, criteria, attempts, cv.KMEANS_RANDOM_CENTERS)
    
    # convert it back to uint8
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    segmented_img = res.reshape((img.shape))

    return segmented_img

