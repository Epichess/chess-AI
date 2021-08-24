from chessBitBoard import Bitboard, BitBoardMoveGenerator
from move import Move


class GameChecker:
    board: Bitboard
    moveGenerator: BitBoardMoveGenerator

    def __init__(self, bitboard: Bitboard):
        self.board = Bitboard(bitboard)
        self.moveGenerator = BitBoardMoveGenerator()

    def checkMove(self, move: Move):
        if move in self.moveGenerator.gen_legal_moves(self.board):
            return True
        else:
            return False

    def getTargetedSquare(self, move: Move) -> int:
        return 0

    def checkGameIsOver(self):
        if len(self.moveGenerator.gen_legal_moves(self.board)) == 0:
            return True
        return False
