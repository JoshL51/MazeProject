import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

commandLine = [
    # Coordinates test
    (0, 0),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (0, 0)
]

currentY = 0
currentX = 0
actionList = []

for command in commandLine:
    moveX = 0
    moveY = 0
    motorPinsX = [11, 12, 13, 15]
    motorPinsY = [31, 33, 35, 37]
    x, y = command

    if currentY != y:
        moveY = y - currentY
        currentY = y

    if currentX != x:
        moveX = x - currentX
        currentX = x

    if moveY < 0:
        motorPinsY = list(reversed(motorPinsY))

    if moveX < 0:
        motorPinsX = list(reversed(motorPinsX))

    action = (moveX, moveY, motorPinsX, motorPinsY)
    actionList.append(action)

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

for action in actionList:
    (moveX, moveY, motorPinsX, motorPinsY) = action

    for pin in motorPinsX:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    for pin in motorPinsY:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, 0)

    for i in range(8):

        for halfStep in range(8):

            for pin in range(4):
                GPIO.output(motorPinsX[pin], halfStepSeq[halfStep][pin])
                GPIO.output(motorPinsY[pin], halfStepSeq[halfStep][pin])

            time.sleep(0.001)

GPIO.cleanup()

# camera software
