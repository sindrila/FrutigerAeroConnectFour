import unittest

from GameLogic.dumb_computer import DumbComputerPlayer
from GameLogic.data_model import Board


class TestDumbComputer(unittest.TestCase):
    def test_valid_moves(self):
        board = Board()
        dumb_computer = DumbComputerPlayer(board, 1, 2)
        for i in range(1, 100):
            self.assertTrue(dumb_computer.get_move() in ['1', '2', '3', '4', '5', '6', '7'])