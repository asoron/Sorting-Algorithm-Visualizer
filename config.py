import numpy as np

class StateManager:
    def __init__(self):
        self.arrayLength = 50
        self.screenWidth = 750
        self.screenHeight = 750

        self.background = "#303030"
        self.baseColor = "#12c2e9"
        self.swapColor = "#e94560"
        self.sortedColor = "#12E948"

        self.unsorted_array = []
        self.scaledData = []
        self.canvases = []

    def create_new_array(self,canvas):
        self.unsorted_array = [np.random.randint(1, self.arrayLength + 1) for _ in range(self.arrayLength)]
        self.scaledData = [(value) / (max(self.unsorted_array) + 1) * self.screenHeight for value in self.unsorted_array]
        canvas.delete("all")
        self.canvases = []

state = StateManager()