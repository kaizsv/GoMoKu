class Player(object):
    def __init__(self, player, learing):
        self.player = player
        self.color = 'Black' if player == 1 else 'White'
        self.is_learning = learing

    def __str__(self):
        return 'player' + self.player + ' is ' + self.color

