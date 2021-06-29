from clearMaskRankFile import *
from chessBitBoard import *
from moveFinder import *
#
# for i in range(15):
#     print(str_bit_board(RAY_NW_MASK[i]))
#
# for i in range(15):
#     print(str_bit_board(RAY_NE_MASK[i]))
#
move_finder = MoveFinder()
#
# for i in range(63):
#     print(str_bit_board(move_finder.knights[i]))
#
# for i in range(63):
print(str_bit_board(move_finder.kings[63]))
print(bin(move_finder.kings[63]))
#
# for i in range(63):
#     print(str_bit_board(move_finder.black_pawns_capture[i]))
#
# for i in range(63):
#     print(str_bit_board(move_finder.white_pawns_capture[i]))

