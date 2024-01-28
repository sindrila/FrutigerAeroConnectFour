from GameLogic.data_model import Board
class ComputerPlayer:
    '''
    Class that represents a computer player
    '''
    def __init__(self, board: Board, human_player: int, computer_player: int):
        self._board = board
        self._human_player = human_player
        self._computer_player = computer_player

