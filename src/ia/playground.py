from chessBitBoard import Bitboard, str_bit_board, BitBoardMoveGenerator
from move import Move
from moveGenerator import MoveGenerator
from magic_moves import *
from move import Move
from moveTable import gen_black_pawn_move_table, gen_white_pawn_move_table
from search import evaluate, search
from gameChecker import GameChecker

board = Bitboard('rnbq1bnr/pppk2Pp/3p4/4p3/8/5P2/PPPP2PP/0RNBQKBNR w KQ - 1 0')

print(board)

moveGenerator = BitBoardMoveGenerator()

# for m in moveGenerator.gen_moves(board):
#     if(m.specialMoveFlag == 3 and m.promotionPieceType == 5):
#         board.make_move(m)
#         break

board.make_move(Move(54, 63, 1, 1, 4, 3, 5))

print(board)

