import pygame

WIDTH, HEIGHT = 800, 900
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
HEADER_HEIGHT = 100

# Enhanced color palette
# Board colors
LIGHT_SQUARE = (100, 115, 170)   # Light blue-purple
DARK_SQUARE = (75, 80, 105)      # Dark gray-purple
BOARD_BORDER = (50, 55, 75)      # Darker border

# Piece colors
RED = (210, 150, 255)            # Pink/Magenta
BLUE = (90, 255, 130)            # Green/Cyan
PIECE_OUTLINE = (255, 100, 200)  # Pink outline
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
