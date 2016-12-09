import numpy as np
import math

class Board:
    def __init__(self, n):
        self.size = n
        self.env = np.zeros((self.size, self.size))
        self.legal_moves = [i for i in range(self.size ** 2)]
        self.symbol = {0:'-', 1:'X', 2:'O'}

    def __str__(self):
        # return a string that print current environment
        space = '    '
        alphabet = ''
        for i in range(self.size):
            alphabet += u'%c ' % (ord('a') + i)
        s = space + alphabet + u'\n'
        s += space + u'= ' * self.size + u'\n'
        for i in range(self.size):
            s += u' %2d' % (i + 1)
            s += u'|'
            for j in range(self.size):
                s += '%c ' % self.symbol[self.env[i][j]]
            s += u'|\n'
        s += space + u'= ' * self.size
        return s

    def reset(self):
        self.env = np.zeros((self.size, self.size))
        self.legal_moves = [i for i in range(self.size ** 2)]

    def is_legal_move(self, action):
        return action in legal_moves

    def decode_action(self, action):
        return math.ceil(action / self.size), (action % self.size)

    def set_action(self, action, symbol):
        pos_x, pos_y = self.decode_action(action)
        self.env[pos_x][pos_y] = symbol
        self.legal_moves.remove(action)

    def fair_board(self):
        # black can olny move outer lines of the board
        # at the first move.
        limit_line = 2
        while True:
            first_move = np.random.choice(self.legal_moves, 1)
            if first_move < self.size * limit_line or \
                first_move > self.size**2 - 1 - self.size * limit_line or \
                first_move % self.size < limit_line or \
                first_move % self.size > self.size - 1 - limit_line:
                return first_move
