import numpy as np
import cv2
import sys
import time
import pickle
from PIL import Image
from AStar import AStar
from Greedy import Greedy
from Dijkstras import Dijkstras
from pathToCommand import commandFunction

maze = sys.argv[1]
imageRGB = Image.open(maze).convert('RGB')  # This converts to RGB so we can draw colours
imageDataRGB = np.asarray(imageRGB)

imageBW = Image.open(maze).convert('1')  # This is black/white
imageDataBW = np.asarray(imageBW)

x, y = imageRGB.size

"""
This draws an image with red gridlines on it for size reference. Use an integer value for size of
gridlines in pixels and then line this up with the walls/corridors in order to find correct
decomposition size (for the ideal image this is 50 x 50).
"""
pixelSizeY = int(imageDataRGB.shape[1]/23)
pixelSizeX = int(imageDataRGB.shape[0]/23)

imageDataPartitioned = np.copy(imageDataRGB)
for x in range(imageDataPartitioned.shape[0]):
    for y in range(imageDataPartitioned.shape[1]):
        if (x % pixelSizeY == 0) or (y % pixelSizeX == 0):
            imageDataPartitioned[x, y] = [255, 0, 0]

Image.fromarray(imageDataPartitioned).show()  # Display red gridlines image

"""
This decomposes the x * y pixel input image, into the decomposed to minimum pixel sizes using 
the grid size found above.
"""
pixelSizeXDecomp = int(x / pixelSizeX)
pixelSizeYDecomp = int(y / pixelSizeY)
decomposedMazeData = np.arange(pixelSizeXDecomp * pixelSizeYDecomp).reshape(pixelSizeXDecomp, pixelSizeYDecomp)

for partX in range(pixelSizeXDecomp):
    for partY in range(pixelSizeYDecomp):
        for orgX in range(partX * pixelSizeX, (partX + 1) * pixelSizeX):
            for orgY in range(partY * pixelSizeY, (partY + 1) * pixelSizeY):
                decomposedMazeData[partX, partY] += imageDataBW[orgX, orgY]
        # print(decomposedMazeData[partX, partY]/(pixelSizeX * pixelSizeY))
        decomposedMazeData[partX, partY] = round(decomposedMazeData[partX, partY] / (pixelSizeX * pixelSizeY))

# print(decomposedMazeData)  # print array of pixel values, 0 is wall, 1 is corridor

smallImageData = Image.fromarray(255 * decomposedMazeData.astype("uint8"), 'L')

smallImageDataRGB = smallImageData.convert('RGB')


# checks to see if pixel is white (not black) [white = path]
def isWhite(p):
    x, y = p
    pixel = decomposedMazeData[x, y]
    if pixel == 0:
        return True


# checking the adjacent pixels in all directions for path
def vonNeumannNeighbours(p):
    x, y = p
    # print(p)
    # do I want to allow diagonal movement?
    neighbors = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    retval = []
    for p in neighbors:
        if isWhite(p):
            continue
        else:
            retval.append(p)
    return retval


# Manhattan success criteria, addition of sides of the triangle
# Deemed one of the most solid for A*
def manhattan(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx + dy


# coordinates for TinyBoy
start = (1, 21)
goal = (21, 1)

# path_pixels = smallImageDataRGB.load()

distance = manhattan  # Doesn't matter the method so much as the magnitude is always 1
heuristic = manhattan  # Heuristic h_score in some notation is costEstimate in mine

path = AStar(start, goal, vonNeumannNeighbours, distance, heuristic)

# path = Greedy(start, goal, vonNeumannNeighbours, distance, heuristic)

# path = Dijkstras(start, goal, vonNeumannNeighbours, distance)

# print(path)

for position in path:
    a, b = position
    decomposedMazeData[a, b] = 255  # (0, 0, 0)  # red

# print(decomposedMazeData)

niceImage = np.copy(decomposedMazeData)
RGB = np.copy(smallImageDataRGB)
for x in range(niceImage.shape[0]):
    for y in range(niceImage.shape[1]):
        if niceImage[x, y] == 255:
            RGB[x, y] = [255, 0, 0]
        if niceImage[x, y] == 0:
            RGB[x, y] = [0, 0, 0]
        if niceImage[x, y] == 1:
            RGB[x, y] = [255, 255, 255]

Image.fromarray(RGB).show()

commandLine = commandFunction(start, goal, path)

# print("\n\n")

# print(commandLine)
