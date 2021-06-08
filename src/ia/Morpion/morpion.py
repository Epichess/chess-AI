from enum import Enum
from typing import Tuple
from copy import deepcopy
from queue import PriorityQueue


class Outcome(Enum):
    NOT_OVER = 0
    CIRCLE = 1
    CROSS = 2
    DRAW = 3


class Symbol(Enum):
    EMPTY = 0
    CIRCLE = 1
    CROSS = 2

    def __str__(self):
        if self == Symbol.EMPTY:
            return ' '
        if self == Symbol.CIRCLE:
            return 'O'
        if self == Symbol.CROSS:
            return 'X'


symbol_to_outcome: dict[Symbol, Outcome] = {
    Symbol.CROSS: Outcome.CROSS,
    Symbol.CIRCLE: Outcome.CIRCLE
}

eval_outcome: dict[Outcome, float] = {
    Outcome.DRAW: 0,
    Outcome.NOT_OVER: 0,
    Outcome.CIRCLE: -float('inf'),
    Outcome.CROSS: float('inf')
}


class Move:
    lin: int
    col: int
    symbol: Symbol

    def __init__(self, lin: int, col: int, symbol: Symbol):
        self.lin = lin
        self.col = col
        self.symbol = symbol

    def __str__(self):
        string = ''
        string += ' move: '
        string += str(self.lin)
        string += ', '
        string += str(self.col)
        string += ' symbol: '
        string += str(self.symbol)
        return string

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return False


class Game:
    board: list[list[Symbol]]  # A board is a 3x3 matrix containing integers representing empty, cross and circle
    to_move: Symbol

    def get_outcome(self) -> Outcome:
        for lin in range(3):
            win: bool = self.board[lin][0] == self.board[lin][1] and self.board[lin][1] == self.board[lin][2]
            if win and not self.board[lin][0] == Symbol.EMPTY:
                return symbol_to_outcome[self.board[lin][0]]
        for col in range(3):
            win: bool = self.board[0][col] == self.board[1][col] and self.board[1][col] == self.board[2][col]
            if win and not self.board[0][col] == Symbol.EMPTY:
                return symbol_to_outcome[self.board[0][col]]
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            if not self.board[0][0] == Symbol.EMPTY:
                return symbol_to_outcome[self.board[0][0]]
        if self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            if not self.board[2][0] == Symbol.EMPTY:
                return symbol_to_outcome[self.board[2][0]]

        for lin in range(3):
            for col in range(3):
                if self.board[lin][col] == Symbol.EMPTY:
                    return Outcome.NOT_OVER
        return Outcome.DRAW

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return False

    def initialize_game(self):
        self.board = list()
        for lin in range(3):
            self.board.append(list())
            for col in range(3):
                self.board[lin].append(Symbol.EMPTY)

        self.to_move = Symbol.CROSS

    def make_move(self, move: Move) -> bool:
        if self.get_outcome() != Outcome.NOT_OVER:
            return False
        if self.to_move == move.symbol:
            if self.board[move.lin][move.col] == Symbol.EMPTY:
                self.board[move.lin][move.col] = move.symbol
                if self.to_move == Symbol.CIRCLE:
                    self.to_move = Symbol.CROSS
                else:
                    self.to_move = Symbol.CIRCLE
                return True
        return False

    def get_avail_moves(self) -> list[Move]:
        available_moves: list[Move] = list()
        for lin in range(3):
            for col in range(3):
                if self.board[lin][col] == Symbol.EMPTY:
                    available_moves.append(Move(lin, col, self.to_move))
        return available_moves

    def eval(self) -> float:
        return eval_outcome.get(self.get_outcome())

    def __str__(self):
        game_string = ''
        for lin in range(3):
            game_string += '|'
            for col in range(3):
                game_string += str(self.board[lin][col])
                game_string += '|'
            game_string += '\n'
        return game_string

    def get_best_move(self) -> Tuple[float, Move or None]:
        if self.get_outcome() != Outcome.NOT_OVER:
            return self.eval(), None
        evals = PriorityQueue()
        for move in self.get_avail_moves():
            child = deepcopy(self)
            # print(child)
            child.make_move(move)
            best_move = child.get_best_move()
            if self.to_move == Symbol.CROSS:
                best_move = (-best_move[0], move)
            else:
                best_move = (best_move[0], move)
            evals.put(best_move)
        best_move = evals.get()
        print(string_eval(best_move))
        while not evals.empty():
            print(string_eval(evals.get()))
        return best_move

    def get_best_move_corrected(self) -> Tuple[float, Move or None]:
        best_move = self.get_best_move()
        return -best_move[0], best_move[1]


def string_eval(eval: Tuple[float, Move]) -> str:
    string = ''
    string += 'Eval: '
    string += str(eval[0])
    string += ' '
    string += str(eval[1])
    return string