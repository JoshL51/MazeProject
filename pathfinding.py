import sys
from PIL import Image
from AStar import AStar
import cv2


# checks to see if pixel is white (not black) [white = path]
def isWhite(p):
    x, y = p
    pixel = pathPixels[x, y]
    if pixel < 225:
        return True


# checking the adjacent pixels in all directions for path
def vonNeumannNeighbours(p):
    x, y = p
    print(p)
    neighbors = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    retval = []
    for p in neighbors:
        if isWhite(p):
            continue
        else:
            retval.append(p)
    return retval


# manhattan success criteria
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# pixel location of start and finish points
start = (69, 1996)
goal = (1946, 43)

# start = (16, 16)
# goal = (481, 493)

pathImg = Image.open(sys.argv[1])
pathPixels = pathImg.load()

distance = manhattan
heuristic = manhattan

path = AStar(start, goal, vonNeumannNeighbours, distance, heuristic)

print(path)

path_img = Image.open(sys.argv[3])
path_pixels = path_img.load()

for position in path:
    x, y = position
    path_pixels[x, y] = (255, 0, 0)  # red

path_img.save(sys.argv[2])

# command: python3 mazesolver.py binary03.jpg completeAStar.jpg
