import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# RGB colors
RED = (255, 85, 85)
GRAY = (68, 71, 90)
COMMENT = (98, 114, 164)
PINK = (255, 121, 198)
PURPLE = (189, 147, 249)
GREEN = (80, 250, 123)

CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (44, 25))
