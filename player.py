import re

class Player(object):
    def __init__(self, player, learing):
        self.player = player
        self.color = 'Black' if player == 1 else 'White'
        self.is_learning = learing

    def __str__(self):
        return 'player' + self.player + ' is ' + self.color

    def move(self):
        row = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
        col = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
        while True:
            move = raw_input('Your move > ')
            x = move[:-1] # except last char
            y = move[-1]  # last char
            if x in col or y in row:
                x = int(x)
                y = ord(y) - ord('a')
                return x, y
            print 'Illegal move'
