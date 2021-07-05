from chessBitBoard import *
from magic_moves import *

hset = set()
vset = set()
gen_horizontal_perms(7, 0b10, 0, hset)
gen_vertical_perms(7, 0b100000000, 0, vset)

for v in vset:
    print(str_bit_board(v << 2))
for h in hset:
    print(str_bit_board(h << 3*8))
