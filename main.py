# Playing tic-tac-toe PvP

BOARD_DIMENSION = 3
PLAYERS_TOTAL = 2

_board = [[0 for __ in range(BOARD_DIMENSION)] for _ in range(BOARD_DIMENSION)]


def print_welcome():
    print('Now you playing tic-tac-toe Player-versus-Player.')
    print('You can enter cell coordinates in format: row column.')
    print('First player puts X, second player puts O.')


def print_board():
    print()
    symbol_to_print = ''
    for i_row in range(BOARD_DIMENSION+1):
        for i_column in range(BOARD_DIMENSION+1):
            if i_column == 0:    # legend in 0 row
                if i_row == 0:
                    symbol_to_print = ' '
                else:
                    symbol_to_print = str(i_row-1)
            elif i_row == 0:     # legen in 0 column
                symbol_to_print = str(i_column-1)
            else:
                if _board[i_row-1][i_column-1] == 1:
                    symbol_to_print = 'X'
                elif _board[i_row-1][i_column-1] == 2:
                    symbol_to_print = 'O'
                else:
                    symbol_to_print = '-'
            print(symbol_to_print, end=' ')
        print()
    print()
    return 0


def ready_player(player_number):
    print('Player number ', player_number)
    while True:
        player_move = input('Player ' + str(player_number) + ' turn: ')

        player_move = player_move.split()
        if len(player_move) != 2:
            print('Must be 2 values. Repeat your move.')
            continue

        move_row, move_column = player_move
        if not (move_row.isdigit() and move_column.isdigit()):
            print('Must be numbers. Repeat your move.')
            continue

        move_row, move_column = list(map(int, player_move))
        if move_row < 0 or move_row >= BOARD_DIMENSION \
            or move_column < 0 or move_column >= BOARD_DIMENSION:
            print('Out of board. Repeat your move.')
            continue

        if _board[move_row][move_column]:
            print('Cell already occupied. Repeat your move.')
            continue

        _board[move_row][move_column] = player_number
        break
    return 0


def player_won(player_number):
    # check rows
    for i_row in range(BOARD_DIMENSION):
        this_row = _board[i_row]
        if this_row.count(player_number) == BOARD_DIMENSION:
            print('Player filled row ' + str(i_row) + '.')
            return True

    # check columns
    for i_column in range(BOARD_DIMENSION):
        this_column = [_board[i_row][i_column] for i_row in range(BOARD_DIMENSION)]
        if this_column.count(player_number) == BOARD_DIMENSION:
            print('Player filled column ' + str(i_column) + '.')
            return True

    # check main diagonal
    this_diagonal = [_board[i][i] for i in range(BOARD_DIMENSION)]
    if this_diagonal.count(player_number) == BOARD_DIMENSION:
        print('Player filled main diagonal.')
        return True

    # check side diagonal
    this_diagonal = [_board[BOARD_DIMENSION - i - 1][i] for i in range(BOARD_DIMENSION)]
    if this_diagonal.count(player_number) == BOARD_DIMENSION:
        print('Player filled side diagonal.')
        return True

    return False


def move_possible():
    # try to find free cell
    for i_row in range(BOARD_DIMENSION):
        for i_column in range(BOARD_DIMENSION):
            if not _board[i_row][i_column]:
                return True
    return False


print_welcome()
print_board()

move_count = 0
while True:
    player_number = move_count % PLAYERS_TOTAL + 1
    ready_player(player_number)
    print_board()
    if player_won(player_number):
        print('Player ' + str(player_number) + ' won.')
        break
    elif not move_possible():
        print('Game ended in a draw.')
        break
    else:
        move_count += 1

print('Bye.')
