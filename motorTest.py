import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

motorPins_01 = [11, 12, 13, 15]
motorPins_02 = [31, 33, 35, 37]

for pin in motorPins_01:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

for pin in motorPins_02:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

halfStepSeq = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1]
]

for i in range(512):
    for halfStep in range(8):
        for pin in range(4):
            GPIO.output(motorPins_01[pin], halfStepSeq[halfStep][pin])
            GPIO.output(motorPins_02[pin], halfStepSeq[halfStep][pin])
        time.sleep(0.001)

GPIO.cleanup()


# camera software