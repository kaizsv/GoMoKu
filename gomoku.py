from game import Game

def main():
    mode = 1
    while mode:
        game = Game()
        mode = game.condition
        player1, player2 = game.get_players()


if __name__ == "__main__":
    main()
