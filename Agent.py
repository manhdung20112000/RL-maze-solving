from color import *
import sys
import numpy as np
import pandas as pd

class QLearning:
    def __init__(self, state_maze, startPos, desPos, learning_rate=1, discount_reward=0.5):
        super().__init__()

        #default init
        self.episode = 0

        self.lr = learning_rate
        self.dr = discount_reward
        self.start = startPos
        self.q_table = self.init_q_table(state_maze=state_maze, desPos=desPos)
        self.reward = self.init_reward_maze(state_maze=state_maze, desPos=desPos)

    def init_q_table(self, state_maze, desPos):
        #create nxn matrix with n is number of posible state
        n = int(np.nanmax(state_maze))
        q_table = np.empty((n, n))
        q_table.fill(np.nan)
        for i in range(n):
            for j in range(n):
                if (i!=j and self.check_q_value(desPos, state_maze, i+1, j+1)):
                    q_table[i][j] = 0
        return q_table

    def init_reward_maze(self, state_maze, desPos):
        n = len(self.q_table)
        desValue = state_maze[desPos[0]][desPos[1]]
        reward_maze = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if (self.q_table[i][j] >= 0):
                    if (j == desValue):
                        #TODO: wrong
                        print(i, j)
                        reward_maze[i][j] = 10

                    else:
                        reward_maze[i][j] = -1
        return reward_maze

    def check_q_value(self, desPos, maze, a, b):
        rows, cols = np.where(maze == b)
        if ((rows[0], cols[0]) == desPos): 
            iterrange = range(-1, 1)
        else: iterrange = range(-1, 2)

        for i in iterrange:
            for j in iterrange:
                if (i!=j and i!=-j and maze[rows[0]+i][cols[0]+j] == a):
                    return True
        return False
    
    def max_current_state(self, currentState):
        max = 0
        for num in self.q_table[currentState]:
            if num > max:
                max = num
        return max

    def update_q_value(self, start, end):
        current = self.q_table[start-1][end-1]
        #TODO: reward array?
        #update q-value:
        self.q_table[start-1][end-1] = current*(1-self.lr) + self.lr*(self.reward[start-1][end-1] + self.dr*self.max_current_state(start-1))

    def print_reward_maze(self):
        print('\n-------------\nReward maze:')
        for col in self.reward:
            for row in col:
                if (row > 0):
                    sys.stdout.write(CYAN)
                    print(int(row), end='\t'.expandtabs(2))
                elif (row < 0):
                    sys.stdout.write(RED)
                    print(int(row), end='\t'.expandtabs(2))
                else:
                    sys.stdout.write(RESET)
                    print(int(row), end=" ")
            print()
        sys.stdout.write(RESET)

    def print_q_table(self):
        print('\n-------------\nQ-table:')
        count = 0
        for col in self.q_table:
            for row in col:
                if (row >= 0):
                    sys.stdout.write(GREEN)
                    print(int(row), end='\t'.expandtabs(2))
                else:
                    sys.stdout.write(RESET)
                    print('x', end='\t'.expandtabs(2))
            print(count)
            count+=1
        sys.stdout.write(RESET)

