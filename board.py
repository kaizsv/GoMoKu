import numpy as np

class Board:
    def __init__(self, n):
        self.size = n
        self.env = np.zeros((self.size, self.size))
        self.legal_moves = [i for i in range(1, self.size ** 2 + 1)]
        self.symbol = {0:'-', 1:'X', 2:'O'}
        self.model = dict()

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

