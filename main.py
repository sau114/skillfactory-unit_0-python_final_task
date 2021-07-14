# Playing tic-tac-toe PvP

BOARD_DIMENSION = 3
PLAYERS_TOTAL = 2

_board = [[0 for __ in range(BOARD_DIMENSION)] for _ in range(BOARD_DIMENSION)]


def print_welcome():
    print('Now you playing tic-tac-toe Player-versus-Player.')
    print('You can enter cell coordinates in format: row column.')
    print('First player puts X, second player puts O.')


def print_board():
    print('Board:')
    symbol_to_print = ''
    for i_row in range(BOARD_DIMENSION+1):
        for i_column in range(BOARD_DIMENSION+1):
            if i_column == 0:    # в 0-м столбце - легенда
                if i_row == 0:
                    symbol_to_print = ' '
                else:
                    symbol_to_print = str(i_row-1)
            elif i_row == 0:     # в 0-й строке - легенда
                symbol_to_print = str(i_column-1)
            else:               # значащее поле доски
                if _board[i_row-1][i_column-1] == 1:
                    symbol_to_print = 'X'
                elif _board[i_row-1][i_column-1] == 2:
                    symbol_to_print = 'O'
                else:
                    symbol_to_print = '-'
            print(symbol_to_print, end=' ')
        print()
    return 0


def ready_player(player_number):
    print('Player number ', player_number)
    while True:
        player_move = input('Player ' + str(player_number) + ' turn: ')
        move_row, move_column = list(map(int, player_move.split()))
        if (0 <= move_row < BOARD_DIMENSION) \
            and (0 <= move_column < BOARD_DIMENSION):
            if not _board[move_row][move_column]:
                _board[move_row][move_column] = player_number
                break
            else:
                print('Cell already occupied. Repeat your move.')
        else:
            print('Out of board. Repeat your move.')
    return 0


def player_won(player_number):
    # проверим строки
    for i_row in range(BOARD_DIMENSION):
        this_row = _board[i_row]
        if this_row.count(player_number) == BOARD_DIMENSION:
            print('Player filled row ' + str(i_row) + '.')
            return True

    # проверим столбцы
    for i_column in range(BOARD_DIMENSION):
        this_column = [_board[i_row][i_column] for i_row in range(BOARD_DIMENSION)]
        if this_column.count(player_number) == BOARD_DIMENSION:
            print('Player filled column ' + str(i_column) + '.')
            return True

    # проверим главную диагональ
    this_diagonal = [_board[i][i] for i in range(BOARD_DIMENSION)]
    if this_diagonal.count(player_number) == BOARD_DIMENSION:
        print('Player filled main diagonal.')
        return True

    # проверим побочную диагональ
    this_diagonal = [_board[BOARD_DIMENSION - i - 1][i] for i in range(BOARD_DIMENSION)]
    if this_diagonal.count(player_number) == BOARD_DIMENSION:
        print('Player filled side diagonal.')
        return True

    return False


def move_possible():
    # есть пустое поле для хода
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
