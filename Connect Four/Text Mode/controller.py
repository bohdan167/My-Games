from view import *
from model import *
# import os


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


def run():
    while True:
        # os.system('cls' if os.name == 'nt' else 'clear')
        board = create_board()
        print('\n' * 80)
        print_board(board)
        game_over = False
        turn = 0
        while not game_over:
            # Player 1
            if turn == 0:
                prompt(turn+1)
                move = readInt('')
                if valid_move(board, move):
                    row = get_next_row(board, move)
                    player_move(board, row, move, 1)
                    if winning_move(board, row, move, 1):
                        game_over = True
                        continue
                else:
                    turn += 1
                # os.system('cls' if os.name == 'nt' else 'clear')
                print('\n' * 80)
                print_board(board)
            # Player 2
            else:
                prompt(turn + 1)
                move = readInt('')
                if valid_move(board, move):
                    row = get_next_row(board, move)
                    player_move(board, row, move, 2)
                    if winning_move(board, row, move, 2):
                        game_over = True
                        continue
                else:
                    turn += 1
                # os.system('cls' if os.name == 'nt' else 'clear')
                print('\n' * 80)
                print_board(board)
            turn += 1
            turn %= 2
        # os.system('cls' if os.name == 'nt' else 'clear')
        print('\n' * 80)
        print_board(board)
        print_winner(turn+1)

        op = input('Play again? [Y/N]: ').upper()
        while not (op in 'YN'):
            printError('Please enter with Y or N.')
        if op == 'N':
            break
