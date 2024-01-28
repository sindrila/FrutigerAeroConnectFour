from GameLogic.computer_functionalities_class import ComputerPlayer
from GameLogic.data_model import Board


class DumbComputerPlayer(ComputerPlayer):
    """
    A dumb computer player that chooses a random valid column to play.
    """

    def __init__(self, board: Board, human_player: int, computer_player: int):
        super().__init__(board, human_player, computer_player)

    def get_move(self):
        """
        Find a random valid column to play.
        """
        import random
        valid_moves = []
        for i in range(1, self._board.columns + 1):
            if self._board.is_valid_move(i - 1):
                valid_moves.append(i)
        choice = random.choice(valid_moves)
        return str(choice)

    def __str__(self):
        return "You are playing against a dumb computer player.\nIf you are really bored, you can try to let it win."
