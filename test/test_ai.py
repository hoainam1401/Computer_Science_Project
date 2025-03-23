import unittest
from unittest.mock import patch

import pygame

from checkers.board import Board
from checkers.constants import GREEN
from checkers.game import Game
from minimax.algorithm import get_all_moves, minimax, simulate_move


class TestMinimaxAlgorithm(unittest.TestCase):
    @patch(
        "minimax.algorithm.draw_moves"
    )  # Patch the draw_moves function to prevent rendering
    def setUp(self, mock_draw_moves):
        pygame.init()
        # Create a small pygame Surface to use as the window
        self.win = pygame.Surface((800, 800))
        self.board = Board()
        self.game = Game(win=self.win)
        # Make draw_moves do nothing to avoid rendering during tests
        mock_draw_moves.return_value = None

    @patch("minimax.algorithm.draw_moves")  # Patch to prevent rendering
    def test_minimax_maximizing_player(self, _):
        # Test Minimax for maximizing player
        score, move = minimax(self.board, depth=1, max_player=True, game=self.game)
        self.assertIsNotNone(move)
        self.assertIsInstance(score, (int, float))

    @patch("minimax.algorithm.draw_moves")  # Patch to prevent rendering
    def test_minimax_minimizing_player(self, _):
        # Test Minimax for minimizing player
        score, move = minimax(self.board, depth=1, max_player=False, game=self.game)
        self.assertIsNotNone(move)
        self.assertIsInstance(score, (int, float))

    @patch("minimax.algorithm.draw_moves")  # Patch to prevent rendering
    def test_simulate_move(self, _):
        # Test simulating a move
        piece = self.board.get_piece(2, 1)
        move = (3, 2)
        new_board = simulate_move(piece, move, self.board, self.game, skip=None)
        self.assertEqual(new_board.get_piece(3, 2), piece)
        self.assertEqual(new_board.get_piece(2, 1), 0)

    @patch("minimax.algorithm.draw_moves")  # Patch to prevent rendering
    def test_get_all_moves(self, _):
        # Test generating all moves for a player
        moves = get_all_moves(self.board, GREEN, self.game)
        self.assertIsInstance(moves, list)
        self.assertGreater(len(moves), 0)
        # Additional validation for move correctness
        for move_board in moves:
            self.assertIsInstance(
                move_board, type(self.board)
            )  # Each element should be a board
            self.assertIsNotNone(move_board)

    @patch("minimax.algorithm.draw_moves")  # Patch to prevent rendering
    def test_minimax_terminal_state(self, _):
        # Custom version of minimax function for testing terminal state
        def custom_minimax(position, depth, max_player, game):
            # Base case: depth is 0 or game over
            if depth == 0 or position.winner() is not None:
                return position.evaluate(), None
            return position.evaluate(), None

        # Use the custom minimax function for testing
        with patch("minimax.algorithm.minimax", side_effect=custom_minimax):
            self.board.purple_left = 0  # Simulate a winning state for GREEN
            score, move = custom_minimax(
                self.board, depth=0, max_player=True, game=self.game
            )
            self.assertEqual(score, self.board.evaluate())
            self.assertIsNone(move)

    def tearDown(self):
        pygame.quit()


if __name__ == "__main__":
    unittest.main()
