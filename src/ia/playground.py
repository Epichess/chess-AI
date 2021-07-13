from chessBitBoard import Bitboard, str_bit_board
from moveGenerator import MoveGenerator
from magic_moves import *

board = Bitboard('6k1/b1Bb2r1/r4B2/3b3r/B2Q1Rb1/Bb4r1/4RR2/1K2B1Br w - - 0 1')
print(board)

moveGenerator = MoveGenerator()


def debug(board: Bitboard, sqr: int, moveGenerator: MoveGenerator):
    print(f'Board Occupancy: \n{str_bit_board(board.occupancy)}')
    print(f'Vertical Mask: \n{str_bit_board(moveGenerator.magic_line_masks[sqr])}')
    print(f'Diagonal Mask: \n{str_bit_board(moveGenerator.magic_diagonal_masks[sqr])}')
    line_hash = magic_hash(moveGenerator.magic_line_masks[sqr] & board.occupancy, moveGenerator.rook_magic[sqr][0], moveGenerator.rook_magic[sqr][1])
    print(f'Line Hash: {line_hash}')
    diagonal_hash = magic_hash(moveGenerator.magic_diagonal_masks[sqr] & board.occupancy, moveGenerator.bishop_magic[sqr][0], moveGenerator.bishop_magic[sqr][1])
    print(f'Diagonal Hash: {diagonal_hash}')
    print(f'Line Hash Result:\n{str_bit_board(moveGenerator.rook_hash_table[sqr][line_hash])}')
    print(f'Diagonal Hash Result:\n{str_bit_board(moveGenerator.bishop_hash_table[sqr][diagonal_hash])}')
    print(f'Generated Rook Attacks:\n{str_bit_board(moveGenerator.gen_rook_attacks(sqr, board.occupancy))}')
    print(f'Generated Bishop Attacks:\n{str_bit_board(moveGenerator.gen_bishop_attacks(sqr, board.occupancy))}')

# print(str_bit_board(moveGenerator.gen_queen_attacks(2, board.occupancy)))

debug(board, 2, moveGenerator)
