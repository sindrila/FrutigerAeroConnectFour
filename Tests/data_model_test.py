import unittest

from GameLogic.data_model import Board
from UI.console_ui import ConsoleUI


class DataModelTest(unittest.TestCase):
    def setUp(self):
        self._board = Board()
        self._ui = ConsoleUI(self._board)

    def test_is_empty_and_make_move(self):
        self.assertTrue(self._board.is_empty(0, 0))
        self._board.make_move(0)
        self.assertFalse(self._board.is_empty(5, 0))

    def test_sample_boards(self):
        # make moves so that there is a horizontal win
        # 1 1 1 1 0 0 0
        for i in range(4):
            self._board.current_player = 1
            self._board.make_move(i)
        self.assertEqual(self._board.check_win((5, 3)), 1)
        self._board.clear_board()

        # 0 0 2 2 2 2 0
        for i in range(2, 6):
            self._board.current_player = 2
            self._board.make_move(i)
        self.assertEqual(self._board.check_win((5, 5)), 2)

        # 1 0 1 2 2 2 2
        self._board.current_player = 1
        self._board.make_move(0)
        self._board.current_player = 1
        self._board.make_move(2)
        for i in range(3, 7):
            self._board.current_player = 2
            self._board.make_move(i)
        self.assertEqual(self._board.check_win((5, 6)), 2)
        self._board.clear_board()

        # make moves so that there is a vertical win
        # 0 0 0 0 0 0 0
        # 1 0 0 0 0 0 0
        # 1 0 0 0 0 0 0
        # 1 0 0 0 0 0 0
        # 1 0 0 0 0 0 0

        for i in range(5):
            self._board.current_player = 1
            self._board.make_move(0)
        self.assertEqual(self._board.check_win((1, 0)), 1)
        self._board.clear_board()

        # 0 0 0 0 0 0 0
        # 0 2 0 0 0 0 0
        # 0 2 0 0 0 0 0
        # 0 2 0 0 0 0 0
        # 0 2 0 0 0 0 0

        for i in range(5):
            self._board.current_player = 2
            self._board.make_move(1)
        self.assertEqual(self._board.check_win((1, 1)), 2)
        self._board.clear_board()

        # 0 0 0 0 0 0 0
        # 0 0 0 1 2 0 0
        # 0 0 0 2 2 0 0
        # 0 0 0 2 2 0 0
        # 0 0 0 2 2 0 0
        for i in range(4):
            self._board.current_player = 2
            self._board.make_move(3)
        self._board.current_player = 1
        self._board.make_move(3)
        self.assertEqual(self._board.check_win((1, 3)), 0)

        for i in range(5):
            self._board.current_player = 2
            self._board.make_move(4)
        self.assertEqual(self._board.check_win((1, 4)), 2)
        self._board.clear_board()

        # make moves so that there is a diagonal win
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 1 0 0 0
        # 0 0 1 2 0 0 0
        # 0 1 2 2 0 0 0
        # 1 2 2 2 0 0 0
        for i in range(1, 4):
            for j in range(i):
                self._board.current_player = 2
                self._board.make_move(i)
            self._board.current_player = 1
            self._board.make_move(i - 1)
        self._board.current_player = 1
        self._board.make_move(3)
        self.assertEqual(self._board.check_win((2, 3)), 1)
        self._board.clear_board()

        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 2 0 0 0 0 0 0
        # 1 2 0 0 0 0 0
        # 1 1 2 0 0 0 0
        # 1 1 1 2 0 0 0

        for i in range(0, 4):
            for j in range(3 - i, 0, -1):
                self._board.current_player = 1
                self._board.make_move(i)
            self._board.current_player = 2
            self._board.make_move(i)
        self.assertEqual(self._board.check_win((5, 3)), 2)
        self._board.clear_board()

        for i in range(7):
            for j in range(6):
                self._board.current_player = 1
                self._board.make_move(i)
        self.assertTrue(self._board.is_board_full())
        self._board.clear_board()
