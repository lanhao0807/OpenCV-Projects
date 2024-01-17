import cv2 as cv
import numpy as np
import filetype
import argparse
import header as h
from scipy.spatial.distance import cdist

parser = argparse.ArgumentParser(description='Argument parser description')
parser.add_argument('-img', nargs='?', help='A path of the input img')
parser.add_argument('-out', nargs='?', help='A path of the output img', default= 'output.jpg')

# input img is required and only img, otherwise, quit
input_img = parser.parse_args().img
if not filetype.is_image(input_img) or input_img is None:
    print("Invalid image file")
    exit()
# ==================================================================================================================


img  = cv.resize(cv.imread(input_img), (789, 443))
cv.imshow('img', img)

cv.namedWindow('Segmented Image')
seg_img = h.K_means(img)

def get_mouse_click(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # Get the label of the clicked pixel
        label = seg_img[y, x, 0]
        
        # Extract the connected component that contains the clicked pixel
        _, labels = cv.connectedComponents((seg_img[:, :, 0] == label).astype(np.uint8) * 255)

        selected_component = labels[y, x]

        # Extract the state corresponding to the selected component
        state = np.zeros_like(seg_img)
        state[labels == selected_component] = 255
# ======================================================================================
        # to make the selected region exclusive, find its separated neighbor using clicked position
        l = labels.copy()
        l[labels == selected_component] = 0
        l = l.astype(np.float32)

        distances = cdist([(y, x)], np.argwhere(l), metric='euclidean').squeeze()
        nearest_pixels = []

        # 5 nearest pixels that are not in the original segment
        nearest_pixel_indices = np.argsort(distances)[:5]
        
        # if they are more than 100 units away, it's another state with same color.
        # so we dont take it. We only take very close and same color pixels

        for idx in nearest_pixel_indices:
            print('5 nearest pixels\' distance: ', distances[idx])
            if distances[idx] <= 30:
                nearest_pixels = np.append(nearest_pixels, np.argwhere(l)[idx], axis = 0)

        # make it point-like
        nearest_pixels = np.reshape(nearest_pixels, (-1,2)).astype(np.int32)
        
        # find the connected components of these near pixels and them to the mask
        for pixel in nearest_pixels:
            _, labels = cv.connectedComponents((seg_img[:, :, 0] == label).astype(np.uint8) * 255)
            selected_component = labels[pixel[0], pixel[1]]
            state[labels == selected_component] = 255

        cv.imshow('states', state.astype(np.uint8))
# ======================================================================================    
        # Get the centroid of the state mask
        moments = cv.moments(state[:, :, 0])
        cx = int(moments['m10'] / moments['m00'])
        cy = int(moments['m01'] / moments['m00'])
        print(f'centroid:  ({cx}, {cy})')

        # affine matrix
        M = np.float32([[2, 0, cx - 2*cx], [0, 2, cy-2*cy]])

        # Apply the affine transform to the state
        state_zoom = cv.warpAffine(state, M, (seg_img.shape[1], seg_img.shape[0]))

        # Overlay the zoomed state on the original map
        map_with_state = cv.addWeighted(seg_img, 0.8, state_zoom, 1, 0)

        # Display the map with the zoomed state
        cv.imshow('Segmented Image', map_with_state)
        cv.waitKey(0)
        

cv.setMouseCallback('Segmented Image', get_mouse_click)

while True:
    cv.imshow('Segmented Image', seg_img)

    key = cv.waitKey(1000)
    if key == ord('q'):
        break

    
cv.destroyAllWindows()