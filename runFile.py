from imageReadIn import imageManipulation
from motorTest import runMotors
from cameraControls import capture
from resizeAndPath import resizeToCommand
from resize import resize

start = (1, 21)
goal = (21, 1)

print('Please enter the name of this test: \n')

testName = input()

capture(testName)

binary = imageManipulation(testName)

commandLine = resizeToCommand(testName, start, goal)

runMotors(commandLine)

proofImage = str(testName) + 'proof'

proofBinary = imageManipulation(proofImage)

resize(proofBinary)