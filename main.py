# Playing tic-tac-toe PvP
BOARD_DIMENSION = 3

_board = [[None for __ in range(BOARD_DIMENSION)] for _ in range(BOARD_DIMENSION)]


def print_welcome():
    print('Now you playing tic-tac-toe Player-versus-Player.')
    print('You can enter cell coordinates in format: row column.')
    print('First player puts X, second - O.')


def print_board():
    print('Board:')
    for iRow in _board:
        for iCell in iRow:
            print(iCell if iCell else '_', end=' ')
        print()
    print('=====')
    return 0


def check_win_or_draw():
    pass


print_welcome()
print_board()
