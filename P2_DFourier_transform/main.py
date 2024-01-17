import cv2 as cv
import numpy as np
import filetype
import argparse

parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('-img', nargs='?', help='A path of the input img')
parser.add_argument('-out', nargs='?', help='A path of the output img', default= 'output.jpg')

# input img is required and only img, otherwise, quit
input_img = parser.parse_args().img
if not filetype.is_image(input_img) or input_img is None:
    print("Invalid image file")
    exit()
# ===================================================================================================================

img  = cv.imread(input_img, cv.IMREAD_GRAYSCALE)
print('img shape: ', img.shape)
# cv.imshow('img', img)

# get optimal size, center of the padded imgw
rows, cols = img.shape
optimal_rows = cv.getOptimalDFTSize(rows)
optimal_cols = cv.getOptimalDFTSize(cols)
print('optimal shape: ', (optimal_rows, optimal_cols))

# padded img with value of 0s
padded_img = cv.copyMakeBorder(img, 0, optimal_rows - rows, 0, optimal_cols - cols, cv.BORDER_CONSTANT, value=0)

# real and imaginary part
real = np.zeros(padded_img.shape, dtype=np.float32)
imag = np.zeros(padded_img.shape, dtype=np.float32)
real[:, :] = padded_img

# merge the real and imaginary planes into a complex image
complex_img = cv.merge([real, imag])

DFT = cv.dft(complex_img, flags=cv.DFT_COMPLEX_OUTPUT)

# get the center of dft img
crow, ccol = DFT.shape[:2]
crow //= 2
ccol //= 2
center = (ccol, crow)

# swap quadrants along the diagonals
DFT2 = np.vstack((np.hstack((DFT[crow:, ccol:], DFT[crow:, :ccol])),
                       np.hstack((DFT[:crow, ccol:], DFT[:crow, :ccol]))))

real_part, imaginary_part = cv.split(DFT2)

# Compute the magnitude of the image
magnitude = 20* np.log(cv.magnitude(real_part, imaginary_part))

# Normalize the magnitude image
cv.normalize(magnitude, magnitude, 0, 1, cv.NORM_MINMAX)

# Convert the normalized magnitude image to uint8 and print
magnitude = (255*magnitude).astype(np.uint8)
cv.imshow('magnitude', magnitude)

# using ROI to make mask
ROI = cv.selectROI('magnitude', magnitude, fromCenter=False, showCrosshair=False)
x,y,w,h = ROI
top_left = (x,y)
bot_right = (x+w, y+h)

inner_radius = min(cv.norm(np.array(center), np.array(bot_right) , cv.NORM_L2), 
    cv.norm(np.array(center), np.array(top_left) , cv.NORM_L2))

outer_radius = max(cv.norm(np.array(center), np.array(bot_right) , cv.NORM_L2), 
    cv.norm(np.array(center), np.array(top_left) , cv.NORM_L2))

mask = np.ones(magnitude.shape[:2], dtype=np.uint8)
cv.circle(mask, center, int(outer_radius), 0, -1)
cv.circle(mask, center, int(inner_radius), 1, -1)

# just have these printed to show the masks
masked_magnitude = cv.bitwise_and(magnitude, magnitude, mask=mask)
cv.imshow('magnitude', masked_magnitude)

_, threshold = cv.threshold(masked_magnitude, 1, 255, cv.THRESH_BINARY)
cv.imshow('threshold mask', threshold)

# apply the mask to DFT complex image
DFT2 = cv.bitwise_and(DFT2, DFT2, mask=mask)
DFT2 = np.vstack((np.hstack((DFT2[crow:, ccol:], DFT2[crow:, :ccol])),
                       np.hstack((DFT2[:crow, ccol:], DFT2[:crow, :ccol]))))

# Inverse DFT
IDFT = cv.idft(DFT2)

# normalize the real image, multiply 255, as type uint8, print the image
result = cv.split(IDFT)[0]
result = (cv.normalize(result, result, 0, 1, cv.NORM_MINMAX)*255).astype(np.uint8)
cv.imshow('result', result)

# save the result using argument name
cv.imwrite(parser.parse_args().out, result)


cv.waitKey()
cv.destroyAllWindows()