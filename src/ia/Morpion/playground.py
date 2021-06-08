from morpion import *

game = Game()
game.initialize_game()

# game.make_move(Move(0, 0, Symbol.CROSS))
# game.make_move(Move(0, 1, Symbol.CIRCLE))
# game.make_move(Move(0, 2, Symbol.CROSS))
# game.make_move(Move(2, 0, Symbol.CIRCLE))
# game.make_move(Move(1, 0, Symbol.CROSS))

# game.make_move(Move(0, 0, Symbol.CROSS))
# game.make_move(Move(0, 1, Symbol.CIRCLE))
# game.make_move(Move(0, 2, Symbol.CROSS))
# game.make_move(Move(1, 1, Symbol.CIRCLE))
# game.make_move(Move(1, 0, Symbol.CROSS))
# game.make_move(Move(1, 2, Symbol.CIRCLE))
# game.make_move(Move(2, 1, Symbol.CROSS))
# game.make_move(Move(2, 0, Symbol.CIRCLE))
# game.make_move(Move(2, 2, Symbol.CROSS))

print(game)

best_move = game.get_best_move()

print(best_move[0])
print(best_move[1])
