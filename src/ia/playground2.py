from gameApi import GameChecker

#board = GameChecker('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
#
#list_move = board.showMove(8)
#print(board.board)
#
#make = board.makeMoveAPI(8, 16)
#print(make.isMoveValid)
#print(make.isKingCheck)
#print(make.isGameOver)
#print(make.fen)


#for i in range(len(list_move.target)):
#    print(list_move.target[i])
#
#print(board.board)
#
#board = GameChecker('4k3/P7/8/8/8/8/8/3K4 w - - 0 1')
#
#list_move = board.showMove(48)
#print(board.board)
#
#make = board.makeMoveAPI(48, 56, 3)
#print(make.isMoveValid)
#print(make.isKingCheck)
#print(make.isGameOver)
#print(make.fen)
#
#
#print(board.board)

#board = GameChecker('4k2R/1N6/2BP4/7Q/4R3/8/8/3K4 w - - 0 1')
#
#list_move = board.showMove(43)
#for i in range(len(list_move.target)):
#    print(list_move.target[i])
#
#make = board.makeMoveAPI(43, 51)
#print(make.isMoveValid)
#print(make.isKingCheck)
#print(make.isGameOver)
#print(make.fen)
#
#print(board.board)


board = GameChecker('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')

print(board.board)
move = (board.makeMoveAI())

print(move.isMoveValid)
print(move.isKingCheck)
print(move.isGameOver)
print(move.fen)

print(board.board)

board = GameChecker('rnbqkbnr/pppppppp/8/8/8/7N/PPPPPPPP/0RNBQKB1R b KQkq - 1 0')

print(board.board)
move = (board.makeMoveAI())

print(move.isMoveValid)
print(move.isKingCheck)
print(move.isGameOver)
print(move.fen)

print(board.board)
board = GameChecker('rnbqkb1r/pppppppp/7n/8/8/7N/PPPPPPPP/0RNBQKB1R w KQkq - 1 0')

print(board.board)
move = (board.makeMoveAI())

print(move.isMoveValid)
print(move.isKingCheck)
print(move.isGameOver)
print(move.fen)

print(board.board)