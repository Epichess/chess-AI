from chessBitBoard import Bitboard, str_bit_board
from moveGenerator import MoveGenerator
from magic_moves import *
from bitboardMoveGenerator import BitBoardMoveGenerator

board = Bitboard('2r5/3P4/8/8/p1n1b3/1P3P2/8/8 w - - 0 1')
bmoveGenerator = BitBoardMoveGenerator()
print(board)

moves = bmoveGenerator.gen_pawn_moves(board, True)
print('Number of moves: ', len(moves))
for m in moves:
    print(m)

# moveGenerator = MoveGenerator()

def debug(board: Bitboard, sqr: int, moveGenerator: MoveGenerator):
    print(f'Board Occupancy: \n{str_bit_board(board.occupancy)}')
    print(f'Vertical Mask: \n{str_bit_board(moveGenerator.magic_line_masks[sqr])}')
    print(f'Diagonal Mask: \n{str_bit_board(moveGenerator.magic_diagonal_masks[sqr])}')
    rook_blockers = moveGenerator.magic_line_masks[sqr] & board.occupancy
    bishop_blockers = moveGenerator.magic_diagonal_masks[sqr] & board.occupancy
    generated_rook_blockers = gen_rook_blockers(sqr)
    generated_bishop_blockers = gen_bishop_blockers(sqr)
    print(f'Rook Blockers: \n{str_bit_board(rook_blockers)}')
    print(f'Bishop Blockers: \n{str_bit_board(bishop_blockers)}')

    print(f'Rook blockers in generated: {rook_blockers in generated_rook_blockers}')
    print(f'Bishop blockers in generated: {bishop_blockers in generated_bishop_blockers}')

    line_hash = magic_hash(moveGenerator.magic_line_masks[sqr] & board.occupancy, moveGenerator.rook_magic[sqr][0], moveGenerator.rook_magic[sqr][1])
    print(f'Line Hash: {line_hash}')
    diagonal_hash = magic_hash(moveGenerator.magic_diagonal_masks[sqr] & board.occupancy, moveGenerator.bishop_magic[sqr][0], moveGenerator.bishop_magic[sqr][1])
    print(f'Diagonal Hash: {diagonal_hash}')
    print(f'Generated Rook Attacks:\n{str_bit_board(moveGenerator.gen_rook_attacks(sqr, board.occupancy))}')
    print(f'Generated Bishop Attacks:\n{str_bit_board(moveGenerator.gen_bishop_attacks(sqr, board.occupancy))}')
    print(f'Line Hash Result:\n{str_bit_board(moveGenerator.rook_hash_table[sqr][line_hash])}')
    print(f'Diagonal Hash Result:\n{str_bit_board(moveGenerator.bishop_hash_table[sqr][diagonal_hash])}')
