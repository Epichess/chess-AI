from chessBitBoard import *
from magic_moves import gen_bishop_blockers, gen_rook_blockers, gen_magic_number, masked_occup_to_bishop_moves, \
    masked_occup_to_rook_moves, gen_magic_hashtable
import random
import CONSTANTS
import sys
from moveFinder import get_magic_diagonal_mask, get_magic_line_mask

mb = get_magic_diagonal_mask()
mr = get_magic_line_mask()

for i, s in enumerate(mb):
    print(i, str_bit_board(s))
