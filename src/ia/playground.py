from chessBitBoard import Bitboard, str_bit_board, BitBoardMoveGenerator
from move import Move
from moveGenerator import MoveGenerator
from magic_moves import *
from move import Move
from moveTable import gen_black_pawn_move_table, gen_white_pawn_move_table
from search import evaluate, search
from gameChecker import GameChecker

board = Bitboard('r1bqkb1r/pppp1ppp/2n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4')

print(board)

moveGenerator = BitBoardMoveGenerator()

for move in moveGenerator.gen_moves(board):
    if move.specialMoveFlag == 2:
        print(move)

print(board.board_info.can_black_queen_side_castle)
print(board.board_info.can_black_king_side_castle)
print(board.board_info.can_white_queen_side_castle)
print(board.board_info.can_white_king_side_castle)