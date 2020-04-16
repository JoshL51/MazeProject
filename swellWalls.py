import cv2
import sys
import numpy as np
from PIL import Image


# def isWall(p):
#     x, y = p
#     pixel = wallPixels[x, y]
#     if pixel < 225:
#         return False


# def box(p):
#     x, y = p
#     swell = []
#     for x in range((x - 3), (x + 3)):
#         for y in range((y - 3), (y + 3)):
#             if isWall(p):
#                 continue
#             else:
#                 swell.append(p)
#     return swell


pathImg = Image.open(sys.argv[1])
wallPixels = pathImg.load()

image = cv2.imread(sys.argv[1])

swell = []
for i in range(10, (image.shape[0] - 10)):
    for j in range(10, (image.shape[1] - 10)):
        # walls = box(wallPixels)
        if np.all(image[i, j] != [0, 0, 0]):
            continue
        else:
            # block = image[i - 3:i + 3, j - 3:j + 3]
            for x in range((i - 10), (i + 10)):
                for y in range((j - 10), (j + 10)):
                    pos = [x, y]
                    swell.append(pos)

print(swell[2])

# path_img = Image.open(sys.argv[3])
# path_pixels = path_img.load()

img = cv2.imread(sys.argv[3])

for position in swell:
    x, y = position
    img[x, y] = (255, 0, 0)  # red
    # img.putpixle([x, y], (0, 0, 0))

cv2.imwrite(sys.argv[2], img)
# img.save(sys.argv[2])

# python3 swellWalls.py binary03.jpg swelled.jpg clean.jpg
