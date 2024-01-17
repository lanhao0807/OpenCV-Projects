import cv2 as cv
import numpy as np
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="SLIC Image Segmentation")
    parser.add_argument("-img", type=str, required=True, help="Path to the input image")
    parser.add_argument("--algorithm", type=str, default="a", choices=["a", "b", "c"],
                        help="SLIC algorithm variant: a = SLIC, b = SLICO, c = MSLIC (default: a)")
    parser.add_argument("--size", type=int, default=10, help="Average superpixel size (default: 10)")
    parser.add_argument("--ruler", type=float, default=10.0, help="Enforcement of superpixel smoothness (default: 10.0)")

    args = parser.parse_args()

    image = cv.imread(args.img)
    # image = cv.resize(image, (789, 443))
    h, w, _ = image.shape

    # set the desired width
    width = 500

    # calculate the new height to preserve aspect ratio
    ratio = width / w
    height = int(h * ratio)

    # resize the image
    image = cv.resize(image, (width, height))
    if image is None:
        print(f"Error: Unable to read input image '{args.img}'.")
        sys.exit(1)

    algorithm = {
        "a": cv.ximgproc.SLIC,
        "b": cv.ximgproc.SLICO,
        "c": cv.ximgproc.MSLIC,
    }[args.algorithm]

    slic = cv.ximgproc.createSuperpixelSLIC(image, algorithm=algorithm, region_size=args.size, ruler=args.ruler)
    slic.iterate()

    # draw contours
    mask = slic.getLabelContourMask()
    contour_image = image.copy()
    contour_image[mask == 255] = (255, 255, 255)

    # Get the labels for all pixels
    labels = slic.getLabels()
    num_superpixels = slic.getNumberOfSuperpixels()

    # Calculate the average color of each superpixel
    average_colors = np.zeros((num_superpixels, 3), dtype=np.uint64)
    counts = np.zeros((num_superpixels,), dtype=np.uint64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            label = labels[i, j]
            average_colors[label] += image[i, j]
            counts[label] += 1
            
    # print(labels)
    # print(labels.shape)
    # print(num_superpixels)
    # print(counts)
    # print(counts.shape)
    # print(average_colors)
    # print(average_colors.shape)

    average_colors = (average_colors / counts[:, None]).astype(np.uint8)

    # Replace each pixel with the average color of its corresponding superpixel
    result = np.zeros_like(image)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            label = labels[i, j]
            result[i, j] = average_colors[label]

    # Show the contour image
    cv.imshow("Contours", contour_image)

    # Show the final result image
    cv.imshow("Result", result)
    result[mask == 255] = (0,0,0)

    cv.imshow('Result + Contours', result)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()