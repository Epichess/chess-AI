from chessBitBoard import *
from magic_moves import *

mbit = 0b0100100000000000000001000100000000000010000000000000101000010000
print(str_bit_board(mbit))
sqr = 23

shifter = 0b1 << sqr

print(str_bit_board(masked_occup_to_rook_moves(mbit, sqr)))
print(str_bit_board(masked_occup_to_bishop_moves(mbit, sqr)))
