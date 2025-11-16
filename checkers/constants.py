import pygame

WIDTH, HEIGHT = 800, 900
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
HEADER_HEIGHT = 100

# Enhanced color palette
# Board colors
LIGHT_SQUARE = (240, 217, 181)  # Warm beige
DARK_SQUARE = (181, 136, 99)     # Rich brown
BOARD_BORDER = (101, 67, 33)     # Dark chocolate

# Piece colors
RED = (220, 53, 69)              # Bold red
BLUE = (13, 110, 253)            # Vibrant blue
PIECE_OUTLINE = (255, 255, 255)  # White outline
PIECE_SHADOW = (50, 50, 50, 100) # Semi-transparent shadow

# UI colors
VALID_MOVE = (46, 204, 113)      # Emerald green
SELECTED_HIGHLIGHT = (255, 193, 7)  # Amber
HEADER_BG = (52, 58, 64)         # Dark gray
TEXT_COLOR = (248, 249, 250)     # Off-white
WINNER_BG = (40, 167, 69)        # Success green

# Legacy colors for compatibility
GRAY = DARK_SQUARE
COMMENT = BOARD_BORDER
PINK = PIECE_OUTLINE
PURPLE = RED
GREEN = BLUE

CROWN = pygame.transform.scale(pygame.image.load("assets/crown.png"), (44, 25))
