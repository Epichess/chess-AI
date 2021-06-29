from chessBitBoard import Bitboard
from moveFinder import MoveFinder

import sys
import time

# start = time.time()
# b = Bitboard("rnbqkbnr/pppppp1p/6p1/8/8/8/PPPPPPPP/RNBQKBNR")
# end = time.time()
# print("Created in " + str((end - start) * 1000) + " ms")

# start = time.time()
# print('FEN', b.get_fen())
# end = time.time()
# print("FEN in " + str((end - start) * 1000) + " ms")
# b.dump_board('P')

finder = MoveFinder()