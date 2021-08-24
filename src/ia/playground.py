from chessBitBoard import Bitboard, str_bit_board
from move import Move
from moveGenerator import MoveGenerator
from magic_moves import *
from move import Move
from moveTable import gen_black_pawn_move_table, gen_white_pawn_move_table
from search import evaluate, search
from gameChecker import GameChecker

board = Bitboard('k3r3/8/4N3/8/8/8/7P/3K4 w - - 0 1')

# print('black king castle: ', board.board_info.can_black_king_side_castle)
# print('black queen castle:', board.board_info.can_black_queen_side_castle)
# print('white king castle: ', board.board_info.can_white_king_side_castle)
# print('white queen castle: ', board.board_info.can_white_queen_side_castle)

# game_checker = GameChecker('6k1/8/3P2K1/8/8/8/8/8 w - - 0 1')

# moves = board.moveGenerator.gen_king_moves(board)
# print(board)
# print(len(moves))
# for m in moves:
#     print(m)
#     board.make_move(m)
#     print(board)
#     board.unmake_move()

r = search(board, 0, 5)
print('eval:', r[0])
print(r[1])
