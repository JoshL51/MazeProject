def Greedy(start, goal, neighbourNodes, distance, costEstimate):

    def reconstructPath(cameFrom, currentNode):
        path = []
        # cycles through nodes moving the current to the end of the list and finally reversed to give the path
        while currentNode is not None:
            path.append(currentNode)
            currentNode = cameFrom[currentNode]
        return list(reversed(path))

    # distToEnd is the distance to the start
    distToEnd = {start: costEstimate(start, goal)}
    openset = {start}
    closedset = set()
    cameFrom = {start: None}

    i = 0
    while openset:
        current = min(openset, key=lambda x: distToEnd[x])
        if current == goal:
            return reconstructPath(cameFrom, goal)
        openset.remove(current)
        closedset.add(current)
        for neighbour in neighbourNodes(current):
            if neighbour in closedset:
                continue
            if neighbour not in openset:
                openset.add(neighbour)
            tempDistToEnd = distToEnd[current] - distance(current, neighbour)
            if tempDistToEnd >= distToEnd.get(neighbour, float('inf')):
                continue
            cameFrom[neighbour] = current
            distToEnd[neighbour] = costEstimate(neighbour, goal)

        # if i % 10000 == 0:
        #     print("ten thousand done")
        # This section would be to print out the maze every 10000 iterations
        # I would also like this to mark the visited cells as gray to show the method
        # i = i + 1
    return []