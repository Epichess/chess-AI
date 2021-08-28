def extract_index(bitboard) -> list[int]:
    a = []
    while bitboard > 0:
        lsb = bitboard & -bitboard
        a.append(lsb.bit_length() - 1)
        bitboard ^= lsb
    return a

def str_bit_board(bits: int) -> str:
    arr = []
    for i in range(8):
        string = '|'
        for j in range(8):
            bit = bits & 0b1
            string += str(bit)
            string += '|'
            bits = bits >> 1
        string += '\n'
        arr.append(string)
    arr.reverse()
    s = ''
    return s.join(arr)