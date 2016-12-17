from player import Player
import numpy as np

class Agent(Player):
    def __init__(self, player, learning, n):
        super(Agent, self).__init__(player, learning, n)

    def move(self, action_prob):
        return np.argmax(np.random.multinomial(1, action_prob[:]))

    def fair_board_move(self, board, action_prob):
        # black can only move outside the limit line
        # of the board at the first move
        limit = board.board_limit
        size = board.size
        while True:
            #action = np.random.choice(board.legal_moves, 1)
            action = self.move(action_prob)
            if self.check_fair_board(action, size, limit):
                return action

    def get_reward(self, winner):
        if self.player == 1:
            if winner == 1:
                return 1
            else:
                return -1
        else:
            if winner == 2:
                return 1
            else:
                return -1
