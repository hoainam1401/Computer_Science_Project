import sys

import pygame

from checkers.constants import GREEN, HEIGHT, SQUARE_SIZE, WIDTH
from checkers.game import Game
from minimax.algorithm import minimax

FPS = 60

# Initialize Pygame and the font module
pygame.init()
pygame.font.init()

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_winner(text):
    font = pygame.font.SysFont("MonoLisaPlus", 100)
    text = font.render(text, 1, (255, 255, 0))
    pygame.draw.rect(
        WIN,
        (255, 0, 0),
        (
            WIDTH // 2 - text.get_width() // 2 - 10,
            HEIGHT // 2 - text.get_height() // 2 - 10,
            text.get_width() + 20,
            text.get_height() + 20,
        ),
        5,
    )
    WIN.blit(
        text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2)
    )
    pygame.display.update()
    pygame.time.delay(3000)


def main(mode, depth):
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if mode == "cpu" and game.turn == GREEN:
            value, new_board = minimax(game.get_board(), depth, GREEN, game)
            game.ai_move(new_board)

        winner = game.winner()
        if winner is not None:
            if winner == GREEN:
                draw_winner("GREEN WINS!")
            else:
                draw_winner("PURPLE WINS!")
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
    if len(sys.argv) < 2 or sys.argv[1] not in ["pvp", "cpu"]:
        print("Usage: main.py [pvp|cpu] [depth]")
    else:
        mode = sys.argv[1]
        depth = (
            int(sys.argv[2]) if len(sys.argv) == 3 else 1
        )  # Default depth is 1 if not provided
        main(mode, depth)
