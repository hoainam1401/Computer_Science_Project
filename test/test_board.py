import unittest

from checkers.board import Board
from checkers.constants import BLUE, RED
from checkers.piece import Piece


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_setup(self):
        blue_pieces = sum(
            1
            for row in self.board.board
            for piece in row
            if piece != 0 and piece.color == BLUE
        )
        red_pieces = sum(
            1
            for row in self.board.board
            for piece in row
            if piece != 0 and piece.color == RED
        )
        self.assertEqual(blue_pieces, 12)
        self.assertEqual(red_pieces, 12)

    def test_move_piece(self):
        piece = self.board.get_piece(2, 1)
        self.board.move(piece, 3, 2)
        self.assertEqual(self.board.get_piece(3, 2), piece)
        self.assertEqual(self.board.get_piece(2, 1), 0)

    def test_make_king(self):
        piece = self.board.get_piece(2, 1)
        self.board.move(piece, 0, 1)
        self.assertTrue(piece.king)

    def test_remove_piece(self):
        piece = self.board.get_piece(2, 1)
        self.board.remove([piece])
        self.assertEqual(self.board.get_piece(2, 1), 0)
        if piece.color == RED:
            self.assertEqual(self.board.red_left, 11)
        elif piece.color == BLUE:
            self.assertEqual(self.board.blue_left, 11)

    def test_winner(self):
        self.board.red_left = 0
        self.assertEqual(self.board.winner(), BLUE)
        self.board.blue_left = 0
        self.board.red_left = 12  # Reset red pieces
        self.assertEqual(self.board.winner(), RED)

    def test_valid_moves(self):
        piece = self.board.get_piece(2, 1)
        valid_moves = self.board.get_valid_moves(piece)
        expected_moves = {(3, 0): [], (3, 2): []}
        self.assertEqual(valid_moves, expected_moves)

    def test_has_valid_moves(self):
        # Test that pieces have valid moves at the start
        self.assertTrue(self.board.has_valid_moves(RED))
        self.assertTrue(self.board.has_valid_moves(BLUE))

    def test_no_valid_moves_draw(self):
        # Create a board with no valid moves for RED
        self.board.board = [[0 for _ in range(8)] for _ in range(8)]
        self.board.red_left = 1
        self.board.blue_left = 1
        # Place red piece in corner with no moves
        self.board.board[0][0] = Piece(0, 0, RED)
        # Place blue piece blocking
        self.board.board[1][1] = Piece(1, 1, BLUE)
        
        # Red piece in corner has no valid moves
        self.assertFalse(self.board.has_valid_moves(RED))


if __name__ == "__main__":
    unittest.main()
