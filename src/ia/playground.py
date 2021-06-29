from chessBitBoard import *
from magic_moves import *

mbit = 0b0
sqr = 27

print(str_bit_board(masked_occup_to_rook_moves(mbit, sqr)))
