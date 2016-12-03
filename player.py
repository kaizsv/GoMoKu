class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_RL = False

    def __str__(self):
        return self.name + " is " + self.color
