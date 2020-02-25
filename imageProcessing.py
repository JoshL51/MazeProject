import cv2
# import numpy as np
# from PIL import Image
# import pytesseract
k = 1

# use of webcam to capture image of sudoku

ar = None
count = 0
# webcam is open
# cap = cv2.VideoCapture(0)

while 1:
    # reading  frame from webcam
    frame = cv2.imread(cv2.samples.findFile('mazePhoto.jpg'))
    k = 0
    # converting image to grayscale and then applying blurs to remove noise
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.GaussianBlur(img, (55, 55), 3)
    # thresholding frame in binary by adaptive thresholding

    thresh = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    cv2.imshow('thresh', thresh)
    # finding contours in image to find sudoku grid
    contours, hie = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # max is variable for maximum area and maxc for maximum contours
    maxc = [0]
    max = 0
    # loop to find largest contour in given frame
    for i in range(len(contours)):
        # finding perimeter of contour and contour approximation
        peri = cv2.arcLength(contours[i], True)
        approx = cv2.approxPolyDP(contours[i], 0.011 * peri, True)

        if cv2.contourArea(contours[i]) > 10000 and cv2.contourArea(contours[i]) > max and len(approx) == 4:
            # checking maximum contours

            max = cv2.contourArea(contours[i])
            maxc = approx
    # if contour have four corners then saving that frame and drawing contours
    if len(maxc) == 4:
        count = count + 1
    else:
        count = 0
    if len(maxc) == 4:
        cv2.drawContours(frame, [maxc], -1, (255, 0, 2), 5)
        cv2.drawContours(frame, maxc, -1, (0, 255,), 8)

    # displaying contous edges and corners

    cv2.imshow('all', frame)
    cv2.waitKey(1)
    if count == 4:
        cv2.imwrite("frame.jpg", frame)
        ar = maxc
        k = 1

    if k == 1:
        break
        #
