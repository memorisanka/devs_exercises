# Zdefiniowany graczy
# Pusta plansza
# Walidacja czy pole jest zajete i czy podana przez usera liczba istnieje
# sprawdzanie czy plasnza jest pelna
# sprawdznaia czy x gracz wygral


ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O, BLANK = 'X', 'O', ' '


def get_blank_board() -> dict:

    board = dict.fromkeys(ALL_SPACES, BLANK)
    # for space in ALL_SPACES:
    #     board[space] = BLANK
    return board


def get_board_str(board):
    return '''
    {}|{}|{}
    {}|{}|{}
    {}|{}|{}
    '''.format(board['1'], board['2'], board['3'],
        board['4'], board['5'], board['6'],
        board['7'], board['8'], board['9'])


def is_valid_space(board, space):
    return space in ALL_SPACES and board[space] == BLANK


def is_board_full(board):
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False
    return True


def is_winner(board, player):
    b, p = board, player
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p)
    )


def update_board(board, space, mark):
    board[space] = mark


def main():
    print('''Witaj w grze "Kółko i Krzyżyk"''')
    game_board = get_blank_board()
    current_player, next_player = X, O
    while True:
        print(get_board_str(game_board))

        move = None
        while not is_valid_space(game_board, move):
            print('Gdzie wpisac {}? (1-9)'.format(current_player))
            move = input('> ')
        update_board(game_board, move, current_player)

        if is_winner(game_board, current_player):
            print(get_board_str(game_board))
            print(current_player, " WYGRAL GRE!")
            break
        elif is_board_full(game_board):
            print(get_board_str(game_board))
            print("Gra zakonczyla sie remisem")
            break
        current_player, next_player = next_player, current_player
    print("Dziekujemy za gre")


if __name__ == '__main__':
    main()
