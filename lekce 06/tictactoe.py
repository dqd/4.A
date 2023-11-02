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
        # horizontálně a vertikálně
        for i in range(Board.ROWS):
            rows = [self.get_cell(i, j) is player for j in range(Board.ROWS)]
            cols = [self.get_cell(j, i) is player for j in range(Board.ROWS)]

            if all(rows) or all(cols):
                return True

        # diagonálně
        diag1 = [self.get_cell(i, i) is player for i in range(Board.ROWS)]
        diag2 = [self.get_cell(i, -(i + 1)) is player for i in range(Board.ROWS)]

        if all(diag1) or all(diag2):
            return True

        return False

    def is_finished(self):
        for row in self._layout:
            for cell in row:
                if cell is Player.EMPTY:
                    return False

        return True


class Score(Enum):
    WIN = Board.ROWS**2 + 1
    LOSS = -(Board.ROWS**2 + 1)
    DRAW = 0
    MIN = -inf
    MAX = inf


class Solver:
    """
    Založeno na algoritmu minimax: https://en.wikipedia.org/wiki/Minimax
    """

    def __init__(self, player, opponent):
        self._player = player
        self._opponent = opponent

    def find_best_move(self, board):
        best_val = Score.MIN.value
        best_move = None, None

        for i in range(Board.ROWS):
            for j in range(Board.ROWS):
                if board.get_cell(i, j) is Player.EMPTY:
                    board.set_cell(i, j, self._player)
                    move_val = self._minimax(board, 0, False)
                    board.set_cell(i, j, Player.EMPTY)

                    if move_val > best_val:
                        best_move = i, j
                        best_val = move_val

        return best_move

    def _minimax(self, board, depth, is_maximizing):
        if board.is_winner(self._player):
            return Score.WIN.value - depth

        if board.is_winner(self._opponent):
            return Score.LOSS.value + depth

        if board.is_finished():
            return Score.DRAW.value

        if is_maximizing:
            score = Score.MIN.value
            player = self._player
            criterion = max
        else:
            score = Score.MAX.value
            player = self._opponent
            criterion = min

        for i in range(Board.ROWS):
            for j in range(Board.ROWS):
                if board.get_cell(i, j) is Player.EMPTY:
                    board.set_cell(i, j, player)
                    score = criterion(score, self._minimax(board, depth + 1, False))
                    board.set_cell(i, j, Player.EMPTY)

        return score


class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.player = Player.CROSS

    def change_player(self):
        if self.player is Player.CROSS:
            self.player = Player.NOUGHT
        else:
            self.player = Player.CROSS

    def make_move(self, row, col):
        if self.board.get_cell(row, col) is Player.EMPTY:
            self.board.set_cell(row, col, self.player)

            if self.board.is_winner(self.player):
                print(f"Hráč {self.player.value} vyhrál.")
                return True

            if self.board.is_finished():
                print("Je to remíza.")
                return True

            self.change_player()
        else:
            print("Zvolte jiné políčko, toto je obsazeno.")

        return False

    def read_input(self):
        try:
            cords = input(
                f"Hráči {self.player.value}, "
                "zadej řádek a sloupec (0-2) oddělený mezerou: "
            ).split()
            row = int(cords[0])
            col = int(cords[1])
            assert 0 <= row < Board.ROWS and 0 <= col < Board.ROWS
        except (ValueError, IndexError, AssertionError):
            row = None
            col = None

        return row, col

    def play(self):
        prompt = "Chcete si zahrát proti počítači? [ano/ne]: "
        use_solver = input(prompt).lower() in ("ano", "a")

        while True:
            self.board.display()

            if use_solver and self.player is Player.NOUGHT:
                solver = Solver(Player.NOUGHT, Player.CROSS)
                row, col = solver.find_best_move(self.board)
                print(f"Hráč {self.player.value} si vybral tah {row} {col}.")
            else:
                row, col = self.read_input()

            if row is None or col is None:
                print("Zadána špatná hodnota.")
            elif self.make_move(row, col):
                self.board.display()
                break


game = TicTacToe()
game.play()
