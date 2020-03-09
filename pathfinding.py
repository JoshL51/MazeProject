import sys
from PIL import Image
from AStar import AStar


def is_blocked(p):
    x, y = p
    pixel = path_pixels[x, y]
    if (pixel < 225):
        return True


def von_neumann_neighbors(p):
    x, y = p
    print(p)
    neighbors = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    retval = []
    for p in neighbors:
        if is_blocked(p):
            continue
        else:
            retval.append(p)
    return retval


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def squared_euclidean(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


start = (69, 1996)
goal = (1946, 43)

# python mazesolver.py <mazefile> <outputfile>

path_img = Image.open(sys.argv[1])
path_pixels = path_img.load()

distance = manhattan
heuristic = manhattan

path = AStar(start, goal, von_neumann_neighbors, distance, heuristic)

print("PATH.......")
print(path)
for position in path:
    x, y = position
    path_pixels[x, y] = (255, 0, 0)  # red

path_img.save(sys.argv[2])
