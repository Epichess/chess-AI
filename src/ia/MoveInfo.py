from enum import Enum


class MoveInfo:
    move: tuple  # Origin and destination square
    side: bool  # Side moving WHITE or BLACK

    piece: int  # Current moving piece
    captured_piece: int  # Captured piece
    capture: bool  # Is this move a capture

    canCastle: tuple  # Can castle booleans
    isCastle: tuple  # Already castled

    isEnPassant: bool  # Is this move an en passant capture
    enPassantCapture: int  # The square left empty when moving pawn

    promotion: bool  # Is this move a promotion
    promotion_piece: int  # The piece we promoted into

    def __init__(self,
                 move,
                 side,
                 piece,
                 captured_piece=None,
                 is_castle=(False, False),
                 can_castle=(False, False),
                 is_en_passant=False,
                 promotion_piece='Q') -> None:
        self.move = move
        self.side = side

        self.piece = (piece.upper() if self.side else piece.lower())
        self.captured_piece = captured_piece
        self.capture = captured_piece is not None

        self.canCastle = can_castle
        self.isCastle = is_castle

        self.isEnPassant = is_en_passant
        self.enPassantCapture = int(sum(list(self.move)) / 2) if ((
                self.piece == 'P' and self.side and (
                7 < self.move[0] < 16) and (
                            move[1] - move[0] == 16))) or ((self.piece == 'p' and not self.side and (
                47 < self.move[0] < 56) and (move[0] - move[1] == 16))) else None

        self.promotion = ((self.piece == 'P' and self.side and self.move[1] > 55) or (
                self.piece == 'p' and not self.side and self.move[1] < 8))
        self.promotion_piece = (promotion_piece.upper() if self.side ==
                                                           self.Side.WHITE else promotion_piece.lower()) if self.promotion else None

    def __str__(self) -> str:
        pieces = {
            'r': 'Rook',
            'n': 'Knight',
            'b': 'Bishop',
            'q': 'Queen',
            'k': 'King',
            'p': 'Pawn',
            'None': 'None'
        }
        return ('Move: {0} -> {1}\nSide: {2}\nPiece: {3}\n{4}\n{5}'.format(self.move[0], self.move[1],
                                                                           "White" if self.side else "Black",
                                                                           pieces[self.piece.lower()],
                                                                           "Captured piece: " + (pieces[
                                                                                                     self.captured_piece] if self.captured_piece != None else "None"),
                                                                           "Promoted to: " + (
                                                                               self.promotion_piece if self.promotion else "None")))
