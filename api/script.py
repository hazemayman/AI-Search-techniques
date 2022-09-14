import random
weightGraph = False
front_end_array = [
    [
        [1, 1],
        [4, 1],
        [4, 1],
        [4, 1],
        [4, 1]

    ], [
        [4, 5],
        [4, 5],
        [4, 5],
        [4, 5],
        [4, 1]

    ], [
        [4, 5],
        [4, 5],
        [3, 5],
        [3, 5],
        [4, 1]

    ], [
        [4, 5],
        [4, 5],
        [3, 5],
        [4, 5],
        [2, 1]

    ]
]


def viewArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=" , ")
        print()
    print('\n\n')


def createWeightedArray(row=20, col=20, min_weight=1, max_weight=100, startNode=[0, 0], goalNode=[19, 19]):
    front_array = [[]for i in range(row)]
    for i in range(row):
        for j in range(col):
            front_array[i].append([4, random.randint(min_weight, max_weight)])

    front_array[startNode[0]][startNode[1]][0] = 1
    front_array[startNode[0]][startNode[1]][1] = 1
    front_array[goalNode[0]][goalNode[1]][0] = 2

    return front_array


if(weightGraph):
    front_end_array = createWeightedArray()


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def append(self, node):
        self.queue.append(node)

    # for popping an element based on Priority
    def pop(self):
        if(len(self.queue) > 0):
            minValue = self.queue[0].f
            minIndex = 0

            for i in range(len(self.queue)):
                if(self.queue[i].f < minValue):
                    minValue = self.queue[i].f
                    minIndex = i
            x = self.queue.pop(minIndex)
            return x


class Node:
    def __init__(self, node_position, node_type, node_weight):
        self.node_position = node_position
        # 1-> start node , 2-> end node , 3-> wall , 4-> free space to walk in
        self.node_type = node_type
        self.node_weight = node_weight
        self.parent = None
        self.visited = False
        self.depth = 0

        # self.childs = []
        self.g = 0
        self.h = 0
        self.f = 0

    def calculate_evaluation_function(self):
        pass


class Grid:
    def __init__(self):
        self.grid = []
        self.start_node = None
        self.goal_node = []

    def createGrid(self, front_end_array):
        for row in range(len(front_end_array)):
            self.grid.append([])
            for col in range(len(front_end_array[0])):
                self.grid[row].append(
                    Node([row, col], front_end_array[row][col][0], front_end_array[row][col][1]))
                if(front_end_array[row][col][0] == 1):
                    self.start_node = self.grid[row][col]
                elif(front_end_array[row][col][0] == 2):
                    self.goal_node.append (self.grid[row][col])

    def viewGrid(self):
        for row in self.grid:
            for node in row:
                print(node.node_type, end=" ")
            print("        ", end="")
            for node in row:
                print(node.node_weight, end=" ")
            print()


