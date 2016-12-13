from game import Game

def main():
    print '\nWelcome to GoMoKu\n'
    print '1) 15x15 board 5 in a row\n'
    print '2) 3x3 board, 3 in a row\n'
    b = input('>')
    while b != 1 and b != 2:
        b = input('>')
    if b == 1:
        s, r = 15, 5
    else:
        s, r = 3, 3
    mode = 1
    while mode:
        game = Game(s, r)
        mode = game.condition
        player1, player2 = game.get_players()


if __name__ == "__main__":
    main()
