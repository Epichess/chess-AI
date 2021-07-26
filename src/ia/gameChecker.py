from chessBitBoard import Bitboard, BitBoardMoveGenerator
from src.ia.move import Move


class GameChecker:
    board: Bitboard
    moveGenerator: BitBoardMoveGenerator

    def __init__(self, fen: str):
        self.board = Bitboard(fen)
        self.moveGenerator = BitBoardMoveGenerator()

    def checkMove(self, move: Move):
        if move in self.moveGenerator.gen_legal_moves(self.board):
            return True
        else:
            return False

    def checkGameIsOver(self):
        if len(self.moveGenerator.gen_legal_moves(self.board)) == 0:
            return True
        return False
