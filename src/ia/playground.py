from chessBitBoard import *
from magic_moves import gen_bishop_blockers, gen_rook_blockers, gen_magic_number, masked_occup_to_bishop_moves, \
    masked_occup_to_rook_moves, gen_magic_hashtable
import random
import CONSTANTS
import sys

# d = dict()
# for i in range(64):
#     print(i)
#     d[i] = gen_magic_number(i, gen_rook_blockers, masked_occup_to_rook_moves, 52, 100000000)

# s = gen_magic_number(24, gen_rook_blockers, masked_occup_to_rook_moves, 53, 100000000)
# s = gen_magic_number(20, gen_bishop_blockers, masked_occup_to_bishop_moves, 57, 1000000000)
#
# print(s)

# l = []
# for i in range(56, 64):
#     print(i)
#     if i % 8 == 0 or i % 8 == 7:
#         l.append(gen_magic_number(i, gen_rook_blockers, masked_occup_to_rook_moves, 52, 100000000))
#     else:
#         l.append(gen_magic_number(i, gen_rook_blockers, masked_occup_to_rook_moves, 53, 100000000))
#
# for i, s in enumerate(l):
#     print(f"{i + 56}: ({s[0][0]}, {s[0][1]}),")

l=[]
for i in range(64):
    l.append(gen_magic_hashtable(0, CONSTANTS.BISHOP_MAGIC[0][0], CONSTANTS.BISHOP_MAGIC[0][1], gen_bishop_blockers, masked_occup_to_bishop_moves))

for i, s in enumerate(l):
    print(i, 'valid magic number', s[0])
