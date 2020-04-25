import sys
import time
import numpy
from PIL import Image
from AStar import AStar
from Greedy import Greedy
from Dijkstras import Dijkstras

# takes time for start of function to calculate time elapsed
startTime = time.time()


# checks to see if pixel is white (not black) [white = path]
def isWhite(p):
    x, y = p
    pixel = pathPixels[x, y]
    if pixel < 255:
        return True


# checking the adjacent pixels in all directions for path
def vonNeumannNeighbours(p):
    x, y = p
    # print(p)
    # do I want to allow diagonal movement?
    neighbors = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    retval = []
    for p in neighbors:
        if isWhite(p):
            continue
        else:
            retval.append(p)
    return retval


# Small note on overestimation of heuristics calculations etc

# Scalar for cost functions (play with me)
D = 1
D2 = 1  # Used for the diagonal distance


# Manhattan success criteria, addition of sides of the triangle
# Deemed one of the most solid for A*
def manhattan(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return D * (dx + dy)


# For if your moves are at any angle
# Shorter than Diagonal or Manhattan so will get shortest path
# but will take longer to run.
def euclidean(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return D * (numpy.sqrt((dx * dx) + (dy * dx)))


# Must be careful here to make sure g_score and costEstimate match in magnitude
# for long distances costEstimate will dwarf g_score as second order
# can i use the same metric for distance - think so
def euclideanSquared(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return D * ((dx * dx) + (dy * dx))


# If the map allows diagonal movement
# Calculates non diagonal route then subtracts the difference.
# When D = 1 and D2 = 1,
# this is called the Chebyshev distance.
# When D = 1 and D2 = sqrt(2),
# this is called the octile distance.
def diagonal(p1, p2):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return D * (dx + dy) + (D2 - (2 * D)) * min(dx, dy)


# pixel location of start and finish points
start = (60, 1980)
goal = (1935, 60)

# Start coordinates for the smallerBoi
# start = (16, 16)
# goal = (481, 493)

# coordinates for TinyBoy
# start = (2, 22)
# goal = (22, 2)

pathImg = Image.open(sys.argv[1])
pathPixels = pathImg.load()


distance = manhattan        # Doesn't matter the method so much as the magnitude is always 1
heuristic = manhattan       # Heuristic h_score in some notation is costEstimate in mine

# path = AStar(start, goal, vonNeumannNeighbours, distance, heuristic)

path = Greedy(start, goal, vonNeumannNeighbours, distance, heuristic)

# path = Dijkstras(start, goal, vonNeumannNeighbours, distance)

# Just here as a check
# print(path)

# recalling the binary image but in RGB from imageReadIn
path_img = Image.open(sys.argv[3])
path_pixels = path_img.load()

for position in path:
    x, y = position
    path_pixels[x, y] = (0, 0, 255) # (0, 0, 0)  # red

path_img.save(sys.argv[2])

print("This test took", time.time() - startTime, "to run.")

print("The path is", len(path), "pixels long.")

# command: python3 pathfinding.py binary03.jpg sol.png clean.jpg
