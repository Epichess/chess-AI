def extract_index(bitboard) -> list[int]:
    a = []
    while bitboard > 0:
        lsb = bitboard & -bitboard
        a.append(lsb.bit_length() - 1)
        bitboard ^= lsb
    return a
