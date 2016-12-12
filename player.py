import re
import numpy as np

class Player(object):
    def __init__(self, player, learing, n):
        self.player = player
        self.color = 'Black' if player == 1 else 'White'
        self.is_learning = learing
        self.board_size = n

    def __str__(self):
        return 'player' + self.player + ' is ' + self.color

    def convert_state(self, state):
        # replace white player state with
        # [0, 0, 1, 2, ...] => [0, 0, 2, 1, ...]
        if self.player == 1:
            return state
        else:
            return np.where(state==0, 0, np.where(state==1, 2, 1))

    def move(self, action_prob = None):
        row = [chr(i) for i in range(ord('a'), ord('a') + self.board_size)]
        col = [str(i) for i in range(1, 1 + self.board_size)]
        while True:
            move = raw_input('Your move > ')
            x = move[:-1] # except last char
            y = move[-1]  # last char
            if x in col and y in row:
                x = int(x) - 1
                y = ord(y) - ord('a')
                return x * self.board_size + y
            elif move == -1:
                # TODO: -1
                return -1
            print 'Illegal move'

    def fair_board_move(self, board):
        # TODO: implement w in learning
        # black can only move outside the limit line
        # of the board at the first move.
        limit = board.board_limit
        size = board.size
        while True:
            if self.is_learning:
                # learning mode
                action = np.random.choice(board.legal_moves, 1)
            else:
                # game mode
                if self.__class__ == Player:
                    # player move first
                    action = self.move()
                else:
                    # TODO
                    # agent move first
                    action = 0

            if action < size * limit or \
                action > size**2 - 1 - size * limit or \
                action % size < limit or \
                action % size > size - 1 - limit:
                return action
            if not self.is_learning:
                print 'fair board rule\nYou need to play outside the limit line ' + str(limit) + '\n'
