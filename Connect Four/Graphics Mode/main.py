from model import *
import sys
import pygame

pygame.init()
myfont = pygame.font.SysFont("monospace", 75)

ROW_COUNT = 6
COLUMN_COUNT = 7

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

SQUARE_SIZE = 100
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
WIDTH = COLUMN_COUNT * SQUARE_SIZE
SIZE = (WIDTH, HEIGHT)
RADIUS = int(SQUARE_SIZE/2 - 5)


def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c*SQUARE_SIZE, r*SQUARE_SIZE+SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK,
                                   (int(c*SQUARE_SIZE+SQUARE_SIZE/2),
                                    int(r*SQUARE_SIZE+SQUARE_SIZE+SQUARE_SIZE/2)), RADIUS)
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED,
                                   (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                    int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW,
                                   (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                    int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
    pygame.display.update()


screen = pygame.display.set_mode(SIZE)


def main():
    board = create_board()
    game_over = False
    turn = 0
    draw_board(board)
    pygame.display.update()
    moves = 0
    while not game_over and (moves < COLUMN_COUNT*ROW_COUNT):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARE_SIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARE_SIZE / 2)), RADIUS)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
                # Player 1
                if turn == 0:
                    # prompt(turn + 1)
                    posx = event.pos[0]
                    move = posx//SQUARE_SIZE
                    if valid_move(board, move):
                        row = get_next_row(board, move)
                        player_move(board, row, move, 1)
                        if winning_move(board, row, move, 1):
                            label = myfont.render("Player 1 wins!!", True, RED)
                            screen.blit(label, (10, 10))
                            game_over = True
                # Player 2
                else:
                    # prompt(turn + 1)
                    posx = event.pos[0]
                    move = posx // SQUARE_SIZE
                    if valid_move(board, move):
                        row = get_next_row(board, move)
                        player_move(board, row, move, 2)
                        if winning_move(board, row, move, 2):
                            label = myfont.render("Player 2 wins!!", True, YELLOW)
                            screen.blit(label, (10, 10))
                            game_over = True
                draw_board(board)
                turn += 1
                turn %= 2
                moves += 1
                if game_over:
                    pygame.time.wait(3000)
                if moves == COLUMN_COUNT*ROW_COUNT and not game_over:
                    label = myfont.render("DRAW!!", True, WHITE)
                    screen.blit(label, (10, 10))
                    draw_board(board)
                    pygame.time.wait(3000)
    main()


if __name__ == '__main__':
    main()
