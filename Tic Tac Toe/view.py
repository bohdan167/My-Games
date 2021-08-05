color = ('\033[1;90m',  # Black
         '\033[1;91m',  # Red
         '\033[1;92m',  # Green
         '\033[1;93m',  # Yellow
         '\033[1;94m',  # Blue
         '\033[1;95m',  # Magenta
         '\033[1;96m',  # Cian
         '\033[1;97m',  # Grey
         '\033[m')      # Clean


def header(msg, c=7):
    print(f'{color[c]}', end='')
    print('=' * 40)
    print(f'|{msg:^38}|')
    print('=' * 40, end='')
    print(f'{color[8]}')


def printBoard(board):
    for i in range(0, 2):
        print(f'\t\t\t   {board[i][0]} {color[3]}|{color[8]} {board[i][1]} {color[3]}|{color[8]} {board[i][2]}')
        print(f'\t\t\t  {color[3]}---|---|---{color[8]}')
    print(f'\t\t\t   {board[2][0]} {color[3]}|{color[8]} {board[2][1]} {color[3]}|{color[8]} {board[2][2]}')


def printError(msg):
    print(f'{color[1]}{msg}{color[8]}')


def printMsg(msg):
    print(msg)


def printMenu(c=7):
    print(f'''{color[c]}|                                      |
|{color[8]}{color[5]}{"1 - SinglePlayer":^38}{color[8]}{color[c]}|
|                                      |
|{color[8]}{color[5]}{"2 - MultiPlayer":^38}{color[8]}{color[c]}|
|                                      |
|{color[8]}{color[5]}{"0 - Exit":^38}{color[8]}{color[c]}|
|                                      |
========================================{color[8]}
|-> ''', end='')
