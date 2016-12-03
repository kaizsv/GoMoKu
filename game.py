from player import Player
from agent import Agent
from board import Board

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.board = Board()
        self.game_condition()

    def game_condition(self):
        self.player1 = Player('Player1', 'B')
        self.player2 = Agent('Player2', 'W')

    def get_players(self):
        return self.player1, self.player2

    def reinforcement_learning(self):
        if self.player1.is_RL:
            RL_player = self.player1
        elif self.player2.is_RL:
            RL_player = self.player2
        else:
            return
