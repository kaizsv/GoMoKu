import numpy as np
from player import Player
from agent import Agent
from board import Board

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.symbol = {'Black':1, 'White':2}
        self.board = None
        self.game_condition()

    def game_condition(self):
        condition = input('\nChoose game mode\n1) single player\n2) learning\n>')
        if condition == 1:
            self.board = Board(n = 15, learning = False)
            first = input('\nYou want to play\n1) black\n2) white\n>')
            if first == 1:
                self.player1 = Player(1, False)
                self.player2 = Agent(2, False)
            elif first == 2:
                self.player1 = Agent(1, False)
                self.player2 = Player(2, False)
        elif condition == 2:
            self.board = Board(n = 15, learning = True)
            self.player1 = Agent(1, True)
            self.player2 = Agent(2, True)
            # start learning
            self.reinforcement_learning()
        else:
            # wrong input, choose again
            return self.game_condition()

    def get_players(self):
        return self.player1, self.player2

    def reinforcement_learning(self):
        iter = 1
        max_seq = self.board.size ** 2
        for j in range(iter):
            self.board.reset()
            start_state = self.board.fair_board()
            reward = 0
            states_seq = []
            action_probability_seq = []
            action_seq = []
            for i in range(max_seq):
                # even for player1, odd for player2
                if i & 1:
                    player = self.player2
                else:
                    player = self.player1

                state = self.board.get_current_state()
                player_state = player.convert_state(state)
                #action_prob = self.board.forward(player_state)
                #action = np.argmax(np.random.multinomial(1, action_prob[:,0]))
                #print action
