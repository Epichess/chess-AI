def masked_occup_to_rook_moves(mbit: int, sqr: int) -> int:
    # mbit is a masked bit board, sqr is between 0-63 and represents the index of the starting square of the sliding
    # piece
    rank_index = sqr // 8
    file_index = sqr % 8
    avail_moves = 0b0
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << (8 * rank_index) != 0:
            break
        shifter >>= 1
        if shifter & mbit > 0:
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << (8 * rank_index + 7) != 0:
            break
        shifter <<= 1
        if shifter & mbit > 0:
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << file_index != 0:
            break
        shifter >>= 8
        if shifter & mbit > 0:
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << (56 + file_index) != 0:
            break
        shifter <<= 8
        if shifter & mbit > 0:
            break
    avail_moves ^= 0b1 << sqr
    return avail_moves
