from chessBitBoard import Bitboard, str_bit_board
from move import Move
from moveGenerator import MoveGenerator
from magic_moves import *
from gameApi import GameChecker

# test echec et mat
#boardAPI = GameChecker('3k2R1/N7/1B6/6Q1/8/3R4/K7/8 w - - 0 1')
#
#print(boardAPI.board)
#
#print(boardAPI.makeMoveAPI((41, 32)))
#print(boardAPI.board)
#print(boardAPI.board.get_fen())
#
#print(boardAPI.makeMoveAPI((41, 32)))
#print(boardAPI.board)
#print(boardAPI.board.get_fen())
#
#print('boardAPI.board.check_mate')
#print(boardAPI.board.check_mate)
#print('echec')
#print(boardAPI.board.king_check)

# echec noir
boardAPI = GameChecker('4k3/8/2P5/8/8/8/8/4K3 w - - 0 1')

print(boardAPI.board)

print(boardAPI.checkMove((42, 50)))
print(boardAPI.board)
print(boardAPI.board.get_fen())
#
print(boardAPI.checkMove((60, 61)))
print(boardAPI.board)
print(boardAPI.board.get_fen())


move = boardAPI.checkMove((50, 58))
if move:
    move.promotionPieceType = 5
    print(boardAPI.makeMoveAPI(move))
    print(boardAPI.board)
    print(boardAPI.board.get_fen())
#
#print('boardAPI.board.check_mate')
#print(boardAPI.board.check_mate)
#
print('echec')
print(boardAPI.board.king_check)
#
#print(boardAPI.makeMoveAPI((50, 58, 5)))
#print(boardAPI.board)
#print(boardAPI.board.get_fen())

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
