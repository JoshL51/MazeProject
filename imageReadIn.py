from skimage import exposure
import numpy as np
import imutils
import cv2

# load image in as 0=grayscale name img
img = cv2.imread('mazePhoto.jpg', 0)

ratio = img.shape[0] / 300.0

# making a copy of the image as some of the commands are destructive
orig = img.copy()

# purely resizing the image
img = imutils.resize(img, height=300)

# cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace[, dst[, borderType]]) → dst
# reduces unwanted noise while keeping edges relatively sharp
img = cv2.bilateralFilter(img, 11, 17, 17)

# popular edge detection algorithm
edged = cv2.Canny(img, 30, 200)

# find contours in the edged image, keep only the largest ones, and initialize our screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None
# loop over our contours
for c in cnts:
    # approximate the length of the contour
    peri = cv2.arcLength(c, True)
    # play around with the precision (1.5%)
    approx = cv2.approxPolyDP(c, 0.015 * peri, True)
    # if our approximated contour has four points, then we can assume that we have found the maze
    if len(approx) == 4:
        screenCnt = approx
        break

# not necessary but draws the line on the image as a check, should be green but image grayscale
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)

# finding the corner coordinates for warping
pts = screenCnt.reshape(4, 2)
rect = np.zeros((4, 2), dtype="float32")

# the top-left point has the smallest sum whereas the
# bottom-right has the largest sum
s = pts.sum(axis=1)
rect[0] = pts[np.argmin(s)]
rect[2] = pts[np.argmax(s)]

# compute the difference between the points -- the top-right
# will have the minimum difference and the bottom-left will
# have the maximum difference
diff = np.diff(pts, axis=1)
rect[1] = pts[np.argmin(diff)]
rect[3] = pts[np.argmax(diff)]

# multiply the rectangle by the original ratio
rect *= ratio

# now that we have our rectangle of points, let's compute the width of our new image
(tl, tr, br, bl) = rect
widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))

# ...and now for the height of our new image
heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))

# take the maximum of the width and height values to reach our final dimensions
maxWidth = max(int(widthA), int(widthB))
maxHeight = max(int(heightA), int(heightB))

# construct our destination points which will be used to map the screen to a top-down, "birds eye" view
dst = np.array([
    [0, 0],
    [maxWidth - 1, 0],
    [maxWidth - 1, maxHeight - 1],
    [0, maxHeight - 1]], dtype="float32")

# calculate the perspective transform matrix and warp the perspective to grab the screen
M = cv2.getPerspectiveTransform(rect, dst)
warp = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))

# extra colour correction, min becomes black-0 max becomes white-255
# warp = exposure.rescale_intensity(warp, out_range=(0, 255))

# thresh = cv2.adaptiveThreshold(warp, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 15)
# thresh = cv2.threshold(warp, 127, 255, cv2.THRESH_BINARY)
ret, binary = cv2.threshold(warp, 127, 255, cv2.THRESH_BINARY)

# print image function
cv2.imwrite("binary03.jpg", binary)
