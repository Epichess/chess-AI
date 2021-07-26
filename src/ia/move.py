class Move:
    start: int  # sqr
    end: int  # sqr
    pieceType: int  # piece type
    moveType: int  # move type
    capturedPieceType: int  # piece type
    specialMoveFlag: int  # special move flag
    promotionPieceType: int  # piece type
    castleSide: bool  # castle side

    def __init__(self, start: int, end: int, piece_type: int, move_type: int, captured_piece_type: int = 0,
                 special_move_flag: int = 0, promotion_piece_type: int = 0, castle_side: bool = True):
        self.start = start
        self.end = end
        self.moveType = move_type
        self.pieceType = piece_type
        self.capturedPieceType = captured_piece_type
        self.specialMoveFlag = special_move_flag
        self.promotionPieceType = promotion_piece_type
        self.castleSide = castle_side

    def __eq__(self, other):
        if not isinstance(other, Move):
            return False
        if self.start is not other.start:
            return False
        if self.end is not other.end:
            return False
        if self.moveType is not other.moveType:
            return False
        if self.specialMoveFlag is not other.specialMoveFlag:
            return False
        if self.pieceType is not other.pieceType:
            return False
        if self.castleSide is not other.castleSide:
            return False
        if self.capturedPieceType is not other.capturedPieceType:
            return False
        if self.promotionPieceType:
            return False
        return True

    def __str__(self):
        return f"Start square : {self.start}\nEnd square: {self.end}\nPiece Type: {self.pieceType}\nMove Type: {self.moveType}\nSpecial Flag: {self.specialMoveFlag}\nPromotion type: {self.promotionPieceType}\nCaptured Piece Type: {self.capturedPieceType}\n"

    def __gt__(self, other):
        return self.moveType > other.moveType

    def __lt__(self, other):
        return self.moveType <= other.moveType


'''
Move Types:
0 - Move
1 - Capture
'''

'''
Special Move Flags:
0 - None
1 - En Passant
2 - Castling
3 - Promotion
4 - Double Pawn Move
'''

'''
Piece Types: 
0 - None
1 - Pawn
2 - Knight
3 - Bishop
4 - Rook
5 - Queen
6 - King
'''

'''
Castle Side:
True - King Side
False - Queen Side
'''
