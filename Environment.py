import numpy as np

class Environment:
    def __init__(self, maze, start, end):
        super().__init__()
        self.maze = maze
        #label all the maze state automatically
        self.state_maze = self.init_state_maze()
        self.start = start
        self.end = end
        self.connect_maze = self.init_connect_maze()

    def init_state_maze(self):
        state_maze = np.empty((len(self.maze), len(self.maze[0])))
        state_maze.fill(np.nan)
        count = 1;
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] != 0: 
                    state_maze[i][j] = count
                    count+=1
        return state_maze

    def print_maze(self):
        print('\n-----------\nOrigin maze:')
        for col in self.maze:
            for row in col:
                print(row, end=' ')
            print()

    def print_state_maze(self):
        print('\n-----------\nState maze:')
        for col in self.state_maze:
            for row in col:
                if row >= 0:
                    print(int(row), end='\t')
                else:
                    print('x', end='\t')
            print()

    def init_connect_maze(self):
        connect = []
        n = int(np.nanmax(self.state_maze))

        iterRange = [x for x in range(n)]
        print(iterRange)
        for i in iterRange:
            iterRange.remove(i)
            for j in iterRange:
                if (i!=j and self.state_maze[i][j] >= 0):
                    if (self.check_connect_maze(n, i, j)): connect.append(i, j)

        return connect

    def check_connect_maze(self, maxsize, curr, des):
        row, col = np.where(self.state_maze == curr)

        startVertical = startHorizontal = -1
        endVertical = endHorizontal = 2
        if (row[0] == 0):
            startHorizontal = 0
        if (col[0] == 0):
            startVertical = 0
        if (row[0] == maxsize-1):
            startHorizontal = 1
        if (col[0] == maxsize-1):
            startVertical = 1
        verticalRange = range(startVertical, endVertical)
        horizontalRange = range(startHorizontal, endHorizontal)

        for i in verticalRange:
            for j in horizontalRange:
                if(i!=j and i!=-j and self.state_maze[row[0] + i][col[0] + j] == des):
                    return True
        return False

    def print_connect_maze(self):
        print(self.connect_maze)
    

