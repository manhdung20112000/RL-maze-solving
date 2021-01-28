import tkinter as tk
import time

from numpy.lib.function_base import sinc
from run_agent import Training
from tkinter import Entry, Label, Tk, constants

class App(tk.Tk):
    def __init__(self, env_agent, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.env_agent = env_agent
        container = tk.Frame(self, width=500, height=300)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (InputFrame, ParameterFrame, TrainingFrame):
            page_name = F.__name__
            frame = F(master=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("InputFrame")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def updateMaze(self, sizeOfMaze):
        self.env_agent.updateMaze(sizeOfMaze)

    def updateLearningRate(self, lr):
        self.env_agent.setLearningRate(lr)

    def updateDiscountFactor(self, df):
        self.env_agent.setDiscountFactor(df)

    def updateStartDes(self, start, des):
        self.env_agent.setStartPosition(start)
        self.env_agent.setDestination(des)

    def getStart(self):
        return self.env_agent.start

    def getDestination(self):
        return self.env_agent.des

    def getMaze(self):
        return self.env_agent.maze

    def getObtacle(self):
        return self.env_agent.getObtacle()

    def printParameter(self):
        self.env_agent.printParameter()

    def getPath(self):
        return self.env_agent.getPath()


class InputFrame(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        self.next = False
        #input interface
        tk.Label(self, text="\nInput for RL model:\n----------------------\n\n").grid(row=0, sticky="w")

        #size of maze
        tk.Label(self, text="Size of maze:\n").grid(row=1, column=0, sticky='w')
        self.m = tk.Entry(self, width=3)
        self.n = tk.Entry(self, width=3)
        tk.Label(self, text="x").grid(row=1, column=2)
        self.m.grid(row=1, column=1)
        self.n.grid(row=1, column=3)

        tk.Label(self, text="Discount factor (γ)\n").grid(row=2, column=0, sticky='w')
        tk.Label(self, text="Learning rate (α)\n").grid(row=3, column=0, sticky='w')
        self.lr = tk.Entry(self, width=3)
        self.df = tk.Entry(self, width=3)
        self.lr.grid(row=2, column=1)
        self.df.grid(row=3, column=1)
            
        Label(self, text="\n----------------------\n").grid(sticky='s')
        btn = tk.Button(self, text="Next", command=self.submit)
        btn.grid(sticky='s')
        # end input interface

    #  discountFactor, learningRate
    def submit(self):
            try:
                a = int(self.m.get())
                b = int(self.n.get())
                lr = float(self.lr.get())
                df = float(self.df.get())
            except:
                print("Parameter(s) is/are not suitable")
            else: 
                status = True
                
                if (status):
                    self.controller.updateMaze((a, b))
                    self.controller.updateLearningRate(lr)
                    self.controller.updateDiscountFactor(df)

                    self.controller.printParameter()

                    self.controller.show_frame("ParameterFrame")
                
class ParameterFrame(tk.Frame):
    def __init__ (self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller

        tk.Label(self, text="\nSelect start location:").grid(row=0 , sticky="w")
        tk.Label(self, text="\nSelect destination:").grid(row=1 , sticky="w")
        self.start = tk.Entry(self, width=3)
        self.des = tk.Entry(self, width=3)
        self.start.grid(row=0, column=1)
        self.des.grid(row=1, column=1)

        Label(self, text="\n----------------------\n").grid(sticky='s')
        btn = tk.Button(self, text="Show map", command=self.updateMap)
        btn.grid(sticky='s')

    def updateMap(self):
        maze = self.controller.getMaze()
        hor, ver = maze.shape

        try:
            start = int(self.start.get())
            des = int(self.des.get())
            self.controller.updateStartDes(start, des)
            print(f"Start position: {start}")
            print(f"Destination: {des}")

            #gray15 for obtacle
            #gray80 for road
            count = 1
            for i in range(hor):
                for j in range(ver):
                    if (start == count):
                        frame = tk.Frame(self, relief=tk.RAISED, borderwidth=0.5, width=50, height=50, bg="gray30")
                    if (des == count):
                        frame = tk.Frame(self, relief=tk.RAISED, borderwidth=0.5, width=50, height=50, bg="green")
                    if (maze[i][j] >= 1):
                        frame = tk.Frame(self, relief=tk.RAISED, borderwidth=0.5, width=50, height=50, bg="gray15")
                    else: 
                        frame = tk.Frame(self, relief=tk.RAISED, borderwidth=0.5, width=50, height=50, bg="gray80")

                    frame.grid(row=i+5, column=j, sticky='w')
                    # label = Label(self, text=count)
                    # label.pack()
                    count+=1
            
            Label(self, text="\n\n").grid(sticky='s')
            btn = tk.Button(self, text="Train!", command=self.nextFrame)
            btn.grid(sticky='s')

        except:
            print("Start of Destination was not decleared!")

        print(self.controller.getObtacle())

    def nextFrame(self):
        self.controller.show_frame("TrainingFrame")


class TrainingFrame(tk.Frame):
    def __init__ (self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        tk.Label(self, text="\nResult after training:\n----------------------\n\n").grid(row=0, sticky="w")
        self.updateFrame()

    def updateFrame(self):
        path = self.controller.getPath()
        maze = self.controller.getMaze()
        hor, ver = maze.shape
        visited = []
        for element in path:
            visited.append[element]
            count = 1
            for i in range(hor):
                for j in range(ver):
                    if (count in visited):
                        frame = tk.Frame(self, relief=tk.RAISED, borderwidth=0.5, width=50, height=50, bg="gray30")
                    if (maze[i][j] >= 1):
                        frame = tk.Frame(self, relief=tk.RAISED, borderwidth=0.5, width=50, height=50, bg="gray15")
                    else: 
                        frame = tk.Frame(self, relief=tk.RAISED, borderwidth=0.5, width=50, height=50, bg="gray80")

                    frame.grid(row=i+5, column=j, sticky='w')
                    # label = Label(self, text=count)
                    # label.pack()
                    count+=1



if __name__ == "__main__":
    training_agent = Training()
    app = App(training_agent)
    app.mainloop()