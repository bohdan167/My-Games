board = [['X', 'X', 'X'],
         ['X', 'X', 'X'],
         ['X', 'X', 'X']]


def clear_board(b):
    for i in range(0, 3):
        for j in range(0, 3):
            b[i][j] = ' '


def is_board_full(b):
    res = True
    i = 0
    while res and i < 3:
        for j in range(0, 3):
            if b[i][j] != 'X' and b[i][j] != 'O':
                res = False
                break
        i += 1
    return res


def is_free_position(row, col):
    return True if board[row][col] == ' ' else False


def interpet_move(m):
    if m == 1:
        return 0, 0
    elif m == 2:
        return 0, 1
    elif m == 3:
        return 0, 2
    elif m == 4:
        return 1, 0
    elif m == 5:
        return 1, 1
    elif m == 6:
        return 1, 2
    elif m == 7:
        return 2, 0
    elif m == 8:
        return 2, 1
    elif m == 9:
        return 2, 2


def player_move(m, op):
    row, col = interpet_move(m)
    if is_free_position(row, col):
        board[row][col] = op
        return True
    else:
        return False


def select_random(lt):
    from random import randrange
    ln = len(lt)
    r = randrange(0, ln)
    return lt[r]


def best_move(b):
    possible_moves = []
    move = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if b[i][j] == ' ':
                possible_moves.append((i, j))

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = b[:]
            board_copy[0] = b[0][:]
            board_copy[1] = b[1][:]
            board_copy[2] = b[2][:]
            board_copy[i[0]][i[1]] = let
            if is_game_over(board_copy) == 1 or is_game_over(board_copy) == 2:
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            corners_open.append(i)

    if len(corners_open) > 0:
        move = select_random(corners_open)
        return move

    if (1, 1) in possible_moves:
        move = (1, 1)
        return move

    edges_open = []
    for i in possible_moves:
        if i in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move


def computer_move():
    move = best_move(board)
    board[move[0]][move[1]] = 'O'
    if move == (0, 0):
        return 1
    elif move == (0, 1):
        return 2
    elif move == (0, 2):
        return 3
    elif move == (1, 0):
        return 4
    elif move == (1, 1):
        return 5
    elif move == (1, 2):
        return 6
    elif move == (2, 0):
        return 7
    elif move == (2, 1):
        return 8
    elif move == (2, 2):
        return 9


def is_game_over_aux(op, b=None):
    if b is None:
        b = board
    if b[0].count(op) == 3:
        return True
    if b[1].count(op) == 3:
        return True
    if b[2].count(op) == 3:
        return True
    if b[0][0] == b[1][0] == b[2][0] == op:
        return True
    if b[0][1] == b[1][1] == b[2][1] == op:
        return True
    if b[0][2] == b[1][2] == b[2][2] == op:
        return True
    if b[0][0] == b[1][1] == b[2][2] == op:
        return True
    if b[0][2] == b[1][1] == b[2][0] == op:
        return True
    return False


def is_game_over(b=None):
    if b is None:
        b = board
    if is_game_over_aux('X', b):
        return 1
    elif is_game_over_aux('O', b):
        return 2
    else:
        return 0
