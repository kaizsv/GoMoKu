import re
import numpy as np

class Player(object):
    def __init__(self, player, learing, n):
        self.player = player
        self.color = 'Black' if player == 1 else 'White'
        self.is_learning = learing
        self.board_size = n

    def __str__(self):
        return self.__class__.__name__ + ' is ' + self.color

    def convert_state(self, state):
        # TODO: this might be wrong
        #return np.where(state==0, 0, np.where(state==1, 1, -1))
        opp_player = 2 if self.player == 1 else 1
        d_phase = { self.player:0, opp_player:1 }
        #d_phase = { 0:2, 1:0, 2:1 }
        c_state = np.zeros((2, self.board_size ** 2), dtype=np.int)
        for idx, s in enumerate(state):
            if s != 0:
                c_state[d_phase[s]][idx] = 1
        return c_state.reshape(2 * self.board_size ** 2)

    def move(self, action_prob = None, legal_moves = None):
        row = [chr(i) for i in range(ord('a'), ord('a') + self.board_size)]
        col = [str(i) for i in range(1, 1 + self.board_size)]
        while True:
            move = raw_input('Your move > ')
            if move == '-1':
                return -1
            x = move[:-1] # except last char
            y = move[-1]  # last char
            if x in col and y in row:
                x = int(x) - 1
                y = ord(y) - ord('a')
                return x * self.board_size + y
            print 'Illegal move'

    def fair_board_move(self, board):
        # black can only move outside the limit line
        # of the board at the first move.
        limit = board.board_limit
        size = board.size
        while True:
            # There is no learning mode in player
            # game mode
            action = self.move()
            if action < 0:
                return action
            if self.check_fair_board(action, size, limit):
                return action
            print 'fair board rule\nYou need to play outside the limit line ' + str(limit) + '\n'

    def check_fair_board(self, action, size, limit):
        if action < size * limit or \
            action > size ** 2 - 1 - size * limit or \
            action % size < limit or \
            action % size > size - 1 - limit:
            return True
        else:
            return False
