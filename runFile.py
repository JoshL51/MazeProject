from imageReadIn import imageManipulation
from motorTest import runMotors
from cameraControls import capture
from resizeAndPath import resizeToCommand
from resize import resize
from PIL import Image
import numpy as np

start = (1, 21)
goal = (21, 1)

print('Please enter the name of this test: \n')

testName = input()

capture(testName)

binary = imageManipulation(testName)

print('Please place ball on table.')

commandLine = resizeToCommand(testName, start, goal)

runMotors(commandLine)

proofImage = str(testName) + 'proof'

while True:
    capture(proofImage)

    proofBinary = imageManipulation(proofImage)

    imageData = resize(proofBinary)

    if imageData[goal] == 0:
        RGB = np.copy(imageData)
        for x in range(imageData.shape[0]):
            for y in range(imageData.shape[1]):
                if imageData[x, y] == 1:
                    RGB[x, y] = [255, 255, 255]
                if imageData[goal] == 0:
                    RGB[goal] = [124, 252, 0]  # lawngreen
                if imageData[x, y] == 0:  # does this need to be an elif?
                    RGB[x, y] = [0, 0, 0]

        Image.fromarray(RGB).show()
        print('The ball has reached its destination!')
        break
