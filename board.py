import numpy as np
import sys

class Board:
    def __init__(self, n, r, learning):
        self.player1 = None
        self.player2 = None
        self.size = n
        self.env = np.zeros((self.size, self.size), dtype=np.int8)
        self.board_limit = 4
        self.renju = r
        self.legal_moves = [i for i in range(self.size ** 2)]
        self.symbol = {0:'-', 1:'X', 2:'O'}
        self.W = dict()
        self.w_file = 'rl_weight.npy'
        self.eta = 0.02
        self.is_learning = learning

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
        self.env = np.zeros((self.size, self.size), dtype=np.int8)
        self.legal_moves = [i for i in range(self.size ** 2)]

    def is_legal_move(self, action):
        return (action in self.legal_moves)

    def _decode_action(self, action):
        return int(action / self.size), (action % self.size)

    def get_state(self):
        return tuple(self.env.reshape(self.size ** 2))

    def set_action(self, action, symbol):
        pos_x, pos_y = self._decode_action(action)
        self.env[pos_x][pos_y] = symbol
        self.legal_moves.remove(action)

    def set_next_state(self, action, symbol):
        self.set_action(action, symbol)
        return self.get_state()

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

    def save_weights(self, n_games):
        path = str(n_games) + '_' + str(self.size) + 'x' + str(self.size) + '_' + self.w_file
        np.save(path, self.W)
        # ignore test file while board size is 15
        if self.size == 3:
            with open('for_test.txt', 'w') as f:
                for key, value in self.W.items():
                    f.write('%s: %s\n' % (key, value))

    def load_weights(self, n_games):
        path = str(n_games) + '_' + str(self.size) + 'x' + str(self.size) + '_' + self.w_file
        try:
            self.W = np.load(path).item()
            return True
        except IOError:
            print '\nPlease choose 2 to learn weight\n'
            return False

    def _reshape(self, s):
        return tuple(s.reshape(self.size**2))

    def in_W(self, state):
        temp = np.asarray(state)
        temp = temp.reshape((self.size, self.size))
        if state in self.W:
            return 1
        elif self._reshape(np.rot90(temp, 1)) in self.W:
            return 2
        elif self._reshape(np.rot90(temp, 2)) in self.W:
            return 3
        elif self._reshape(np.rot90(temp, 3)) in self.W:
            return 4
        elif self._reshape(np.flipud(temp)) in self.W:
            return 5
        elif self._reshape(np.fliplr(temp)) in self.W:
            return 6
        elif self._reshape(np.fliplr(np.flipud(temp.T))) in self.W:
            return 7
        elif self._reshape(temp.T) in self.W:
            return 8
        else:
            return 0

    def get_W(self, case, state):
        temp = np.asarray(state)
        temp = temp.reshape((self.size, self.size))
        if case == 1 or case == 0:
            return self.W[state]
        elif case == 2:
            prob = self.W[self._reshape(np.rot90(temp, 1))]
            prob = prob.reshape((self.size, self.size))
            return np.rot90(prob, 3).reshape(self.size**2)
        elif case == 3:
            prob = self.W[self._reshape(np.rot90(temp, 2))]
            prob = prob.reshape((self.size, self.size))
            return np.rot90(prob, 2).reshape(self.size**2)
        elif case == 4:
            prob = self.W[self._reshape(np.rot90(temp, 3))]
            prob = prob.reshape((self.size, self.size))
            return np.rot90(prob, 1).reshape(self.size**2)
        elif case == 5:
            prob = self.W[self._reshape(np.flipud(temp))]
            prob = prob.reshape((self.size, self.size))
            return np.flipud(prob).reshape(self.size**2)
        elif case == 6:
            prob = self.W[self._reshape(np.fliplr(temp))]
            prob = prob.reshape((self.size, self.size))
            return np.fliplr(prob).reshape(self.size**2)
        elif case == 7:
            prob = self.W[self._reshape(np.fliplr(np.flipud(temp.T)))]
            prob = prob.reshape((self.size, self.size))
            return np.fliplr(np.flipud(prob.T)).reshape(self.size**2)
        elif case == 8:
            prob = self.W[self._reshape(temp.T)]
            prob = prob.reshape((self.size, self.size))
            return prob.T.reshape(self.size**2)

    def get_reshape_state(self, case, state):
        temp = np.asarray(state)
        temp = temp.reshape((self.size, self.size))
        if case == 1 or case == 0:
            return state
        elif case == 2:
            return self._reshape(np.rot90(temp, 1))
        elif case == 3:
            return self._reshape(np.rot90(temp, 2))
        elif case == 4:
            return self._reshape(np.rot90(temp, 3))
        elif case == 5:
            return self._reshape(np.flipud(temp))
        elif case == 6:
            return self._reshape(np.fliplr(temp))
        elif case == 7:
            return self._reshape(np.fliplr(np.flipud(temp.T)))
        elif case == 8:
            return self._reshape(temp.T)

    def get_reshape_delta(self, case, delta):
        delta = delta.reshape((self.size, self.size))
        if case == 1 or case == 0:
            return delta.reshape(self.size**2)
        elif case == 2:
            return np.rot90(delta, 1).reshape(self.size**2)
        elif case == 3:
            return np.rot90(delta, 2).reshape(self.size**2)
        elif case == 4:
            return np.rot90(delta, 3).reshape(self.size**2)
        elif case == 5:
            return np.flipud(delta).reshape(self.size**2)
        elif case == 6:
            return np.fliplr(delta).reshape(self.size**2)
        elif case == 7:
            return np.fliplr(np.flipud(delta.T)).reshape(self.size**2)
        elif case == 8:
            return delta.T.reshape(self.size**2)

    def forward(self, state, legal_moves):
        case = self.in_W(state)
        if case == 0:
            if not self.is_learning:
                print '\nno state in policy network\n'
                sys.exit()
            self.W[state] = np.random.rand(self.size ** 2) / (2*self.size**2)
        a_in = self.get_W(case, state)
        a_in = np.exp(a_in)
        for i in range(len(a_in)):
            a_in[i] = 0 if i not in legal_moves else a_in[i]
        a_out = (a_in) / np.sum(a_in)
        return case, a_out

    def backward(self, reward, case, state, characteristic, d):
        if d:
            print 'b state ', state
            print 'b charac ', characteristic
            print 'b ', self.eta * reward * characteristic
        delta = self.eta * reward * characteristic
        state = self.get_reshape_state(case, state)
        self.W[state] += self.get_reshape_delta(case, delta)

