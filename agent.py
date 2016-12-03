from player import Player
import numpy as np

np.random.seed(1)

class Agent(Player):
    def __init__(self, name, color):
        Player.__init__(self, name, color)
        self.is_RL = True