class BFS:
    def __init__(self, front_end_array):
        self.gridBoard = Grid()
        self.closeSet = []
        self.finalGoalNode = None
        condition = True
        try:
            self.gridBoard.createGrid(front_end_array)
        except:
            condition = False
            print("error")
        if(condition):
            print("\nthe Grid has been created ! \n")
            # self.gridBoard.viewGrid()

    def expandNode(self, node, queueCheck=False , closeset = []):

        neighboursList = []

        if(node.node_position[0]-1 >= 0 and self.gridBoard.grid[node.node_position[0]-1][node.node_position[1]].visited == False):
            next_node = self.gridBoard.grid[node.node_position[0] -
                                            1][node.node_position[1]]
            if(next_node.node_type != 3):
                if(queueCheck == False):
                    if(next_node in closeset):
                        next_node.visited = True
                    else:
                        neighboursList.append(next_node)
                        next_node.visited = queueCheck
                else:
                    neighboursList.append(next_node)
                    next_node.visited = queueCheck
                # next_node.parent = node

        if(node.node_position[0]+1 < len(self.gridBoard.grid) and self.gridBoard.grid[node.node_position[0]+1][node.node_position[1]].visited == False):
            next_node = self.gridBoard.grid[node.node_position[0] +
                                            1][node.node_position[1]]
            if(next_node.node_type != 3):
                if(queueCheck == False):
                    if(next_node in closeset):
                        next_node.visited = True
                    else:
                        neighboursList.append(next_node)
                        next_node.visited = queueCheck
                else:
                    neighboursList.append(next_node)
                    next_node.visited = queueCheck
                # next_node.parent = node

        if(node.node_position[1]-1 >= 0 and self.gridBoard.grid[node.node_position[0]][node.node_position[1]-1].visited == False):
            next_node = self.gridBoard.grid[node.node_position[0]
                                            ][node.node_position[1]-1]
            if(next_node.node_type != 3):
                if(queueCheck == False):
                    if(next_node in closeset):
                        next_node.visited = True
                    else:
                        neighboursList.append(next_node)
                        next_node.visited = queueCheck
                else:
                    neighboursList.append(next_node)
                    next_node.visited = queueCheck
                # next_node.parent = node

        if(node.node_position[1]+1 < len(self.gridBoard.grid[0]) and self.gridBoard.grid[node.node_position[0]][node.node_position[1]+1].visited == False):
            next_node = self.gridBoard.grid[node.node_position[0]
                                            ][node.node_position[1]+1]
            if(next_node.node_type != 3):
                if(queueCheck == False):
                    if(next_node in closeset):
                        next_node.visited = True
                    else:
                        neighboursList.append(next_node)
                        next_node.visited = queueCheck
                else:
                    neighboursList.append(next_node)
                    next_node.visited = queueCheck
                # next_node.parent = node

        return neighboursList

    def SearchForPath(self):
        queue = []
        queue.append(self.gridBoard.start_node)
        self.gridBoard.start_node.visited = True

        found = False

        while queue:
            node = queue.pop(0)
            self.closeSet.append(node)
            if(node in self.gridBoard.goal_node):
                self.finalGoalNode = node
                found = True
                break

            neighboursList = self.expandNode(node, True)

            for sub_node in neighboursList:
                sub_node.parent = node
                queue.append(sub_node)
        if(found):
            print("\n\ngoal is found ! \n\n")

    def viewPath(self):
        count = 0
        chainNode = self.gridBoard.goal_node
        while(chainNode != None):
            count += 1
            print(chainNode.node_position, end=" , ")
            chainNode = chainNode.parent
        print(count, end=" , ")

    def SearchForPathDFS(self):
        stack = []
        stack.append(self.gridBoard.start_node)
        self.gridBoard.start_node.visited = True

        found = False

        while stack:
            node = stack.pop()
            self.closeSet.append(node)
            if(node in self.gridBoard.goal_node):
                self.finalGoalNode = node
                found = True
                break

            neighboursList = self.expandNode(node, False , self.closeSet)

            for sub_node in neighboursList:
                sub_node.parent = node
                stack.append(sub_node)
        if(found):
            print("\n\ngoal is found ! \n\n")

    def SearchForPathDLS(self, depth=1 , stack = []):
        if(depth == 1):
            stack.append(self.gridBoard.start_node)
            self.gridBoard.start_node.visited = True
        found = False
        levelNodes = []
        # print(stack)
        while stack:
            node = stack.pop()
            if(node.depth > depth):
                levelNodes.append(node)
                continue
            self.closeSet.append(node)
            if(node in self.gridBoard.goal_node):
                self.finalGoalNode = node
                found = True
                return found
            neighboursList = self.expandNode(node, True , self.closeSet)
            for sub_node in neighboursList:
                sub_node.parent = node
                stack.append(sub_node)
                sub_node.depth = node.depth + 1
       
        # print(levelNodes)
        if(levelNodes == []):
            return False
        else:
            # print("here")
            # print(levelNodes)
            # print(levelNodes.reverse())
            self.SearchForPathDLS(depth + 1 , levelNodes)
                

       

    def SearchForPathIDDS(self):
    
        found = self.SearchForPathDLS(1)
        if(found):
            print("\n\ngoal is found ! \n\n")
        else:
            print("wrong")
   

    def SearchForPathASTAR(self):
        myQueue = PriorityQueue()
        myQueue.append(self.gridBoard.start_node)
        self.gridBoard.start_node.visited = True

        found = False

        while not myQueue.isEmpty():
            node = myQueue.pop()
            self.closeSet.append(node)
            if(node in self.gridBoard.goal_node):
                found = True
                self.finalGoalNode = node
                break

            neighboursList = self.expandNode(node , False , self.closeSet)

            for sub_node in neighboursList:
                # calculate g for the current node
                g = None
                if len(self.gridBoard.goal_node) > 1:
                    g = sub_node.node_weight + node.g
                else:
                    g = sub_node.node_weight + node.g

                # calculate h for the current node

                minValue = 100000000
                
                if len(self.gridBoard.goal_node) > 1:
                    # print('1')
                    if(sub_node.node_weight <= 1):
                        # print('2')
                        minValue = abs(self.gridBoard.goal_node[0].node_position[0] - sub_node.node_position[0])  + abs(
                        self.gridBoard.goal_node[0].node_position[1] - sub_node.node_position[1]) 
                    else:
                        # print('3')
                        for goalNode in range(len(self.gridBoard.goal_node)):
                            if(20*abs(self.gridBoard.goal_node[goalNode].node_position[0] - sub_node.node_position[0])+ 20*abs(
                            self.gridBoard.goal_node[goalNode].node_position[1] - sub_node.node_position[1]) < minValue):
                                minValue = 20*abs(self.gridBoard.goal_node[goalNode].node_position[0] - sub_node.node_position[0])  + 20*abs(
                                self.gridBoard.goal_node[goalNode].node_position[1] - sub_node.node_position[1])
                else:
                    if(sub_node.node_weight <= 1):
                        # print('4')
                        minValue = abs(self.gridBoard.goal_node[0].node_position[0] - sub_node.node_position[0]) + abs(
                                self.gridBoard.goal_node[0].node_position[1] - sub_node.node_position[1]) 
                    else:
                        # print('5')
                        for goalNode in range(len(self.gridBoard.goal_node)):
                            if(20*abs(self.gridBoard.goal_node[goalNode].node_position[0] - sub_node.node_position[0])+ 20*abs(
                            self.gridBoard.goal_node[goalNode].node_position[1] - sub_node.node_position[1]) < minValue):
                                minValue = 20*abs(self.gridBoard.goal_node[goalNode].node_position[0] - sub_node.node_position[0])  + 20*abs(
                                self.gridBoard.goal_node[goalNode].node_position[1] - sub_node.node_position[1])
                h = minValue


                # h = 4*abs(self.gridBoard.goal_node[0].node_position[0] - sub_node.node_position[0]) + 2 + 4*abs(
                # self.gridBoard.goal_node[0].node_position[1] - sub_node.node_position[1]) + 2

                # caluclate f for the current node

                f = g + h

                if(sub_node.f == 0):
                    sub_node.g = g
                    sub_node.h = h
                    sub_node.f = f
                    sub_node.parent = node
                    myQueue.append(sub_node)
                else:
                    if(f < sub_node.f):
                        sub_node.g = g
                        sub_node.h = h
                        sub_node.f = f
                        sub_node.parent = node

        if(found):
            print("\n\ngoal is found ! \n\n")

    def SearchForPathGreedy(self):
        myQueue = PriorityQueue()
        myQueue.append(self.gridBoard.start_node)
        self.gridBoard.start_node.visited = True

        found = False

        while not myQueue.isEmpty():
            node = myQueue.pop()
            self.closeSet.append(node)
            if(node in self.gridBoard.goal_node):
                self.finalGoalNode = node
                found = True
                break

            neighboursList = self.expandNode(node, False)

            for sub_node in neighboursList:
                # calculate g for the current node

                g = 0

                # calculate h for the current node

                minValue = 100000000
                
                if len(self.gridBoard.goal_node) > 1:
                    # print('1')
                    if(sub_node.node_weight <= 1):
                        # print('2')
                        minValue = abs(self.gridBoard.goal_node[0].node_position[0] - sub_node.node_position[0])  + abs(
                        self.gridBoard.goal_node[0].node_position[1] - sub_node.node_position[1]) 
                    else:
                        # print('3')
                        for goalNode in range(len(self.gridBoard.goal_node)):
                            if(20*abs(self.gridBoard.goal_node[goalNode].node_position[0] - sub_node.node_position[0])+ 20*abs(
                            self.gridBoard.goal_node[goalNode].node_position[1] - sub_node.node_position[1]) < minValue):
                                minValue = 20*abs(self.gridBoard.goal_node[goalNode].node_position[0] - sub_node.node_position[0])  + 20*abs(
                                self.gridBoard.goal_node[goalNode].node_position[1] - sub_node.node_position[1])
                else:
                    if(sub_node.node_weight <= 1):
                        # print('4')
                        minValue = abs(self.gridBoard.goal_node[0].node_position[0] - sub_node.node_position[0]) + abs(
                                self.gridBoard.goal_node[0].node_position[1] - sub_node.node_position[1]) 
                    else:
                        # print('5')
                        for goalNode in range(len(self.gridBoard.goal_node)):
                            if(20*abs(self.gridBoard.goal_node[goalNode].node_position[0] - sub_node.node_position[0])+ 20*abs(
                            self.gridBoard.goal_node[goalNode].node_position[1] - sub_node.node_position[1]) < minValue):
                                minValue = 20*abs(self.gridBoard.goal_node[goalNode].node_position[0] - sub_node.node_position[0])  + 20*abs(
                                self.gridBoard.goal_node[goalNode].node_position[1] - sub_node.node_position[1])
                h = minValue

                # h = 4*abs(self.gridBoard.goal_node[0].node_position[0] - sub_node.node_position[0]) + 2 + 4*abs(
                #                 self.gridBoard.goal_node[0].node_position[1] - sub_node.node_position[1]) + 2
                # caluclate f for the current node

                f = g + h

                if(sub_node.f == 0):
                    sub_node.g = g
                    sub_node.h = h
                    sub_node.f = f
                    sub_node.parent = node
                    myQueue.append(sub_node)
                else:
                    if(f < sub_node.f):
                        sub_node.g = g
                        sub_node.h = h
                        sub_node.f = f
                        sub_node.parent = node

        if(found):
          
            print("\n\ngoal is found ! \n\n")
          

    def SearchForPathUCS(self):
        myQueue = PriorityQueue()
        myQueue.append(self.gridBoard.start_node)
        self.gridBoard.start_node.visited = True

        found = False

        while not myQueue.isEmpty():
            node = myQueue.pop()
            self.closeSet.append(node)
            if(node in self.gridBoard.goal_node):
                self.finalGoalNode = node
                found = True
                break

            neighboursList = self.expandNode(node, True)

            for sub_node in neighboursList:
                # calculate g for the current node

                g = sub_node.node_weight + node.g

                # calculate h for the current node

                h = 0

                # caluclate f for the current node

                f = g + h

                if(sub_node.f == 0):
                    sub_node.g = g
                    sub_node.h = h
                    sub_node.f = f
                    sub_node.parent = node
                    myQueue.append(sub_node)
                else:
                    if(f < sub_node.f):
                        sub_node.g = g
                        sub_node.h = h
                        sub_node.f = f
                        sub_node.parent = node

        if(found):
            print("\n\ngoal is found ! \n\n")
 

    def returnCloseSet(self):
        closeSetReturned = []
        for i in self.closeSet:
            closeSetReturned.append(i.node_position)
        return closeSetReturned

    def returnPath(self):
        pathList = []
        chainNode = self.finalGoalNode
        while(chainNode != None):
            pathList.append(chainNode.node_position)
            chainNode = chainNode.parent
        pathList.reverse()
        return pathList


# myBFS = BFS(front_end_array)
# myBFS.SearchForPathDFS()
# # myBFS.SearchForPath()
# # myBFS.SearchForPathDFS()
# # myBFS.SearchForPathASTAR()
# # myBFS.SearchForPathGreedy()
# # myBFS.SearchForPathUCS()
# # myBFS.SearchForPathDLS(3)

# myBFS.viewPath()
# print('\n\n')
# for i in myBFS.closeSet:
#     print(i.node_position, end=" , ")
# print(len(myBFS.closeSet))
