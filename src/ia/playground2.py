from zobrist import ZobristInformations
from zobrist_board import ZobristBoard

zobrist = ZobristBoard('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
print(zobrist.current_hash)

game_checker = ZobristBoard('rnbqkbnr/pppppppp/8/8/8/3P4/PPP1PPPP/RNBQKBNR b KQkq - 0 1')
print(game_checker.current_hash)

game = ZobristBoard('rnbqkbnr/pppp1ppp/4p3/8/8/3P4/PPP1PPPP/RNBQKBNR w KQkq - 0 2')
print(game.current_hash)

zobrist.current_hash ^= game.current_hash

print(zobrist.current_hash)

zobrist.current_hash ^= game.current_hash

print(zobrist.current_hash)