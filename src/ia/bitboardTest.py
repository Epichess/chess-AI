from chessBitBoard import Bitboard
# from moveFinder import MoveFinder

from bitarray import bitarray

import sys
import time

# start = time.time()
b = Bitboard("rnbqkbnr/pppppp1p/6p1/8/8/8/PPPPPPPP/RNBQKBNR")
# end = time.time()
# print("Created in " + str((end - start) * 1000) + " ms")

# start = time.time()
# print('FEN', b.get_fen())
# end = time.time()
# print("FEN in " + str((end - start) * 1000) + " ms")
# b.dump_board('P')

# finder = MoveFinder()

# finder.get_captures()

# print(b.get_captures('n', 35))


# def str_bit_board(bits: int) -> str:
#     string = ''
#     for i in range(8):
#         string += '|'
#         for j in range(8):
#             bit = bits & 0b1
#             string += str(bit)
#             string += '|'
#             bits = bits >> 1
#         string += '\n'
#     return string


# print(str_bit_board(0b1110000010000000000000000000000000000000000000000000000000000000))

# a = 0b1110000010000000000000000000000000000000000000000000000000000000
# b = a * 20400080
# c = b >> 34
# print(c)

# 1730496430080


# print(f'{0x000101010101017E:064b}')
