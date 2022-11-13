import cv2 as cv
import numpy as np

# resize frame
def rescaleFrame(frame, scale = 0.25):
    # used for img, video, live video
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    # enlarge img use interpolation INTER_LINEAL or INTER_CUBIC, shrinking use INTER_AREA
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# change resolution
# def changeRes(width, height):
#     # used for live video
#     capture.set(3, width)
#     capture.set(4, height)


# READ VIDEO (using while loop)
# capture = cv.VideoCapture('earth1.mp4')
# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)
#     # cv.imshow('resized video', rescaleFrame(frame)) # resized video
#     if cv.waitKey(20) & 0xFF == ord('q'):
#         # video is through or press key q to close
#         break
# capture.release()
# cv.destroyAllWindows()

# READ IMAGE
img = cv.imread('pepe.png')
# cv.imshow('Scatter-Plots', img)
# resized img
# resized_img = rescaleFrame(img)
# cv.imshow('resized plot', resized_img)

# # Gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gary', gray)

# # Blur
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# # increase number in (5,5) to blur it more 
# cv.imshow('blur', blur)


# # Edge Cascade (detect)
# canny = cv.Canny(img, 175,175)
# canny = cv.Canny(blur, 175,175)  # a blur img yields less edges
# cv.imshow('canny', canny)


# # Dilating (thicker the edge)
# dilated = cv.dilate(canny, (7,7), iterations= 3)
# cv.imshow('dialated', dilated)


# # Eroding (thinner the edge)
# eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('eroded', eroded)

# Resize
resizee = cv.resize(img, (300,300))
cv.imshow('resize', resizee)

# # Cropping (showing the specific part of the img)
# cropped = img[400:900, 200:700]
# cv.imshow('cropped', cropped)



# Drawing txt & shape
# create a blank img (black)
blank = np.zeros((500,500,3), dtype='uint8')
# blank[:] = 0, 255, 0
# cv.imshow('green', blank)
# blank[200:300, 300:400] = 0,0,255 # rough way to draw rectangle
# cv.imshow('square in blank', blank)

# # Draw Rectangle
# cv.rectangle(blank, (0,0), (250,250), (255, 0,0), thickness=cv.FILLED)
# # cv.rectangle( surface, startPoint, endPoint, color, thinkness = -1 or cv.FILLED is full colored, or 1,2,3..for border only)
# cv.imshow('rectangle', blank)

# # Draw circle
# cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
# # cv.circle( surface, origin, radian, color, thinkness = -1 or cv.FILLED is full colored, or 1,2,3..for border only)
# cv.imshow('circle', blank)

# # Draw line
# cv.line(blank, (0,0), (250,250), (255,255,255), thickness=3)
# # cv.line( surface, startPoint, endPoint, color, thinkness = -1 or cv.FILLED is full colored, or 1,2,3..for border only)
# cv.imshow('line', blank)

# # Write txt
# cv.putText(blank, 'hello', (250,325), cv.FONT_HERSHEY_TRIPLEX, 2.0, (0,255,0), thickness=2)
# # cv.putText( surface, content, startPoint, fontType, fontScale, color, thinkness)
# cv.imshow('txt', blank)


cv.waitKey(0)