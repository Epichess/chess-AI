import CONSTANTS


class ZobristInformations:
    wp: int
    bp: int
    wn: int
    bn: int
    wb: int
    bb: int
    wr: int
    br: int
    wq: int
    bq: int
    wk: int
    bk: int
    toMove: bool
    canWhiteCastleKingSide: bool
    canWhiteCastleQueenSide: bool
    canBlackCastleKingSide: bool
    canBlackCastleQueenSide: bool
    canEnPassant: bool
    enPassantSquare: int
    pieceList: list[int]

    def __init__(self, wp, bp, wn, bn, wb, bb, wr, br, wq, bq, wk, bk, to_move, wksc, wqsc, bksc, bqsc, ep, eps):
        self.wp = wp
        self.bp = bp
        self.wn = wn
        self.bn = bn
        self.wb = wb
        self.bb = bb
        self.wr = wr
        self.br = br
        self.wq = wq
        self.bq = bq
        self.wk = wk
        self.bk = bk
        self.pieceList = [wp, wn, wb, wr, wq, wk, bp, bn, bb, br, bq, bk]
        self.toMove = to_move
        self.canWhiteCastleKingSide = wksc
        self.canWhiteCastleQueenSide = wqsc
        self.canBlackCastleKingSide = bksc
        self.canBlackCastleQueenSide = bqsc
        self.canEnPassant = ep
        self.enPassantSquare = eps

    def __hash__(self):
        zobrist_key = 0
        for j in range(12):
            for i in range(64):
                if self.pieceList[j] & 1 << i > 0:
                    zobrist_key ^= CONSTANTS.ZOBRIST_KEYS[i + 64 * j]
        if self.toMove:
            zobrist_key ^= CONSTANTS.ZOBRIST_KEYS[768]
        if self.canWhiteCastleKingSide:
            zobrist_key ^= CONSTANTS.ZOBRIST_KEYS[769]
        if self.canWhiteCastleQueenSide:
            zobrist_key ^= CONSTANTS.ZOBRIST_KEYS[770]
        if self.canBlackCastleKingSide:
            zobrist_key ^= CONSTANTS.ZOBRIST_KEYS[771]
        if self.canBlackCastleQueenSide:
            zobrist_key ^= CONSTANTS.ZOBRIST_KEYS[772]
        if self.canEnPassant:
            for i in range(8):
                if self.enPassantSquare % 8 == i:
                    zobrist_key ^= CONSTANTS.ZOBRIST_KEYS[773 + i]
        return zobrist_key
