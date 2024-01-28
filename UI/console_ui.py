import texttable as tt

from GameLogic.dumb_computer import DumbComputerPlayer
from GameLogic.medium_ai import MediumComputerPlayer
from GameLogic.data_model import Board
from game_exception import GameException, GameOver


class ConsoleUI:
    def __init__(self, board: Board):
        self._board = board

    def print_table(self):
        table = tt.Texttable()
        table.add_row([' '] + [str(i + 1) for i in range(self._board.columns)])
        for i in range(self._board.rows):
            row = [str(i + 1)]
            for j in range(self._board.columns):
                if self._board.board[i][j] == 0:
                    row.append(' ')
                elif self._board.board[i][j] == 1:
                    row.append('X')
                else:
                    row.append('O')
            table.add_row(row)
        print(table.draw())

    def start(self, human: int, computer: int):
        print("Welcome to Connect 4!")
        difficulty = input("Choose difficulty:\n1 - Dumb\n2 - Above average\n> ")
        computer_engine = None
        if difficulty == "1":
            computer_engine = DumbComputerPlayer(self._board, human, computer)
        elif difficulty == "2":
            computer_engine = MediumComputerPlayer(self._board, human, computer)
        else:
            print("Since you don't want to choose one, you will play against the dumb one.")
        print(computer_engine)
        if human == 1:
            print("You go first.")
        else:
            print("Computer goes first.")
        print("---------------------------------")

        while self._board.is_board_full() is False:
            if self._board.current_player == human:
                self.print_table()
                col = input("Your stupid move, enter a column: ")
            else:
                print("My turn...")
                col = computer_engine.get_move()
                print("I choose column " + col)

            if isinstance(col, str) is False or col.isdigit() is False:
                print(GameException("Invalid move."))
                continue
            else:
                col = int(col) - 1
                try:
                    row = self._board.make_move(col)
                    win = self._board.check_win((row, col))
                    if win:
                        self.print_table()
                        if win == human:
                            print(GameOver("Congratulations, human, you won..."))
                        if win == computer:
                            print(GameOver("I won you fool!"))
                        break
                except GameException:
                    print(GameException("Invalid move."))
                    continue
        if self._board.is_board_full():
            self.print_table()
            print("It's a tie!")
