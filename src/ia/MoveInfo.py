from enum import Enum


class MoveInfo:
    class Side(Enum):
        WHITE = True
        BLACK = False

    move = tuple                                        # Origin and destination square
    side = Side                                         # Side moving WHITE or BLACK

    piece = int                                         # Current moving piece
    captured_piece = int                                # Captured piece
    capture = bool                                      # Is this move a capture

    canCastle = tuple                                   # Can castle booleans
    isCastle = tuple                                    # Already castled

    isEnPassant = bool                                  # Is this move an en passant capture
    enPassantCapture = int                              # The square left empty when moving pawn

    promotion = bool                                    # Is this move a promotion
    promotion_piece = int                               # The piece we promoted into

    def __init__(self,
                 move,
                 side,
                 piece,
                 captured_piece=None,
                 is_castle=(False, False),
                 can_castle=(False, False),
                 isEnPassant=False,
                 promotion_piece='Q') -> None:
        self.move = move
        self.side = side

        self.piece = (piece.upper() if self.side == self.Side.WHITE else piece.lower())
        self.captured_piece = captured_piece
        self.capture = captured_piece != None

        self.canCastle = can_castle
        self.isCastle = is_castle

        self.isEnPassant = isEnPassant
        self.enPassantCapture = int(sum(list(self.move)) / 2) if ((self.piece == 'P' and self.side == self.Side.WHITE and (self.move[0] > 7 and self.move[0] < 16) and (
            move[1] - move[0] == 16))) or ((self.piece == 'p' and self.side == self.Side.BLACK and (self.move[0] > 47 and self.move[0] < 56) and (move[0] - move[1] == 16))) else None

        self.promotion = ((self.piece == 'P' and self.side == self.Side.WHITE and self.move[1] > 55) or (
            self.piece == 'p' and self.side == self.Side.BLACK and self.move[1] < 8))
        self.promotion_piece = (promotion_piece.upper() if self.side ==
                                self.Side.WHITE else promotion_piece.lower()) if self.promotion else None
