import sys

import pygame
from checkers.constants import GREEN, HEIGHT, SQUARE_SIZE, WIDTH
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main(mode):
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if mode == "cpu" and game.turn == GREEN:
            value, new_board = minimax(game.get_board(), 4, GREEN, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            print("GREEN WINS!" if game.winner() == GREEN else "PURPLE WINS!")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    pygame.quit()


if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ["pvp", "cpu"]:
        print("Usage: main.py [pvp|cpu]")
    else:
        main(sys.argv[1])
