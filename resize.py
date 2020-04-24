import numpy as np
from PIL import Image
import runFile


def resize(image):
    maze = image
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
    pixelSizeY = 50
    pixelSizeX = 50

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
            decomposedMazeData[partX, partY] = round(decomposedMazeData[partX, partY] / (pixelSizeX * pixelSizeY))

    # print(decomposedMazeData)  # print array of pixel values, 0 is wall, 1 is corridor

    smallImageData = Image.fromarray(255 * decomposedMazeData.astype("uint8"), 'L')

    smallImageDataRGB = smallImageData.convert('RGB')

    niceImage = np.copy(decomposedMazeData)
    RGB = np.copy(smallImageDataRGB)
    for x in range(niceImage.shape[0]):
        for y in range(niceImage.shape[1]):
            if niceImage[x, y] == 1:
                RGB[x, y] = [255, 255, 255]
            if niceImage[runFile.start] == 0:
                RGB[runFile.start] = [124, 252, 0]  # lawngreen
                print('The ball has reached its destination!')
            if niceImage[x, y] == 0:    # does this need to be an elif?
                RGB[x, y] = [0, 0, 0]

    Image.fromarray(RGB).show()
