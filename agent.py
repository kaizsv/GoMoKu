from player import Player
import numpy as np

class Agent(Player):
    def __init__(self, player, learning, n):
        super(Agent, self).__init__(player, learning, n)

    def move(self, action_prob, legal_moves):
        if not self.is_learning:
            print action_prob
        #if self.player == 2:
            #action_prob = np.negative(action_prob)
        action_prob = 1.0 + action_prob
        action_prob = action_prob / np.sum(action_prob)

        if self.is_learning:
            return np.argmax(np.random.multinomial(1, action_prob[:]))
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
                return -1
            else:
                return -1
        elif winner == 2:
            if self.player == 1:
                return 1
            else:
                return 1
        else:
            if self.player == 1:
                return 0.2
            else:
                return -0.05
