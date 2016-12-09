from player import Player
from agent import Agent
from board import Board

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.symbol = {'Black':1, 'White':2}
        self.board = Board(n = 15)
        self.game_condition()

    def game_condition(self):
        condition = input('\nChoose game mode\n1) single play\n2) learning\n>')
        if condition == 1:
            first = input('\nYou want to play\n1) black\n2) white\n>')
            if first == 1:
                self.player1 = Player(1, False)
                self.player2 = Agent(2, False)
            elif first == 2:
                self.player1 = Agent(1, False)
                self.player2 = Player(2, False)
        elif condition == 2:
            self.player1 = Agent(1, True)
            self.player2 = Agent(2, True)

            self.reinforcement_learning()
        else:
            # wrong input, choose again
            return self.game_condition()


    def get_players(self):
        return self.player1, self.player2

    def reinforcement_learning(self):
        print(self.board)
