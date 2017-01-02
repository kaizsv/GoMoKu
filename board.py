import numpy as np
import pickle
from neural.network import NeuralNetwork

f_name = '.obj'

class Board:
    def __init__(self, n, r, learning):
        self.player1 = None
        self.player2 = None
        self.size = n
        self.env = np.zeros((self.size, self.size), dtype=np.int)
        self.board_limit = 4
        self.renju = r
        self.legal_moves = [i for i in range(self.size ** 2)]
        self.symbol = {0:'-', 1:'X', 2:'O'}
        self.nn = NeuralNetwork(self.size)

    def set_player(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

    def __str__(self):
        # return a string that print current environment
        space = '    '
        alphabet = ''
        s = u'\n\n'
        for i in range(self.size):
            alphabet += u'%c ' % (ord('a') + i)
        s += space + alphabet + u'\n'
        s += space + u'= ' * self.size + u'\n'
        for i in range(self.size):
            s += u' %2d' % (i + 1)
            s += u'|'
            for j in range(self.size):
                s += '%c ' % self.symbol[self.env[i][j]]
            s += u'|'
            if i == 1:
                s += space
                s += self.player1.__str__()
            elif i == 2:
                s += space
                s += self.player2.__str__()
            elif i == 4:
                s += space
                s += u'-1: new game'
            s += u'\n'
        s += space + u'= ' * self.size
        return s

    def reset(self):
        self.env = np.zeros((self.size, self.size), dtype=np.int)
        self.legal_moves = [i for i in range(self.size ** 2)]

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
        return self.env.reshape(self.size**2).copy()

    def is_full(self):
        # if there are only one action left in legal_moves
        # then it must be fulled
        return len(self.legal_moves) == 1

    def is_terminal(self, action, symbol):
        x, y = self._decode_action(action)

        def check_boundary(x, y):
            return x >= 0 and x < self.size and y >= 0 and y < self.size

        count = 1
        # check horizontal
        for i in range(1, self.renju):
            if check_boundary(x, y+i) and self.env[x][y+i] == symbol:
                count += 1
            else:
               break
        for j in range(1, self.renju):
            if check_boundary(x, y-j) and self.env[x][y-j] == symbol:
                count += 1
            else:
                break
        if count >= self.renju:
            return True

        count = 1
        # check vertical
        for i in range(1, self.renju):
            if check_boundary(x+i, y) and self.env[x+i][y] == symbol:
                count += 1
            else:
                break
        for j in range(1, self.renju):
            if check_boundary(x-j, y) and self.env[x-j][y] == symbol:
                count += 1
            else:
                break
        if count >= self.renju:
            return True

        count = 1
        # check splash
        for i in range(1, self.renju):
            if check_boundary(x-i, y-i) and self.env[x-i][y-i] == symbol:
                count += 1
            else:
               break
        for j in range(1, self.renju):
            if check_boundary(x+j, y+j) and self.env[x+j][y+j] == symbol:
                count += 1
            else:
                break
        if count >= self.renju:
            return True

        count = 1
        # check back splash
        for i in range(1, self.renju):
            if check_boundary(x-i, y+i) and self.env[x-i][y+i] == symbol:
                count += 1
            else:
                break
        for j in range(1, self.renju):
            if check_boundary(x+j, y-j) and self.env[x+j][y-j] == symbol:
                count += 1
            else:
                break
        if count >= self.renju:
            return True

        return False

    def save_nn(self, n_games):
        path = str(self.size) + 'x' + str(self.size) + '_' + str(n_games) + 'games_' + self.nn.__str__() + f_name
        with open(path, 'wb') as save:
            pickle.dump(self.nn, save)

    def load_nn(self, n_games):
        path = str(self.size) + 'x' + str(self.size) + '_' + str(n_games) + 'games_' + self.nn.__str__() + f_name
        try:
            with open(path, 'rb') as load:
                self.nn = pickle.load(load)
            return True
        except IOError:
            print '\nPlease choose 2 to learn weight\n'
            return False

    def forward(self, state, symbol):
        self.nn.set_input(state)
        self.nn.update()
        out = self.nn.get_output()
        if symbol == 2:
            out = np.negative(out)
        out = np.exp(out)
        for i in range(len(out)):
            out[i] = 0 if i not in self.legal_moves else out[i]
        return (out / np.sum(out)).copy()

    def backward(self, reward, state, action_gold):
        self.nn.set_input(state)
        self.nn.update()
        self.nn.backpropagation(reward, action_gold)
