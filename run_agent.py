from Agent import QLearning
from Environment import Environment
import numpy as np

#maze 8x8
maze = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

startPostition = (1, 1)
exitPostition = (5, 9)

env = Environment(maze=maze, start=startPostition, end=exitPostition)
env.print_maze()
env.print_connect_maze()
#state labels
env.print_state_maze()

#q table 
agent = QLearning(state_maze=env.getStateMaze(), startPos=env.getStartPosition(), desPos=env.getDestination())
agent.print_q_table()
agent.print_reward_maze()
