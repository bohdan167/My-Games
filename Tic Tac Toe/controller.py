from model import *
from view import *


def readInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            printError('Error! Enter with a valid Integer.')
            continue
        except KeyboardInterrupt:
            printError('User preferred not input this number.')
            return 0
        else:
            return num


def player(letter):
    if letter == 'X':
        # Player X
        if is_game_over() == 2:
            return 0
        move = readInt('Select a position for "X" (1-9 or 0 to EXIT)\n|-> ')
        while not (0 <= move <= 9):
            printError('Write a number between 0-9!')
            move = readInt('|-> ')
        if move == 0:
            return 0
        while not player_move(move, 'X'):
            printError('This position has already been played')
            move = readInt('|-> ')
            while not (0 <= move <= 9):
                printError('Write a number between 0-9!')
                move = readInt('|-> ')
            if move == 0:
                break
        return move
    elif letter == 'O':
        if is_game_over() == 1:
            return 0
        move = readInt('Select a position for "O" (1-9 or 0 to EXIT)\n|-> ')
        while not (0 <= move <= 9):
            printError('Write a number between 0-9!')
            move = readInt('|-> ')
        if move == 0:
            return 0
        while not player_move(move, 'O'):
            printError('This position has already been played')
            move = readInt('|-> ')
            while not (0 <= move <= 9):
                printError('Write a number between 0-9!')
                move = readInt('|-> ')
            if move == 0:
                break
        return move
    else:
        return 0


def single_player():
    while not is_board_full(board):
        move = player('X')
        if move == 0:
            break
        printBoard(board)

        # Computer
        if not is_board_full(board):
            if is_game_over() == 1:
                break
            m = computer_move()
            printMsg(f'Computer has played {m}')
            printBoard(board)
    # Game Over
    if is_game_over() == 0 and is_board_full(board):
        header('DRAW!!')
    if is_game_over() == 1:
        header('Congrats! Player WON!', 2)
    if is_game_over() == 2:
        header('Sorry.. Computer WON!', 2)


def multi_player():
    while not is_board_full(board):
        # Player X
        move = player('X')
        if move == 0:
            break
        printBoard(board)

        # Player O
        if not is_board_full(board):
            move = player('O')
            if move == 0:
                break
            printBoard(board)
    # Game Over
    if is_game_over() == 0 and is_board_full(board):
        header('DRAW!!')
    if is_game_over() == 1:
        header('GAME OVER! Player with "X" WON!', 2)
    if is_game_over() == 2:
        header('GAME OVER! Player with "O" WON!', 2)


def run():
    while True:
        header('TIC TAC TOE', 6)
        clear_board(board)

        printMenu(6)
        n = readInt('')
        while n != 1 and n != 2 and n != 0:
            printError('Type between 0 and 2, please')
            n = readInt('|-> ')

        if n == 1:
            printBoard(board)
            single_player()
        elif n == 2:
            printBoard(board)
            multi_player()
        else:
            break

        op = input('Play again? [Y/N]: ').upper()
        while not (op in 'YN'):
            printError('Please enter with Y or N.')
            op = input('Play again? [Y/N]: ').upper()
        if op in 'Nn':
            break
