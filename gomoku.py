from game import Game

def main():
    print '\nWelcome to GoMoKu\n'
    print '1) 15x15 board 5 in a row\n'
    print '2) 3x3 board, 3 in a row\n'
    print '3) 7x7 board, 5 in a row\n'
    b = input('>')
    while b != 1 and b != 2 and b != 3:
        b = input('>')
    if b == 1:
        s, r = 15, 5
    elif b == 2:
        s, r = 3, 3
    elif b == 3:
        s, r = 5, 5
    mode = 1
    game = Game(s, r)
    while mode:
        game.game_condition()
        mode = game.condition
        player1, player2 = game.get_players()


if __name__ == "__main__":
    main()
