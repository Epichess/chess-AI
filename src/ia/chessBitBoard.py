class Bitboard:
    wp: int
    wn: int
    wb: int
    wr: int
    wq: int
    wk: int
    bp: int
    bn: int
    bb: int
    br: int
    bq: int
    bk: int


class Move:
    start: int
    end: int
    flag: int
    promotedPiece: int


def str_bit_board(bits: int) -> str:
    string = ''
    for i in range(8):
        string += '|'
        for j in range(8):
            bit = bits & 0b1
            string += str(bit)
            string += '|'
            bits = bits >> 1
        string += '\n'
    return string
