from resizeAndPath import resizeToCommand
import time

startTime = time.time()

start = (1, 21)
goal = (21, 1)

cells = 23

fileName = 'multipleSol.png'

solName = 'multiSolAStarSol.png'

algorithm = 'AStar'

resizeToCommand(fileName, start, goal, solName, algorithm, cells)

print("This test took", time.time() - startTime, "to run.")
