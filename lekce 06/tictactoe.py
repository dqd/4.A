from math import inf
from enum import Enum  # https://docs.python.org/3/library/enum.html

# Piškvorky 3×3


class Player(Enum):
    CROSS = "X"
    NOUGHT = "O"
    EMPTY = " "


class Board:
    ROWS = 3

    def __init__(self):
        self._layout = []

        for _ in range(Board.ROWS):
            # [" "] * 3 vytvoří [" ", " ", " "]
            self._layout.append([Player.EMPTY] * Board.ROWS)

    def display(self):
        first = True

        for row in self._layout:
            # horizontální čáru vypisujeme pouze mimo první iteraci
            if first:
                first = False
            else:
                # 2 znaky mezery + 1 znak hodnota + 1 znak vertikální čára
                print("-" * (Board.ROWS * 4 - 1))

            print("|".join([" {} ".format(cell.value) for cell in row]))

    def get_cell(self, row, col):
        return self._layout[row][col]

    def set_cell(self, row, col, value):
        self._layout[row][col] = value

    def is_winner(self, player):
        pass

    def is_draw(self):
        pass


board = Board()
board.set_cell(0, 0, Player.NOUGHT)
board.set_cell(0, 1, Player.CROSS)
board.display()


class Score(Enum):
    WIN = Board.ROWS**2 + 1
    LOSS = -(Board.ROWS**2 + 1)
    DRAW = 0
    MIN = -inf
    MAX = inf


class Solver:
    def __init__(self, player, opponent):
        pass

    def find_best_move(self, board):
        pass

    def _minimax(self, board, depth, is_maximizing):
        pass


class TicTacToe:
    def __init__(self):
        pass

    def change_player(self):
        pass

    def make_move(self, row, col):
        pass

    def read_input(self):
        pass

    def play(self):
        pass


# game = TicTacToe()
# game.play()
