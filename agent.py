from player import Player
import numpy as np

class Agent(Player):
    def __init__(self, player, learning, n):
        super(Agent, self).__init__(player, learning, n)

    def move(self, action_prob):
        return np.argmax(np.random.multinomial(1, action_prob[:]))
