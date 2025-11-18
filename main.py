import sys

import pygame

from checkers.constants import BLUE, HEIGHT, RED, SQUARE_SIZE, WIDTH, HEADER_HEIGHT
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
    row = (y - HEADER_HEIGHT) // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_winner(text):
    # Create semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 0))
    WIN.blit(overlay, (0, 0))
    
    # Winner text styling
    font_large = pygame.font.SysFont("Arial", 80, bold=True)
    font_small = pygame.font.SysFont("Arial", 30)
    
    # Determine winner color
    if "Purple" in text:
        winner_color = RED
    elif "Green" in text:
        winner_color = BLUE
    else:
        # Draw - use gray color
        winner_color = (150, 150, 150)
    
    # Draw winner box
    box_width = 600
    box_height = 300
    box_x = WIDTH // 2 - box_width // 2
    box_y = HEIGHT // 2 - box_height // 2
    
    # Draw shadow
    pygame.draw.rect(WIN, (0, 0, 0), (box_x + 5, box_y + 5, box_width, box_height), border_radius=20)
    
    # Draw main box
    pygame.draw.rect(WIN, (255, 255, 255), (box_x, box_y, box_width, box_height), border_radius=20)
    pygame.draw.rect(WIN, winner_color, (box_x, box_y, box_width, box_height), 8, border_radius=20)
    
    # Draw confetti-like decorations
    for i in range(20):
        color = RED if i % 2 == 0 else BLUE
        conf_x = box_x + 50 + (i * 25)
        conf_y = box_y + 20
        pygame.draw.circle(WIN, color, (conf_x, conf_y), 5)
        pygame.draw.circle(WIN, color, (conf_x, box_y + box_height - 20), 5)
    
    # Draw crown icon (larger)
    crown_text = "👑"
    try:
        crown_font = pygame.font.SysFont("Arial", 60)
        crown_surface = crown_font.render(crown_text, True, (255, 215, 0))
        WIN.blit(crown_surface, (WIDTH // 2 - 30, box_y + 50))
    except:
        pass
    
    # Draw winner text
    winner_text = font_large.render(text, True, winner_color)
    WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, box_y + 130))
    
    # Draw subtitle
    subtitle = font_small.render("Game Over", True, (100, 100, 100))
    WIN.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, box_y + 220))
    
    pygame.display.update()
    pygame.time.delay(5000)


def main(mode, depth):
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if mode == "cpu" and game.turn == BLUE:
            value, new_board = minimax(game.get_board(), depth, BLUE, game)
            game.ai_move(new_board)

        # Check for draw first
        if game.is_draw():
            draw_winner("Draw!")
            run = False
        
        # Then check for winner
        winner = game.winner()
        if winner is not None:
            if winner == BLUE:
                draw_winner("Green Wins!")
            else:
                draw_winner("Purple Wins!")
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # Only process clicks on the board (not header)
                if row >= 0 and row < 8:
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
