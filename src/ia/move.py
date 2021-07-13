class Move:
    start: int  # sqr
    end: int  # sqr
    pieceType: int  # piece type
    moveType: int  # move type
    capturedPieceType: int  # piece type
    specialMoveFlag: int  # special move flag
    promotionPieceType: int  # piece type

    def __init__(self, start: int, end: int, piece_type: int, move_type: int, captured_piece_type: int = 0, special_move_flag: int = 0, promotion_piece_type: int = 0):
        self.start = start
        self.end = end
        self.moveType = move_type
        self.pieceType = piece_type
        self.capturedPieceType = captured_piece_type
        self.specialMoveFlag = special_move_flag
        self.promotionPieceType = promotion_piece_type

    def __str__(self):
        return f"Start square : {self.start}\nEnd square: {self.end}\nPiece Type: {self.pieceType}\nMove Type: {self.moveType}\nSpecial Flag: {self.specialMoveFlag}\n Promotion type: {self.promotionPieceType}\nCaptured Piece Type: {self.capturedPieceType}"


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