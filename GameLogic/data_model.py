# connect four board
from game_exception import GameException


class Board():
    def __init__(self, rows=6, columns=7):
        self._rows = rows
        self._columns = columns
        self._board = [[0 for i in range(columns)] for j in range(rows)]
        self._current_player = 1

    @property
    def columns(self) -> int:
        return self._columns

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def board(self) -> list:
        return self._board

    def set_board_value(self, row, col, value):
        self._board[row][col] = value

    @property
    def current_player(self) -> int:
        return self._current_player

    @current_player.setter
    def current_player(self, player: int):
        self._current_player = player

    def clear_board(self):
        """
        Makes the board empty
        """
        self._board = [[0 for i in range(self._columns)] for j in range(self._rows)]
        self._current_player = 1

    def is_empty(self, row, col):
        """
        check if the cell at (row, col) is empty
        """
        return self._board[row][col] == 0

    def is_valid_move(self, col: int) -> bool:
        """
        check if the move to column col is valid
        """
        return self._board[0][col] == 0

    def is_board_full(self) -> bool:
        """
        check if the board is full
        """
        for i in range(self._columns):
            if self._board[0][i] == 0:
                return False
        return True

    def get_next_empty_row(self, col: int) -> int:
        """
        get the next empty row in column col
        """
        row = None
        for i in range(self._rows):
            if self.is_empty(i, col):
                row = i
        return row

    def make_move(self, col: int):
        """
        make a move to column col
        """
        if col < 0 or col >= self._columns:
            raise GameException('Invalid move!')
        if not self.is_valid_move(col):
            raise GameException("Invalid move!")

        row = self.get_next_empty_row(col)

        self._board[row][col] = self._current_player
        self._current_player = 1 if self._current_player == 2 else 2
        return row

    def check_diagonal_win(self, row, col):
        """
        check if there is a diagonal win by checking the 2 diagonals of the last move
        """
        player = self._board[row][col]

        # check the diagonal from top left to bottom right from the last move
        i = row - 1
        j = col - 1
        top_left_discs = 0
        # check the top left diagonal
        while i >= 0 and j >= 0:
            if self._board[i][j] == player:
                top_left_discs += 1
            elif self._board[i][j] != player:
                break
            i -= 1
            j -= 1
        # check the bottom right diagonal
        i = row + 1
        j = col + 1
        bottom_right_discs = 0
        while i < self._rows and j < self._columns:
            if self._board[i][j] == player:
                bottom_right_discs += 1
            elif self._board[i][j] != player:
                break
            i += 1
            j += 1
        # check if there are 3 discs in the diagonal
        if top_left_discs + bottom_right_discs == 3:
            return True

        # check the diagonal from top right to bottom left from the last move
        i = row - 1
        j = col + 1
        top_right_discs = 0
        # check the top right diagonal
        while i >= 0 and j < self._columns:
            if self._board[i][j] == player:
                top_right_discs += 1
            elif self._board[i][j] != player:
                break
            i -= 1
            j += 1
        # check the bottom left diagonal
        i = row + 1
        j = col - 1
        bottom_left_discs = 0
        # check the bottom left diagonal
        while i < self._rows and j >= 0:
            if self._board[i][j] == player:
                bottom_left_discs += 1
            elif self._board[i][j] != player:
                break
            i += 1
            j -= 1
        # check if there are 3 discs in the diagonal
        if top_right_discs + bottom_left_discs  == 3:
            return True

        return False

    def check_win(self, last_move: tuple) -> int:
        """
        check if there is a winner
        return 1 if player 1 wins
        2 if player 2 wins
        0 if no winner
        """
        row, col = last_move
        player = self._board[row][col]
        # check horizontally
        discs = 0
        for i_col in range(0, self._columns):
            if self._board[row][i_col] != player:
                discs = 0
            elif self._board[row][i_col] == player:
                discs += 1
                if discs == 4:
                    return player

        # check vertically
        discs = 0
        for i_row in range(0, self._rows):
            if self._board[i_row][col] != player:
                discs = 0
            elif self._board[i_row][col] == player:
                discs += 1
                if discs == 4:
                    return player

        # check diagonally
        if self.check_diagonal_win(row, col) is True:
            return player

        return 0
