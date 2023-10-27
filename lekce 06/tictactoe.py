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
        pass

    def display(self):
        pass

    def get_cell(self, row, col):
        pass

    def set_cell(self, row, col, value):
        pass

    def is_winner(self, player):
        pass

    def is_draw(self):
        pass


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


game = TicTacToe()
game.play()
