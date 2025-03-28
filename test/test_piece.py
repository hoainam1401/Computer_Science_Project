import unittest
from unittest.mock import Mock, patch

from checkers.constants import PINK  # Updated to use the correct module path
from checkers.constants import SQUARE_SIZE
from checkers.piece import Piece  # Updated to use the correct module path


class TestPiece(unittest.TestCase):
    def setUp(self):
        self.row = 2
        self.col = 3
        self.color = PINK
        self.piece = Piece(self.row, self.col, self.color)

    def test_initialization(self):
        self.assertEqual(self.piece.row, self.row)
        self.assertEqual(self.piece.col, self.col)
        self.assertEqual(self.piece.color, self.color)
        self.assertFalse(self.piece.king)
        self.assertEqual(self.piece.x, SQUARE_SIZE * self.col + SQUARE_SIZE // 2)
        self.assertEqual(self.piece.y, SQUARE_SIZE * self.row + SQUARE_SIZE // 2)

    def test_calc_pos(self):
        self.piece.row = 4
        self.piece.col = 5
        self.piece.calc_pos()
        self.assertEqual(self.piece.x, SQUARE_SIZE * 5 + SQUARE_SIZE // 2)
        self.assertEqual(self.piece.y, SQUARE_SIZE * 4 + SQUARE_SIZE // 2)

    def test_make_king(self):
        self.assertFalse(self.piece.king)
        self.piece.make_king()
        self.assertTrue(self.piece.king)

    @patch("checkers.piece.pygame")  # Updated to match the correct import path
    def test_draw(self, mock_pygame):
        mock_win = Mock()
        self.piece.draw(mock_win)
        self.assertTrue(mock_pygame.draw.circle.called)
        if self.piece.king:
            self.assertTrue(mock_win.blit.called)

    def test_move(self):
        new_row = 5
        new_col = 6
        self.piece.move(new_row, new_col)
        self.assertEqual(self.piece.row, new_row)
        self.assertEqual(self.piece.col, new_col)
        self.assertEqual(self.piece.x, SQUARE_SIZE * new_col + SQUARE_SIZE // 2)
        self.assertEqual(self.piece.y, SQUARE_SIZE * new_row + SQUARE_SIZE // 2)

    def test_repr(self):
        self.assertEqual(repr(self.piece), str(self.color))


if __name__ == "__main__":
    unittest.main()
