def AStar(start, goal, neighbourNodes, distance, costEstimate):
    def reconstructPath(cameFrom, currentNode):
        path = []
        #
        while currentNode is not None:
            path.append(currentNode)
            currentNode = cameFrom[currentNode]
        return list(reversed(path))

    g_score = {start: 0}
    f_score = {start: g_score[start] + costEstimate(start, goal)}
    openset = {start}
    closedset = set()
    cameFrom = {start: None}

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
    return []
