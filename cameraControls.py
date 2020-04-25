import picamera
import time
import cv2


def capture(testName):
    camera = picamera.PiCamera()

    camera.awb_mode = 'auto'

    # camera.colour_effects = (128, 128)

    camera.contrast = 50

    camera.brightness = 50

    camera.exposure.mode = 'spotlight'

    camera.ISO = 100

    # camera.resolution = (2000, 2000)

    camera.sharpness = 50

    camera.crop = (0.0, 0.0, 1.0,)
    # test and finalise

    camera.start_preview()
    time.sleep(5)
    cv2.waitKey()
    camera.capture(testName, '.png')
    # name this 'test_X_initial photo and address it to the folder just created
    camera.stop_preview()
