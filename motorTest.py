import RPi.GPIO as GPIO
import time


def runMotors(commands):
    GPIO.setmode(GPIO.BOARD)

    commandLine = commands

    waitTime = 0.009        # variable
    stepperSteps = 10       # variable

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
    """
    This is here of if i want less torque but more accuracy.
    Make sure i change the names and the full step range.
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
    """
    fullStepSeq = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]
    for action in actionList:
        (moveX, moveY, motorPinsX, motorPinsY) = action

        for pin in motorPinsX:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        for pin in motorPinsY:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)
        # may need to move the *8 out of the bracket and also hopefully zero doesnt break it!
        for i in range(abs(moveX) * stepperSteps):

            for fullStep in range(4):

                for pin in range(4):
                    GPIO.output(motorPinsX[pin], fullStepSeq[fullStep][pin])

                time.sleep(waitTime)

        for j in range(abs(moveY) * stepperSteps):

            for fullStep in range(4):

                for pin in range(4):
                    GPIO.output(motorPinsY[pin], fullStepSeq[fullStep][pin])

                time.sleep(waitTime)

    GPIO.cleanup()
