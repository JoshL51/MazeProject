import picamera
import time


def capture(testName):
    camera = picamera.PiCamera()

    camera.contrast = 100

    camera.resolution = (1944, 1944)

    camera.sharpness = 100

    camera.rotation = 270

    camera.start_preview()

    time.sleep(5)

    camera.capture(testName, '.png')

    camera.stop_preview()
