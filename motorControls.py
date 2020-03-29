# Name: Steptwo.py
#
# Author: Rob Davis
# Based on the Stepper Motor code from matt.hawkins www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/
#
# Created: 2014/03/12
#
# Takes parameters for number of steps and which direction for each motor from the command line.
# e.g.
# sudo python step.py 4100 CCW 2050 CW
# To operate motor 1 for 4100 steps (a complete revolution) in a counter clockwise
# direction and at the same time turn motor 2 in a Clockwise direct for 2050 steps (180 degrees).
# -----------------------------------

# !/usr/bin/env python

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO

# Use physical pin numbers
# instead of BCM GPIO references
GPIO.setmode(GPIO.Board)

# Define GPIO signals to use
stepPinsX = [24, 25, 8, 7]  # Clockwise rotation
if sys.argv[2] == "CCW":
    stepPinsX = [7, 8, 25, 24]  # Anti-Clockwise rotation

stepPinsY = [14, 15, 18, 23]  # Clockwise rotation
if sys.argv[4] == "CCW":
    stepPinsY = [23, 18, 15, 14]  # Anti-Clockwise rotation

# Set all pins as output
for pin in stepPinsX:
    # print "Setup pins"
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

for pin in stepPinsY:
    # print "Setup pins"
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

# Define some settings
stepCounter = 0
waitTime = 0.01

# Define simple sequence
StepCount1 = 4
seq1 = []
seq1 = range(0, StepCount1)
seq1[0] = [1, 0, 0, 0]
seq1[1] = [0, 1, 0, 0]
seq1[2] = [0, 0, 1, 0]
seq1[3] = [0, 0, 0, 1]

# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 8
seq2 = []
seq2 = range(0, StepCount2)
seq2[0] = [1, 0, 0, 0]
seq2[1] = [1, 1, 0, 0]
seq2[2] = [0, 1, 0, 0]
seq2[3] = [0, 1, 1, 0]
seq2[4] = [0, 0, 1, 0]
seq2[5] = [0, 0, 1, 1]
seq2[6] = [0, 0, 0, 1]
seq2[7] = [1, 0, 0, 1]

# Choose a sequence to use
# Seq = seq1
# StepCount = StepCount1
Seq = seq2
StepCount = StepCount2

# Start main loop
steps1 = int(sys.argv[1])
steps2 = int(sys.argv[3])
stepC = 0
while (stepC <= steps1) or (stepC <= steps2):
    if stepC <= steps1:
        print("Step %i of %i" % (stepC, steps1))
    if stepC <= steps2:
        print("Step %i of %i" % (stepC, steps2))

for pin in range(0, 4):
    if stepC <= steps1:
        xPin1 = stepPinsX[pin]
        if Seq[stepCounter][pin] != 0:
            # print " Step %i Enable %i" %(StepCounter,xPin1)
            GPIO.output(xPin1, True)
        else:
            GPIO.output(xPin1, False)
    if stepC <= steps2:
        xPin2 = stepPinsY[pin]
        if Seq[stepCounter][pin] != 0:
            # print " Step %i Enable %i" %(StepCounter,xPin2)
            GPIO.output(xPin2, True)
        else:
            GPIO.output(xPin2, False)

stepCounter += 1

# If we reach the end of the sequence
# start again
if stepCounter == StepCount:
    stepCounter = 0
if stepCounter < 0:
    stepCounter = StepCount

# Wait before moving on
time.sleep(waitTime)
stepC += 1

GPIO.cleanup()
