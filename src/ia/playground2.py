from chessBitBoard import *
from magic_moves import *

for sqr in range(64):
    print(len(gen_rook_blockers(sqr)))

