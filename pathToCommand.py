def commandFunction(start, goal, path):
    lastPosition = start
    resetCommand = (0, 0)
    commandLine = []
    for positions in path:
        if positions == goal:
            currentPosition = positions
            move = (currentPosition[0] - lastPosition[0], currentPosition[1] - lastPosition[1])
            commandLine.append(move)
            commandLine.append(resetCommand)
            break
        currentPosition = positions
        move = (currentPosition[0] - lastPosition[0], currentPosition[1] - lastPosition[1])
        commandLine.append(move)
        lastPosition = currentPosition
    return list(reversed(commandLine))


def commandReduction(commandLine):
    for item in range(0, len(commandLine)):
        if item == (len(commandLine) - 1):
            break
        if commandLine[item] == commandLine[item + 1]:
            del commandLine[item]
    return list(reversed(commandLine))

# def compoundCommand(commandLine):
#     for item in range(0, len(commandLine)):
#         if item == (len(commandLine)-1):
#             break
#         if commandLine[item] != commandLine[item + 1]:
