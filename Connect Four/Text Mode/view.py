color = ('\033[1;90m',  # Black
         '\033[1;91m',  # Red
         '\033[1;92m',  # Green
         '\033[1;93m',  # Yellow
         '\033[1;94m',  # Blue
         '\033[1;95m',  # Magenta
         '\033[1;96m',  # Cian
         '\033[1;97m',  # Grey
         '\033[m')      # Clean


def print_board(board):
    row = len(board)
    col = len(board[0])
    for i in range(0, row):
        print(f'{color[4]}', end='')
        print('-' * (col * 4 + 1), end='')
        print(f'{color[8]}')
        for j in range(0, col):
            if board[i][j] == 0:
                print(f'{color[4]}|{color[8]} 0 ', end='')
            if board[i][j] == 1:
                print(f'{color[4]}|{color[8]} {color[1]}1{color[8]} ', end='')
            if board[i][j] == 2:
                print(f'{color[4]}|{color[8]} {color[3]}2{color[8]} ', end='')
        print(f'{color[4]}|{color[8]}')
    print(f'{color[4]}', end='')
    print('-' * (col * 4 + 1))
    print(f'{color[8]} ', end='')
    for i in range(0, col):
        print(f' {i}  ', end='')
    print()


def prompt(plr):
    if plr == 1:
        c = 1
    else:
        c = 3
    print(f'Player {color[c]}{plr}{color[8]} select a row to play: ', end='')


def print_winner(player):
    if player == 1:
        c = 1
    else:
        c = 3
    print(f'{color[c]}')
    print('=' * 30)
    print(f'|{f"Player {player} won!!!":^28}|')
    print('=' * 30)
    print(f'{color[8]}')


def printError(msg):
    print(f'{color[5]}{msg}{color[8]}')
