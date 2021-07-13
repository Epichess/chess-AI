from chessBitBoard import *
from magic_moves import *
import CONSTANTS

for b in gen_rook_blockers(18):
    print(str_bit_board(b))

print(magic_hash(0b1000000000000000000, CONSTANTS.ROOK_MAGIC[18][0], CONSTANTS.ROOK_MAGIC[18][1]))
