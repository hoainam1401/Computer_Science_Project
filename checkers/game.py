import pygame

from checkers.board import Board

from .constants import (BLUE, HEADER_BG, HEADER_HEIGHT, RED,
                        SELECTED_HIGHLIGHT, SQUARE_SIZE, TEXT_COLOR,
                        VALID_MOVE, WIDTH)


class Game:

    def __init__(self, win):
        self._init()
        self.win = win
        self.font_large = pygame.font.SysFont("Arial", 32, bold=True)
        self.font_small = pygame.font.SysFont("Arial", 20)

    def update(self):
        self.board.draw(self.win)
        self.draw_header()
        self.draw_selected_piece()
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def is_draw(self):
        # Check if current player has no valid moves
        if not self.board.has_valid_moves(self.turn):
            return True
        return False

    def reset(self):
        self._init()

    def draw_header(self):
        # Draw header background
        pygame.draw.rect(self.win, HEADER_BG, (0, 0, WIDTH, HEADER_HEIGHT))
        pygame.draw.line(
            self.win, TEXT_COLOR, (0, HEADER_HEIGHT - 2), (WIDTH, HEADER_HEIGHT - 2), 3
        )

        # Draw title
        title = self.font_large.render("CHECKERS", True, TEXT_COLOR)
        self.win.blit(title, (20, 15))

        # Draw current turn indicator
        turn_text = "Purple's Turn" if self.turn == RED else "Green's Turn"
        turn_color = RED if self.turn == RED else BLUE

        # Draw turn indicator circle
        pygame.draw.circle(self.win, turn_color, (WIDTH - 180, 35), 15)
        pygame.draw.circle(self.win, TEXT_COLOR, (WIDTH - 180, 35), 15, 2)

        turn_label = self.font_small.render(turn_text, True, TEXT_COLOR)
        self.win.blit(turn_label, (WIDTH - 155, 25))

        # Draw score
        score_text = f"Purple: {self.board.red_left}  Green: {self.board.blue_left}"
        score_label = self.font_small.render(score_text, True, TEXT_COLOR)
        self.win.blit(score_label, (20, 60))

    def draw_selected_piece(self):
        if self.selected:
            row, col = self.selected.row, self.selected.col
            x = col * SQUARE_SIZE
            y = row * SQUARE_SIZE + HEADER_HEIGHT

            # Draw animated selection border
            pygame.draw.rect(
                self.win, SELECTED_HIGHLIGHT, (x, y, SQUARE_SIZE, SQUARE_SIZE), 5
            )

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            # Draw larger, more visible valid move indicators
            center_x = col * SQUARE_SIZE + SQUARE_SIZE // 2
            center_y = row * SQUARE_SIZE + SQUARE_SIZE // 2 + HEADER_HEIGHT

            # Draw outer glow
            pygame.draw.circle(self.win, VALID_MOVE, (center_x, center_y), 20, 3)
            # Draw inner circle
            pygame.draw.circle(self.win, VALID_MOVE, (center_x, center_y), 10)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = BLUE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
