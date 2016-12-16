import numpy as np
import timeit
from player import Player
from agent import Agent
from board import Board

class Game:
    def __init__(self, size, renju):
        self.player1 = None
        self.player2 = None
        self.symbol = {'Black':1, 'White':2}
        self.size = size
        self.renju = renju
        self.board = None
        self.condition = 1
        self.rl_iter_games = 1
        self.game_condition()

    def game_condition(self):
        condition = input('\nChoose game mode\n1) single player\n2) learning\n3) exit\n>')
        if condition == 1:
            self.board = Board(n=self.size, r=self.renju, learning=False)
            first = input('\nYou want to play\n1) black\n2) white\n>')
            if first == 1:
                self.player1 = Player(1, False, self.board.size)
                self.player2 = Agent(2, False, self.board.size)
            elif first == 2:
                self.player1 = Agent(1, False, self.board.size)
                self.player2 = Player(2, False, self.board.size)
            # start game
            self.board.set_player(self.player1, self.player2)
            self.play_game()
        elif condition == 2:
            self.board = Board(n=self.size, r=self.renju, learning=True)
            self.player1 = Agent(1, True, self.board.size)
            self.player2 = Agent(2, True, self.board.size)
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
        max_seq = self.board.size ** 2
        start_time = timeit.default_timer()
        for j in range(self.rl_iter_games):
            self.board.reset()
            # black first move
            action = self.player1.fair_board_move(self.board)
            print 'first action ' + str(action)
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
                print 'state ', state
                # opponent's action
                opponent_state = opponent.convert_state(state)
                print 'opponent_state ', opponent_state
<<<<<<< HEAD
                action_prob = self.board.forward(opponent_state, opponent.player)
=======
                action_prob = self.board.forward(opponent_state)
>>>>>>> 771e76359eae08cf6460448e77aa2779b33624f7
                print 'action_prob ', action_prob
                action = opponent.move(action_prob)
                while not self.board.is_legal_move(action):
                    #print self.board.legal_move
                    action = opponent.move(action_prob)
                print 'action ', action
                # TODO: exploring
                state = np.copy(state)
                action_prob = np.copy(action_prob)
                action = np.copy(action)
                states_seq.append(state)
                action_probability_seq.append(action_prob)
                action_seq.append(action)
                if self.board.is_terminal(action, symbol=opponent.player):
                    # opponent win
                    print opponent.player, ' wins'
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
                print 'state ', state
                winner_state = winner.convert_state(state)
                print 'winner_state ', winner_state
                loser_state = loser.convert_state(state)
                print 'loser_stte ', loser_state
                # opponent's action
                a_out = action_probability_seq[idx]
                print 'a_out ', a_out
                a_gold_idx = action_seq[idx]
                a_gold = np.zeros(len(a_out))
                a_gold[a_gold_idx] = 1
                print 'a_gold ', a_gold
                if reward == 1:
                    self.board.backward(1, winner_state, a_gold - a_out)
                    self.board.backward(-1, loser_state, a_gold - a_out)
                elif reward == 0.5:
                    self.board.backward(0.5, winner_state, a_gold - a_out)
                    self.board.backward(0.5, loser_state, a_gold - a_out)
        end_time = timeit.default_timer()
        self.board.save_weights(self.rl_iter_games)
        print "Finish learning %d games in %d seconds" % (self.rl_iter_games, end_time-start_time)

    def play_game(self):

        # sub function for new game
        def new_game():
            c = input('\n1) New game?\n2) No, I want to leave\n>')
            if c != 1:
                print '\nBye Bye.\n'
                self.condition = 0

        # start to play game
        if not self.board.load_weights(self.rl_iter_games):
            return
        max_seq = self.board.size ** 2
        print(self.board)
        # black first move
        action = self.player1.fair_board_move(self.board)
        if action < 0:
            new_game()
            return
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
            print(self.board)
            # opponent's action
            opponent_state = opponent.convert_state(state)
            action_prob = self.board.forward(opponent_state, opponent.player)
            action = opponent.move(action_prob)
            while not self.board.is_legal_move(action) and not action < 0:
                if type(opponent) is Player:
                    print 'Illegal move'
                action = opponent.move(action_prob)
            if action < 0:
                new_game()
                return
            if self.board.is_terminal(action, symbol=opponent.player):
                # opponent win
                state = self.board.set_next_state(action, symbol=opponent.player)
                print(self.board)
                if type(opponent) is Player:
                    print '\nGood job, You win!!!\n'
                else:
                    print '\nToo bad, player ' + str(player.player) + ' beats you!!!\n'
                new_game()
                return
            elif self.board.is_full():
                print '\nTie game\n'
                new_game()
                return
