import cv2
import numpy as np

i = cv2.imread('mazePhoto.jpg')

# Convert to binary
# Find the contour, draw
# Make a mask and Dilate
# Then, Erode
# Find the difference
# Get the new mask (Solution)
# Merge the images and show

gray_scale = cv2.cvtColor(i, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_scale, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(thresh, contours, 0, (255, 255, 255), -1)
ret, thresh = cv2.threshold(thresh, 240, 255, cv2.THRESH_BINARY)

dilate_mask = np.ones((19, 19), np.uint8)
dilate_result = cv2.dilate(thresh, dilate_mask, iterations = 1)

erosion_result = cv2.erode(dilate_result, dilate_mask, iterations = 1)

difference = cv2.absdiff(dilate_result, erosion_result)

b, g, r = cv2.split(i)
mask = difference
result_mask_inverse = cv2.bitwise_not(difference)
r = cv2.bitwise_and(r, r, mask = result_mask_inverse)
g = cv2.bitwise_and(g, g, mask = result_mask_inverse)


result = cv2.merge((b, g, r))
cv2.imshow('solved maze', result)

cv2.waitKey(0)
cv2.destoyAllWindows()