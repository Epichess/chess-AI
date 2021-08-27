from gameApi import GameChecker

board = GameChecker('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

list_move = board.showMove(8)

make = board.makeMoveAPI(8, 16)

#print(list_move.target)
#
#for i in range(len(list_move.target)):
#    print(list_move.target[i])

print(board.board)
print(make)
