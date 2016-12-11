import numpy as np

class Board:
    def __init__(self, n, learning):
        self.size = n
        self.env = np.zeros((self.size, self.size), dtype=np.int)
        self.legal_moves = [i for i in range(self.size ** 2)]
        self.symbol = {0:'-', 1:'X', 2:'O'}
        self.W = None
        self.eta = 0.02
        self._init_weights(learning)

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
        self.env = np.zeros((self.size, self.size), dtype=np.int)
        self.legal_moves = [i for i in range(self.size ** 2)]

    def _init_weights(self, learning):
        # TODO: if not learning, load weight
        if learning:
            self.W = np.random.rand(self.size**2, self.size**2) / (2 * self.size**2)

    def is_legal_move(self, action):
        return (action in self.legal_moves)

    def _decode_action(self, action):
        return int(action / self.size), (action % self.size)

    def set_action(self, action, symbol):
        pos_x, pos_y = self._decode_action(action)
        self.env[pos_x][pos_y] = symbol
        self.legal_moves.remove(action)

    def set_next_state(self, action, symbol):
        self.set_action(action, symbol)
        return self.env.reshape(self.size**2)

    def fair_board(self):
        # TODO: implement by W
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

    def is_full(self):
        return not self.legal_moves

    def is_terminal(self, action, symbol):
        x, y = self._decode_action(action)

        def check_boundary(x, y):
            return x >= 0 and x < self.size and y >= 0 and y < self.size

        count = 1
        # check horizontal
        for i in range(1, 5):
            if check_boundary(x, y+i) and self.env[x][y+i] == symbol:
                count += 1
            else:
               break
        for j in range(1, 5):
            if check_boundary(x, y-j) and self.env[x][y-j] == symbol:
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        # check vertical
        for i in range(1, 5):
            if check_boundary(x+i, y) and self.env[x+i][y] == symbol:
                count += 1
            else:
                break
        for j in range(1, 5):
            if check_boundary(x-j, y) and self.env[x-j][y] == symbol:
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        # check splash
        for i in range(1, 5):
            if check_boundary(x-i, y-i) and self.env[x-i][y-i] == symbol:
                count += 1
            else:
               break
        for j in range(1, 5):
            if check_boundary(x+j, y+j) and self.env[x+j][y+j] == symbol:
                count += 1
            else:
                break
        if count >= 5:
            return True

        count = 1
        # check back splash
        for i in range(1, 5):
            if check_boundary(x-i, y+i) and self.env[x-i][y+i] == symbol:
                count += 1
            else:
                break
        for j in range(1, 5):
            if check_boundary(x+j, y-j) and self.env[x+j][y-j] == symbol:
                count += 1
            else:
                break
        if count >= 5:
            return True

        return False

    def forward(self, state):
        a_in = np.dot(state, self.W)
        a_out = (np.exp(a_in) / np.sum(np.exp(a_in)))
        return a_out

    def backward(self, reward, state, characteristic):
        state = state.reshape(len(state), 1)
        characteristic = characteristic.reshape(len(characteristic), 1)
        self.W += self.eta * reward * np.dot(state, characteristic.T)
