import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def valid_move(board, move):
    if (0 <= move <= 6) and board[0][move] == 0:
        return True
    else:
        return False


def get_next_row(board, move):
    r = len(board)
    for i in range(r-1, -1, -1):
        if board[i][move] == 0:
            return i


def player_move(board, row, col, ply):
    board[row][col] = ply


def winning_move(board, row, col, piece):
    # Horizontal check
    for c in range(COLUMN_COUNT - 3):
        if board[row][c] == board[row][c+1] == board[row][c+2] == board[row][c+3] == piece:
            return True

    # Vertical check
    for r in range(ROW_COUNT - 3):
        if board[r][col] == board[r+1][col] == board[r+2][col] == board[r+3][col] == piece:
            return True

    # Diagonal Right Down check
    for i in range(0, 3):
        for j in range(0, 4):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == piece:
                return True

    # Diagonal Left Down
    for i in range(0, 3):
        for j in range(3, COLUMN_COUNT):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == piece:
                return True

    # Diagonal Right Up
    for i in range(3, ROW_COUNT):
        for j in range(0, 4):
            if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == piece:
                return True

    # Diagonal Left Up
    for i in range(3, ROW_COUNT):
        for j in range(3, COLUMN_COUNT):
            if board[i][j] == board[i-1][j-1] == board[i-2][j-2] == board[i-3][j-3] == piece:
                return True
    return False
