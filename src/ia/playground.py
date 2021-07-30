from chessBitBoard import Bitboard, str_bit_board
from move import Move
from moveGenerator import MoveGenerator
from magic_moves import *
from gameApi import GameChecker

#board = Bitboard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
#board = Bitboard('rnbqkbnr/pppp1ppp/4p3/8/8/8/PPPPPPPP/RNBQKBNR b KQkq - 0 1')
#print(board)

#moveGenerator = MoveGenerator()
#print(board.make_move(Move(44, 28, 1, 0, 0, 4)))
#print(board)
#print(board.get_fen())

boardAPI = GameChecker('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 0')

print(boardAPI.makeMoveAPI((8, 16)))
print(boardAPI.board)
print(boardAPI.board.get_fen())

print(boardAPI.makeMoveAPI((55, 47)))
print(boardAPI.board)

print(boardAPI.makeMoveAPI((16, 24)))
print(boardAPI.board)
print(boardAPI.board.get_fen())

print(boardAPI.makeMoveAPI((47, 39)))
print(boardAPI.board)
print(boardAPI.board.get_fen())

print(boardAPI.makeMoveAPI((0, 16)))
print(boardAPI.board)
print(boardAPI.board.get_fen())

print(boardAPI.makeMoveAPI((63, 55)))
print(boardAPI.board)
print(boardAPI.board.get_fen())

print(boardAPI.makeMoveAPI((15, 23)))
print(boardAPI.board)
print(boardAPI.board.get_fen())

#board.gameAPI.make_move_API((44, 28))
#
###print(board.make_move(Move(13, 29, 1, 0, 0, 4)))
###print(board)
###print(board.get_fen())
####
###print(board.make_move(Move(28, 21, 1, 1, 1, 1)))
###print(board)
###print(board.get_fen())

#def debug(board: Bitboard, sqr: int, moveGenerator: MoveGenerator):
#    print(f'Board Occupancy: \n{str_bit_board(board.occupancy)}')
#    print(f'Vertical Mask: \n{str_bit_board(moveGenerator.magic_line_masks[sqr])}')
#    print(f'Diagonal Mask: \n{str_bit_board(moveGenerator.magic_diagonal_masks[sqr])}')
#    line_hash = magic_hash(moveGenerator.magic_line_masks[sqr] & board.occupancy, moveGenerator.rook_magic[sqr][0], moveGenerator.rook_magic[sqr][1])
#    print(f'Line Hash: {line_hash}')
#    diagonal_hash = magic_hash(moveGenerator.magic_diagonal_masks[sqr] & board.occupancy, moveGenerator.bishop_magic[sqr][0], moveGenerator.bishop_magic[sqr][1])
#    print(f'Diagonal Hash: {diagonal_hash}')
#    print(f'Line Hash Result:\n{str_bit_board(moveGenerator.rook_hash_table[sqr][line_hash])}')
#    print(f'Diagonal Hash Result:\n{str_bit_board(moveGenerator.bishop_hash_table[sqr][diagonal_hash])}')
#    print(f'Generated Rook Attacks:\n{str_bit_board(moveGenerator.gen_rook_attacks(sqr, board.occupancy))}')
#    print(f'Generated Bishop Attacks:\n{str_bit_board(moveGenerator.gen_bishop_attacks(sqr, board.occupancy))}')
#
## print(str_bit_board(moveGenerator.gen_queen_attacks(2, board.occupancy)))
#
#debug(board, 2, moveGenerator)
