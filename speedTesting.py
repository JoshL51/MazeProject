from resizeAndPath import resizeToCommand
import time

startTime = time.time()

start = (1, 158)
goal = (148, 1)

cells = 160

fileName = 'colossal.png'

solName = 'mediumGreedySol.png'

algorithm = 'Greedy'

resizeToCommand(fileName, start, goal, solName, algorithm, cells)

print("This test took", time.time() - startTime, "to run.")
