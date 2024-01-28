import random

from UI.GUI.gui import GUI
from GameLogic.data_model import Board

if __name__ == "__main__":
    board = Board()
    human = random.randint(1, 2)
    computer = 3 - human
    # ui = ConsoleUI(board)
    ui = GUI(board)
    board.current_player = human
    ui.start(human, computer)
