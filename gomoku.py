from game import Game

def main():
    game = Game()
    player1, player2 = game.get_players()

    game.reinforcement_learning()

if __name__ == "__main__":
    main()
