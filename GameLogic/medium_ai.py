import math

from GameLogic.computer_functionalities_class import ComputerPlayer
import random
from GameLogic.data_model import Board


class MediumComputerPlayer(ComputerPlayer):
    '''
    Computer player that uses a series of strategies to choose a column to play.
    '''

    def __init__(self, board: Board, human_player: int, computer_player: int):
        super().__init__(board, human_player, computer_player)

    # check if it's worth playing in a column
    def is_winnable_move(self, col):
        col -= 1
        # get the next empty row
        row = self._board.get_next_empty_row(col)

        # if the computer doesn't have the possibility to make 4 discs in this row, there are other conditions to check
        if row < 3:
            # get the next disc in the column
            i = row + 1
            # check if the next disc is the same color as the computer's disc
            if self._board.board[i][col] == self._human_player or i >= self._board.rows - 1:
                return False
            # calculate the number of consecutive discs in the column that are the same color as the computer's disc
            while self._board.board[i][col] == self._computer_player and i < self._board.rows - 1:
                i += 1
            # if there are enough spaces to make 4 discs in a row, return True
            if row + 1 >= 4 - (i - (row + 1)):
                return True
            return False
        else:
            # can make 4 discs in a row
            return True

    def get_move(self):
        """
        Treat corner cases, then use a series of strategies to choose a column to play.
        """
        best_column = None
        max_score = -10000000

        # add the columns that are worth playing in to a list
        valid_columns = []
        for col in range(1, self._board.columns + 1):
            if self._board.is_valid_move(col - 1):
                valid_columns.append(col)
        # sort it so that the middle columns are checked first
        valid_columns.sort(key=lambda x: abs(x - math.ceil(self._board.columns / 2)))

        # treat corner cases, computer or human has 3 discs in a row
        for col in valid_columns:
            row = self._board.make_move(col - 1)
            # check if the move is a winning move for the computer and then reinitialize the board
            winning_move = self._board.check_win((row, col - 1))
            self._board.current_player = self._computer_player
            self._board.set_board_value(row, col - 1, 0)

            # if the move is a winning move, return the column
            if winning_move == self._computer_player:
                self._board.set_board_value(row, col - 1, 0)
                return str(col)

            # Check if the opponent can win in the next move.
            else:
                for i in range(1, self._board.columns + 1):
                    if not self._board.is_valid_move(i - 1):
                        continue
                    # if the opponent can win in the next move, block it
                    self._board.current_player = self._human_player
                    human_row = self._board.make_move(i - 1)
                    is_won = self._board.check_win((human_row, i - 1))
                    self._board.current_player = self._computer_player
                    self._board.set_board_value(human_row, i - 1, 0)
                    if is_won == self._human_player:
                        return str(i)

        # find the best column to play
        for col in valid_columns:
            row = self._board.get_next_empty_row(col - 1)
            score = 0
            # check if the move is a winnable move in the future
            if self.is_winnable_move(col):
                score += 100
            if score > max_score:
                max_score = score
                best_column = col

        # if there isn't a move that is worth playing, choose a random column
        if best_column is None:
            valid_moves = []
            for i in range(1, self._board.columns + 1):
                if self._board.is_valid_move(i - 1):
                    valid_moves.append(i)
            best_column = random.choice(valid_moves)
        self._board.current_player = self._computer_player

        return str(best_column)

    def __str__(self):
        return "You are playing against an above average computer player.\nIt is not that smart, but it is not that dumb either."
