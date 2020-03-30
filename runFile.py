import os
import picamera
import cameraControls
import imageReadIn
import pathfinding
import pathToCommand
import motorTest

# # # sudo python runFile.py # # #

# run and begin with a camera view
camera = picamera.PiCamera()
camera.start_preview()

# if all okay, wait for key to continue with prompt
answer = input("Press 'a' if happy with position or 'b' to exit: ")
for i in answer:
    if answer == str('a'):
        camera.stop_preview()
        continue
    elif answer == str('b'):
        exit()
    else:
        exit()

# (wonder if key controls can be used to flatten the table manually?)
print('Please use arrow keys to flatten table, followed by return.')

# request name of test
testName = input('Now please enter the name of your test followed by return: ')
# can  python create a new folder here for all of its files?
os.mkdir(testName)  # not sure if i need the inverted commas?

# run cameraControls

# run image processing file and output into folder the image
# show image for a few seconds to check okay, if not specific key press with prompt.
# if okay request use of which algorithm, A* or GA
# runs and saves final image and path file in folder
# opens the image and waits for few seconds with stop key again and prompt
# runs motor program
# (perhaps runs camera to video its attempt or external camera?)
