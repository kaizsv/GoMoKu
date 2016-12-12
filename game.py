import numpy as np
import timeit
from player import Player
from agent import Agent
from board import Board

class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.symbol = {'Black':1, 'White':2}
        self.board = None
        self.condition = 1
        self.game_condition()

    def game_condition(self):
        condition = input('\nChoose game mode\n1) single player\n2) learning\n3) exit\n>')
        if condition == 1:
            self.board = Board(n = 15, learning = False)
            first = input('\nYou want to play\n1) black\n2) white\n>')
            if first == 1:
                self.player1 = Player(1, False)
                self.player2 = Agent(2, False)
            elif first == 2:
                self.player1 = Agent(1, False)
                self.player2 = Player(2, False)
            # start game
            self.play_game()
        elif condition == 2:
            self.board = Board(n = 15, learning = True)
            self.player1 = Agent(1, True)
            self.player2 = Agent(2, True)
            # start learning
            self.reinforcement_learning()
        elif condition == 3:
            self.condition = 0
        else:
            # wrong input, choose again
            return self.game_condition()

    def get_players(self):
        return self.player1, self.player2

    def reinforcement_learning(self):
        iteration = 10
        max_seq = self.board.size ** 2
        start_time = timeit.default_timer()
        for j in range(iteration):
            self.board.reset()
            action = self.board.fair_board()
            reward = 0
            winner = None
            loser = None
            states_seq = []
            action_probability_seq = []
            action_seq = []
            for i in range(max_seq - 1):
                # even for player1 (black), odd for player2 (white)
                if i & 1:
                    player = self.player2
                    opponent = self.player1
                else:
                    player = self.player1
                    opponent = self.player2

                # current state
                state = self.board.set_next_state(action, symbol=player.player)
                # opponent's action
                player_state = opponent.convert_state(state)
                action_prob = self.board.forward(player_state)
                action = np.argmax(np.random.multinomial(1, action_prob[:]))
                # TODO: this might be stark
                while not self.board.is_legal_move(action):
                    action = np.argmax(np.random.multinomial(1, action_prob[:]))
                # TODO: exploring
                states_seq.append(state)
                action_probability_seq.append(action_prob)
                action_seq.append(action)
                if self.board.is_terminal(action, symbol=opponent.player):
                    # opponent win
                    reward = 1
                    winner = opponent
                    loser = player
                    break
                elif self.board.is_full():
                    # tie game
                    reward = 0.5
                    winner = player
                    loser = opponent
                    break

            if reward == 0:
                continue
            for idx in range(len(states_seq)):
                # TODO: check this implement is correct
                # current state
                state = states_seq[idx]
                winner_state = winner.convert_state(state)
                loser_state = loser.convert_state(state)
                # opponet's action
                a_out = action_probability_seq[idx]
                a_gold_idx = action_seq[idx]
                a_gold = np.zeros(len(a_out))
                # even for black and odd for white
                # while this is opponent's action, must exchange turn
                a_gold[a_gold_idx] = 1 if (idx & 1) else 2
                if reward == 1:
                    self.board.backward(1, winner_state, a_gold - a_out)
                    self.board.backward(-1, loser_state, a_gold - a_out)
                elif reward == 0.5:
                    self.board.backward(0.5, winner_state, a_gold - a_out)
                    self.board.backward(0.5, loser_state, a_gold - a_out)
        end_time = timeit.default_timer()
        self.board.save_weights()
        print "Finish learning %d games in %d seconds" % (iteration, end_time-start_time)

    def play_game(self):
        if not self.board.load_weights():
            return
        iteration = self.board.size ** 2
        print self.board
        # first move
        x, y = self.player1.move()
        pass
