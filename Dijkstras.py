def Dijkstras(start, goal, neighbourNodes, distance):

    def reconstructPath(cameFrom, currentNode):
        path = []
        # cycles through nodes moving the current to the end of the list and finally reversed to give the path
        while currentNode is not None:
            path.append(currentNode)
            currentNode = cameFrom[currentNode]
        return list(reversed(path))

    distToStart = {start: 0}
    openset = {start}
    closedset = set()
    cameFrom = {start: None}

    i = 0
    while openset:
        current = min(openset, key=lambda x: distToStart[x])
        if current == goal:
            return reconstructPath(cameFrom, goal)
        openset.remove(current)
        closedset.add(current)
        for neighbour in neighbourNodes(current):
            if neighbour in closedset:
                continue
            if neighbour not in openset:
                openset.add(neighbour)
            tempDistToStart = distToStart[current] + distance(current, neighbour)
            if tempDistToStart >= distToStart.get(neighbour, float('inf')):
                continue
            cameFrom[neighbour] = current
            distToStart[neighbour] = tempDistToStart

            
    return []

