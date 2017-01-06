from player import Player
from neural.network import NeuralNetwork
import numpy as np

class Agent(Player):
    def __init__(self, player, learning, n):
        super(Agent, self).__init__(player, learning, n)
        self.nn = NeuralNetwork(n, phase=3)

    def move(self, action_prob, legal_moves):
        if not self.is_learning:
            print action_prob
        #if self.player == 2:
            #action_prob = np.negative(action_prob)
        '''action_prob = np.exp(action_prob)
        for i in range(len(action_prob)):
            action_prob[i] = 0 if i not in legal_moves else action_prob[i]
        action_prob = action_prob / np.sum(action_prob)
        '''
        if self.is_learning:
            max_out = 4
            for i in range(len(action_prob)):
                if action_prob[i] > action_prob[max_out]:
                    max_out = i
            return max_out
            #return np.argmax(np.random.multinomial(1, action_prob[:]))
            #return np.argmax(action_prob)
        else:
            for i in range(len(action_prob)):
                action_prob[i] = 0 if i not in legal_moves else action_prob[i]
            print action_prob
            return np.argmax(action_prob)

    def fair_board_move(self, board):
        # TODO: implement fair board weights
        # black can only move outside the limit line
        # of the board at the first move
        limit = board.board_limit
        size = board.size
        while True:
            action = np.random.choice(board.legal_moves, 1)
            if self.check_fair_board(action, size, limit):
                return action

    def get_reward(self, winner):
        if winner == 1:
            if self.player == 1:
                return 1
            else:
                return -1
        elif winner == 2:
            if self.player == 1:
                return -1
            else:
                return 1
        else:
            if self.player == 1:
                return 0.5
            else:
                return 0.5

    def forward(self, state):
        self.nn.set_input(state)
        self.nn.update()
        print self.nn.get_output()
        return self.nn.get_output()

    def backward(self, state, action_gold):
        self.nn.set_input(state)
        self.nn.update()
        self.nn.backpropagation(action_gold)
