import sys
import numpy as np
from morpion_bit_board import *

bit_board = BitBoard()
bit_board.initialize_game()
bit_board.make_move(Move(np.uintc(1), Symbol.CIRCLE))
print(bit_board.to_move)
best_move = bit_board.get_best_move()
print(bit_board.get_best_move()[0])
