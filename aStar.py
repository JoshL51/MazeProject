def AStar(start, goal, neighbourNodes, distance, costEstimate):
    def reconstructPath(cameFrom, currentNode):
        path = []
        # cycles through nodes moving the current to the end of the list and finally reversed to give the path
        while currentNode is not None:
            path.append(currentNode)
            currentNode = cameFrom[currentNode]
        return list(reversed(path))

    # g_score is the distance to the start
    g_score = {start: 0}
    # f_score is the sum of the distance to the start and the manhattan cost to the goal
    f_score = {start: g_score[start] + costEstimate(start, goal)}
    # openset is all visited nodes
    openset = {start}
    # closed set are visited nodes
    closedset = set()
    cameFrom = {start: None}

    i = 0
    while openset:
        current = min(openset, key=lambda x: f_score[x])
        if current == goal:
            return reconstructPath(cameFrom, goal)
        openset.remove(current)
        closedset.add(current)
        for neighbour in neighbourNodes(current):
            if neighbour in closedset:
                continue
            if neighbour not in openset:
                openset.add(neighbour)
            tentative_g_score = g_score[current] + distance(current, neighbour)
            if tentative_g_score >= g_score.get(neighbour, float('inf')):
                continue
            cameFrom[neighbour] = current
            g_score[neighbour] = tentative_g_score
            f_score[neighbour] = tentative_g_score + costEstimate(neighbour, goal)

        # if i % 10000 == 0:
        #     print("ten thousand done")
        # This section would be to print out the maze every 10000 iterations
        # I would also like this to mark the visited cells as gray to show the method
        # i = i + 1
    return []
