from chessBitBoard import Bitboard, str_bit_board
from move import Move
from moveGenerator import MoveGenerator
from magic_moves import *
from move import Move
from moveTable import gen_black_pawn_move_table, gen_white_pawn_move_table
from search import evaluate, search
from gameChecker import GameChecker

board = Bitboard('k3r3/8/4N3/8/8/8/7P/3K4 w - - 0 1')

print(board)
board.make_move(Move(3, 4, 6, 0))
print(board)

print(board.get_fen())