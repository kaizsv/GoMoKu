from player import Player
import numpy as np

class Agent(Player):
    def __init__(self, player, learning):
        super(Agent, self).__init__(player, learning)

    def convert_state(self, state):
        # replace white player state with
        # [0, 0, 1, 2, ...] => [0, 0, 2, 1, ...]
        if self.player == 1:
            return state
        else:
            rep = {1:2, 2:1}
            return [i if i==0 else rep[i] for i in state]
