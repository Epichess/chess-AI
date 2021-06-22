import numpy as np
import morpion
from enum import Enum
from typing import Union
from queue import PriorityQueue


class Symbol(Enum):
    CROSS = np.bool_(True)
    CIRCLE = np.bool_(False)


class Result(Enum):
    DRAW = np.short(0)
    CROSS = np.short(1)
    CIRCLE = np.short(2)
    NOT_OVER = np.short(3)


winning_pos: np.array = np.array([
    np.uintc(0b111000000),
    np.uintc(0b000111000),
    np.uintc(0b000000111),
    np.uintc(0b100100100),
    np.uintc(0b010010010),
    np.uintc(0b001001001),
    np.uintc(0b100010001),
    np.uintc(0b001010100)
])

winning_pos_set = set(winning_pos)

evaluation: dict[Result, float] = {
    Result.CIRCLE: float('inf'),
    Result.CROSS: -float('inf'),
    Result.DRAW: 0
}

class Move:
    destination: np.uintc
    symbol: Symbol

    def __init__(self, destination: np.uintc, symbol: Symbol):
        self.destination = destination
        self.symbol = symbol

    def to_mask(self):
        return np.left_shift(np.uintc(0b1), self.destination)

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return False


class BitBoard:
    circle: np.uintc
    cross: np.uintc
    mask: np.uintc = np.uintc(0b111111111)
    to_move: Symbol

    def initialize_game(self):
        self.circle = np.uintc(0)
        self.cross = np.uintc(0)
        self.to_move = Symbol.CIRCLE

    def get_avail_moves(self):
        return np.bitwise_and(np.invert(np.bitwise_or(self.circle, self.cross)), self.mask)

    def get_avail_moves_array(self) -> list[Move]:
        result = list()
        moves = self.get_avail_moves()
        for i in range(9):
            if np.bitwise_and(moves, 0b1) == 0b1:
                result.append(Move(np.uintc(i), self.to_move))
            moves = np.right_shift(moves, 1)
        return result

    def undo_move(self, move: Move):
        if move.symbol == Symbol.CIRCLE:
            self.circle = np.bitwise_xor(self.circle, move.to_mask())
            self.to_move = Symbol.CIRCLE
        else:
            self.cross = np.bitwise_xor(self.cross, move.to_mask())
            self.to_move = Symbol.CROSS

    def to_morpion_board(self) -> morpion.Game:
        game = morpion.Game()
        game.initialize_game()
        circles = self.circle
        crosses = self.cross
        for i in range(9):
            circle = np.bitwise_and(circles, 0b1)
            cross = np.bitwise_and(crosses, 0b1)
            circles = np.right_shift(circles, 1)
            crosses = np.right_shift(crosses, 1)
            if circle == 0b1:
                game.board[i // 3][i % 3] = morpion.Symbol.CIRCLE
            if cross == 0b1:
                game.board[i // 3][i % 3] = morpion.Symbol.CROSS
        return game

    def __str__(self):
        return str(self.to_morpion_board())

    def make_move(self, move: Move):
        if self.to_move == Symbol.CROSS:
            self.cross = np.bitwise_or(self.cross, move.to_mask())
            self.to_move = Symbol.CIRCLE
        else:
            self.circle = np.bitwise_or(self.circle, move.to_mask())
            self.to_move = Symbol.CROSS


    def is_game_over(self) -> Result:
        for win_pos in winning_pos:
            if winning_pos_set.__contains__(np.bitwise_and(self.circle, win_pos)):
                return Result.CIRCLE
            if winning_pos_set.__contains__(np.bitwise_and(self.cross, win_pos)):
                return Result.CROSS
        if np.bitwise_or(self.circle, self.cross) == np.uintc(0b111111111):
            return Result.DRAW
        return Result.NOT_OVER

    def get_best_move(self) -> tuple[float, Union[Move, None]]:
        outcome = self.is_game_over()
        if outcome != Result.NOT_OVER:
            return evaluation[outcome], None

        evals = PriorityQueue()
        for move in self.get_avail_moves_array():
            self.make_move(move)
            best_child_move = self.get_best_move()
            self.undo_move(move)
            if self.to_move == Symbol.CROSS:
                best_child_move = (-best_child_move[0], move)
            else:
                best_child_move = (best_child_move[0], move)
            evals.put(best_child_move)
        best_move = evals.get()
        if self.to_move == Symbol.CROSS:
            best_move = (-best_move[0], best_move[1])
        return best_move
