import unittest
from unittest.mock import MagicMock

from minimax.algorithm import get_all_moves, minimax, simulate_move


class TestMinimaxAlgorithm(unittest.TestCase):
    def setUp(self):
        # Mocking the game and board objects
        self.mock_game = MagicMock()
        self.mock_board = MagicMock()
        self.mock_piece = MagicMock()

    def test_minimax_max_player(self):
        # Mock the board's winner and evaluate methods
        self.mock_board.winner.return_value = None
        self.mock_board.evaluate = MagicMock(return_value=10)
        # Mock the game's get_all_moves method
        self.mock_game.get_all_moves = MagicMock(return_value=[])

        # Call the minimax function
        result = minimax(self.mock_board, depth=0, max_player=True, game=self.mock_game)

        # Ensure evaluate is called
        self.mock_board.evaluate.assert_called_once()
        self.assertEqual(result[0], 10)
        self.assertIsNotNone(result[1])

    def test_minimax_min_player(self):
        # Mock the board's winner and evaluate methods
        self.mock_board.winner.return_value = None
        self.mock_board.evaluate = MagicMock(return_value=-10)
        # Mock the game's get_all_moves method
        self.mock_game.get_all_moves = MagicMock(return_value=[])

        # Call the minimax function
        result = minimax(
            self.mock_board, depth=0, max_player=False, game=self.mock_game
        )

        # Ensure evaluate is called
        self.mock_board.evaluate.assert_called_once()
        self.assertEqual(result[0], -10)
        self.assertIsNotNone(result[1])

    def test_simulate_move(self):
        # Mock the board's move and remove methods
        self.mock_board.move = MagicMock()
        self.mock_board.remove = MagicMock()

        # Call the simulate_move function
        result = simulate_move(
            self.mock_piece,
            (1, 1),
            self.mock_board,
            self.mock_game,
            skip=self.mock_piece,
        )

        # Ensure move and remove are called
        self.mock_board.move.assert_called_once_with(self.mock_piece, 1, 1)
        self.mock_board.remove.assert_called_once_with(self.mock_piece)
        self.assertEqual(result, self.mock_board)

    def test_get_all_moves(self):
        # Mock the board's methods
        self.mock_board.get_all_pieces.return_value = [self.mock_piece]
        self.mock_board.get_valid_moves.return_value = {(1, 1): self.mock_piece}
        self.mock_board.get_piece.return_value = self.mock_piece

        # Call the get_all_moves function
        result = get_all_moves(
            self.mock_board, color=(255, 255, 255), game=self.mock_game
        )

        # Ensure the result is as expected
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.mock_board)


if __name__ == "__main__":
    unittest.main()
