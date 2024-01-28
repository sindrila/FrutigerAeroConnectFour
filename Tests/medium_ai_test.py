import unittest

from GameLogic.medium_ai import MediumComputerPlayer
from GameLogic.data_model import Board


class TestMediumAI(unittest.TestCase):
    def test_valid_moves(self):
        board = Board()
        medium_ai = MediumComputerPlayer(board, 1, 2)
        for i in range(1, 100):
            self.assertTrue(medium_ai.get_move() in ['1', '2', '3', '4', '5', '6', '7'])

    # treat corner cases

    def test_corner_cases(self):
        board = Board()
        medium_ai = MediumComputerPlayer(board, 1, 2)
        # block user's win
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 1 1 1 0 0 0 0
        board.current_player = 2
        board.board[board.rows - 1][0] = 1
        board.board[board.rows - 1][1] = 1
        board.board[board.rows - 1][2] = 1
        col = medium_ai.get_move()
        self.assertEqual(col, '4')
        board.clear_board()

        # computer's win
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 1
        # 0 0 0 0 0 0 1
        # 2 2 2 0 0 0 1
        board.current_player = 2
        board.board[board.rows - 1][0] = 2
        board.board[board.rows - 1][1] = 2
        board.board[board.rows - 1][2] = 2
        board.board[board.rows - 1][6] = 1
        board.board[board.rows - 2][6] = 1
        board.board[board.rows - 3][6] = 1
        col = medium_ai.get_move()
        self.assertEqual(col, '4')
        board.clear_board()

        # check if computer has a preference for middle column
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        board.current_player = 2
        col = medium_ai.get_move()
        self.assertEqual(col, '4')

        # check if computer understands if a column is worth
        # 0 0 0 0 0 0 0
        # 0 0 0 0 0 0 0
        # 0 0 0 1 0 0 0
        # 0 0 0 2 0 0 0
        # 0 0 0 1 0 0 0
        board.current_player = 2
        board.board[board.rows - 1][3] = 1
        board.board[board.rows - 2][3] = 2
        board.board[board.rows - 3][3] = 1
        col = medium_ai.get_move()
        self.assertEqual(col, '3')