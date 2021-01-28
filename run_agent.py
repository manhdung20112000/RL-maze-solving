from Agent import QLearning
from Environment import Environment
import numpy as np

class Training():
        def __init__ (self):
                self.maze = []
                self.obtacle = []
                self.lr = 1
                self.df = 0.9
                self.start = 0
                self.des = 0

        def updateMaze(self, mazeSize):
                #generate random maze
                #TODO: for real training, comment this below seed config
                np.random.seed(42)
                self.mazeSize = mazeSize
                self.maze = np.random.randint(2 ,size=mazeSize)

        def setLearningRate(self, learningRate):
                self.lr = learningRate

        def setDiscountFactor(self, discountFactor):
                self.df = discountFactor

        def setStartPosition (self, start):
                self.start = start

        def setDestination (self, destination):
                self.des = destination

        def getObtacle(self):
                hor, ver = self.maze.shape
                self.stateLabel = np.zeros((hor, ver))
                
                count = 1
                for i in range(hor):
                        for j in range(ver):
                                self.stateLabel[i][j] = count
                                if (self.maze[i][j] >= 1): 
                                        #it mean [i][j] is obtacle
                                        self.obtacle.append(self.stateLabel[i][j])
                                count += 1
                return self.obtacle

        def getPath(self):
                #demo path
                return [1, 2, 7, 12, 17, 22, 23]

        def printParameter(self):
                print (f"Learning rate (α): {self.lr}")
                print (f"Discount factor (γ): {self.df}")
                print (f"Maze: \n{self.maze}")
                print (f"Start position: {self.start}")
                print (f"Destination: {self.des}")