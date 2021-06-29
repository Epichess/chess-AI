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
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << (8 * rank_index + 7) != 0:
            break
        shifter <<= 1
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << file_index != 0:
            break
        shifter >>= 8
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & 1 << (56 + file_index) != 0:
            break
        shifter <<= 8
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    avail_moves ^= 0b1 << sqr
    return avail_moves

def masked_occup_to_bishop_moves(mbit: int, sqr: int) -> int:
    # mbit is a masked bit board, sqr is between 0-63 and represents the index of the starting square of the sliding
    # piece

    top_rank = 0xFF00000000000000
    bottom_rank = 0xFF
    left_file = 0b0000000100000001000000010000000100000001000000010000000100000001
    right_file = 0b1000000010000000100000001000000010000000100000001000000010000000
    rank_index = sqr // 8
    file_index = sqr % 8
    avail_moves = 0b0
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & top_rank != 0 or shifter & left_file != 0:
            break
        shifter <<= 7
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & top_rank != 0 or shifter & right_file != 0:
            break
        shifter <<= 9
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & bottom_rank != 0 or shifter & left_file != 0:
            break
        shifter >>= 9
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    shifter = 0b1 << sqr
    while True:
        avail_moves |= shifter
        if shifter & bottom_rank != 0 or shifter & right_file != 0:
            break
        shifter >>= 7
        if shifter & mbit > 0:
            avail_moves |= shifter
            break
    avail_moves ^= 0b1 << sqr
    return avail_moves

# def gen_blockers(sqr: int, shifter: int, result: list[int]) -> list[int]:
#     return result
#
# def gen_all_n_bits_int(n :int, i: int, binary: int, result: list[int]) -> list[int]:
#     if i == n:
#         return binary
